---
symbol: "ELP6"
type: "gene"
col: 8790
ensembl_id: "ENSG00000163832"
name: "elongator acetyltransferase complex subunit 6"
location: "3p21.31"
module: 4
arm: "+"
pooled_cpm: 13.72
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ELP6

*elongator acetyltransferase complex subunit 6* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.48× (z +5.0, q 3e-04, up in 18 of 41 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 5.01×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.401× (z -16.4, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSTK]] (+0.63, fdr 1e-05), [[RAD51D]] (+0.63, fdr 1e-05), [[SNRPD1]] (+0.61, fdr 7e-06); moves opposite to [[TMEM269]] (-0.54, fdr 2e-05), [[MAP1LC3B]] (-0.52, fdr 5e-05), [[ADCY10]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8790.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 5.01×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +5.0 | 3e-04 | 18/41 (LoVo, A-427, …) | two highest doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.2 | 0.008 | 9/19 (J82, SW480, …) | two highest doses | cell-cycle shift (explains ~20% here); composition shift |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.40× | +3.0 | 0.35 | 5/46 (NCI-H1792, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8790.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.401×** | -16.4 | 0e+00 | 45/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.512×** | -12.0 | 1e-30 | 40/47 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.460×** | -9.8 | 1e-20 | 42/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.509×** | -8.6 | 1e-15 | 33/47 (SW 900, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.566×** | -7.2 | 6e-11 | 30/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.576×** | -7.0 | 3e-10 | 31/47 (C-33 A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.364×** | -6.7 | 2e-09 | 29/48 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.601×** | -6.5 | 7e-09 | 27/47 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -6.2 | 5e-08 | 27/47 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.627×** | -5.9 | 2e-07 | 25/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -5.7 | 5e-07 | 25/46 (HOP62, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.638×** | -5.7 | 6e-07 | 26/46 (SW 900, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.452×** | -5.3 | 6e-06 | 26/44 (SK-MEL-2, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.661×** | -5.2 | 6e-06 | 23/47 (SHP-77, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.667×** | -4.9 | 3e-05 | 19/42 (SNU-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.667×** | -4.9 | 3e-05 | 23/46 (RKO, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.686×** | -4.8 | 6e-05 | 23/48 (RKO, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8790. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -14.0) |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 12.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.3) |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -12.5) |
| [[RKO (line)]] | wt | 18.1 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -11.6) |
| [[SW480 (line)]] | alt | 22.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 24.4 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -9.6) |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -16.1) |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0683× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0929× (z -11.0) |
| [[A-427 (line)]] | wt | 20.3 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0841× (z -8.7) |
| [[C32 (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -10.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 9.55 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 8.54 | 0 | 1 | — | [[Sulfatinib (drug)]] 0.05 µM 0.0594× (z -8.8) |
| [[J82 (line)]] | alt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -9.2) |
| [[LoVo (line)]] | wt | 12.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +10.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 11.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -9.8) |
| [[SHP-77 (line)]] | alt | 25.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 22.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -13.3) |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.159× (z -8.9) |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.253× (z -8.9) |
| [[A-172 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8790), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSTK]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[RAD51D]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SNRPD1]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[KHDC1-AS1]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SARS2]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[E2F6]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[LSM12]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[MCRS1]] | +0.55 | +0.42 / +0.62 | both halves | 4e-05 | pathway: Chromatin modifying enzymes |
| [[MINDY4]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[COA1]] | +0.54 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[NAA40]] | +0.54 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CHST10]] | +0.54 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM269]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[MAP1LC3B]] | -0.52 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[ADCY10]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[IGSF11]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[LSMEM1]] | -0.52 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[YPEL5]] | -0.51 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[KLRD1]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[GPC5]] | -0.50 | -0.43 / -0.47 | both halves | 4e-05 |  |
| [[CYLD]] | -0.49 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[LVRN]] | -0.49 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[OSER1-DT]] | -0.49 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[PIWIL2]] | -0.48 | -0.50 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.6, -42.1); signed map (-10.9, -47.9). **Vector** length 67.9, 12.1% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | -2.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.8 | +2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.6 | +1.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -12.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -6.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -5.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -2.5 | -3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -16.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | elongator acetyltransferase complex subunit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:47,495,640-47,513,712 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20211; previously TMEM103, C3orf75 |
| Gene groups (HGNC) | Elongator acetyltransferase complex |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0PNE2](https://www.uniprot.org/uniprotkb/Q0PNE2) (Elongator complex protein 6):

> Component of the elongator complex which is required for multiple tRNA modifications, including mcm5U (5-methoxycarbonylmethyl uridine), mcm5s2U (5-methoxycarbonylmethyl-2-thiouridine), and ncm5U (5-carbamoylmethyl uridine). The elongator complex catalyzes formation of carboxymethyluridine in the wobble base at position 34 in tRNAs. Involved in cell migration (By similarity).

**Summary**, from NCBI Gene [54859](https://www.ncbi.nlm.nih.gov/gene/54859):

> Predicted to be involved in positive regulation of cell migration. Predicted to act upstream of or within several processes, including autophagosome maturation; gene expression; and homeostasis of number of retina cells. Located in cytosol and nucleus. Part of elongator holoenzyme complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25976](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25976) · Entrez [54859](https://www.ncbi.nlm.nih.gov/gene/54859) · UniProt [Q0PNE2](https://www.uniprot.org/uniprotkb/Q0PNE2) · Ensembl [ENSG00000163832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163832)

## Data

Gene col 8790: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8790); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8790, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8790]; `tensor/DDL_lfc|DDL_z.npy` [8790]; `embed/gene_vectors.npy` [8790]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8790 or target_col == 8790). Every well: [[ELP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
