---
symbol: "ALG3"
type: "gene"
col: 13178
ensembl_id: "ENSG00000214160"
name: "ALG3 alpha-1,3- mannosyltransferase"
location: "3q27.1"
module: 33
arm: "+"
pooled_cpm: 12.61
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# ALG3

*ALG3 alpha-1,3- mannosyltransferase* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.91× (z +7.6, q 2e-11, up in 29 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.28× (z +5.1, q 4e-05, up in 21 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.528× (z -10.7, q 5e-24, down in 38 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (SK-MEL-2 0.291×, PANC-1 0.389×, A498 0.402×, AsPC-1 0.213×, …); [[Cobimetinib (drug)]] 5 µM in 2 lines (NCI-H2030 0.0799×, HepG2/C3A 0.0603×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.139×; ⚠ cell-cycle shift, explains ~0% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H2030 0.0877×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAA20]] (+0.71, fdr 7e-06), [[TOMM70]] (+0.69, fdr 7e-06), [[EARS2]] (+0.64, fdr 1e-05); moves opposite to [[WBP4]] (-0.57, fdr 3e-05), [[UPF3B]] (-0.57, fdr 2e-05), [[NOTCH2NLB]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13178.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.91×** | +7.6 | 2e-11 | 29/38 (A498, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.74×** | +6.3 | 1e-07 | 14/20 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +5.7 | 2e-06 | 8/48 (A498, KATO III, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.5 | 4e-06 | 27/40 (SW1417, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.28×** | +5.1 | 4e-05 | 21/43 (HS-578T, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.36×** | +5.0 | 4e-05 | 23/45 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +4.5 | 5e-04 | 21/46 (NCI-H23, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.45×** | +4.3 | 0.001 | 20/41 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.63×** | +4.0 | 0.004 | 12/27 (SW480, A549, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +3.8 | 0.010 | 16/45 (NCI-H2347, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.34×** | +3.4 | 0.028 | 11/47 (SW480, A-172, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.51×** | +3.4 | 0.028 | 11/42 (SK-MEL-2, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.49×** | +3.4 | 0.033 | 7/45 (A498, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +3.3 | 0.033 | 14/47 (HS-578T, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.33×** | +3.3 | 0.033 | 18/47 (A-172, HOP62, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.058 | 9/47 (NCI-H1573, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13178.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (SK-MEL-2 0.291×, PANC-1 0.389×, A498 0.402×, AsPC-1 0.213×, …); [[Cobimetinib (drug)]] 5 µM in 2 lines (NCI-H2030 0.0799×, HepG2/C3A 0.0603×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.139×; ⚠ cell-cycle shift, explains ~0% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H2030 0.0877×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.528×** | -10.7 | 5e-24 | 38/46 (SK-MEL-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | 0.746× | -3.4 | 0.21 | 15/45 (NCI-H2030, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | 0.756× | -3.2 | 0.21 | 15/46 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.769× | -3.0 | 0.21 | 13/45 (C32, CHP-212, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM |  | 0.769× | -3.0 | 0.21 | 11/45 (SW48, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13178. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 4.47 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0799× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 23.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.8) |
| [[A498 (line)]] | wt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 7.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HepG2_C3A (line)]] | wt | 9.08 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0603× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 9.04 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -9.4) |
| [[PANC-1 (line)]] | alt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -10.2) |
| [[A-172 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13178), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA20]] | +0.71 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[TOMM70]] | +0.69 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[EARS2]] | +0.64 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[TFB2M]] | +0.63 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[POLR1B]] | +0.62 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[WDR3]] | +0.62 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[PHB1]] | +0.61 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[DEXI]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PTRH2]] | +0.60 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[NKRF]] | +0.60 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[WDR36]] | +0.60 | +0.69 / +0.40 | both halves | 5e-05 |  |
| [[DCAF13]] | +0.59 | +0.62 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP4]] | -0.57 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[UPF3B]] | -0.57 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[NOTCH2NLB]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[NOTCH2NLC]] | -0.54 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[CHMP4A]] | -0.51 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TIA1]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[GPS2]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[NOTCH2NLA]] | -0.50 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[RAB13]] | -0.50 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[PABPN1]] | -0.50 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[TFE3]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.634). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.1, -30.5); signed map (-14.8, -56.3). **Vector** length 70.4, 13.5% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.51 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.51 to 10); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +5.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +5.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +2.3 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.0 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.8 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -10.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.5 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ALG3 alpha-1,3- mannosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:184,242,301-184,249,548 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NOT56L, Not56, CDGS4, D16Ertd36e |
| Gene groups (HGNC) | Dolichyl D-mannosyl phosphate dependent mannosyltransferases |
| Reactome | 5 pathways, smallest: Diseases associated with N-glycosylation of proteins; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92685](https://www.uniprot.org/uniprotkb/Q92685) (Dol-P-Man:Man(5)GlcNAc(2)-PP-Dol alpha-1,3-mannosyltransferase):

> Dol-P-Man:Man(5)GlcNAc(2)-PP-Dol alpha-1,3-mannosyltransferase that operates in the biosynthetic pathway of dolichol-linked oligosaccharides, the glycan precursors employed in protein asparagine (N)-glycosylation. The assembly of dolichol-linked oligosaccharides begins on the cytosolic side of the endoplasmic reticulum membrane and finishes in its lumen. The sequential addition of sugars to dolichol pyrophosphate produces dolichol-linked oligosaccharides containing fourteen sugars, including …

**Summary**, from NCBI Gene [10195](https://www.ncbi.nlm.nih.gov/gene/10195):

> This gene encodes a member of the ALG3 family. The encoded protein catalyses the addition of the first dol-P-Man derived mannose in an alpha 1,3 linkage to Man5GlcNAc2-PP-Dol. Defects in this gene have been associated with congenital disorder of glycosylation type Id (CDG-Id) characterized by abnormal N-glycosylation. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2008]

**Accessions** — [HGNC:23056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23056) · Entrez [10195](https://www.ncbi.nlm.nih.gov/gene/10195) · UniProt [Q92685](https://www.uniprot.org/uniprotkb/Q92685) · Ensembl [ENSG00000214160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214160)

## Data

Gene col 13178: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13178); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13178, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13178]; `tensor/DDL_lfc|DDL_z.npy` [13178]; `embed/gene_vectors.npy` [13178]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13178 or target_col == 13178). Every well: [[ALG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
