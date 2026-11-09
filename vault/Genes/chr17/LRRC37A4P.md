---
symbol: "LRRC37A4P"
type: "gene"
col: 13202
ensembl_id: "ENSG00000214425"
name: "leucine rich repeat containing 37 member A4, pseudogene"
location: "17q21.31"
module: 68
arm: "+"
pooled_cpm: 7.44
n_lines_expressing: 42
n_dd_up: 2
n_dd_down: 25
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# LRRC37A4P

*leucine rich repeat containing 37 member A4, pseudogene* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.17× (z +6.7, q 1e-08, up in 14 of 40 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 1.49× (z +4.7, q 6e-04, up in 14 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.353× (z -12.4, q 9e-33, down in 34 of 39 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGME1]] (+0.60, fdr 4e-05), [[HOXA7]] (+0.56, fdr 8e-05), [[ANKRD18A]] (+0.55, fdr 2e-04); moves opposite to [[KCTD21]] (-0.59, fdr 6e-05), [[TMEM41B]] (-0.56, fdr 9e-05), [[NEAT1]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 068]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13202.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +6.7 | 1e-08 | 14/40 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +4.7 | 6e-04 | 14/38 (KATO III, A-427, …) | two highest doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.060 | 11/38 (KATO III, A549, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13202.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.353×** | -12.4 | 9e-33 | 34/39 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.370×** | -11.9 | 4e-30 | 34/39 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.389×** | -11.3 | 3e-27 | 33/39 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.503×** | -8.2 | 3e-14 | 26/38 (SW 900, HepG2/C3A, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.500×** | -7.8 | 5e-13 | 25/36 (HEC-1-A, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.532×** | -7.5 | 4e-12 | 24/39 (J82, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.537×** | -7.4 | 8e-12 | 20/35 (MIA PaCa-2, HCT15, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.539×** | -7.1 | 8e-11 | 16/28 (A549, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.689×** | -6.3 | 2e-08 | 22/36 (HEC-1-A, MIA PaCa-2, …) | two highest doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.595×** | -6.2 | 3e-08 | 22/39 (LoVo, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.609×** | -5.9 | 2e-07 | 20/39 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.712×** | -5.7 | 4e-07 | 18/39 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.619×** | -5.5 | 2e-06 | 18/38 (MIA PaCa-2, A549, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.661×** | -5.0 | 3e-05 | 16/39 (NCI-H460, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.665×** | -4.7 | 1e-04 | 16/31 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.695×** | -4.4 | 5e-04 | 13/38 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.721×** | -3.9 | 0.003 | 12/36 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.019 | 13/39 (NCI-H661, CHP-212, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.823×** | -3.3 | 0.023 | 7/39 (HCT15, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.0 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -12.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.138× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 21.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -10.5) |
| [[SW480 (line)]] | alt | 15.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -12.2) |
| [[A-172 (line)]] | wt | 9.07 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -9.2) |
| [[A-427 (line)]] | wt | 7.69 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0700× (z -11.5) |
| [[A549 (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.1) ⚠ cell-cycle shift, explains ~56% of this change |
| [[CFPAC-1 (line)]] | alt | 6.64 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -8.6) |
| [[HT-29 (line)]] | alt | 3.77 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.0700× (z -9.0) |
| [[J82 (line)]] | alt | 9.16 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.165× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 3.50 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0693× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.119× (z -10.8) ⚠ toxic |
| [[SW 900 (line)]] | alt | 5.02 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0553× (z -9.6) |
| [[A498 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.925 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGME1]] | +0.60 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[HOXA7]] | +0.56 | +0.46 / +0.37 | both halves | 8e-05 |  |
| [[ANKRD18A]] | +0.55 | +0.49 / +0.29 | both halves | 2e-04 |  |
| [[TNPO2]] | +0.54 | +0.45 / +0.30 | both halves | 2e-04 |  |
| [[ZNF700]] | +0.53 | +0.45 / +0.33 | both halves | 1e-04 |  |
| [[UBTF]] | +0.52 | +0.29 / +0.40 | both halves | 2e-04 |  |
| [[NNT-AS1]] | +0.52 | +0.33 / +0.36 | both halves | 1e-04 |  |
| [[PRIMPOL]] | +0.52 | +0.40 / +0.36 | both halves | 9e-05 |  |
| [[ARID1A]] | +0.51 | +0.36 / +0.34 | both halves | 1e-04 |  |
| [[RMI2]] | +0.51 | +0.45 / +0.37 | both halves | 8e-05 |  |
| [[FOXP4-AS1]] | +0.51 | +0.41 / +0.28 | both halves | 3e-04 |  |
| [[CASD1]] | +0.50 | +0.32 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD21]] | -0.59 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[TMEM41B]] | -0.56 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[NEAT1]] | -0.54 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[YIPF1]] | -0.54 | -0.45 / -0.21 | both halves | 6e-04 |  |
| [[MKNK1]] | -0.52 | -0.29 / -0.37 | both halves | 2e-04 |  |
| [[SEC22B]] | -0.50 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[PLPPR2]] | -0.50 | -0.17 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[TMEM184B]] | -0.50 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[PSME4]] | -0.49 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[SYP]] | -0.49 | -0.18 / -0.50 | ⚠ not reproduced | 1e-03 |  |
| [[SIPA1]] | -0.49 | -0.32 / -0.29 | both halves | 3e-04 |  |
| [[WIPI1]] | -0.49 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[OAZ1]] | -0.49 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[CLINT1]] | -0.49 | -0.41 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.364). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-0.0, 6.9); signed map (28.0, -27.0). **Vector** length 53.0, 7.68% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +1.8 | -5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | -1.6 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.0 | +2.2 |
|  | [[Afatinib (drug)]] 5 µM |  | +0.9 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.7 | -4.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.5 | -11.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -8.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 37 member A4, pseudogene |
| Locus type | pseudogene |
| Location | 17q21.31 — chr17:45,508,109-45,550,335 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | FLJ10120; previously LRRC37A4 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25479](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25479) · Entrez [55073](https://www.ncbi.nlm.nih.gov/gene/55073) · Ensembl [ENSG00000214425](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214425)

## Data

Gene col 13202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13202); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13202]; `tensor/DDL_lfc|DDL_z.npy` [13202]; `embed/gene_vectors.npy` [13202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13202 or target_col == 13202). Every well: [[LRRC37A4P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC37A4P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
