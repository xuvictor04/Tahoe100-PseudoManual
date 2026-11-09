---
symbol: "ZFP62"
type: "gene"
col: 12262
ensembl_id: "ENSG00000196670"
name: "ZFP62 zinc finger protein"
location: "5q35.3"
module: 1
arm: "+"
pooled_cpm: 16.78
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ZFP62

*ZFP62 zinc finger protein* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.37× (z +4.0, q 0.029, up in 18 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.578× (z -10.1, q 5e-21, down in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.633× (z -5.9, q 4e-07, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF239]] (+0.70, fdr 7e-06), [[RFT1]] (+0.69, fdr 7e-06), [[COG8]] (+0.68, fdr 7e-06); moves opposite to [[TESK2]] (-0.61, fdr 1e-05), [[SIRT2]] (-0.60, fdr 1e-05), [[SELENOK]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12262.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.0 | 0.029 | 18/47 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.9 | 0.029 | 0/48 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.30× | +3.4 | 0.14 | 13/48 (A-172, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.30× | +3.1 | 0.25 | 16/46 (SK-MEL-2, LoVo, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12262.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.578×** | -10.1 | 5e-21 | 35/47 (PANC-1, COLO 205, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.499×** | -9.0 | 6e-17 | 37/46 (J82, C-33 A, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.530×** | -8.2 | 4e-14 | 37/48 (SW480, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.602×** | -6.6 | 7e-09 | 29/47 (C-33 A, RKO, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.633×** | -5.9 | 4e-07 | 27/47 (J82, BT-474, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.636×** | -5.9 | 4e-07 | 29/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.662×** | -5.3 | 7e-06 | 29/47 (LoVo, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.624×** | -5.2 | 1e-05 | 25/47 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.658×** | -4.6 | 2e-04 | 21/45 (PANC-1, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.705×** | -4.3 | 0.001 | 21/47 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.559×** | -3.9 | 0.004 | 18/38 (SK-MEL-2, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.748×** | -3.8 | 0.008 | 22/46 (SK-MEL-2, RPMI-7951, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.785×** | -3.1 | 0.071 | 12/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.713×** | -3.1 | 0.071 | 6/47 (SW480, Hs 766T, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **0.790×** | -3.1 | 0.084 | 4/48 (NCI-H661, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.9 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.171× (z -10.9) ⚠ cell-cycle shift, explains ~53% of this change |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -14.2) ⚠ cell-cycle shift, explains ~55% of this change |
| [[J82 (line)]] | alt | 18.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 22.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.0) ⚠ cell-cycle shift, explains ~55% of this change |
| [[C-33 A (line)]] | alt | 23.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0727× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 14.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.178× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 19.3 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 0.05 µM 0.130× (z -8.5) |
| [[SW480 (line)]] | alt | 20.9 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.278× (z -11.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -8.9) ⚠ cell-cycle shift, explains ~55% of this change |
| [[C32 (line)]] | wt | 8.89 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0765× (z -10.9) |
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -10.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.7) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.8) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H23 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 9.61 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.122× (z -8.7) |
| [[A498 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF239]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 | same gene group |
| [[RFT1]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[COG8]] | +0.68 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[B3GALT9]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[RPE]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[SCO1]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[DNAJC14]] | +0.64 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[RUVBL1]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[EXOSC2]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ZFP41]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 | same gene group |
| [[PRPF19]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TESK2]] | -0.61 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[SIRT2]] | -0.60 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[SELENOK]] | -0.60 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[CCDC65]] | -0.59 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[MFSD11]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[RASA4B]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[PHKG1]] | -0.55 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[SELENOW]] | -0.55 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.55 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[AHCYL1]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[MICU1]] | -0.53 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[INAFM1]] | -0.53 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.0, -35.2); signed map (-5.4, -42.7). **Vector** length 64.5, 10.4% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +0.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.6 | -0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -4.7 | -10.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.1 | -4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.0 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.9 | -5.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -5.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ZFP62 zinc finger protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:180,847,611-180,861,285 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34231, ZET, ZNF755 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NB50](https://www.uniprot.org/uniprotkb/Q8NB50) (Zinc finger protein 62 homolog):

> May play a role in differentiating skeletal muscle.

**Summary**, from NCBI Gene [643836](https://www.ncbi.nlm.nih.gov/gene/643836):

> Predicted to enable transcription cis-regulatory region binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23241](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23241) · Entrez [643836](https://www.ncbi.nlm.nih.gov/gene/643836) · UniProt [Q8NB50](https://www.uniprot.org/uniprotkb/Q8NB50) · Ensembl [ENSG00000196670](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196670)

## Data

Gene col 12262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12262); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12262]; `tensor/DDL_lfc|DDL_z.npy` [12262]; `embed/gene_vectors.npy` [12262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12262 or target_col == 12262). Every well: [[ZFP62 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP62.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
