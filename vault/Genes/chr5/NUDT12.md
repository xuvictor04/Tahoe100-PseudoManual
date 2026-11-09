---
symbol: "NUDT12"
type: "gene"
col: 3414
ensembl_id: "ENSG00000112874"
name: "nudix hydrolase 12"
location: "5q21.2"
module: 28
arm: "+"
pooled_cpm: 9.94
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# NUDT12

*nudix hydrolase 12* — 5q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.43× (z +4.6, q 0.003, up in 18 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.228× (z -19.0, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KBTBD6]] (+0.75, fdr 7e-06), [[KBTBD7]] (+0.71, fdr 7e-06), [[IFTAP]] (+0.70, fdr 7e-06); moves opposite to [[CCDC168]] (-0.62, fdr 1e-05), [[TPTEP2-CSNK1E]] (-0.62, fdr 7e-06), [[PRDM10]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3414.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +4.6 | 0.003 | 18/46 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +3.8 | 0.043 | 4/18 (MIA PaCa-2, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | 1.29× | +3.2 | 0.22 | 10/45 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.28× | +3.0 | 0.22 | 8/46 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.26× | +3.0 | 0.22 | 12/46 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.22× | +3.0 | 0.22 | 6/47 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3414.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.228×** | -19.0 | 0e+00 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.401×** | -16.6 | 0e+00 | 37/43 (Hs 766T, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.314×** | -14.9 | 0e+00 | 40/45 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.321×** | -14.6 | 0e+00 | 42/46 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.397×** | -11.9 | 2e-30 | 34/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.303×** | -8.0 | 9e-14 | 31/42 (MIA PaCa-2, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.333×** | -7.4 | 1e-11 | 28/46 (PANC-1, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.563×** | -7.1 | 9e-11 | 27/44 (LOX-IMVI, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.710×** | -6.2 | 3e-08 | 23/46 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.635×** | -5.8 | 3e-07 | 17/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.652×** | -5.3 | 7e-06 | 20/39 (NCI-H1792, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.675×** | -5.0 | 2e-05 | 19/46 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.745×** | -3.8 | 0.007 | 17/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.752×** | -3.6 | 0.011 | 17/45 (NCI-H2030, CHP-212, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.759×** | -3.5 | 0.015 | 14/46 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.599×** | -3.4 | 0.020 | 14/42 (HT-29, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -3.4 | 0.020 | 15/46 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.766×** | -3.4 | 0.020 | 14/46 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.769×** | -3.2 | 0.037 | 20/46 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3414. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.3 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0977× (z -19.1) |
| [[RKO (line)]] | wt | 15.4 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0210× (z -20.3) |
| [[SW480 (line)]] | alt | 14.4 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -15.6) |
| [[HOP62 (line)]] | alt | 9.23 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -11.6) |
| [[LoVo (line)]] | wt | 9.02 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0561× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 7.63 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0757× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -9.9) |
| [[BT-474 (line)]] | alt | 5.72 | 0 | 3 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0573× (z -10.2) ⚠ transcription drop · without an alert: [[Dihydroartemisinin (drug)]] 0.5 µM 0.0788× (z -9.1) |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -13.8) |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -10.4) |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -14.1) |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -9.0) |
| [[HT-29 (line)]] | alt | 12.1 | 0 | 2 | — | [[PF-06260933 (drug)]] 5 µM 0.0490× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 9.84 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 8.87 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0618× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 12.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.116× (z -10.1) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -9.0) |
| [[A-172 (line)]] | wt | 12.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 5.51 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -10.5) |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0782× (z -9.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -11.6) |
| [[SNU-423 (line)]] | alt | 7.95 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -8.5) |
| [[SW 900 (line)]] | alt | 6.26 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0874× (z -8.7) |
| [[A-427 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.26 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3414), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD6]] | +0.75 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[KBTBD7]] | +0.71 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[IFTAP]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[ZSCAN26]] | +0.69 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[SNAPIN]] | +0.69 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[DBT]] | +0.69 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.69 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MKS1]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[BBS5]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[PTCD2]] | +0.68 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[KLHL9]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[CEP290]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC168]] | -0.62 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.62 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[PRDM10]] | -0.61 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[NR2C2]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SLC6A16]] | -0.56 | -0.46 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.9, 0.7); signed map (-21.2, -16.9). **Vector** length 70.7, 12.6% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | -1.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +4.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.4 | -16.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -11.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -14.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.4 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q21.2 — chr5:103,548,855-103,562,790 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP761I172 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Nudix hydrolase family |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 3 pathways, smallest: Nicotinate metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQG2](https://www.uniprot.org/uniprotkb/Q9BQG2) (NAD-capped RNA hydrolase NUDT12):

> mRNA decapping enzyme that specifically removes the nicotinamide adenine dinucleotide (NAD) cap from a subset of mRNAs by hydrolyzing the diphosphate linkage to produce nicotinamide mononucleotide (NMN) and 5' monophosphate mRNA. The NAD-cap is present at the 5'-end of some RNAs; in contrast to the canonical N7 methylguanosine (m7G) cap, the NAD cap promotes mRNA decay. Preferentially acts on NAD-capped transcripts in response to nutrient stress. Also acts on free nicotinamide adenine …

**Summary**, from NCBI Gene [83594](https://www.ncbi.nlm.nih.gov/gene/83594):

> Nucleotides are involved in numerous biochemical reactions and pathways within the cell as substrates, cofactors, and effectors. Nudix hydrolases, such as NUDT12, regulate the concentrations of individual nucleotides and of nucleotide ratios in response to changing circumstances (Abdelraheim et al., 2003 [PubMed 12790796]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18826) · Entrez [83594](https://www.ncbi.nlm.nih.gov/gene/83594) · UniProt [Q9BQG2](https://www.uniprot.org/uniprotkb/Q9BQG2) · Ensembl [ENSG00000112874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112874)

## Data

Gene col 3414: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3414); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3414, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3414]; `tensor/DDL_lfc|DDL_z.npy` [3414]; `embed/gene_vectors.npy` [3414]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3414 or target_col == 3414). Every well: [[NUDT12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
