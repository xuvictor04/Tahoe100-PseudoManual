---
symbol: "GADD45GIP1"
type: "gene"
col: 11016
ensembl_id: "ENSG00000179271"
name: "GADD45G interacting protein 1"
location: "19p13.13"
module: 24
arm: "+"
pooled_cpm: 33.3
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# GADD45GIP1

*GADD45G interacting protein 1* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.55× (z +6.2, q 4e-07, up in 37 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.592× (z -4.8, q 7e-04, down in 34 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.149×, SK-MEL-2 0.251×); [[Selinexor (drug)]] 5 µM in 1 line (J82 0.257×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTLN]] (+0.76, fdr 1e-05, ⚠ MTLN in the vector space only through flagged drug-doses), [[MRPL36]] (+0.76, fdr 3e-05), [[POLR2I]] (+0.74, fdr 1e-05), [[EMC6]] (+0.74, fdr 1e-04); moves opposite to [[CD164]] (-0.62, fdr 1e-05), [[MOB1A]] (-0.62, fdr 9e-05), [[SRSF1]] (-0.59, fdr 3e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11016.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.55×** | +6.2 | 4e-07 | 37/45 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.18×** | +4.9 | 2e-04 | 28/37 (A498, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.94×** | +4.4 | 0.002 | 36/46 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +4.1 | 0.005 | 40/47 (COLO 205, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.39× | +3.1 | 0.24 | 31/48 (C-33 A, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11016.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.149×, SK-MEL-2 0.251×); [[Selinexor (drug)]] 5 µM in 1 line (J82 0.257×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.592×** | -4.8 | 7e-04 | 34/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 5 µM |  | 0.383× | -3.2 | 0.28 | 37/48 (J82, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.594× | -3.1 | 0.28 | 38/48 (A498, KATO III, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.403× | -3.0 | 0.28 | 29/48 (H4, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11016. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.257× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 43.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 27.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -9.5) |
| [[A-172 (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11016), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 25 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTLN]] ⚠ | +0.76 | +0.53 / +0.76 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL36]] | +0.76 | +0.46 / +0.81 | both halves | 3e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 961 |
| [[POLR2I]] | +0.74 | +0.55 / +0.78 | both halves | 1e-05 |  |
| [[EMC6]] | +0.74 | +0.36 / +0.84 | both halves | 1e-04 |  |
| [[CHCHD1]] | +0.72 | +0.31 / +0.82 | both halves | 2e-04 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 922 |
| [[LEO1]] | +0.71 | +0.39 / +0.76 | both halves | 6e-05 |  |
| [[SMIM26]] ⚠ | +0.71 | +0.38 / +0.78 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF593]] | +0.71 | +0.45 / +0.81 | both halves | 3e-05 |  |
| [[UQCR10]] ⚠ | +0.71 | +0.41 / +0.80 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[KRTCAP2]] | +0.70 | +0.26 / +0.84 | both halves | 4e-04 |  |
| [[MRPL46]] | +0.70 | +0.36 / +0.81 | both halves | 1e-04 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 965 |
| [[ATP5ME]] | +0.70 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[RPP21]] | +0.70 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[TIMM13]] | +0.69 | +0.38 / +0.74 | both halves | 7e-05 |  |
| [[TRAPPC5]] | +0.68 | +0.33 / +0.71 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD164]] | -0.62 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.62 | -0.36 / -0.62 | both halves | 9e-05 |  |
| [[SRSF1]] | -0.59 | -0.28 / -0.63 | both halves | 3e-04 |  |
| [[FGD5-AS1]] | -0.59 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[PAPOLA]] | -0.57 | -0.23 / -0.65 | both halves | 5e-04 |  |
| [[ATN1]] | -0.57 | -0.19 / -0.55 | ⚠ one half (not replicated) | 8e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-44.3, -11.9); signed map (-13.0, -7.4). **Vector** length 61.7, 20.7% of its response variance represented; |z| ≥ 3 in 424 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.52 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.6 | +0.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | -0.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -5.2 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -5.0 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -0.9 | +1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | GADD45G interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,953,119-12,957,223 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PLINP-1, MGC4667, MGC4758, CKBBP2, PRG6, Plinp1, CRIF1, CKbetaBP2 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAE8](https://www.uniprot.org/uniprotkb/Q8TAE8) (Large ribosomal subunit protein mL64):

> Acts as a negative regulator of G1 to S cell cycle phase progression by inhibiting cyclin-dependent kinases. Inhibitory effects are additive with GADD45 proteins but also occur in the absence of GADD45 proteins. Acts as a repressor of the orphan nuclear receptor NR4A1 by inhibiting AB domain-mediated transcriptional activity. May be involved in the hormone-mediated regulation of NR4A1 transcriptional activity. May play a role in mitochondrial protein synthesis.

**Summary**, from NCBI Gene [90480](https://www.ncbi.nlm.nih.gov/gene/90480):

> This gene encodes a nuclear-localized protein that may be induced by p53 and regulates the cell cycle by inhibiting G1 to S phase progression. The encoded protein may interact with other cell cycle regulators. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:29996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29996) · Entrez [90480](https://www.ncbi.nlm.nih.gov/gene/90480) · UniProt [Q8TAE8](https://www.uniprot.org/uniprotkb/Q8TAE8) · Ensembl [ENSG00000179271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179271)

## Data

Gene col 11016: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11016); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11016, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11016]; `tensor/DDL_lfc|DDL_z.npy` [11016]; `embed/gene_vectors.npy` [11016]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11016 or target_col == 11016). Every well: [[GADD45GIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GADD45GIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
