---
symbol: "UBA52"
type: "gene"
col: 13326
ensembl_id: "ENSG00000221983"
name: "ubiquitin A-52 residue ribosomal protein fusion product 1"
location: "19p13.1-p12"
module: 43
arm: "+"
pooled_cpm: 100.35
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# UBA52

*ubiquitin A-52 residue ribosomal protein fusion product 1* — 19p13.1-p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.80× (z +8.3, q 8e-14, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +4.8, q 2e-04, up in 44 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H1573 6.47×, SW480 4.98×, NCI-H460 5.37×, NCI-H23 4.56×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 5.83×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL35]] (+0.91, fdr 7e-06, ⚠ RPL35 in the vector space only through flagged drug-doses), [[RPLP1]] (+0.91, fdr 7e-06), [[RPS14]] (+0.91, fdr 7e-06), [[RPS27]] (+0.90, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13326.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H1573 6.47×, SW480 4.98×, NCI-H460 5.37×, NCI-H23 4.56×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 5.83×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.80×** | +8.3 | 8e-14 | 49/49 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **3.03×** | +6.6 | 1e-08 | 43/44 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +4.8 | 2e-04 | 44/49 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +4.8 | 2e-04 | 46/47 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.31×** | +4.8 | 2e-04 | 40/45 (KATO III, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **2.14×** | +4.7 | 3e-04 | 44/48 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.03×** | +4.4 | 1e-03 | 46/48 (NCI-H460, KATO III, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.69×** | +3.2 | 0.086 | 42/48 (COLO 205, SW480, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13326.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.651× | -3.7 | 0.13 | 34/48 (C-33 A, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 64.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.47× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[KATO III (line)]] | alt | 65.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H23 (line)]] | alt | 93.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H460 (line)]] | wt | 96.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 80.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW480 (line)]] | alt | 95.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 96.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 77.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 113 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 98.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 85.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 125 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 109 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 160 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 114 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 123 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL35]] ⚠ | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPLP1]] | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.91 | +0.87 / +0.90 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 999 |
| [[RPS27]] | +0.90 | +0.82 / +0.93 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 999 |
| [[RPL12]] | +0.90 | +0.83 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.90 | +0.84 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.90 | +0.86 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS19]] | +0.90 | +0.86 / +0.92 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 999 |
| [[RPL26]] | +0.89 | +0.82 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 997 |
| [[RPL19]] | +0.89 | +0.82 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS12]] | +0.89 | +0.82 / +0.91 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 999 |
| [[RPS17]] ⚠ | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL27]] | +0.87 | +0.84 / +0.87 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP2]] | +0.87 | +0.80 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.898). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.1, -27.0); signed map (-59.3, -4.4). **Vector** length 72.3, 38.1% of its response variance represented; |z| ≥ 3 in 495 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.74 to 19); *Translation initiation complex formation* (reactome, mean cos +0.70 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.70 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +1.5 | +3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.5 | -0.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.5 | +1.0 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.4 | -0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +0.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -6.4 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -6.2 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -6.1 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.2 | +2.3 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin A-52 residue ribosomal protein fusion product 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.1-p12 — chr19:18,571,730-18,577,550 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPL40, CEP52, HUBCEP52, MGC57125, MGC126879, MGC126881, L40 |
| Gene groups (HGNC) | L ribosomal proteins; Ubiquitins |
| Reactome | 439 pathways, smallest: Maturation of protein E_9683683; Maturation of protein E_9694493; FLT3 signaling by CBL mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [P62987](https://www.uniprot.org/uniprotkb/P62987) (Ubiquitin-ribosomal protein eL40 fusion protein):

> [Ubiquitin]: Exists either covalently attached to another protein, or free (unanchored). When covalently bound, it is conjugated to target proteins via an isopeptide bond either as a monomer (monoubiquitin), a polymer linked via different Lys residues of the ubiquitin (polyubiquitin chains) or a linear polymer linked via the initiator Met of the ubiquitin (linear polyubiquitin chains). Polyubiquitin chains, when attached to a target protein, have different functions depending on the Lys residue …

**Summary**, from NCBI Gene [7311](https://www.ncbi.nlm.nih.gov/gene/7311):

> Ubiquitin is a highly conserved nuclear and cytoplasmic protein that has a major role in targeting cellular proteins for degradation by the 26S proteosome. It is also involved in the maintenance of chromatin structure, the regulation of gene expression, and the stress response. Ubiquitin is synthesized as a precursor protein consisting of either polyubiquitin chains or a single ubiquitin moiety fused to an unrelated protein. This gene encodes a fusion protein consisting of ubiquitin at the N …

**Accessions** — [HGNC:12458](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12458) · Entrez [7311](https://www.ncbi.nlm.nih.gov/gene/7311) · UniProt [P62987](https://www.uniprot.org/uniprotkb/P62987) · Ensembl [ENSG00000221983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221983)

## Data

Gene col 13326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13326); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13326]; `tensor/DDL_lfc|DDL_z.npy` [13326]; `embed/gene_vectors.npy` [13326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13326 or target_col == 13326). Every well: [[UBA52 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBA52.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
