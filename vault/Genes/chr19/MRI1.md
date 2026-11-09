---
symbol: "MRI1"
type: "gene"
col: 445
ensembl_id: "ENSG00000037757"
name: "methylthioribose-1-phosphate isomerase 1"
location: "19p13.13"
module: 30
arm: "+"
pooled_cpm: 10.77
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# MRI1

*methylthioribose-1-phosphate isomerase 1* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.92× (z +11.0, q 2e-25, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.608× (z -8.3, q 4e-14, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM185A]] (+0.73, fdr 7e-06), [[UBAC1]] (+0.68, fdr 1e-05), [[C12orf76]] (+0.68, fdr 1e-05); moves opposite to [[ERCC6L2]] (-0.63, fdr 4e-05), [[ENOX2]] (-0.62, fdr 6e-05), [[LINC01191]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 445.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +11.0 | 2e-25 | 36/47 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.82×** | +10.0 | 3e-21 | 36/47 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +8.8 | 2e-16 | 33/47 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +7.5 | 8e-12 | 11/22 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.4 | 2e-08 | 16/34 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +5.4 | 6e-06 | 16/38 (NCI-H2030, COLO 205, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.9 | 9e-05 | 11/47 (SW480, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +4.8 | 9e-05 | 12/47 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +4.7 | 2e-04 | 22/48 (A498, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 0.001 | 12/43 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.0 | 0.003 | 11/47 (hTERT-HPNE, NCI-H23, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.013 | 5/48 (Panc 03.27, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.6 | 0.015 | 8/48 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.038 | 2/42 (COLO 205, SW48) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.3 | 0.039 | 8/48 (A498, MIA PaCa-2, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.066 | 8/41 (HEC-1-A, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.084 | 2/47 (A-172, KATO III) | top dose only | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.089 | 1/47 (A498) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 445.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.608×** | -8.3 | 4e-14 | 25/47 (SNU-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.654×** | -6.8 | 2e-09 | 20/46 (SW 900, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.516×** | -5.8 | 1e-06 | 19/42 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.713×** | -5.7 | 2e-06 | 21/47 (A-427, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.596×** | -4.5 | 7e-04 | 19/47 (SW480, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.831×** | -4.4 | 0.001 | 20/46 (COLO 205, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -4.3 | 0.001 | 3/48 (SK-MEL-2, SW 1271, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.800×** | -3.7 | 0.013 | 14/47 (NCI-H2030, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.815×** | -3.4 | 0.037 | 17/43 (RPMI-7951, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.835× | -3.0 | 0.14 | 1/47 (SNU-1) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 445. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 2 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0672× (z -14.5) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 23.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.47× (z +9.2) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.34 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.152× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +10.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 9.22 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.155× (z -8.5) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 8.83 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -9.9) ⚠ cell-cycle shift, explains ~19% of this change |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.162× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -9.6) ⚠ cell-cycle shift, explains ~19% of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0986× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 8.42 | 0 | 1 | — | [[Rifaximin (drug)]] 0.5 µM 0.0562× (z -8.8) |
| [[A-172 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 445), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185A]] | +0.73 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[UBAC1]] | +0.68 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[C12orf76]] | +0.68 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.66 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[BRAT1]] | +0.66 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[STX7]] | +0.65 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[SUFU]] | +0.65 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SNX1]] | +0.64 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[OSBPL7]] | +0.64 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[FBXO44]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[ATPAF2]] | +0.64 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[MPND]] | +0.64 | +0.36 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.63 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[ENOX2]] | -0.62 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[LINC01191]] | -0.60 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[LINC02803]] | -0.59 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | -0.57 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[DGKH]] | -0.57 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[SLC2A9]] | -0.56 | -0.39 / -0.29 | both halves | 2e-04 |  |
| [[LINC00571]] | -0.56 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[SLC20A2]] | -0.56 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[E2F3]] | -0.56 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[MSRA]] | -0.56 | -0.42 / -0.45 | both halves | 4e-05 | STRING 443 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.736). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.9, -8.6); signed map (-31.5, -8.6). **Vector** length 55.8, 7.38% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.1 | +8.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +11.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +10.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +2.2 | +4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.5 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -2.7 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.5 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | methylthioribose-1-phosphate isomerase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:13,764,522-13,774,282 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3207, Ypr118w, mtnA, MRDI |
| Reactome | 3 pathways, smallest: Methionine salvage pathway; Sulfur amino acid metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BV20](https://www.uniprot.org/uniprotkb/Q9BV20) (Methylthioribose-1-phosphate isomerase):

> Catalyzes the interconversion of methylthioribose-1-phosphate (MTR-1-P) into methylthioribulose-1-phosphate (MTRu-1-P). Independently from catalytic activity, promotes cell invasion in response to constitutive RhoA activation by promoting FAK tyrosine phosphorylation and stress fiber turnover.

**Summary**, from NCBI Gene [84245](https://www.ncbi.nlm.nih.gov/gene/84245):

> This enzyme functions in the methionine salvage pathway by catalyzing the interconversion of methylthioribose-1-phosphate and methythioribulose-1-phosphate. Elevated expression of the encoded protein is associated with metastatic melanoma and this protein promotes melanoma cell invasion independent of its enzymatic activity. Mutations in this gene may be associated with vanishing white matter disease (VMWD). [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:28469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28469) · Entrez [84245](https://www.ncbi.nlm.nih.gov/gene/84245) · UniProt [Q9BV20](https://www.uniprot.org/uniprotkb/Q9BV20) · Ensembl [ENSG00000037757](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000037757)

## Data

Gene col 445: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 445); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 445, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 445]; `tensor/DDL_lfc|DDL_z.npy` [445]; `embed/gene_vectors.npy` [445]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 445 or target_col == 445). Every well: [[MRI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
