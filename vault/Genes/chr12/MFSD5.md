---
symbol: "MFSD5"
type: "gene"
col: 11298
ensembl_id: "ENSG00000182544"
name: "solute carrier family 61 member 1"
location: "12q13.13"
module: 119
arm: "+"
pooled_cpm: 3.24
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# MFSD5

*solute carrier family 61 member 1* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.92× (z +9.0, q 2e-16, up in 17 of 21 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.80× (z +7.4, q 4e-11, up in 19 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.657× (z -5.3, q 5e-05, down in 22 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM115]] (+0.67, fdr 1e-05), [[NCBP2AS2]] (+0.66, fdr 4e-05), [[GPATCH3]] (+0.63, fdr 1e-05); moves opposite to [[CSRP1]] (-0.53, fdr 2e-04), [[MYH9]] (-0.53, fdr 1e-04), [[COTL1]] (-0.51, fdr 4e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.92×** | +9.0 | 2e-16 | 17/21 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.80×** | +7.4 | 4e-11 | 19/45 (PANC-1, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +4.6 | 6e-04 | 4/16 (KATO III, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.5 | 0.001 | 14/36 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.91× | +3.0 | 0.28 | 2/6 (A-427, A498) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11298.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.657×** | -5.3 | 5e-05 | 22/44 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.610×** | -4.2 | 0.009 | 13/43 (A498, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.636×** | -4.1 | 0.009 | 13/35 (SK-MEL-2, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.627×** | -3.9 | 0.013 | 17/39 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.665×** | -3.7 | 0.027 | 12/42 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.699× | -3.2 | 0.12 | 4/45 (SNU-423, HEC-1-A, …) | inconsistent across doses |  |
| [[Tomivosertib (drug)]] 5 µM |  | 0.516× | -3.1 | 0.15 | 4/33 (SK-MEL-2, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.42 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 5.89 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0790× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 4.26 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.251× (z -8.6) |
| [[A-172 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM115]] | +0.67 | +0.50 / +0.68 | both halves | 1e-05 | STRING 506 |
| [[NCBP2AS2]] | +0.66 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[GPATCH3]] | +0.63 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ATP6V0B]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[EIF4E2]] | +0.62 | +0.34 / +0.74 | both halves | 1e-04 |  |
| [[MRPS12]] | +0.61 | +0.37 / +0.64 | both halves | 9e-05 |  |
| [[CCDC12]] | +0.60 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[NGDN]] | +0.60 | +0.32 / +0.65 | both halves | 1e-04 |  |
| [[SPNS1]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 | STRING 485 |
| [[CLPP]] | +0.60 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[ZNF576]] | +0.60 | +0.34 / +0.73 | both halves | 1e-04 |  |
| [[SCNM1]] | +0.59 | +0.33 / +0.74 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSRP1]] | -0.53 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[MYH9]] | -0.53 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[COTL1]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PFKP]] | -0.50 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[MYBL1]] | -0.49 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[HNRNPA2B1]] | -0.49 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[ANXA5]] | -0.49 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[EPB41L2]] | -0.48 | -0.37 / -0.55 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.7, -10.4); signed map (-11.1, -10.1). **Vector** length 48.0, 6.24% of its response variance represented; |z| ≥ 3 in 722 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.3 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[EX229 (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.0 | +2.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.0 | +1.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.1 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.1 | +1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.1 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 61 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,251,251-53,254,406 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11308, HsMOT2; previously MFSD5 |
| Gene groups (HGNC) | Solute carrier family 61 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6N075](https://www.uniprot.org/uniprotkb/Q6N075) (Solute carrier family 61 member 1):

> Mediates high-affinity intracellular uptake of the rare oligo-element molybdenum.

**Summary**, from NCBI Gene [84975](https://www.ncbi.nlm.nih.gov/gene/84975):

> Enables molybdate ion transmembrane transporter activity. Involved in molybdate ion transport. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28156](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28156) · Entrez [84975](https://www.ncbi.nlm.nih.gov/gene/84975) · UniProt [Q6N075](https://www.uniprot.org/uniprotkb/Q6N075) · Ensembl [ENSG00000182544](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182544)

## Data

Gene col 11298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11298); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11298]; `tensor/DDL_lfc|DDL_z.npy` [11298]; `embed/gene_vectors.npy` [11298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11298 or target_col == 11298). Every well: [[MFSD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
