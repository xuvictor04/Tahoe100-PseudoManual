---
symbol: "SMIM26"
type: "gene"
col: 13846
ensembl_id: "ENSG00000232388"
name: "small integral membrane protein 26"
location: "20p11.23"
module: 24
arm: "+"
pooled_cpm: 13.71
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# SMIM26

*small integral membrane protein 26* — 20p11.23

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.34× (z +4.3, q 0.011, up in 38 of 42 measured lines) ⚠ toxic.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL36AL]] (+0.87, fdr 7e-06, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[NACA4P]] (+0.84, fdr 7e-06, ⚠ NACA4P in the vector space only through flagged drug-doses), [[NKAP]] (+0.82, fdr 7e-06), [[MRPS18C]] (+0.82, fdr 7e-06), [[LAMTOR5]] (+0.82, fdr 7e-06); moves opposite to [[MOB1A]] (-0.79, fdr 7e-06), [[DHFR]] (-0.77, fdr 1e-05), [[IPO5]] (-0.75, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13846.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.34×** | +4.3 | 0.011 | 38/42 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | 1.91× | +3.4 | 0.20 | 29/43 (AsPC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13846.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.533× | -3.0 | 0.64 | 30/48 (Panc 03.27, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13846. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13846), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 13 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL36AL]] ⚠ | +0.87 | +0.67 / +0.92 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NACA4P]] ⚠ | +0.84 | +0.74 / +0.85 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NKAP]] | +0.82 | +0.74 / +0.85 | both halves | 7e-06 |  |
| [[MRPS18C]] | +0.82 | +0.66 / +0.86 | both halves | 7e-06 |  |
| [[LAMTOR5]] | +0.82 | +0.58 / +0.87 | both halves | 7e-06 |  |
| [[SCAND1]] | +0.81 | +0.67 / +0.88 | both halves | 7e-06 |  |
| [[CHCHD5]] | +0.81 | +0.56 / +0.84 | both halves | 1e-05 |  |
| [[KRT10]] ⚠ | +0.81 | +0.68 / +0.86 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MC2]] | +0.80 | +0.71 / +0.83 | both halves | 7e-06 |  |
| [[ZNF593]] | +0.79 | +0.61 / +0.84 | both halves | 7e-06 |  |
| [[TMEM258]] | +0.79 | +0.63 / +0.83 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.79 | +0.73 / +0.82 | both halves | 7e-06 |  |
| [[MRPL32]] | +0.79 | +0.64 / +0.87 | both halves | 7e-06 |  |
| [[TOMM7]] | +0.78 | +0.62 / +0.86 | both halves | 7e-06 |  |
| [[RPP21]] | +0.78 | +0.52 / +0.84 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.79 | -0.73 / -0.78 | both halves | 7e-06 |  |
| [[DHFR]] | -0.77 | -0.54 / -0.80 | both halves | 1e-05 |  |
| [[IPO5]] | -0.75 | -0.65 / -0.78 | both halves | 7e-06 |  |
| [[MAPRE1]] | -0.74 | -0.55 / -0.77 | both halves | 1e-05 |  |
| [[PSME3]] | -0.74 | -0.62 / -0.75 | both halves | 7e-06 |  |
| [[TXNDC5]] | -0.72 | -0.54 / -0.79 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.72 | -0.76 / -0.75 | both halves | 7e-06 |  |
| [[EMC1]] | -0.72 | -0.55 / -0.74 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.71 | -0.58 / -0.72 | both halves | 8e-06 |  |
| [[NUP188]] | -0.70 | -0.53 / -0.74 | both halves | 1e-05 |  |
| [[YWHAQ]] | -0.70 | -0.64 / -0.77 | both halves | 7e-06 |  |
| [[HNRNPA3]] | -0.70 | -0.64 / -0.69 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.900). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-41.2, -14.8); signed map (-14.1, -3.9). **Vector** length 80.5, 26.7% of its response variance represented; |z| ≥ 3 in 353 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.60 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | -1.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +0.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.6 | +1.4 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.1 | +0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.7 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.4 | +0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -3.0 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:18,567,347-18,569,563 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOC388789; previously LINC00493 |
| Matched by | ensembl_id |

**Function**, from UniProt [A0A096LP01](https://www.uniprot.org/uniprotkb/A0A096LP01) (Small integral membrane protein 26):

> Interacts with voltage-gated ion channel VDAC1 in the outer mitochondrial membrane and with ADP:ATP antiporter SLC25A6 in the inner mitochondrial membrane, and is essential for respiratory chain function by coordinating metabolite transport through the inner and outer mitochondrial membranes. Also interacts with serine transporter SFXN1 and with the mitochondrial large ribosomal subunit, forming a functional triad that promotes SFXN1-mediated mitochondrial serine import which is essential for …

**Summary**, from NCBI Gene [388789](https://www.ncbi.nlm.nih.gov/gene/388789):

> Enables protein kinase binding activity and transmembrane transporter binding activity. Located in mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:43430](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43430) · Entrez [388789](https://www.ncbi.nlm.nih.gov/gene/388789) · UniProt [A0A096LP01](https://www.uniprot.org/uniprotkb/A0A096LP01) · Ensembl [ENSG00000232388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232388)

## Data

Gene col 13846: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13846); `tables/drug_effects.parquet` (3 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13846, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13846]; `tensor/DDL_lfc|DDL_z.npy` [13846]; `embed/gene_vectors.npy` [13846]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13846 or target_col == 13846). Every well: [[SMIM26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
