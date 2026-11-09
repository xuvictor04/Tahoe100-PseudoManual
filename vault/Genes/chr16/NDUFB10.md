---
symbol: "NDUFB10"
type: "gene"
col: 6474
ensembl_id: "ENSG00000140990"
name: "NADH:ubiquinone oxidoreductase subunit B10"
location: "16p13.3"
module: 24
arm: "+"
pooled_cpm: 27.37
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# NDUFB10

*NADH:ubiquinone oxidoreductase subunit B10* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.34× (z +9.9, q 3e-20, up in 42 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (LoVo 7.31×, PANC-1 6.17×, NCI-H460 7.66×, SW480 5.94×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 6.03×, LoVo 6.45×, A-172 4.93×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.415× (z -5.9, q 3e-06, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2I]] (+0.78, fdr 1e-05), [[THYN1]] (+0.77, fdr 7e-06), [[MRPS34]] (+0.77, fdr 1e-05); moves opposite to [[MIATNB]] (-0.62, fdr 3e-05), [[PRNP]] (-0.61, fdr 2e-04), [[SECISBP2]] (-0.60, fdr 0.002, ⚠ one half only (not replicated)), [[HCFC1]] (-0.59, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6474.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (LoVo 7.31×, PANC-1 6.17×, NCI-H460 7.66×, SW480 5.94×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 6.03×, LoVo 6.45×, A-172 4.93×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **4.34×** | +9.9 | 3e-20 | 42/42 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.79×** | +8.6 | 2e-15 | 37/37 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.28×** | +5.2 | 5e-05 | 35/40 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.89×** | +4.3 | 0.002 | 35/46 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.7 | 0.028 | 27/44 (CFPAC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.61× | +3.2 | 0.12 | 26/48 (HT-29, KATO III, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6474.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.415×** | -5.9 | 3e-06 | 43/48 (HT-29, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.515×** | -4.4 | 0.002 | 40/48 (SW 900, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.611×** | -4.4 | 0.002 | 34/47 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.580×** | -3.6 | 0.042 | 33/47 (SW 900, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.627× | -3.1 | 0.23 | 25/46 (H4, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 34.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.31× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 37.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.17× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 38.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.93× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A549 (line)]] | wt | 24.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.61× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HOP62 (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.67× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[Hs 766T (line)]] | wt | 37.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.99× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HT-29 (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[KATO III (line)]] | alt | 36.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.8× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H460 (line)]] | wt | 25.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.66× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW 900 (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW480 (line)]] | alt | 24.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.94× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-427 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 11 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2I]] | +0.78 | +0.54 / +0.78 | both halves | 1e-05 | STRING 432 |
| [[THYN1]] | +0.77 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[MRPS34]] | +0.77 | +0.54 / +0.72 | both halves | 1e-05 | STRING 502 |
| [[MRPL43]] | +0.71 | +0.43 / +0.68 | both halves | 3e-05 | STRING 416 |
| [[ATP5PO]] ⚠ | +0.69 | +0.42 / +0.72 | both halves | 4e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 860; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA8]] | +0.68 | +0.37 / +0.71 | both halves | 7e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[TSR3]] | +0.68 | +0.64 / +0.52 | both halves | 1e-05 | STRING 406 |
| [[SSNA1]] | +0.67 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[EHMT2]] | +0.67 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[BBS5]] | +0.67 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[NDUFA12]] | +0.66 | +0.39 / +0.60 | both halves | 6e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[TMEM256]] | +0.66 | +0.22 / +0.60 | both halves | 6e-04 |  |
| [[METTL26]] | +0.66 | +0.34 / +0.54 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIATNB]] | -0.62 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[PRNP]] | -0.61 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[SECISBP2]] | -0.60 | -0.11 / -0.62 | ⚠ one half (not replicated) | 0.002 |  |
| [[HCFC1]] | -0.59 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[DDX5]] | -0.58 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[SPON1-AS1]] | -0.57 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[SLC25A53]] | -0.55 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[SUSD1]] | -0.55 | -0.41 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-45.2, -14.1); signed map (-19.8, -6.9). **Vector** length 57.3, 17.1% of its response variance represented; |z| ≥ 3 in 556 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +2.2 | +3.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | -0.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +0.8 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -3.8 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -3.7 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -0.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit B10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,959,538-1,961,975 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PDSW |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O96000](https://www.uniprot.org/uniprotkb/O96000) (NADH dehydrogenase):

> Accessory subunit that is involved in the functional assembly of the mitochondrial respiratory chain complex I. Complex I has an NADH dehydrogenase activity with ubiquinone as an immediate electron acceptor and mediates the transfer of electrons from NADH to the respiratory chain.

**Summary**, from NCBI Gene [4716](https://www.ncbi.nlm.nih.gov/gene/4716):

> Predicted to enable NADH dehydrogenase (ubiquinone) activity. Predicted to be involved in mitochondrial electron transport, NADH to ubiquinone and proton motive force-driven mitochondrial ATP synthesis. Located in mitochondrial inner membrane. Part of respiratory chain complex I. Implicated in nuclear type mitochondrial complex I deficiency 35. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7696) · Entrez [4716](https://www.ncbi.nlm.nih.gov/gene/4716) · UniProt [O96000](https://www.uniprot.org/uniprotkb/O96000) · Ensembl [ENSG00000140990](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140990)

## Data

Gene col 6474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6474); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6474]; `tensor/DDL_lfc|DDL_z.npy` [6474]; `embed/gene_vectors.npy` [6474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6474 or target_col == 6474). Every well: [[NDUFB10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFB10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
