---
symbol: "TMEM126A"
type: "gene"
col: 10070
ensembl_id: "ENSG00000171202"
name: "transmembrane protein 126A"
location: "11q14.1"
module: 24
arm: "+"
pooled_cpm: 14.94
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# TMEM126A

*transmembrane protein 126A* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.22× (z +7.6, q 1e-11, up in 42 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.70× (z +5.1, q 6e-05, up in 29 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C-33 A 0.0778×; ⚠ cell-cycle shift, explains ~52% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHCHD5]] (+0.68, fdr 4e-05), [[NDUFB4]] (+0.67, fdr 2e-05), [[MRPS18C]] (+0.65, fdr 1e-05); moves opposite to [[ILF2]] (-0.58, fdr 3e-05), [[HNRNPAB]] (-0.57, fdr 3e-05), [[NOLC1]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10070.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.22×** | +7.6 | 1e-11 | 42/46 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.07×** | +7.0 | 8e-10 | 34/48 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.85×** | +5.3 | 2e-05 | 25/37 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +5.1 | 6e-05 | 29/47 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +5.0 | 8e-05 | 32/47 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.68×** | +4.8 | 2e-04 | 16/31 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +4.3 | 0.001 | 27/48 (NCI-H2030, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.2 | 0.002 | 27/43 (MIA PaCa-2, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.49×** | +3.9 | 0.007 | 22/43 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +3.8 | 0.008 | 25/47 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.39×** | +3.2 | 0.082 | 19/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10070.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C-33 A 0.0778×; ⚠ cell-cycle shift, explains ~52% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | 0.778× | -3.4 | 0.43 | 16/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10070. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0778× (z -9.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H460 (line)]] | wt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW480 (line)]] | alt | 17.8 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +8.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10070), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 10 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHCHD5]] | +0.68 | +0.41 / +0.71 | both halves | 4e-05 |  |
| [[NDUFB4]] | +0.67 | +0.48 / +0.68 | both halves | 2e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[MRPS18C]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[NDUFS4]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[MRPL22]] | +0.64 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[SMIM26]] ⚠ | +0.64 | +0.54 / +0.64 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[IFI27L2]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[MRPL32]] | +0.63 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[DYNC2LI1]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[MRPS36]] ⚠ | +0.62 | +0.49 / +0.63 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; ⚠ in the vector space only through flagged drug-doses |
| [[RBIS]] | +0.62 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[ATP5MC2]] | +0.62 | +0.47 / +0.62 | both halves | 2e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[CCDC43]] | +0.62 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[EMC2]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILF2]] | -0.58 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[HNRNPAB]] | -0.57 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[NOLC1]] | -0.56 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[MORC2]] | -0.52 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[GATAD2A]] | -0.52 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[MCM7]] | -0.51 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[KPNA4]] | -0.51 | -0.34 / -0.57 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.2, -15.4); signed map (-13.8, -4.4). **Vector** length 60.0, 11.7% of its response variance represented; |z| ≥ 3 in 582 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.3 | +4.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.2 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +5.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | -0.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.9 | +2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 126A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:85,647,967-85,656,547 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586C1924, OPA7 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H061](https://www.uniprot.org/uniprotkb/Q9H061) (Transmembrane protein 126A):

> Protein required for the cotranslational protein quality control in the inner membrane of the mitochondria. Associates with newly synthesized polypeptides and may act as a chaperone that cooperates with OXA1L for the insertion of newly synthesized mitochondrial proteins into the inner membrane. Required for the assembly of the ND4 module of mitochondrial complex I.

**Summary**, from NCBI Gene [84233](https://www.ncbi.nlm.nih.gov/gene/84233):

> The protein encoded by this gene is a mitochondrial membrane protein of unknown function. Defects in this gene are a cause of optic atrophy type 7 (OPA7). Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:25382](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25382) · Entrez [84233](https://www.ncbi.nlm.nih.gov/gene/84233) · UniProt [Q9H061](https://www.uniprot.org/uniprotkb/Q9H061) · Ensembl [ENSG00000171202](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171202)

## Data

Gene col 10070: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10070); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10070, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10070]; `tensor/DDL_lfc|DDL_z.npy` [10070]; `embed/gene_vectors.npy` [10070]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10070 or target_col == 10070). Every well: [[TMEM126A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM126A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
