---
symbol: "C5orf22"
type: "gene"
col: 1341
ensembl_id: "ENSG00000082213"
name: "chromosome 5 open reading frame 22"
location: "5p13.3"
module: 1
arm: "+"
pooled_cpm: 25.49
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# C5orf22

*chromosome 5 open reading frame 22* — 5p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.87× (z +12.3, q 4e-32, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.737× (z -6.1, q 7e-07, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM209]] (+0.63, fdr 7e-06), [[NDUFAF5]] (+0.62, fdr 1e-05), [[ORC5]] (+0.60, fdr 1e-05); moves opposite to [[ELAVL3]] (-0.59, fdr 4e-05), [[MIR9-1HG]] (-0.59, fdr 1e-05), [[CCNP]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1341.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +12.3 | 4e-32 | 43/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +11.6 | 1e-28 | 41/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +9.7 | 5e-20 | 31/45 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.64×** | +9.7 | 5e-20 | 40/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.43×** | +9.1 | 7e-18 | 30/48 (HEC-1-A, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +8.8 | 2e-16 | 27/47 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +7.3 | 3e-11 | 29/48 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +7.0 | 1e-10 | 30/47 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +7.0 | 1e-10 | 30/48 (PANC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +6.0 | 1e-07 | 25/48 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +5.8 | 4e-07 | 19/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +5.6 | 8e-07 | 23/47 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +5.4 | 4e-06 | 20/48 (HOP62, C-33 A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.19× | +4.5 | 3e-04 | 18/48 (HT-29, KATO III, …) | top dose only | low cells (technical?) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.25×** | +4.3 | 6e-04 | 10/47 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.001 | 13/48 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.001 | 17/48 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.008 | 6/47 (COLO 205, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.014 | 10/48 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.028 | 6/47 (Hs 766T, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1341.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.737×** | -6.1 | 7e-07 | 23/48 (SW 900, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.808×** | -5.4 | 2e-05 | 22/47 (SHP-77, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -3.8 | 0.023 | 12/48 (SNU-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.766×** | -3.8 | 0.023 | 14/48 (SHP-77, LoVo, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.840× | -3.5 | 0.057 | 10/48 (A498, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1341. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 71.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 40.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -10.2) |
| [[BT-474 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.253× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.312× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1341), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM209]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[NDUFAF5]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ORC5]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PROSER1]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[RRP36]] | +0.59 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[XPO7]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[VPS50]] | +0.58 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[TRAPPC11]] | +0.57 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[RNF25]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[AP3S2]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[AP3M1]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[RBM45]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELAVL3]] | -0.59 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[MIR9-1HG]] | -0.59 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[CCNP]] | -0.54 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[TXK]] | -0.54 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[AVIL]] | -0.53 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[CATSPERG]] | -0.52 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[TRIM72]] | -0.52 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[PEAK1]] | -0.52 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[KIF17]] | -0.52 | -0.33 / -0.60 | both halves | 1e-04 |  |
| [[PRKCG]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[CPNE9]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[MASP2]] | -0.51 | -0.29 / -0.55 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.349). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.8, -2.2); signed map (-25.6, -17.9). **Vector** length 80.2, 15.8% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +9.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +9.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.6 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +5.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.6 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | +8.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -2.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 5 open reading frame 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.3 — chr5:31,532,287-31,555,053 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11193 |
| Matched by | ensembl_id |

UniProt [Q49AR2](https://www.uniprot.org/uniprotkb/Q49AR2) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25639](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25639) · Entrez [55322](https://www.ncbi.nlm.nih.gov/gene/55322) · UniProt [Q49AR2](https://www.uniprot.org/uniprotkb/Q49AR2) · Ensembl [ENSG00000082213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082213)

## Data

Gene col 1341: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1341); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1341, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1341]; `tensor/DDL_lfc|DDL_z.npy` [1341]; `embed/gene_vectors.npy` [1341]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1341 or target_col == 1341). Every well: [[C5orf22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C5orf22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
