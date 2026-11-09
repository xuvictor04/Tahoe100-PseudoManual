---
symbol: "PLSCR3"
type: "gene"
col: 11955
ensembl_id: "ENSG00000187838"
name: "phospholipid scramblase 3"
location: "17p13.1"
module: 2
arm: "+"
pooled_cpm: 6.23
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PLSCR3

*phospholipid scramblase 3* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.61× (z +10.0, q 8e-21, up in 24 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.42× (z +3.5, q 0.066, up in 10 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 5.10×, A498 5.15×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.520× (z -9.7, q 2e-19, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STUB1]] (+0.64, fdr 3e-05), [[RIC8A]] (+0.63, fdr 7e-06), [[MFSD10]] (+0.61, fdr 1e-05); moves opposite to [[HNMT]] (-0.56, fdr 3e-05), [[PNISR]] (-0.50, fdr 2e-04), [[RPRD2]] (-0.49, fdr 3e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11955.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 5.10×, A498 5.15×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +10.0 | 8e-21 | 24/27 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +8.8 | 4e-16 | 10/12 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +5.9 | 5e-07 | 13/20 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.066 | 10/45 (AsPC-1, KATO III, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.39×** | +3.4 | 0.066 | 7/34 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.093 | 8/45 (PANC-1, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11955.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.520×** | -9.7 | 2e-19 | 30/41 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.503×** | -7.2 | 2e-10 | 24/38 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.551×** | -6.2 | 8e-08 | 24/45 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.591×** | -5.5 | 5e-06 | 26/47 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.630×** | -4.8 | 1e-04 | 17/45 (C-33 A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.704×** | -3.5 | 0.037 | 14/45 (LOX-IMVI, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.717×** | -3.5 | 0.038 | 18/46 (RPMI-7951, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | **0.725×** | -3.4 | 0.050 | 14/44 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.542×** | -3.4 | 0.050 | 11/40 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.555×** | -3.2 | 0.070 | 12/44 (AsPC-1, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 12.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 8.22 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 6.45 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0818× (z -14.1) |
| [[A498 (line)]] | wt | 7.44 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.15× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 8.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0763× (z -12.0) |
| [[LoVo (line)]] | wt | 3.06 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0534× (z -10.4) |
| [[LS 180 (line)]] | wt | 7.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -9.7) |
| [[RKO (line)]] | wt | 9.17 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 4.29 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0793× (z -9.2) |
| [[SW1417 (line)]] | alt | 5.06 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.103× (z -8.9) |
| [[A-172 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | +0.64 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[RIC8A]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[MFSD10]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[STK25]] | +0.60 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[TESK1]] | +0.58 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[HTRA2]] | +0.58 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[BCKDK]] | +0.58 | +0.60 / +0.38 | both halves | 7e-05 |  |
| [[PORCN]] | +0.57 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[GPS1]] | +0.56 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[CAP1]] | +0.56 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[RPUSD1]] | +0.56 | +0.42 / +0.31 | both halves | 2e-04 |  |
| [[ELOVL1]] | +0.56 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNMT]] | -0.56 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[PNISR]] | -0.50 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[RPRD2]] | -0.49 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[NAPEPLD]] | -0.49 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[DICER1-AS1]] | -0.48 | -0.51 / -0.21 | both halves | 6e-04 |  |
| [[GALNT7-DT]] | -0.47 | -0.45 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[NR1H3]] | -0.47 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[UNK]] | -0.46 | -0.50 / -0.10 | ⚠ not reproduced | 0.003 |  |
| [[NFYC]] | -0.46 | -0.45 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[TTC32]] | -0.46 | -0.43 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[CASP10]] | -0.46 | -0.40 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.601). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (15.1, -0.4); signed map (-25.9, 3.7). **Vector** length 50.6, 6.97% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.3 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.7 | -9.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.6 | -6.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Vandetanib (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | phospholipid scramblase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,389,727-7,394,842 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phospholipid scramblases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRY6](https://www.uniprot.org/uniprotkb/Q9NRY6) (Phospholipid scramblase 3):

> Catalyzes calcium-induced ATP-independent rapid bidirectional and non-specific movement of the phospholipids (lipid scrambling or lipid flip-flop) between the inner and outer membrane of the mitochondria. Plays an important role in mitochondrial respiratory function, morphology, and apoptotic response. Mediates the translocation of cardiolipin from the mitochondrial inner membrane to outer membrane enhancing t-Bid induced cytochrome c release and apoptosis. Enhances TNFSF10-induced apoptosis by …

**Summary**, from NCBI Gene [57048](https://www.ncbi.nlm.nih.gov/gene/57048):

> Enables calcium-dependent protein binding activity; metal ion binding activity; and phospholipid scramblase activity. Involved in several processes, including apoptotic process; mitochondrial membrane organization; and regulation of release of cytochrome c from mitochondria. Located in cytosol; mitochondrion; and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16495](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16495) · Entrez [57048](https://www.ncbi.nlm.nih.gov/gene/57048) · UniProt [Q9NRY6](https://www.uniprot.org/uniprotkb/Q9NRY6) · Ensembl [ENSG00000187838](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187838)

## Data

Gene col 11955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11955); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11955]; `tensor/DDL_lfc|DDL_z.npy` [11955]; `embed/gene_vectors.npy` [11955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11955 or target_col == 11955). Every well: [[PLSCR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLSCR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
