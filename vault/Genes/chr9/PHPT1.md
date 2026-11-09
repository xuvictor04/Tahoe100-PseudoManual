---
symbol: "PHPT1"
type: "gene"
col: 602
ensembl_id: "ENSG00000054148"
name: "phosphohistidine phosphatase 1"
location: "9q34.3"
module: 48
arm: "+"
pooled_cpm: 34.83
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# PHPT1

*phosphohistidine phosphatase 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.18× (z +6.0, q 9e-07, up in 38 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 4.66×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.431× (z -8.9, q 2e-16, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLH]] (+0.72, fdr 7e-06), [[DPM3]] (+0.71, fdr 7e-06), [[SIRT2]] (+0.68, fdr 7e-06); moves opposite to [[CCT5]] (-0.73, fdr 7e-06), [[CCT2]] (-0.69, fdr 7e-06), [[CCT6A]] (-0.64, fdr 9e-06).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 602.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 4.66×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.18×** | +6.0 | 9e-07 | 38/44 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +5.1 | 9e-05 | 24/35 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.68×** | +4.0 | 0.012 | 32/46 (AsPC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Arbutin (drug)]] 5 µM |  | 1.52× | +3.1 | 0.27 | 30/48 (HS-578T, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 602.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.431×** | -8.9 | 2e-16 | 43/47 (HCT15, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.429×** | -6.6 | 1e-08 | 43/48 (HCT15, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.469×** | -5.9 | 8e-07 | 37/48 (NCI-H1792, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.564×** | -4.5 | 0.001 | 32/48 (SNU-423, AsPC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.568×** | -4.4 | 0.001 | 34/48 (AN3 CA, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.519×** | -4.3 | 0.001 | 35/48 (SNU-423, HCT15, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.578×** | -4.3 | 0.002 | 30/47 (A-427, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.586×** | -4.2 | 0.002 | 38/48 (HS-578T, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.600×** | -3.8 | 0.008 | 30/48 (COLO 205, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.575×** | -3.7 | 0.013 | 31/47 (Panc 03.27, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.625×** | -3.7 | 0.013 | 29/48 (SW 1088, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.633×** | -3.3 | 0.050 | 30/48 (RPMI-7951, HT-29, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.670×** | -3.1 | 0.078 | 27/47 (NCI-H23, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.383×** | -3.1 | 0.088 | 24/47 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 602. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 37.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 33.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -11.1) |
| [[A-427 (line)]] | wt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -10.4) |
| [[C32 (line)]] | wt | 49.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -8.6) |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -8.9) |
| [[HOP62 (line)]] | alt | 33.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -9.5) |
| [[HS-578T (line)]] | alt | 48.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -8.5) |
| [[HT-29 (line)]] | alt | 24.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -8.9) |
| [[KATO III (line)]] | alt | 25.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.3) |
| [[SNU-1 (line)]] | wt | 57.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -13.2) |
| [[SW 900 (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -8.5) |
| [[A-172 (line)]] | wt | 72.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 602), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLH]] | +0.72 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[DPM3]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[SIRT2]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[SERF2]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[PPM1D]] | +0.65 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[FDXR]] | +0.65 | +0.53 / +0.71 | both halves | 1e-05 | STRING 505 |
| [[MIF]] | +0.65 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ZNF654]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[CNNM2]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[FKBP2]] ⚠ | +0.65 | +0.59 / +0.66 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[DDB2]] | +0.64 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[NDUFB11]] ⚠ | +0.64 | +0.60 / +0.65 | both halves | 7e-06 | STRING 569; ⚠ in the vector space only through flagged drug-doses |
| [[TMEM134]] | +0.64 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[TRIM7-AS2]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | -0.73 | -0.70 / -0.72 | both halves | 7e-06 |  |
| [[CCT2]] | -0.69 | -0.70 / -0.69 | both halves | 7e-06 |  |
| [[CCT6A]] | -0.64 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[PTPN11]] | -0.62 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[CCT3]] | -0.61 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[PSMD12]] | -0.61 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[STIP1]] | -0.60 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[NUDC]] | -0.59 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[SLC25A24]] | -0.59 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[MAK16]] | -0.59 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.59 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[TMX3]] | -0.59 | -0.56 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-22.7, -31.9); signed map (-28.5, 10.4). **Vector** length 81.4, 26.6% of its response variance represented; |z| ≥ 3 in 642 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +2.2 | -1.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.9 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.9 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.9 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.6 | -4.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.6 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | -1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | +0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphohistidine phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,848,724-136,851,027 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PHP14, HSPC141, CGI-202, DKFZp564M173, bA216L13.10 |
| Gene groups (HGNC) | Protein phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRX4](https://www.uniprot.org/uniprotkb/Q9NRX4) (14 kDa phosphohistidine phosphatase):

> Exhibits phosphohistidine phosphatase activity.

**Summary**, from NCBI Gene [29085](https://www.ncbi.nlm.nih.gov/gene/29085):

> This gene encodes an enzyme that catalyzes the reversible dephosphorylation of histidine residues in proteins. It may be involved in the dephosphorylation of G-beta and ATP citrate lyase and in negatively regulating CD4 T lymphocytes by dephosphorylation and inhibition of KCa3.1 channels. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:30033](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30033) · Entrez [29085](https://www.ncbi.nlm.nih.gov/gene/29085) · UniProt [Q9NRX4](https://www.uniprot.org/uniprotkb/Q9NRX4) · Ensembl [ENSG00000054148](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054148)

## Data

Gene col 602: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 602); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 602, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 602]; `tensor/DDL_lfc|DDL_z.npy` [602]; `embed/gene_vectors.npy` [602]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 602 or target_col == 602). Every well: [[PHPT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHPT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
