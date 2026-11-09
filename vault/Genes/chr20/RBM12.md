---
symbol: "RBM12"
type: "gene"
col: 14404
ensembl_id: "ENSG00000244462"
name: "RNA binding motif protein 12"
location: "20q11.22"
module: 3
arm: "-"
pooled_cpm: 40.5
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# RBM12

*RNA binding motif protein 12* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.32× (z +17.2, q 0e+00, up in 45 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (HEC-1-A 0.114×; ⚠ toxic); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW48 0.216×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0929×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THOC6]] (+0.71, fdr 7e-06), [[SRCAP]] (+0.71, fdr 7e-06), [[PUF60]] (+0.70, fdr 7e-06); moves opposite to [[MALSU1]] (-0.66, fdr 7e-06), [[PLEKHH3]] (-0.66, fdr 7e-06), [[VPS37D]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14404.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.32×** | +17.2 | 0e+00 | 45/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.95×** | +9.6 | 1e-19 | 44/48 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.95×** | +9.6 | 1e-19 | 42/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +7.7 | 2e-12 | 35/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +6.6 | 4e-09 | 33/47 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +6.4 | 2e-08 | 36/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +4.5 | 6e-04 | 28/47 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +4.4 | 6e-04 | 29/48 (NCI-H1792, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.4 | 6e-04 | 28/47 (C32, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.7 | 0.014 | 23/47 (HCT15, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +3.6 | 0.018 | 21/44 (SK-MEL-2, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.030 | 17/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14404.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (HEC-1-A 0.114×; ⚠ toxic); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW48 0.216×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0929×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.839× | -3.6 | 0.16 | 18/48 (J82, BT-474, …) | rises with dose |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.853× | -3.3 | 0.29 | 15/48 (HS-578T, HT-29, …) | rises with dose | position effect removed |
| [[Decitabine (drug)]] 0.5 µM |  | 0.805× | -3.0 | 0.46 | 12/47 (SNU-423, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14404. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 26.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +15.3) | — |
| [[AsPC-1 (line)]] | alt | 53.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 43.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.7) | [[Lonafarnib (drug)]] 5 µM 0.114× (z -10.8) ⚠ toxic |
| [[KATO III (line)]] | alt | 38.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 42.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +14.3) | — |
| [[NCI-H460 (line)]] | wt | 41.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +16.4) | — |
| [[Panc 03.27 (line)]] | alt | 51.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[PANC-1 (line)]] | alt | 29.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.8) | — |
| [[SW480 (line)]] | alt | 45.0 | 2 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.65× (z +10.1) | — |
| [[A498 (line)]] | wt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.9) | — |
| [[AN3 CA (line)]] | alt | 41.8 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0929× (z -9.3) |
| [[C32 (line)]] | wt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 40.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +12.9) | — |
| [[HOP62 (line)]] | alt | 34.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +16.6) | — |
| [[Hs 766T (line)]] | wt | 52.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 26.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +11.6) | — |
| [[HT-29 (line)]] | alt | 42.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.0) | — |
| [[J82 (line)]] | alt | 50.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 45.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 29.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 39.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 44.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 62.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 36.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 35.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 35.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 78.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.4) | — |
| [[SW48 (line)]] | wt | 46.7 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.216× (z -10.0) |
| [[A-427 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 65.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14404), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | +0.71 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[SRCAP]] | +0.71 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[PUF60]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 | same gene group |
| [[PLAGL2]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ELK4]] | +0.67 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PSME3]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[WDR77]] | +0.64 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[EIF4G1]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[TMEM185B]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ZNF655]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[PRRC2A]] | +0.63 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ARMC6]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALSU1]] | -0.66 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[PLEKHH3]] | -0.66 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[VPS37D]] | -0.66 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[RAB40C]] | -0.65 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[ELP2]] | -0.65 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[RAB6A]] | -0.64 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[SRP54]] | -0.63 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[CRYZL1]] | -0.63 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[MACO1]] | -0.62 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[TRIM7-AS2]] | -0.62 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[ARL3]] | -0.62 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | -0.62 | -0.49 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-17.7, -2.0); signed map (1.3, -33.0). **Vector** length 94.2, 22.2% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +17.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.0 | +9.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.7 | +3.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +2.7 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +2.0 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.7 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +0.9 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -3.6 | -3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.4 | -2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:35,648,925-35,664,956 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HRIHFB2091, KIAA0765, SWAN |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTZ6](https://www.uniprot.org/uniprotkb/Q9NTZ6) (RNA-binding protein 12):

> RNA binding protein. Acts as a repressor of the G protein-coupled receptor/cAMP/PKA signaling axis. Represses fetal hemoglobin expression through an unknown mechanism.

**Summary**, from NCBI Gene [10137](https://www.ncbi.nlm.nih.gov/gene/10137):

> This gene encodes a protein that contains several RNA-binding motifs, potential transmembrane domains, and proline-rich regions. This gene and the gene for copine I overlap at map location 20q11.21. Alternative splicing in the 5' UTR results in four transcript variants. All variants encode the same protein. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:9898](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9898) · Entrez [10137](https://www.ncbi.nlm.nih.gov/gene/10137) · UniProt [Q9NTZ6](https://www.uniprot.org/uniprotkb/Q9NTZ6) · Ensembl [ENSG00000244462](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244462)

## Data

Gene col 14404: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14404); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14404, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14404]; `tensor/DDL_lfc|DDL_z.npy` [14404]; `embed/gene_vectors.npy` [14404]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14404 or target_col == 14404). Every well: [[RBM12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
