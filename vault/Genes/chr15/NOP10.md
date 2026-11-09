---
symbol: "NOP10"
type: "gene"
col: 11241
ensembl_id: "ENSG00000182117"
name: "NOP10 ribonucleoprotein"
location: "15q14"
module: 54
arm: "+"
pooled_cpm: 20.95
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# NOP10

*NOP10 ribonucleoprotein* — 15q14

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.35× (z +5.6, q 1e-05, up in 40 of 45 measured lines) ⚠ toxic. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (SNU-1 0.0826×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.342×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMC6]] (+0.73, fdr 1e-05), [[RPL36AL]] (+0.72, fdr 1e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[ATP5MK]] (+0.70, fdr 7e-06), [[COMMD6]] (+0.68, fdr 3e-05); moves opposite to [[HNRNPL]] (-0.60, fdr 2e-05), [[CBX5]] (-0.60, fdr 2e-04), [[COPS3]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11241.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +5.6 | 1e-05 | 40/45 (NCI-H1573, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.26×** | +5.5 | 1e-05 | 33/41 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.06×** | +4.9 | 2e-04 | 39/46 (PANC-1, COLO 205, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.07×** | +4.7 | 3e-04 | 22/30 (A498, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.72×** | +3.7 | 0.025 | 32/44 (SW 900, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 1.61× | +3.2 | 0.11 | 23/47 (NCI-H460, HT-29, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11241.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (SNU-1 0.0826×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.342×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | 0.540× | -3.6 | 0.18 | 36/48 (LoVo, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11241. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 69.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -8.8) |
| [[SNU-1 (line)]] | wt | 14.8 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0826× (z -9.1) |
| [[A-172 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11241), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 19 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC6]] | +0.73 | +0.51 / +0.77 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.72 | +0.57 / +0.76 | both halves | 1e-05 | pathway: rRNA processing; STRING 450; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.68 | +0.46 / +0.76 | both halves | 3e-05 |  |
| [[SF3B5]] ⚠ | +0.67 | +0.53 / +0.72 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | +0.67 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[MRPS36]] ⚠ | +0.66 | +0.46 / +0.68 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL41]] ⚠ | +0.66 | +0.59 / +0.70 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[C4orf48]] | +0.66 | +0.46 / +0.74 | both halves | 3e-05 |  |
| [[CHCHD1]] | +0.66 | +0.33 / +0.75 | both halves | 1e-04 |  |
| [[MRPS12]] | +0.66 | +0.41 / +0.76 | both halves | 4e-05 |  |
| [[ZNF593]] | +0.66 | +0.36 / +0.75 | both halves | 9e-05 |  |
| [[EXOSC4]] | +0.65 | +0.37 / +0.72 | both halves | 8e-05 | pathway: rRNA processing |
| [[CIAO2B]] | +0.64 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[SF3B6]] | +0.64 | +0.35 / +0.74 | both halves | 1e-04 |  |
| [[POP7]] | +0.64 | +0.36 / +0.72 | both halves | 9e-05 | STRING 916 |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPL]] | -0.60 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[CBX5]] | -0.60 | -0.32 / -0.72 | both halves | 2e-04 |  |
| [[COPS3]] | -0.59 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[CNOT1]] | -0.58 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[HNRNPM]] | -0.57 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[EWSR1]] | -0.57 | -0.37 / -0.63 | both halves | 9e-05 |  |
| [[HNRNPUL1]] | -0.57 | -0.25 / -0.61 | both halves | 4e-04 |  |
| [[BACE1-AS]] | -0.57 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[HP1BP3]] | -0.55 | -0.26 / -0.68 | both halves | 4e-04 |  |
| [[PRPF8]] | -0.54 | -0.29 / -0.61 | both halves | 2e-04 |  |
| [[ARHGEF9]] | -0.54 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[HNRNPD]] | -0.54 | -0.34 / -0.60 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-43.9, -20.7); signed map (-32.6, 8.8). **Vector** length 59.7, 15.6% of its response variance represented; |z| ≥ 3 in 468 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +3.2 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.3 | +1.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -2.7 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -2.6 | +5.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.9 | -3.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | NOP10 ribonucleoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:34,339,159-34,343,180 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NOP10P, MGC70651; previously NOLA3 |
| Gene groups (HGNC) | H/ACA ribonucleoprotein complex; Telomerase holoenzyme subunits |
| Reactome | 9 pathways, smallest: Telomere Extension By Telomerase; Extension of Telomeres; rRNA modification in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPE3](https://www.uniprot.org/uniprotkb/Q9NPE3) (H/ACA ribonucleoprotein complex subunit 3):

> Required for ribosome biogenesis and telomere maintenance. Part of the H/ACA small nucleolar ribonucleoprotein (H/ACA snoRNP) complex, which catalyzes pseudouridylation of rRNA. This involves the isomerization of uridine such that the ribose is subsequently attached to C5, instead of the normal N1. Each rRNA can contain up to 100 pseudouridine ('psi') residues, which may serve to stabilize the conformation of rRNAs. May also be required for correct processing or intranuclear trafficking of …

**Summary**, from NCBI Gene [55505](https://www.ncbi.nlm.nih.gov/gene/55505):

> This gene is a member of the H/ACA snoRNPs (small nucleolar ribonucleoproteins) gene family. snoRNPs are involved in various aspects of rRNA processing and modification and have been classified into two families: C/D and H/ACA. The H/ACA snoRNPs also include the DKC1, NOLA1 and NOLA2 proteins. These four H/ACA snoRNP proteins localize to the dense fibrillar components of nucleoli and to coiled (Cajal) bodies in the nucleus. Both 18S rRNA production and rRNA pseudouridylation are impaired if any …

**Accessions** — [HGNC:14378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14378) · Entrez [55505](https://www.ncbi.nlm.nih.gov/gene/55505) · UniProt [Q9NPE3](https://www.uniprot.org/uniprotkb/Q9NPE3) · Ensembl [ENSG00000182117](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182117)

## Data

Gene col 11241: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11241); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11241, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11241]; `tensor/DDL_lfc|DDL_z.npy` [11241]; `embed/gene_vectors.npy` [11241]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11241 or target_col == 11241). Every well: [[NOP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
