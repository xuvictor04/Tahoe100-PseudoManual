---
symbol: "ABT1"
type: "gene"
col: 7065
ensembl_id: "ENSG00000146109"
name: "activator of basal transcription 1"
location: "6p22.2"
module: 7
arm: "+"
pooled_cpm: 8.2
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ABT1

*activator of basal transcription 1* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.72× (z +9.8, q 6e-20, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.720× (z -4.5, q 0.004, down in 7 of 14 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 3 lines (A549 0.0802×, C-33 A 0.0801×, BT-474 0.105×); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H2030 0.103×, SW480 0.238×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.234×, CFPAC-1 0.193×; ⚠ toxic; transcription drop); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SNU-423 0.105×); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 900 0.0671×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KTI12]] (+0.74, fdr 7e-06), [[MRFAP1L1]] (+0.74, fdr 7e-06), [[ZNF317]] (+0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7065.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.72×** | +9.8 | 6e-20 | 39/46 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.98×** | +9.7 | 8e-20 | 34/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +9.2 | 6e-18 | 30/43 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~14% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +9.1 | 2e-17 | 25/37 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.48×** | +7.9 | 4e-13 | 24/43 (NCI-H1573, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.72×** | +7.5 | 7e-12 | 30/46 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.71×** | +7.4 | 8e-12 | 23/43 (NCI-H2030, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.62×** | +6.9 | 4e-10 | 25/47 (NCI-H460, PANC-1, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.52×** | +5.6 | 2e-06 | 19/43 (PANC-1, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +5.4 | 4e-06 | 15/47 (MIA PaCa-2, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.45×** | +5.3 | 6e-06 | 14/39 (KATO III, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.2 | 0.001 | 13/45 (RPMI-7951, BT-474, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.0 | 0.002 | 1/48 (AsPC-1) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.69×** | +3.9 | 0.004 | 5/39 (SK-MEL-2, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.018 | 8/45 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.024 | 13/46 (NCI-H23, PANC-1, …) | top dose only | position effect removed |
| [[Pemigatinib (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.048 | 4/46 (J82, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7065.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 3 lines (A549 0.0802×, C-33 A 0.0801×, BT-474 0.105×); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H2030 0.103×, SW480 0.238×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.234×, CFPAC-1 0.193×; ⚠ toxic; transcription drop); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SNU-423 0.105×); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 900 0.0671×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.720×** | -4.5 | 0.004 | 7/14 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.795× | -3.3 | 0.26 | 14/32 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.777× | -3.2 | 0.26 | 8/47 (A-427, NCI-H23, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7065. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 17.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -14.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 5.43 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0802× (z -10.4) |
| [[BT-474 (line)]] | alt | 7.42 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.105× (z -8.5) |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0801× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 8.28 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -8.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 8.80 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0680× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 8.61 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.105× (z -11.2) |
| [[SW 900 (line)]] | alt | 6.74 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0671× (z -10.8) |
| [[SW480 (line)]] | alt | 9.22 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7065), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KTI12]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.74 | +0.59 / +0.80 | both halves | 7e-06 |  |
| [[ZNF317]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[PHAX]] | +0.72 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[TBCC]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[ZBTB6]] | +0.72 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[SMG8]] | +0.71 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[TRMT10C]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[MRM2]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 | STRING 634 |
| [[SURF6]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 | STRING 625 |
| [[KLHL9]] | +0.70 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[MRPS18A]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-36.3, 5.9); signed map (-1.7, -22.8). **Vector** length 55.1, 7.86% of its response variance represented; |z| ≥ 3 in 720 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +9.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +7.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +5.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.5 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | +0.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.0 | -0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.0 | +0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -0.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -0.9 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | activator of basal transcription 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:26,596,953-26,600,739 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Esf2 |
| Gene groups (HGNC) | SSU processome |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULW3](https://www.uniprot.org/uniprotkb/Q9ULW3) (Activator of basal transcription 1):

> Could be a novel TATA-binding protein (TBP) which can function as a basal transcription activator. Can act as a regulator of basal transcription for class II genes (By similarity).

**Summary**, from NCBI Gene [29777](https://www.ncbi.nlm.nih.gov/gene/29777):

> Basal transcription of genes by RNA polymerase II requires the interaction of TATA-binding protein (TBP) with the core region of class II promoters. Studies in mouse suggest that the protein encoded by this gene likely activates basal transcription from class II promoters by interaction with TBP and the class II promoter DNA. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17369](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17369) · Entrez [29777](https://www.ncbi.nlm.nih.gov/gene/29777) · UniProt [Q9ULW3](https://www.uniprot.org/uniprotkb/Q9ULW3) · Ensembl [ENSG00000146109](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146109)

## Data

Gene col 7065: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7065); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7065, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7065]; `tensor/DDL_lfc|DDL_z.npy` [7065]; `embed/gene_vectors.npy` [7065]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7065 or target_col == 7065). Every well: [[ABT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
