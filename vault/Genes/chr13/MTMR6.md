---
symbol: "MTMR6"
type: "gene"
col: 6310
ensembl_id: "ENSG00000139505"
name: "myotubularin related protein 6"
location: "13q12.13"
module: 28
arm: "+"
pooled_cpm: 29.86
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# MTMR6

*myotubularin related protein 6* — 13q12.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.02× (z +17.2, q 0e+00, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SNU-1 0.127×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM199X]] (+0.64, fdr 1e-05), [[SCRN3]] (+0.63, fdr 7e-06), [[EXOC5]] (+0.62, fdr 1e-05); moves opposite to [[TMEM41A]] (-0.52, fdr 4e-05), [[EEF1D]] (-0.52, fdr 3e-05), [[PI4KAP2]] (-0.51, fdr 2e-04).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6310.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +17.2 | 0e+00 | 44/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +10.8 | 1e-24 | 42/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.87×** | +10.4 | 4e-23 | 43/48 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +8.5 | 2e-15 | 37/48 (SW480, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +8.4 | 6e-15 | 33/45 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.5 | 5e-09 | 26/48 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +6.5 | 7e-09 | 25/37 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +6.0 | 2e-07 | 27/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +5.8 | 4e-07 | 26/40 (MIA PaCa-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +5.4 | 3e-06 | 27/48 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.8 | 7e-05 | 22/47 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +4.5 | 4e-04 | 16/48 (COLO 205, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.1 | 0.002 | 14/48 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.18× | +4.1 | 0.002 | 18/48 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.0 | 0.002 | 19/48 (RKO, A-427, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.004 | 14/48 (COLO 205, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.010 | 17/48 (SW 900, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.033 | 11/48 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 5 µM |  | 1.20× | +3.0 | 0.072 | 5/48 (AsPC-1, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SNU-1 0.127×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 34.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +14.9) | — |
| [[A-427 (line)]] | wt | 21.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +9.4) | — |
| [[RKO (line)]] | wt | 44.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.4) | — |
| [[A549 (line)]] | wt | 25.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 31.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 26.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 54.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 39.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.9) | — |
| [[hTERT-HPNE (line)]] | wt | 29.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.5) | — |
| [[KATO III (line)]] | alt | 34.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.1) | — |
| [[LoVo (line)]] | wt | 23.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 48.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 39.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.127× (z -12.0) |
| [[SNU-423 (line)]] | alt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 29.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +8.7) | — |
| [[A-172 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM199X]] | +0.64 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[SCRN3]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[EXOC5]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[FAM114A2]] | +0.60 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[AASDHPPT]] | +0.60 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[TMEM128]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[PLEKHA3]] | +0.59 | +0.65 / +0.49 | both halves | 1e-05 | pathway: PI Metabolism |
| [[DCUN1D1]] | +0.59 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[GMFB]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ANXA7]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PEX1]] | +0.58 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[UBLCP1]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM41A]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[EEF1D]] | -0.52 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[PI4KAP2]] | -0.51 | -0.61 / -0.30 | both halves | 2e-04 |  |
| [[BIN3]] | -0.50 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[PI4KAP1]] | -0.49 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[ATAT1]] | -0.48 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[UXT]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[HIC2]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.524). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.7, 3.8); signed map (7.2, -27.6). **Vector** length 84.9, 17.9% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +17.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.9 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -3.6 | +2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +2.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -0.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | myotubularin related protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.13 — chr13:25,246,222-25,287,510 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Myotubularins; Phosphoinositide phosphatases |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y217](https://www.uniprot.org/uniprotkb/Q9Y217) (Phosphatidylinositol-3,5-bisphosphate 3-phosphatase MTMR6):

> Lipid phosphatase that specifically dephosphorylates the D-3 position of phosphatidylinositol 3-phosphate and phosphatidylinositol 3,5-bisphosphate, generating phosphatidylinositol and phosphatidylinositol 5-phosphate. Binds with high affinity to phosphatidylinositol 3,5-bisphosphate (PtdIns(3,5)P2) but also to phosphatidylinositol 3-phosphate (PtdIns(3)P), phosphatidylinositol 4-phosphate (PtdIns(4)P), and phosphatidylinositol 5-phosphate (PtdIns(5)P), phosphatidic acid and phosphatidylserine. …

**Summary**, from NCBI Gene [9107](https://www.ncbi.nlm.nih.gov/gene/9107):

> Enables phosphatidylinositol-3,5-bisphosphate phosphatase activity and phosphatidylinositol-3-phosphate phosphatase activity. Involved in phosphatidylinositol dephosphorylation. Located in cytoplasm and nuclear envelope. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7453) · Entrez [9107](https://www.ncbi.nlm.nih.gov/gene/9107) · UniProt [Q9Y217](https://www.uniprot.org/uniprotkb/Q9Y217) · Ensembl [ENSG00000139505](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139505)

## Data

Gene col 6310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6310); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6310]; `tensor/DDL_lfc|DDL_z.npy` [6310]; `embed/gene_vectors.npy` [6310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6310 or target_col == 6310). Every well: [[MTMR6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTMR6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
