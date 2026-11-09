---
symbol: "BUD31"
type: "gene"
col: 2732
ensembl_id: "ENSG00000106245"
name: "BUD31 spliceosome associated protein"
location: "7q22.1"
module: 41
arm: "+"
pooled_cpm: 55.14
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# BUD31

*BUD31 spliceosome associated protein* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.03× (z +9.7, q 3e-19, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.88× (z +6.1, q 8e-08, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDIT3]] (+0.74, fdr 7e-06), [[YIPF3]] (+0.70, fdr 9e-06), [[AKAP17A]] (+0.67, fdr 7e-06); moves opposite to [[VMA21]] (-0.64, fdr 1e-05), [[TMEM33]] (-0.56, fdr 3e-05), [[GOT2]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2732.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.03×** | +9.7 | 3e-19 | 42/48 (C32, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.28×** | +8.0 | 4e-13 | 42/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.95×** | +6.5 | 2e-08 | 45/48 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +6.1 | 8e-08 | 40/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.35×** | +6.1 | 8e-08 | 45/49 (RKO, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.88×** | +6.1 | 8e-08 | 44/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.1 | 8e-08 | 39/48 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.88×** | +5.9 | 3e-07 | 31/40 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.70×** | +5.1 | 2e-05 | 45/48 (SW480, SK-MEL-2, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.69×** | +4.9 | 6e-05 | 35/48 (NCI-H460, C32, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.65×** | +4.5 | 3e-04 | 33/44 (C-33 A, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.5 | 3e-04 | 34/47 (C32, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.59×** | +4.5 | 3e-04 | 32/47 (CFPAC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +4.4 | 5e-04 | 33/48 (A-427, LoVo, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.51×** | +3.8 | 0.005 | 30/47 (LoVo, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2732.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.800× | -3.0 | 0.95 | 27/49 (RKO, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2732. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 39.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +13.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.67× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 41.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +11.4) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[C32 (line)]] | wt | 85.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +15.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.39× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 56.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +13.2) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SW480 (line)]] | alt | 68.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[A-172 (line)]] | wt | 52.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +11.3) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[A549 (line)]] | wt | 40.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +8.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[HOP62 (line)]] | alt | 31.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.4) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[Hs 766T (line)]] | wt | 51.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.3) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 40.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.0) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[J82 (line)]] | alt | 44.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.5) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[LoVo (line)]] | wt | 64.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.5) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[LOX-IMVI (line)]] | wt | 39.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +8.9) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 55.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +13.2) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H1792 (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.2) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 50.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +11.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SNU-423 (line)]] | alt | 41.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +11.0) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SW 900 (line)]] | alt | 51.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.7) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[A-427 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 95.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 101 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 74.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2732), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDIT3]] | +0.74 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[YIPF3]] | +0.70 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[AKAP17A]] | +0.67 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[NRBF2]] | +0.65 | +0.76 / +0.50 | both halves | 1e-05 |  |
| [[PMM1]] | +0.64 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[HAX1]] | +0.63 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[ACBD3]] | +0.62 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[ARG2]] | +0.62 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[NFKBIL1]] | +0.62 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[COQ10B]] | +0.62 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[STX5-DT]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.64 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.56 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[GOT2]] | -0.55 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[ADAT2]] | -0.55 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[FUCA2]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[CLN6]] | -0.54 | -0.56 / -0.43 | both halves | 4e-05 |  |
| [[EIF5A]] | -0.54 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[TUBGCP4]] | -0.54 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[CDCA7]] | -0.53 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[CSE1L]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[HACD3]] | -0.53 | -0.69 / -0.34 | both halves | 1e-04 |  |
| [[RPE]] | -0.53 | -0.53 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (9.4, -41.2); signed map (-12.3, 5.2). **Vector** length 73.4, 22.1% of its response variance represented; |z| ≥ 3 in 723 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.0 | +9.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.5 | +6.1 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.7 | -0.3 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.6 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | +1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.6 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | +1.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.4 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | BUD31 spliceosome associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,408,641-99,419,616 (+) |
| Ensembl biotype | protein_coding |
| Also known as | YCR063W, EDG-2, EDG2, fSAP17, Cwc14; previously G10 |
| Gene groups (HGNC) | NTC associated proteins; Spliceosomal B complex; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P41223](https://www.uniprot.org/uniprotkb/P41223) (Protein BUD31 homolog):

> Involved in the pre-mRNA splicing process. May play a role as regulator of AR transcriptional activity; may increase AR transcriptional activity.

**Summary**, from NCBI Gene [8896](https://www.ncbi.nlm.nih.gov/gene/8896):

> Enables nuclear receptor binding activity and transcription coactivator activity. Involved in mRNA splicing, via spliceosome. Located in chromatin and nucleoplasm. Part of U2-type catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29629) · Entrez [8896](https://www.ncbi.nlm.nih.gov/gene/8896) · UniProt [P41223](https://www.uniprot.org/uniprotkb/P41223) · Ensembl [ENSG00000106245](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106245)

## Data

Gene col 2732: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2732); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2732, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2732]; `tensor/DDL_lfc|DDL_z.npy` [2732]; `embed/gene_vectors.npy` [2732]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2732 or target_col == 2732). Every well: [[BUD31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BUD31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
