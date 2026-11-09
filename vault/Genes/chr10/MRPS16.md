---
symbol: "MRPS16"
type: "gene"
col: 11254
ensembl_id: "ENSG00000182180"
name: "mitochondrial ribosomal protein S16"
location: "10q22.2"
module: 11
arm: "+"
pooled_cpm: 27.83
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MRPS16

*mitochondrial ribosomal protein S16* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.57× (z +10.5, q 6e-23, up in 36 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.50× (z +4.5, q 7e-04, up in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A498 3.73×, SNU-423 3.78×, NCI-H460 3.11×, PANC-1 2.57×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (KATO III 4.83×, NCI-H460 3.47×, HEC-1-A 3.95×, A498 3.31×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.435× (z -5.2, q 1e-04, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.330×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERCC4]] (+0.63, fdr 1e-05), [[MRPL58]] (+0.63, fdr 7e-06), [[DPH5]] (+0.62, fdr 7e-06); moves opposite to [[PBXIP1]] (-0.59, fdr 2e-05), [[LAPTM4A]] (-0.59, fdr 1e-05), [[SEMA6C]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11254.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A498 3.73×, SNU-423 3.78×, NCI-H460 3.11×, PANC-1 2.57×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (KATO III 4.83×, NCI-H460 3.47×, HEC-1-A 3.95×, A498 3.31×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +10.5 | 6e-23 | 36/42 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +10.0 | 3e-21 | 30/37 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.58×** | +5.0 | 1e-04 | 26/41 (SW480, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.48×** | +4.6 | 6e-04 | 29/46 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.5 | 7e-04 | 27/45 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +4.5 | 7e-04 | 31/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.002 | 25/47 (NCI-H23, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.45×** | +4.2 | 0.002 | 27/48 (SNU-423, A-172, …) | rises with dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.23×** | +3.4 | 0.037 | 21/48 (SK-MEL-2, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.12 | 15/48 (RPMI-7951, NCI-H1792, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.31× | +3.1 | 0.12 | 22/46 (NCI-H23, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11254.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.330×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.435×** | -5.2 | 1e-04 | 35/48 (H4, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.467×** | -4.7 | 7e-04 | 34/46 (LOX-IMVI, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11254. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 23.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 31.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 40.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -8.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 22.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +9.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 28.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +8.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 52.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 37.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11254), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC4]] | +0.63 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[MRPL58]] | +0.63 | +0.67 / +0.65 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 996 |
| [[DPH5]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[YTHDC2]] | +0.61 | +0.77 / +0.43 | both halves | 3e-05 |  |
| [[PYCR2]] | +0.61 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[CCAR1]] | +0.61 | +0.75 / +0.44 | both halves | 3e-05 |  |
| [[RPL7L1]] | +0.61 | +0.69 / +0.55 | both halves | 1e-05 | STRING 967 |
| [[ST7L]] | +0.61 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[ARL14EP]] | +0.61 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[AFG3L1P]] | +0.60 | +0.77 / +0.41 | both halves | 4e-05 |  |
| [[GLRX2]] | +0.60 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[DNAJC11]] | +0.59 | +0.67 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBXIP1]] | -0.59 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[LAPTM4A]] | -0.59 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[SEMA6C]] | -0.58 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[PCOLCE]] | -0.57 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[MOSPD3]] | -0.56 | -0.71 / -0.35 | both halves | 1e-04 |  |
| [[NUCB1]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.55 | -0.66 / -0.30 | both halves | 2e-04 |  |
| [[SEZ6L2]] | -0.55 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[OS9]] | -0.55 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[CD99]] | -0.55 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[CD46]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[ADIPOR1]] | -0.54 | -0.66 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-31.5, 5.5); signed map (14.0, -26.6). **Vector** length 56.8, 10.9% of its response variance represented; |z| ≥ 3 in 606 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.3 | +4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.1 | -5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -0.9 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.8 | -0.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -0.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,248,843-73,252,693 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-132, bS16m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9Y3D3](https://www.uniprot.org/uniprotkb/Q9Y3D3) carries no function annotation.

**Summary**, from NCBI Gene [51021](https://www.ncbi.nlm.nih.gov/gene/51021):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14048](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14048) · Entrez [51021](https://www.ncbi.nlm.nih.gov/gene/51021) · UniProt [Q9Y3D3](https://www.uniprot.org/uniprotkb/Q9Y3D3) · Ensembl [ENSG00000182180](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182180)

## Data

Gene col 11254: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11254); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11254, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11254]; `tensor/DDL_lfc|DDL_z.npy` [11254]; `embed/gene_vectors.npy` [11254]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11254 or target_col == 11254). Every well: [[MRPS16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
