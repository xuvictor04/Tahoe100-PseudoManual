---
symbol: "COG1"
type: "gene"
col: 9343
ensembl_id: "ENSG00000166685"
name: "component of oligomeric golgi complex 1"
location: "17q25.1"
module: 41
arm: "+"
pooled_cpm: 25.57
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# COG1

*component of oligomeric golgi complex 1* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.13× (z +8.0, q 7e-13, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.559× (z -11.4, q 4e-27, down in 24 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.827× (z -3.7, q 0.014, down in 9 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SW 900 0.110×, SHP-77 0.198×, PANC-1 0.341×, HOP62 0.323×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (CHP-212 0.0725×, HOP62 0.358×, NCI-H2347 0.354×, A549 0.316×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 0.316×, AsPC-1 0.413×; ⚠ cell-cycle shift, explains ~0% of this change); [[Raltitrexed (drug)]] 0.5 µM in 1 line (SW48 0.122×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF805]] (+0.65, fdr 1e-05), [[OSBP]] (+0.63, fdr 9e-06), [[GOLGA5]] (+0.61, fdr 1e-05); moves opposite to [[LINC00342]] (-0.51, fdr 9e-05), [[STAU2]] (-0.50, fdr 5e-05), [[DENND1A]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9343.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.13×** | +8.0 | 7e-13 | 31/48 (LS 180, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.76×** | +6.0 | 7e-07 | 26/47 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.21×** | +3.9 | 0.017 | 20/47 (A-427, RKO, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.027 | 13/47 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.056 | 14/47 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.21 | 16/47 (A-427, SW480, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9343.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SW 900 0.110×, SHP-77 0.198×, PANC-1 0.341×, HOP62 0.323×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (CHP-212 0.0725×, HOP62 0.358×, NCI-H2347 0.354×, A549 0.316×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 0.316×, AsPC-1 0.413×; ⚠ cell-cycle shift, explains ~0% of this change); [[Raltitrexed (drug)]] 0.5 µM in 1 line (SW48 0.122×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.559×** | -11.4 | 4e-27 | 24/36 (SW 900, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.639×** | -9.1 | 2e-17 | 32/42 (CHP-212, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.622×** | -7.7 | 3e-12 | 23/38 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.752×** | -5.6 | 3e-06 | 26/45 (NCI-H23, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.811×** | -4.3 | 0.002 | 15/48 (H4, NCI-H1792, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.812×** | -4.1 | 0.004 | 15/47 (SW48, CHP-212, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.829×** | -3.8 | 0.011 | 17/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.827×** | -3.7 | 0.014 | 9/48 (LoVo, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.828×** | -3.7 | 0.014 | 13/48 (NCI-H23, NCI-H661, …) | top dose only |  |
| [[Ritonavir (drug)]] 5 µM |  | 0.886× | -3.5 | 0.025 | 9/48 (NCI-H460, SHP-77, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.845× | -3.4 | 0.029 | 13/48 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.890× | -3.4 | 0.033 | 10/48 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.730×** | -3.4 | 0.035 | 8/48 (A549, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9343. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 38.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -10.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 41.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -12.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 21.3 | 0 | 2 (1 ⚠) | — | [[Raltitrexed (drug)]] 0.5 µM 0.122× (z -10.1) |
| [[A-427 (line)]] | wt | 22.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +9.3) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[A549 (line)]] | wt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -9.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0725× (z -12.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 40.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.239× (z -10.1) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -9.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -11.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -14.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9343), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF805]] | +0.65 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[OSBP]] | +0.63 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[GOLGA5]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 772 |
| [[TBL2]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[YIPF5]] | +0.61 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ZNF526]] | +0.61 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[ZNF550]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[MYNN]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ERCC5]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SLC30A5]] | +0.58 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[RUSF1]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ARHGAP1]] | +0.58 | +0.61 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00342]] | -0.51 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[STAU2]] | -0.50 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[DENND1A]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (12.5, -37.9); signed map (-53.6, 13.4). **Vector** length 71.6, 12.5% of its response variance represented; |z| ≥ 3 in 786 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | -0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +0.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.5 |
|  | [[Lipoic acid (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | -0.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | -1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +2.5 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.8 | -5.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | +0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Acetohexamide (drug)]] 5 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | component of oligomeric golgi complex 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:73,193,055-73,208,507 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1381; previously LDLB |
| Gene groups (HGNC) | Components of oligomeric golgi complex |
| Reactome | 12 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WTW3](https://www.uniprot.org/uniprotkb/Q8WTW3) (Conserved oligomeric Golgi complex subunit 1):

> Required for normal Golgi function.

**Summary**, from NCBI Gene [9382](https://www.ncbi.nlm.nih.gov/gene/9382):

> The protein encoded by this gene is one of eight proteins (Cog1-8) which form a Golgi-localized complex (COG) required for normal Golgi morphology and function. It is thought that this protein is required for steps in the normal medial and trans Golgi-associated processing of glycoconjugates and plays a role in the organization of the Golgi-localized complex. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6545](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6545) · Entrez [9382](https://www.ncbi.nlm.nih.gov/gene/9382) · UniProt [Q8WTW3](https://www.uniprot.org/uniprotkb/Q8WTW3) · Ensembl [ENSG00000166685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166685)

## Data

Gene col 9343: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9343); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9343, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9343]; `tensor/DDL_lfc|DDL_z.npy` [9343]; `embed/gene_vectors.npy` [9343]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9343 or target_col == 9343). Every well: [[COG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
