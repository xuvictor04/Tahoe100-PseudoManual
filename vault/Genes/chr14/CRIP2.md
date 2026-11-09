---
symbol: "CRIP2"
type: "gene"
col: 11328
ensembl_id: "ENSG00000182809"
name: "cysteine rich protein 2"
location: "14q32.33"
module: 5
arm: "-"
pooled_cpm: 12.88
n_lines_expressing: 39
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# CRIP2

*cysteine rich protein 2* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.35× (z +8.6, q 3e-15, up in 24 of 28 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (PANC-1 7.58×, NCI-H1573 15.7×, KATO III 7.65×, C32 6.51×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 5.87×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.430× (z -6.0, q 1e-06, down in 21 of 32 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDAH2]] (+0.66, fdr 1e-05), [[LMNA]] (+0.62, fdr 2e-05), [[GNAI2]] (+0.59, fdr 3e-05); moves opposite to [[ALG8]] (-0.57, fdr 4e-05), [[ANAPC1]] (-0.54, fdr 4e-05), [[NSMAF]] (-0.54, fdr 6e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11328.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (PANC-1 7.58×, NCI-H1573 15.7×, KATO III 7.65×, C32 6.51×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 5.87×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.35×** | +8.6 | 3e-15 | 24/28 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +7.0 | 7e-10 | 17/19 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +5.1 | 7e-05 | 14/24 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +3.7 | 0.030 | 5/37 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 2.15× | +3.1 | 0.18 | 16/26 (NCI-H1573, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11328.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.430×** | -6.0 | 1e-06 | 21/32 (A-427, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.585×** | -5.4 | 2e-05 | 20/31 (SK-MEL-2, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.464×** | -5.2 | 5e-05 | 22/35 (SK-MEL-2, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.503×** | -4.9 | 1e-04 | 23/36 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.515×** | -4.7 | 3e-04 | 21/36 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.531×** | -4.5 | 6e-04 | 20/35 (BT-474, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.567×** | -4.0 | 0.004 | 21/36 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.592×** | -3.7 | 0.014 | 20/35 (BT-474, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.614×** | -3.5 | 0.032 | 20/35 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.623×** | -3.4 | 0.043 | 16/36 (J82, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.638×** | -3.2 | 0.070 | 16/36 (HT-29, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 41.0 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.113× (z -11.6) |
| [[HT-29 (line)]] | alt | 33.3 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -16.2) |
| [[CFPAC-1 (line)]] | alt | 49.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -10.0) |
| [[KATO III (line)]] | alt | 12.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.65× (z +8.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 12.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 7.65 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 15.7× (z +10.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -10.3) |
| [[PANC-1 (line)]] | alt | 17.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.58× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0739× (z -16.7) |
| [[A-172 (line)]] | wt | 53.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.263× (z -8.7) |
| [[A-427 (line)]] | wt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -10.3) |
| [[C32 (line)]] | wt | 23.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.51× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.179× (z -8.6) |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0452× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.989 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.54 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDAH2]] | +0.66 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[LMNA]] | +0.62 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[GNAI2]] | +0.59 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[KMT2C]] | +0.58 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[MYADM]] | +0.58 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[KLF2]] | +0.57 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[FAM89B]] | +0.57 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[RRAS]] | +0.56 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[FOXO6]] | +0.56 | +0.42 / +0.36 | both halves | 9e-05 |  |
| [[CDKN2D]] | +0.55 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[AGPAT2]] | +0.54 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[TFEB]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG8]] | -0.57 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ANAPC1]] | -0.54 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[NSMAF]] | -0.54 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[TRNT1]] | -0.54 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[PRMT3]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[RCC1L]] | -0.52 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[DCTD]] | -0.51 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[HDDC2]] | -0.51 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[SUCLG2]] | -0.51 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[DNAJC11]] | -0.51 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[METTL3]] | -0.50 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[YARS2]] | -0.50 | -0.40 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.488). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (22.1, 0.5); signed map (-18.4, 22.6). **Vector** length 69.5, 16.4% of its response variance represented; |z| ≥ 3 in 660 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.2 | +1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.2 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.0 | -5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.4 | -4.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | cysteine rich protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:105,472,962-105,480,162 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CRP2, ESP1 |
| Gene groups (HGNC) | LIM domain containing |
| Hallmark sets | COAGULATION |
| Matched by | ensembl_id |

UniProt [P52943](https://www.uniprot.org/uniprotkb/P52943) carries no function annotation.

**Summary**, from NCBI Gene [1397](https://www.ncbi.nlm.nih.gov/gene/1397):

> This gene encodes a putative transcription factor with two LIM zinc-binding domains. The encoded protein may participate in the differentiation of smooth muscle tissue. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:2361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2361) · Entrez [1397](https://www.ncbi.nlm.nih.gov/gene/1397) · UniProt [P52943](https://www.uniprot.org/uniprotkb/P52943) · Ensembl [ENSG00000182809](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182809)

## Data

Gene col 11328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11328); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11328]; `tensor/DDL_lfc|DDL_z.npy` [11328]; `embed/gene_vectors.npy` [11328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11328 or target_col == 11328). Every well: [[CRIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
