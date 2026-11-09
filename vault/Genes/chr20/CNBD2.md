---
symbol: "CNBD2"
type: "gene"
col: 7400
ensembl_id: "ENSG00000149646"
name: "cyclic nucleotide binding domain containing 2"
location: "20q11.23"
module: 53
arm: "+"
pooled_cpm: 5.0
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 24
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# CNBD2

*cyclic nucleotide binding domain containing 2* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.59× (z +16.0, q 0e+00, up in 34 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.538× (z -3.9, q 0.060, down in 12 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.194×; ⚠ cell-cycle shift, explains ~57% of this change); [[Vilanterol (drug)]] 0.05 µM in 1 line (HT-29 0.0709×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL9]] (+0.73, fdr 7e-06), [[CPT1C]] (+0.72, fdr 7e-06), [[MFSD2B]] (+0.71, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.59×** | +16.0 | 0e+00 | 34/40 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +13.3 | 6e-38 | 25/41 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +9.8 | 3e-20 | 21/29 (SW480, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +9.5 | 2e-19 | 5/10 (HS-578T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +9.4 | 8e-19 | 5/15 (HOP62, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +7.7 | 9e-13 | 25/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.3 | 2e-08 | 8/24 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +6.2 | 4e-08 | 16/46 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +5.0 | 3e-05 | 12/47 (NCI-H23, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +4.8 | 8e-05 | 17/39 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 5e-04 | 13/44 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.46×** | +4.2 | 0.001 | 16/44 (A498, LoVo, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.001 | 10/47 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 13/46 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.002 | 13/47 (A498, J82, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.004 | 13/45 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.010 | 9/46 (LS 180, H4, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.012 | 4/45 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.026 | 7/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7400.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.194×; ⚠ cell-cycle shift, explains ~57% of this change); [[Vilanterol (drug)]] 0.05 µM in 1 line (HT-29 0.0709×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.538×** | -3.9 | 0.060 | 12/35 (C-33 A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.738×** | -3.6 | 0.075 | 5/46 (HepG2/C3A, SW480, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.741× | -3.4 | 0.10 | 9/44 (NCI-H23, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Pentoxifylline (drug)]] 0.5 µM |  | 0.759× | -3.3 | 0.10 | 6/42 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.754× | -3.3 | 0.10 | 14/43 (J82, A-427, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.596× | -3.2 | 0.10 | 9/41 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.757× | -3.2 | 0.10 | 10/37 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Methotrexate (drug)]] 0.5 µM |  | 0.777× | -3.0 | 0.17 | 9/45 (HEC-1-A, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -9.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A498 (line)]] | wt | 2.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 3.58 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0709× (z -9.1) |
| [[LoVo (line)]] | wt | 3.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.72× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 4.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +12.5) | — |
| [[A-172 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL9]] | +0.73 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.72 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[MFSD2B]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[HNRNPD-DT]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[LINC01030]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[MASP2]] | +0.69 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[USP50]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[PRC1-AS1]] | +0.69 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[SGSM3-AS1]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PILRA]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.735). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.7, -16.4); signed map (19.4, 11.4). **Vector** length 58.6, 7.92% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +16.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +9.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.6 |
| fall | [[NG25 (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.7 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +0.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cyclic nucleotide binding domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:35,954,564-36,030,700 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ954P9.1; previously C20orf152, CNMPD1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96M20](https://www.uniprot.org/uniprotkb/Q96M20) (Cyclic nucleotide-binding domain-containing protein 2):

> Essential for male fertility. Plays an important role in spermatogenesis and regulates sperm motility by controlling the development of the flagellar bending of sperm.

**Summary**, from NCBI Gene [140894](https://www.ncbi.nlm.nih.gov/gene/140894):

> Predicted to enable cAMP binding activity. Predicted to be involved in spermatogenesis. Located in sperm midpiece. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16145](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16145) · Entrez [140894](https://www.ncbi.nlm.nih.gov/gene/140894) · UniProt [Q96M20](https://www.uniprot.org/uniprotkb/Q96M20) · Ensembl [ENSG00000149646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149646)

## Data

Gene col 7400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7400); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7400]; `tensor/DDL_lfc|DDL_z.npy` [7400]; `embed/gene_vectors.npy` [7400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7400 or target_col == 7400). Every well: [[CNBD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNBD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
