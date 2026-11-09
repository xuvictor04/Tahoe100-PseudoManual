---
symbol: "MPND"
type: "gene"
col: 171
ensembl_id: "ENSG00000008382"
name: "MPN domain containing"
location: "19p13.3"
module: 3
arm: "+"
pooled_cpm: 3.8
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MPND

*MPN domain containing* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.79× (z +16.5, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.651× (z -5.2, q 1e-04, down in 15 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP131]] (+0.76, fdr 9e-06), [[MIGA2]] (+0.73, fdr 1e-05), [[AHDC1]] (+0.73, fdr 1e-05); moves opposite to [[ERCC6L2]] (-0.66, fdr 4e-05), [[ST7L]] (-0.63, fdr 4e-05), [[MCTS1]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 171.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.79×** | +16.5 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.05×** | +13.8 | 8e-41 | 41/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.62×** | +11.9 | 1e-30 | 37/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +7.9 | 3e-13 | 11/21 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +5.8 | 7e-07 | 15/37 (A498, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +4.8 | 1e-04 | 6/46 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +4.6 | 3e-04 | 11/39 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.5 | 4e-04 | 8/39 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +4.0 | 0.004 | 4/33 (LS 180, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.9 | 0.005 | 3/24 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.3 | 0.048 | 6/27 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.2 | 0.062 | 6/40 (HS-578T, SNU-423, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.074 | 3/39 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.081 | 2/42 (NCI-H2347, PANC-1) | inconsistent across doses | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.098 | 5/37 (C32, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.098 | 3/46 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Macitentan (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.098 | 2/42 (KATO III, SHP-77) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 171.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.651×** | -5.2 | 1e-04 | 15/44 (A-427, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.697×** | -4.5 | 0.002 | 11/37 (C-33 A, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Thymopentin (drug)]] 5 µM |  | **0.723×** | -3.9 | 0.017 | 7/45 (LOX-IMVI, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.740×** | -3.8 | 0.019 | 6/44 (SNU-423, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.741×** | -3.8 | 0.019 | 15/46 (SW 900, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Posaconazole (drug)]] 0.05 µM |  | 0.762× | -3.2 | 0.14 | 4/43 (hTERT-HPNE, C32, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.780× | -3.1 | 0.14 | 8/46 (C32, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.785× | -3.1 | 0.14 | 6/45 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.770× | -3.0 | 0.14 | 6/45 (COLO 205, SNU-423, …) | inconsistent across doses |  |
| [[Penfluridol (drug)]] 0.5 µM |  | 0.786× | -3.0 | 0.14 | 4/46 (SNU-1, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 171. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.14 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.65× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.0728× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[A-172 (line)]] | wt | 4.72 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.114× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 3.36 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0762× (z -8.5) ⚠ cell-cycle shift, explains ~19% of this change |
| [[SW1417 (line)]] | alt | 5.62 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0993× (z -9.2) |
| [[A-427 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 171), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP131]] | +0.76 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[MIGA2]] | +0.73 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.73 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[RAB40C]] | +0.72 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[SLC27A1]] | +0.71 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[DNAAF3]] | +0.70 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[RAB3A]] | +0.69 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[GNAI2]] | +0.68 | +0.50 / +0.37 | both halves | 7e-05 |  |
| [[HSDL1]] | +0.68 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.67 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.67 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[SLC26A6]] | +0.66 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.66 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[ST7L]] | -0.63 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[MCTS1]] | -0.62 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[TFAM]] | -0.61 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[TRMT5]] | -0.61 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[SMIM15]] | -0.61 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.61 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[DECR1]] | -0.60 | -0.40 / -0.29 | both halves | 2e-04 |  |
| [[ZBTB33]] | -0.60 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[RXYLT1]] | -0.60 | -0.40 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[CSTF3]] | -0.59 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[MCPH1]] | -0.59 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[WARS2-AS1]] | -0.59 | -0.30 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.4, -2.8); signed map (-35.4, 0.9). **Vector** length 47.7, 5.40% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +16.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +13.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | +11.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +7.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.1 | +2.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +3.1 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.0 | -0.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.2 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | MPN domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,343,527-4,360,086 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14981 |
| Gene groups (HGNC) | JAMM/MPN+ metallopeptidase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N594](https://www.uniprot.org/uniprotkb/Q8N594) (MPN domain-containing protein):

> Probable protease (By similarity). Acts as a sensor of N(6)-methyladenosine methylation on DNA (m6A): recognizes and binds m6A DNA, leading to its degradation. Binds only double strand DNA (dsDNA) in a sequence-independent manner (By similarity).

**Summary**, from NCBI Gene [84954](https://www.ncbi.nlm.nih.gov/gene/84954):

> Predicted to enable metallopeptidase activity and polyubiquitin modification-dependent protein binding activity. Predicted to be involved in double-strand break repair. Predicted to be part of BRCA1-A complex and BRISC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25934](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25934) · Entrez [84954](https://www.ncbi.nlm.nih.gov/gene/84954) · UniProt [Q8N594](https://www.uniprot.org/uniprotkb/Q8N594) · Ensembl [ENSG00000008382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008382)

## Data

Gene col 171: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 171); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 171, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 171]; `tensor/DDL_lfc|DDL_z.npy` [171]; `embed/gene_vectors.npy` [171]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 171 or target_col == 171). Every well: [[MPND — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPND.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
