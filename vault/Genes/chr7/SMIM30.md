---
symbol: "SMIM30"
type: "gene"
col: 13184
ensembl_id: "ENSG00000214194"
name: "small integral membrane protein 30"
location: "7q31.1"
module: 24
arm: "+"
pooled_cpm: 20.28
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SMIM30

*small integral membrane protein 30* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.16× (z +7.4, q 5e-11, up in 28 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.52× (z +4.0, q 0.011, up in 27 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 6.75×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 3.12×).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.569× (z -5.3, q 5e-05, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5PO]] (+0.63, fdr 1e-05, ⚠ ATP5PO in the vector space only through flagged drug-doses), [[MIR181A1HG]] (+0.61, fdr 3e-05), [[MNAT1]] (+0.60, fdr 6e-04), [[METTL5]] (+0.59, fdr 2e-04); moves opposite to [[DHRS11]] (-0.61, fdr 4e-05), [[AKT1]] (-0.58, fdr 1e-05), [[NDOR1]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13184.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 6.75×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 3.12×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.16×** | +7.4 | 5e-11 | 28/30 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.21×** | +7.0 | 8e-10 | 37/41 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.011 | 27/46 (A-172, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.7 | 0.032 | 29/42 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +3.5 | 0.055 | 24/46 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.43×** | +3.4 | 0.064 | 29/46 (NCI-H1792, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.70×** | +3.3 | 0.076 | 24/35 (LOX-IMVI, J82, …) | all doses, stronger at high dose | composition shift |
| [[Bendamustine (drug)]] 5 µM |  | 1.63× | +3.2 | 0.12 | 26/45 (AN3 CA, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13184.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.569×** | -5.3 | 5e-05 | 29/45 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.285×** | -4.4 | 0.003 | 32/43 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.530×** | -4.3 | 0.004 | 35/46 (LoVo, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.346×** | -3.7 | 0.028 | 28/44 (SK-MEL-2, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.379×** | -3.4 | 0.076 | 28/46 (SW480, C-33 A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.613×** | -3.3 | 0.096 | 21/46 (SW 1271, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.627× | -3.1 | 0.14 | 21/45 (LoVo, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 23.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0848× (z -8.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 40.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -10.8) |
| [[PANC-1 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -9.0) |
| [[RKO (line)]] | wt | 50.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -12.2) |
| [[SW 900 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.75× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A-427 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 7 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5PO]] ⚠ | +0.63 | +0.52 / +0.61 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MIR181A1HG]] | +0.61 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[MNAT1]] | +0.60 | +0.22 / +0.58 | both halves | 6e-04 |  |
| [[METTL5]] | +0.59 | +0.29 / +0.67 | both halves | 2e-04 |  |
| [[NDUFC2]] | +0.59 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[TTC3P1]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[NDUFA8]] | +0.57 | +0.27 / +0.66 | both halves | 3e-04 |  |
| [[TRAPPC5]] | +0.56 | +0.36 / +0.60 | both halves | 9e-05 |  |
| [[SEC62]] | +0.56 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[HDAC8]] | +0.56 | +0.31 / +0.65 | both halves | 2e-04 |  |
| [[GTF2H5]] | +0.56 | +0.31 / +0.61 | both halves | 2e-04 |  |
| [[IFI27L2]] | +0.55 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[SSB]] | +0.55 | +0.39 / +0.60 | both halves | 5e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHRS11]] | -0.61 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[AKT1]] | -0.58 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[NDOR1]] | -0.58 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[MAN2A2]] | -0.57 | -0.32 / -0.62 | both halves | 1e-04 |  |
| [[INPPL1]] | -0.56 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CERS2]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ILF2]] | -0.55 | -0.26 / -0.65 | both halves | 4e-04 |  |
| [[DYRK4]] | -0.55 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[NDST2]] | -0.53 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[GUCD1]] | -0.53 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[GTPBP1]] | -0.53 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[SBF1]] | -0.53 | -0.51 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.373). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-25.8, -6.0); signed map (-21.8, -12.2). **Vector** length 66.4, 18.2% of its response variance represented; |z| ≥ 3 in 578 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +4.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -2.9 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -2.7 | +3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -3.7 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.3 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +0.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.2 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:113,116,718-113,118,560 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAVI1; previously LINC00998 |
| Matched by | ensembl_id |

**Function**, from UniProt [A4D0T7](https://www.uniprot.org/uniprotkb/A4D0T7) (Small integral membrane protein 30):

> Negatively regulates antiviral innate immune responses. Disrupts the interaction of antiviral protein MAVS with innate immune receptor RIGI and inhibits MAVS aggregation, resulting in the repression of type I interferon signaling and innate immune responses.

**Summary**, from NCBI Gene [401397](https://www.ncbi.nlm.nih.gov/gene/401397):

> Involved in negative regulation of type I interferon-mediated signaling pathway. Located in endoplasmic reticulum membrane and mitochondrial membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:48953](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48953) · Entrez [401397](https://www.ncbi.nlm.nih.gov/gene/401397) · UniProt [A4D0T7](https://www.uniprot.org/uniprotkb/A4D0T7) · Ensembl [ENSG00000214194](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214194)

## Data

Gene col 13184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13184); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13184]; `tensor/DDL_lfc|DDL_z.npy` [13184]; `embed/gene_vectors.npy` [13184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13184 or target_col == 13184). Every well: [[SMIM30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
