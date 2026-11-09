---
symbol: "PROSER1"
type: "gene"
col: 4202
ensembl_id: "ENSG00000120685"
name: "proline and serine rich 1"
location: "13q13.3"
module: 1
arm: "+"
pooled_cpm: 20.96
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PROSER1

*proline and serine rich 1* — 13q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.77× (z +7.5, q 3e-11, up in 31 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.44× (z +5.0, q 1e-04, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.715× (z -6.5, q 4e-08, down in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 0.153×, LoVo 0.263×, RKO 0.266×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.110×, SW48 0.205×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.324×, NCI-H460 0.471×); [[Triclosan (drug)]] 0.5 µM in 1 line (NCI-H661 0.0578×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H2030 0.237×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AIFM1]] (+0.66, fdr 7e-06), [[PRPF19]] (+0.63, fdr 1e-05), [[BLTP3A]] (+0.62, fdr 7e-06); moves opposite to [[RABGEF1]] (-0.60, fdr 9e-06), [[ELL]] (-0.58, fdr 2e-05), [[TEX21P]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4202.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +7.5 | 3e-11 | 31/46 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +5.6 | 5e-06 | 29/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +5.0 | 1e-04 | 27/47 (SNU-423, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +4.8 | 2e-04 | 24/47 (H4, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +4.6 | 6e-04 | 23/47 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +3.9 | 0.010 | 22/47 (A-172, SNU-423, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.32×** | +3.8 | 0.014 | 17/47 (A-172, Hs 766T, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.015 | 19/47 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.081 | 9/47 (LOX-IMVI, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.081 | 14/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.081 | 6/47 (HOP62, HEC-1-A, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.097 | 15/48 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4202.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 0.153×, LoVo 0.263×, RKO 0.266×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.110×, SW48 0.205×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.324×, NCI-H460 0.471×); [[Triclosan (drug)]] 0.5 µM in 1 line (NCI-H661 0.0578×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H2030 0.237×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -6.5 | 4e-08 | 28/47 (SW48, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.783× | -3.2 | 0.34 | 14/34 (KATO III, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 38.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -9.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 31.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.51× (z +9.7) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 9.49 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -8.7) ⚠ toxic; transcription drop · without an alert: [[Pimozide (drug)]] 0.05 µM 0.237× (z -8.6) |
| [[SW48 (line)]] | wt | 38.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -9.5) |
| [[C-33 A (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -11.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 15.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 1 | — | [[Triclosan (drug)]] 0.5 µM 0.0578× (z -9.5) |
| [[RKO (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 39.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIFM1]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PRPF19]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[BLTP3A]] | +0.62 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[PTGES2]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TSEN15]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[POMK]] | +0.61 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[C5orf22]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[HEATR3]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MRPL3]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[POGK]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[KLHL2]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ATIC]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGEF1]] | -0.60 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[ELL]] | -0.58 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[TEX21P]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[TPT1-AS1]] | -0.56 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[PHKG1]] | -0.56 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[PAIP2]] | -0.55 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[KPNB1-DT]] | -0.55 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[ATP6V1D]] | -0.55 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[CATSPERG]] | -0.55 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[MICU1]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[RAB7A]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[CCDC65]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.0, -35.7); signed map (-15.3, -46.1). **Vector** length 79.5, 15.6% of its response variance represented; |z| ≥ 3 in 747 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.8 | +7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +5.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.8 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +4.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.9 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.8 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[9-ING-41 (drug)]] 0.05 µM |  | -1.4 | -1.1 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | proline and serine rich 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.3 — chr13:39,009,865-39,038,089 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA50D16.2, FLJ12661; previously C13orf23 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XN7](https://www.uniprot.org/uniprotkb/Q86XN7) (Proline and serine-rich protein 1):

> Mediates OGT interaction with and O-GlcNAcylation of TET2 to control TET2 stabilization at enhancers and CpG islands (CGIs).

**Summary**, from NCBI Gene [80209](https://www.ncbi.nlm.nih.gov/gene/80209):

> This gene encodes a conserved protein containing proline and serine rich regions. These regions may be important in protein-protein interactions. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:20291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20291) · Entrez [80209](https://www.ncbi.nlm.nih.gov/gene/80209) · UniProt [Q86XN7](https://www.uniprot.org/uniprotkb/Q86XN7) · Ensembl [ENSG00000120685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120685)

## Data

Gene col 4202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4202); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4202]; `tensor/DDL_lfc|DDL_z.npy` [4202]; `embed/gene_vectors.npy` [4202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4202 or target_col == 4202). Every well: [[PROSER1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PROSER1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
