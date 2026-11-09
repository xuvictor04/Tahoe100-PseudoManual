---
symbol: "USF1"
type: "gene"
col: 8189
ensembl_id: "ENSG00000158773"
name: "upstream transcription factor 1"
location: "1q23.3"
module: 20
arm: "+"
pooled_cpm: 10.27
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# USF1

*upstream transcription factor 1* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +7.7, q 6e-12, up in 35 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (CFPAC-1 0.117×, HS-578T 0.0653×, NCI-H1792 0.106×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C32 0.0992×, A-172 0.131×, SW 900 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change); [[Vilanterol (drug)]] 0.5 µM in 2 lines (Panc 03.27 0.0820×, LOX-IMVI 0.0968×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (KATO III 0.0791×); [[Larotrectinib (drug)]] 0.5 µM in 1 line (LS 180 0.133×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LDB1]] (+0.74, fdr 7e-06), [[EOLA2]] (+0.67, fdr 7e-06), [[CIPC]] (+0.67, fdr 7e-06); moves opposite to [[EIF5B]] (-0.56, fdr 1e-05), [[MAP7D3]] (-0.54, fdr 3e-05), [[EIF3J]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8189.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +7.7 | 6e-12 | 35/43 (NCI-H2030, LoVo, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.77×** | +6.9 | 2e-09 | 42/47 (SW480, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.23×** | +6.8 | 3e-09 | 38/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **4.15×** | +6.3 | 5e-08 | 33/43 (C32, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +4.4 | 0.001 | 21/45 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +3.7 | 0.018 | 21/46 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.31× | +3.2 | 0.11 | 16/48 (MIA PaCa-2, BT-474, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.45× | +3.1 | 0.12 | 16/47 (C32, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8189.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (CFPAC-1 0.117×, HS-578T 0.0653×, NCI-H1792 0.106×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C32 0.0992×, A-172 0.131×, SW 900 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change); [[Vilanterol (drug)]] 0.5 µM in 2 lines (Panc 03.27 0.0820×, LOX-IMVI 0.0968×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (KATO III 0.0791×); [[Larotrectinib (drug)]] 0.5 µM in 1 line (LS 180 0.133×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.855× | -4.6 | 0.002 | 26/48 (COLO 205, SW1417, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.669× | -3.4 | 0.19 | 19/45 (SNU-423, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.686× | -3.2 | 0.27 | 13/34 (NCI-H1573, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~21% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8189. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 6.57 | 0 | 2 (1 ⚠) | — | [[Monocrotaline (drug)]] 0.05 µM 0.0791× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 0.5 µM 0.103× (z -8.8) |
| [[A-172 (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.136× (z -9.3) ⚠ toxic |
| [[C32 (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0992× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -10.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0653× (z -10.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 7.12 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0985× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 9.21 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0777× (z -9.0) ⚠ cell-cycle shift, explains ~49% of this change |
| [[LOX-IMVI (line)]] | wt | 5.82 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0968× (z -9.2) |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 1 | — | [[Larotrectinib (drug)]] 0.5 µM 0.133× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 21.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 9.06 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0820× (z -10.1) |
| [[SNU-423 (line)]] | alt | 6.90 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0982× (z -8.6) |
| [[SW 900 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[A-427 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8189), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDB1]] | +0.74 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[EOLA2]] | +0.67 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[CIPC]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[HLA-C]] | +0.66 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[NAXD]] | +0.66 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ANKRD30BL]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[C5orf15]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[HFM1]] | +0.63 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[HLA-H]] | +0.63 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[KLHL11]] | +0.62 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[CUL2]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[COPS7B]] | +0.61 | +0.70 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF5B]] | -0.56 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[MAP7D3]] | -0.54 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[EIF3J]] | -0.54 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[THOC2]] | -0.54 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[PILRB]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[NSRP1]] | -0.52 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[HORMAD2-AS1]] | -0.52 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[CAAP1]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[JMJD1C]] | -0.51 | -0.55 / -0.45 | both halves | 3e-05 | STRING 485 |
| [[SCFD1]] | -0.50 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[CCDC88A]] | -0.50 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[BCAN-AS1]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-19.0, -16.4); signed map (-20.1, -33.1). **Vector** length 81.8, 15.7% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +3.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.4 | +2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.0 | +1.1 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.8 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -4.5 | -1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.9 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | upstream transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,039,251-161,045,977 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UEF, MLTFI, bHLHb11 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Reactome | 6 pathways, smallest: Regulation of MITF-M-dependent genes involved in pigmentation; Estrogen-dependent gene expression; MITF-M-dependent gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P22415](https://www.uniprot.org/uniprotkb/P22415) (Upstream stimulatory factor 1):

> Transcription factor that binds to a symmetrical DNA sequence (E-boxes) (5'-CACGTG-3') that is found in a variety of viral and cellular promoters.

**Summary**, from NCBI Gene [7391](https://www.ncbi.nlm.nih.gov/gene/7391):

> This gene encodes a member of the basic helix-loop-helix leucine zipper family, and can function as a cellular transcription factor. The encoded protein can activate transcription through pyrimidine-rich initiator (Inr) elements and E-box motifs. This gene has been linked to familial combined hyperlipidemia (FCHL). Alternative splicing of this gene results in multiple transcript variants. A related pseudogene has been defined on chromosome 21. [provided by RefSeq, Feb 2013]

**Accessions** — [HGNC:12593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12593) · Entrez [7391](https://www.ncbi.nlm.nih.gov/gene/7391) · UniProt [P22415](https://www.uniprot.org/uniprotkb/P22415) · Ensembl [ENSG00000158773](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158773)

## Data

Gene col 8189: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8189); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8189, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8189]; `tensor/DDL_lfc|DDL_z.npy` [8189]; `embed/gene_vectors.npy` [8189]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8189 or target_col == 8189). Every well: [[USF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
