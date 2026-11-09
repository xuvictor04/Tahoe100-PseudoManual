---
symbol: "ATXN7L3B"
type: "gene"
col: 14835
ensembl_id: "ENSG00000253719"
name: "ataxin 7 like 3B"
location: "12q21.1"
module: 16
arm: "+"
pooled_cpm: 35.15
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ATXN7L3B

*ataxin 7 like 3B* — 12q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.43× (z +9.7, q 2e-19, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.749× (z -7.9, q 2e-12, down in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H1792 0.233×, NCI-H1573 0.362×, PANC-1 0.413×, J82 0.485×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A-172 0.325×, CHP-212 0.191×, LOX-IMVI 0.424×, SNU-1 0.329×; ⚠ cell-cycle shift, explains ~14% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.262×, SW48 0.227×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Orlistat (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.159×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL50]] (+0.61, fdr 1e-05), [[PURB]] (+0.59, fdr 2e-05), [[PAFAH2]] (+0.59, fdr 1e-05); moves opposite to [[TMEM50B]] (-0.51, fdr 5e-05), [[ZFAND2B]] (-0.51, fdr 6e-05), [[SGK3]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14835.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +9.7 | 2e-19 | 38/48 (A549, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.62×** | +9.6 | 2e-19 | 42/49 (SW480, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +8.1 | 8e-14 | 36/48 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +6.7 | 3e-09 | 29/48 (SW480, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +6.0 | 2e-07 | 28/47 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.38×** | +5.8 | 6e-07 | 30/47 (A-172, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +5.3 | 8e-06 | 24/43 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +4.6 | 3e-04 | 23/48 (LoVo, KATO III, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +4.5 | 3e-04 | 21/48 (LoVo, SW480, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.26×** | +4.4 | 6e-04 | 18/48 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +4.1 | 0.002 | 20/48 (A-172, LoVo, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.003 | 15/47 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled); position effect removed |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +3.8 | 0.007 | 11/48 (A549, NCI-H2347, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.20×** | +3.5 | 0.017 | 17/45 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.19× | +3.3 | 0.037 | 6/48 (NCI-H1792, SW 900, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.053 | 8/48 (PANC-1, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14835.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H1792 0.233×, NCI-H1573 0.362×, PANC-1 0.413×, J82 0.485×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A-172 0.325×, CHP-212 0.191×, LOX-IMVI 0.424×, SNU-1 0.329×; ⚠ cell-cycle shift, explains ~14% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.262×, SW48 0.227×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Orlistat (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.159×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.749×** | -7.9 | 2e-12 | 25/47 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.882× | -3.4 | 0.17 | 21/48 (A-172, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14835. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 82.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -22.7) |
| [[PANC-1 (line)]] | alt | 30.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 48.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.476× (z -9.2) |
| [[SNU-1 (line)]] | wt | 26.4 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0953× (z -12.6) ⚠ cell-cycle shift, explains ~8% of this change |
| [[A-172 (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -14.4) ⚠ cell-cycle shift, explains ~14% of this change |
| [[CHP-212 (line)]] | wt | 59.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -12.9) ⚠ cell-cycle shift, explains ~14% of this change |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.159× (z -8.8) |
| [[J82 (line)]] | alt | 29.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.3) |
| [[LoVo (line)]] | wt | 52.3 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +8.5) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[LOX-IMVI (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -11.7) ⚠ cell-cycle shift, explains ~14% of this change |
| [[NCI-H1573 (line)]] | alt | 43.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 36.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.43× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 44.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 38.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.46× (z +9.0) | — |
| [[A-427 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14835), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL50]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PURB]] | +0.59 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[PAFAH2]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ZNF808]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[RANBP6]] | +0.59 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[PLPP6]] | +0.58 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ZBTB40]] | +0.57 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[BBS10]] | +0.57 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[EID1]] | +0.57 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[TAF7]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[TSPYL4]] | +0.57 | +0.43 / +0.61 | both halves | 3e-05 | STRING 416 |
| [[SOCS4]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM50B]] | -0.51 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[ZFAND2B]] | -0.51 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[SGK3]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SLC25A29]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[LONRF1]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[TYK2]] | -0.49 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[HABP4]] | -0.48 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[SNHG12]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[PMM1]] | -0.46 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[CAMTA1]] | -0.46 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[ARFGAP3]] | -0.46 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[MGRN1]] | -0.45 | -0.43 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.505). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.8, 16.4); signed map (-0.8, -30.1). **Vector** length 87.6, 16.9% of its response variance represented; |z| ≥ 3 in 794 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.8 | +9.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -3.4 | -3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -2.5 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[AT7519 (drug)]] 5 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ataxin 7 like 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.1 — chr12:74,537,835-74,545,430 (+) |
| Ensembl biotype | protein_coding |
| Also known as | lnc-SCA7 |
| Gene groups (HGNC) | Ataxin 7 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GX2](https://www.uniprot.org/uniprotkb/Q96GX2) (Ataxin-7-like protein 3B):

> By binding to ENY2, interferes with the nuclear functions of the deubiquitinase (DUB) module of the SAGA complex which consists of ENY2, ATXN7, ATXN7L3 and the histone deubiquitinating component USP22. Affects USP22 DUB activity toward histones indirectly by changing the subcellular distribution of ENY2 and altering ENY2 availability for ATXN7L3 interaction. Regulates H2B monoubiquitination (H2Bub1) levels through cytoplasmic sequestration of ENY2 resulting in loss of nuclear ENY2-ATXN7L3 …

**Summary**, from NCBI Gene [552889](https://www.ncbi.nlm.nih.gov/gene/552889):

> Involved in regulation of gene expression. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:37931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37931) · Entrez [552889](https://www.ncbi.nlm.nih.gov/gene/552889) · UniProt [Q96GX2](https://www.uniprot.org/uniprotkb/Q96GX2) · Ensembl [ENSG00000253719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253719)

## Data

Gene col 14835: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14835); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14835, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14835]; `tensor/DDL_lfc|DDL_z.npy` [14835]; `embed/gene_vectors.npy` [14835]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14835 or target_col == 14835). Every well: [[ATXN7L3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATXN7L3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
