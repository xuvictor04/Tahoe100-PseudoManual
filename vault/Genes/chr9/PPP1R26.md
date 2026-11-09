---
symbol: "PPP1R26"
type: "gene"
col: 12203
ensembl_id: "ENSG00000196422"
name: "protein phosphatase 1 regulatory subunit 26"
location: "9q34.3"
module: 2
arm: "+"
pooled_cpm: 14.52
n_lines_expressing: 47
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PPP1R26

*protein phosphatase 1 regulatory subunit 26* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.05 µM: 1.47× (z +5.3, q 7e-05, up in 22 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.298× (z -25.3, q 0e+00, down in 39 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLCG1]] (+0.56, fdr 4e-05), [[TATDN2]] (+0.55, fdr 1e-05), [[CSK]] (+0.55, fdr 3e-05); moves opposite to [[FNDC3A]] (-0.48, fdr 4e-05), [[COX7B]] (-0.48, fdr 5e-05), [[PTPN2]] (-0.48, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12203.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.05 µM |  | **1.47×** | +5.3 | 7e-05 | 22/42 (AsPC-1, RKO, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.34×** | +4.4 | 0.003 | 14/38 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.043 | 11/43 (HCT15, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.35 | 11/41 (H4, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12203.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.298×** | -25.3 | 0e+00 | 39/44 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.344×** | -15.1 | 0e+00 | 38/43 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.460×** | -11.5 | 4e-28 | 33/44 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.473×** | -11.0 | 4e-26 | 32/44 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.485×** | -10.7 | 2e-24 | 30/44 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.515×** | -9.8 | 1e-20 | 26/41 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.553×** | -8.7 | 2e-16 | 27/44 (Panc 03.27, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.566×** | -8.4 | 4e-15 | 25/44 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.581×** | -8.0 | 9e-14 | 30/44 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.620×** | -7.0 | 1e-10 | 26/43 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.725×** | -4.7 | 1e-04 | 17/44 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.754×** | -4.0 | 0.003 | 15/39 (BT-474, NCI-H23, …) | top dose only | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.786×** | -3.5 | 0.019 | 10/44 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.641×** | -3.4 | 0.026 | 11/43 (AsPC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.803×** | -3.2 | 0.047 | 14/44 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 39.6 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -17.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.223× (z -17.0) |
| [[A-172 (line)]] | wt | 26.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -19.6) |
| [[NCI-H460 (line)]] | wt | 20.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -21.0) |
| [[SW480 (line)]] | alt | 18.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -16.4) |
| [[RKO (line)]] | wt | 26.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -13.9) |
| [[LoVo (line)]] | wt | 11.3 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0662× (z -17.2) |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 6.06 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0524× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.198× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 17.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -10.8) |
| [[A498 (line)]] | wt | 16.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -12.5) |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~21% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.162× (z -10.1) |
| [[C32 (line)]] | wt | 7.92 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0375× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 32.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -14.4) |
| [[HOP62 (line)]] | alt | 19.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -17.6) |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 9.36 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -10.4) |
| [[SNU-1 (line)]] | wt | 11.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.110× (z -8.6) |
| [[A-427 (line)]] | wt | 10.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.161× (z -9.0) |
| [[A549 (line)]] | wt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.7) |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -9.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 9.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 7.23 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0435× (z -11.1) |
| [[J82 (line)]] | alt | 27.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 6.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 9.23 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0985× (z -10.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 8.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -11.2) |
| [[SNU-423 (line)]] | alt | 7.84 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0820× (z -11.0) |
| [[SW1417 (line)]] | alt | 18.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -9.7) |
| [[SW48 (line)]] | wt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -9.1) |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLCG1]] | +0.56 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[TATDN2]] | +0.55 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[CSK]] | +0.55 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[LLGL1]] | +0.54 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[RNF4]] | +0.53 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[KIF26A]] | +0.53 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[ZFP69]] | +0.51 | +0.31 / +0.48 | both halves | 2e-04 |  |
| [[EPHB4]] | +0.51 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[TOR4A]] | +0.51 | +0.54 / +0.43 | both halves | 4e-05 |  |
| [[BRSK2]] | +0.51 | +0.48 / +0.39 | both halves | 6e-05 |  |
| [[ITPR3]] | +0.51 | +0.59 / +0.39 | both halves | 5e-05 | same gene group |
| [[INPP5E]] | +0.50 | +0.43 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNDC3A]] | -0.48 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[COX7B]] | -0.48 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[PTPN2]] | -0.48 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[AHI1]] | -0.47 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[B2M]] | -0.47 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[GTF2IRD2]] | -0.46 | -0.60 / -0.25 | both halves | 4e-04 |  |
| [[MAK]] | -0.46 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[TMEM167B]] | -0.46 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[ENSA]] | -0.45 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[BBOF1]] | -0.45 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[TMEM91]] | -0.45 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[TMEM205]] | -0.44 | -0.59 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.455). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.4, -19.7); signed map (-44.7, -13.4). **Vector** length 70.6, 12.3% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.8 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +0.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.7 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -25.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.5 | -15.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -11.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -8.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -8.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -0.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:135,479,079-135,488,893 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0649 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T8A7](https://www.uniprot.org/uniprotkb/Q5T8A7) (Protein phosphatase 1 regulatory subunit 26):

> Inhibits phosphatase activity of protein phosphatase 1 (PP1) complexes. May positively regulate cell proliferation.

**Summary**, from NCBI Gene [9858](https://www.ncbi.nlm.nih.gov/gene/9858):

> Predicted to enable protein phosphatase inhibitor activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29089](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29089) · Entrez [9858](https://www.ncbi.nlm.nih.gov/gene/9858) · UniProt [Q5T8A7](https://www.uniprot.org/uniprotkb/Q5T8A7) · Ensembl [ENSG00000196422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196422)

## Data

Gene col 12203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12203); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12203]; `tensor/DDL_lfc|DDL_z.npy` [12203]; `embed/gene_vectors.npy` [12203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12203 or target_col == 12203). Every well: [[PPP1R26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
