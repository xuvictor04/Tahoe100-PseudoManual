---
symbol: "MRPS36"
type: "gene"
col: 5503
ensembl_id: "ENSG00000134056"
name: "alpha-ketoglutarate dehydrogenase subunit 4"
location: "5q13.2"
module: 24
arm: "+"
pooled_cpm: 21.05
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

# MRPS36

*alpha-ketoglutarate dehydrogenase subunit 4* — 5q13.2

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.75× (z +5.6, q 1e-05, up in 27 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 3.61×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.177×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR83OS]] (+0.76, fdr 7e-06, ⚠ WDR83OS in the vector space only through flagged drug-doses), [[SMIM26]] (+0.75, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[COX6B1]] (+0.74, fdr 7e-06), [[IFI27L2]] (+0.72, fdr 1e-05), [[TMEM258]] (+0.70, fdr 1e-05); moves opposite to [[WDR1]] (-0.65, fdr 1e-05), [[EIF4G1]] (-0.62, fdr 1e-05), [[MYH9]] (-0.61, fdr 9e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5503.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 3.61×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.75×** | +5.6 | 1e-05 | 27/42 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.57×** | +4.4 | 0.003 | 18/31 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.7 | 0.037 | 20/43 (J82, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.42×** | +3.5 | 0.060 | 24/47 (SHP-77, NCI-H460, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.26× | +3.3 | 0.10 | 24/47 (HEC-1-A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | 1.39× | +3.2 | 0.14 | 20/45 (LoVo, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5503.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.177×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.794× | -3.2 | 0.76 | 25/48 (SW 900, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5503. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[SNU-1 (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5503), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 20 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR83OS]] ⚠ | +0.76 | +0.66 / +0.73 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SMIM26]] ⚠ | +0.75 | +0.59 / +0.80 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[COX6B1]] | +0.74 | +0.59 / +0.76 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[RPL36AL]] ⚠ | +0.73 | +0.55 / +0.77 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFB11]] ⚠ | +0.72 | +0.56 / +0.76 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; ⚠ in the vector space only through flagged drug-doses |
| [[IFI27L2]] | +0.72 | +0.51 / +0.78 | both halves | 1e-05 |  |
| [[TMEM258]] | +0.70 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[POLR2J]] ⚠ | +0.70 | +0.57 / +0.80 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | +0.70 | +0.53 / +0.75 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[MRPS18C]] | +0.70 | +0.54 / +0.75 | both halves | 1e-05 | pathway: Mitochondrial ribosome-associated quality control; STRING 696 |
| [[SMIM27]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[ATP5PD]] | +0.69 | +0.52 / +0.75 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[CHCHD5]] | +0.69 | +0.33 / +0.78 | both halves | 1e-04 |  |
| [[EIF1B]] | +0.69 | +0.51 / +0.77 | both halves | 1e-05 |  |
| [[EMC6]] | +0.68 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[NDUFA1]] | +0.67 | +0.54 / +0.69 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[COMMD6]] | +0.67 | +0.46 / +0.77 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR1]] | -0.65 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.62 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[MYH9]] | -0.61 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[MAPRE1]] | -0.60 | -0.30 / -0.71 | both halves | 2e-04 |  |
| [[IPO5]] | -0.60 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.60 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[FLNA]] | -0.59 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[NOLC1]] | -0.59 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[TXNDC5]] | -0.59 | -0.41 / -0.67 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.759). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-44.0, -20.2); signed map (-32.5, 8.3). **Vector** length 54.3, 10.6% of its response variance represented; |z| ≥ 3 in 388 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +2.3 | +3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | +1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +3.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +1.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.4 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -0.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | +2.1 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | +0.2 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | alpha-ketoglutarate dehydrogenase subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:69,217,760-69,230,158 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DC47, MRP-S36; previously MRPS36 |
| Gene groups (HGNC) | Oxoglutarate dehydrogenase complex subunits |
| Reactome | 12 pathways, smallest: OGDH complex synthesizes succinyl-CoA from 2-OG; Glycine degradation; Glyoxylate metabolism and glycine degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P82909](https://www.uniprot.org/uniprotkb/P82909) (Alpha-ketoglutarate dehydrogenase component 4):

> Molecular adapter that is necessary to form a stable 2-oxoglutarate dehydrogenase enzyme complex (OGDHC). Enables the specific recruitment of E3 subunit to E2 subunit in the 2-oxoglutarate dehydrogenase complex (OGDHC).

**Summary**, from NCBI Gene [92259](https://www.ncbi.nlm.nih.gov/gene/92259):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. The mitochondrial ribosome (mitoribosome) consists of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:16631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16631) · Entrez [92259](https://www.ncbi.nlm.nih.gov/gene/92259) · UniProt [P82909](https://www.uniprot.org/uniprotkb/P82909) · Ensembl [ENSG00000134056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134056)

## Data

Gene col 5503: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5503); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5503, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5503]; `tensor/DDL_lfc|DDL_z.npy` [5503]; `embed/gene_vectors.npy` [5503]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5503 or target_col == 5503). Every well: [[MRPS36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
