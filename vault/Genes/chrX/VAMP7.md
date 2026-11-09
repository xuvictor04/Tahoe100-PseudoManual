---
symbol: "VAMP7"
type: "gene"
col: 4519
ensembl_id: "ENSG00000124333"
name: "vesicle associated membrane protein 7"
location: "Xq28 and Yq12"
module: 57
arm: "+"
pooled_cpm: 43.14
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# VAMP7

*vesicle associated membrane protein 7* — Xq28 and Yq12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.99× (z +7.5, q 4e-11, up in 35 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.700× (z -10.5, q 7e-23, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (KATO III 0.479×, LOX-IMVI 0.462×, Hs 766T 0.467×, SW 900 0.475×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.169×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACP1]] (+0.68, fdr 7e-06), [[STARD3NL]] (+0.63, fdr 1e-05), [[SKIC3]] (+0.63, fdr 2e-05); moves opposite to [[HIVEP1]] (-0.65, fdr 1e-05), [[NOP56]] (-0.64, fdr 1e-05), [[TSC22D1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4519.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +7.5 | 4e-11 | 35/49 (A-427, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +7.3 | 1e-10 | 26/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +6.6 | 1e-08 | 29/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +6.4 | 2e-08 | 31/48 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +5.9 | 4e-07 | 26/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +5.8 | 8e-07 | 26/48 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +5.5 | 3e-06 | 24/48 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +5.4 | 6e-06 | 27/48 (HT-29, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.19× | +5.1 | 2e-05 | 21/48 (CFPAC-1, LoVo, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +4.8 | 9e-05 | 21/48 (SW480, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +4.7 | 1e-04 | 23/48 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +4.2 | 0.001 | 19/40 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +3.8 | 0.007 | 17/46 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.024 | 16/47 (NCI-H460, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.18× | +3.4 | 0.024 | 11/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.034 | 8/48 (J82, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.1 | 0.070 | 6/48 (A498, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4519.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (KATO III 0.479×, LOX-IMVI 0.462×, Hs 766T 0.467×, SW 900 0.475×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.169×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -10.5 | 7e-23 | 35/48 (KATO III, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.787×** | -4.8 | 5e-04 | 21/47 (HepG2/C3A, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.816×** | -4.2 | 0.005 | 20/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.839× | -3.7 | 0.037 | 15/47 (C32, HEC-1-A, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.852× | -3.3 | 0.080 | 12/48 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.894× | -3.3 | 0.080 | 9/48 (NCI-H2347, SW 1088, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 0.895× | -3.3 | 0.080 | 10/48 (CHP-212, SW 900, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.855× | -3.3 | 0.080 | 14/48 (CHP-212, NCI-H2347, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.860× | -3.1 | 0.11 | 8/48 (Panc 03.27, HOP62, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.864× | -3.0 | 0.14 | 8/48 (NCI-H460, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4519. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.3) | — |
| [[A-172 (line)]] | wt | 67.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 45.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.169× (z -9.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 52.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -9.5) |
| [[HT-29 (line)]] | alt | 55.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.42× (z +8.6) | — |
| [[KATO III (line)]] | alt | 49.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 46.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 70.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.95× (z +9.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 37.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.6) | — |
| [[SW 900 (line)]] | alt | 58.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -9.0) |
| [[A-427 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 39.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4519), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACP1]] | +0.68 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[STARD3NL]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.63 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[LONP2]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[CYB5R4]] | +0.62 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[SEL1L]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[VTI1B]] | +0.62 | +0.52 / +0.59 | both halves | 1e-05 | STRING 995 |
| [[RBL2]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[NDRG3]] | +0.61 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[TM9SF2]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[DYNC1LI2]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[ERP44]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP1]] | -0.65 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[NOP56]] | -0.64 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[TSC22D1]] | -0.64 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[KCNJ14]] | -0.62 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[SATB2]] | -0.60 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[PPRC1]] | -0.59 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[BAZ1A]] | -0.58 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ENDOG]] | -0.58 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ZCCHC3]] | -0.57 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[RPP25]] | -0.56 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[PWWP2A]] | -0.56 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[ZBED5]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.711). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.3, -5.8); signed map (-34.2, -14.5). **Vector** length 87.3, 18.5% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.5 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.9 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | -0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.3 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.7 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +0.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | vesicle associated membrane protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 and Yq12 — chrX:155,881,345-155,943,769 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VAMP-7, TI-VAMP; previously SYBL1 |
| Gene groups (HGNC) | Vesicle associated membrane proteins; Pseudoautosomal region 2 |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 11 pathways, smallest: Lysosome Vesicle Biogenesis; Interleukin-12 signaling; Interleukin-12 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P51809](https://www.uniprot.org/uniprotkb/P51809) (Vesicle-associated membrane protein 7):

> Involved in the targeting and/or fusion of transport vesicles to their target membrane during transport of proteins from the early endosome to the lysosome. Required for heterotypic fusion of late endosomes with lysosomes and homotypic lysosomal fusion. Required for calcium regulated lysosomal exocytosis. Involved in the export of chylomicrons from the endoplasmic reticulum to the cis Golgi. Required for exocytosis of mediators during eosinophil and neutrophil degranulation, and target cell …

**Summary**, from NCBI Gene [6845](https://www.ncbi.nlm.nih.gov/gene/6845):

> This gene encodes a transmembrane protein that is a member of the soluble N-ethylmaleimide-sensitive factor attachment protein receptor (SNARE) family. The encoded protein localizes to late endosomes and lysosomes and is involved in the fusion of transport vesicles to their target membranes. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:11486](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11486) · Entrez [6845](https://www.ncbi.nlm.nih.gov/gene/6845) · UniProt [P51809](https://www.uniprot.org/uniprotkb/P51809) · Ensembl [ENSG00000124333](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124333)

## Data

Gene col 4519: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4519); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4519, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4519]; `tensor/DDL_lfc|DDL_z.npy` [4519]; `embed/gene_vectors.npy` [4519]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4519 or target_col == 4519). Every well: [[VAMP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAMP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
