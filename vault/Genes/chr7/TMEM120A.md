---
symbol: "TMEM120A"
type: "gene"
col: 12087
ensembl_id: "ENSG00000189077"
name: "transmembrane protein 120A"
location: "7q11.23"
module: 3
arm: "+"
pooled_cpm: 9.07
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TMEM120A

*transmembrane protein 120A* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.80× (z +8.1, q 2e-13, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.498× (z -5.0, q 3e-04, down in 16 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATOSB]] (+0.63, fdr 1e-05), [[PMM1]] (+0.62, fdr 1e-05), [[TOLLIP]] (+0.60, fdr 3e-05); moves opposite to [[PRTFDC1]] (-0.56, fdr 2e-05), [[XRCC5]] (-0.50, fdr 3e-05), [[HNRNPR]] (-0.50, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +8.1 | 2e-13 | 31/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +7.1 | 3e-10 | 26/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.68×** | +5.1 | 5e-05 | 15/38 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.0 | 8e-05 | 7/17 (NCI-H2030, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.8 | 1e-04 | 15/32 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 3e-04 | 15/43 (HT-29, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +4.4 | 8e-04 | 17/40 (AsPC-1, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.006 | 15/43 (HT-29, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.008 | 10/44 (A498, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.012 | 6/40 (Hs 766T, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.041 | 8/47 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.057 | 5/44 (HEC-1-A, KATO III, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.079 | 3/44 (A-172, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.25× | +3.0 | 0.11 | 9/44 (A-172, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12087.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -5.0 | 3e-04 | 16/46 (SW480, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.701×** | -4.9 | 3e-04 | 23/48 (BT-474, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.694×** | -4.8 | 3e-04 | 18/37 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.518×** | -4.7 | 3e-04 | 17/42 (Panc 03.27, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.708×** | -4.7 | 3e-04 | 17/45 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.712×** | -4.7 | 3e-04 | 16/46 (NCI-H1573, SNU-423, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.734×** | -4.2 | 0.002 | 15/45 (SNU-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.746×** | -4.0 | 0.004 | 16/46 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.751×** | -3.9 | 0.006 | 12/46 (NCI-H1573, A-172, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.745×** | -3.8 | 0.009 | 10/42 (AsPC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.827×** | -3.7 | 0.013 | 19/48 (MIA PaCa-2, SHP-77, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.780×** | -3.2 | 0.068 | 14/45 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 0.654× | -3.0 | 0.10 | 3/44 (CFPAC-1, A549, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.802× | -3.0 | 0.11 | 9/47 (LS 180, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 21.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +15.3) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.83× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 12.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.57× (z +20.4) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.44× (z +10.2) | — |
| [[A-172 (line)]] | wt | 12.7 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.57× (z +10.5) ⚠ cell-cycle shift, explains ~16% of this change | — |
| [[J82 (line)]] | alt | 7.88 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.32× (z +15.6) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[CFPAC-1 (line)]] | alt | 8.01 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +9.9) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[NCI-H23 (line)]] | alt | 4.37 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0710× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 7.75 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.201× (z -8.6) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 9.98 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -8.8) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SNU-423 (line)]] | alt | 9.65 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +8.8) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[A-427 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATOSB]] | +0.63 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[PMM1]] | +0.62 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[TOLLIP]] | +0.60 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[TBC1D17]] | +0.58 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[MPND]] | +0.57 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[PRKCD]] | +0.57 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[RCE1]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PPARA]] | +0.57 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[SIRT7]] | +0.56 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[CARD19]] | +0.56 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[TBC1D10A]] | +0.56 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[DGKQ]] | +0.55 | +0.39 / +0.52 | both halves | 5e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRTFDC1]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[XRCC5]] | -0.50 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[HNRNPR]] | -0.50 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[RMDN2]] | -0.50 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[RNASEH2B]] | -0.49 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[SOCS4]] | -0.48 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[DPY19L1P2]] | -0.47 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[SLC12A2-DT]] | -0.46 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[PON2]] | -0.45 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[TFAM]] | -0.45 | -0.40 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.3, -49.1); signed map (-25.2, 12.1). **Vector** length 66.1, 10.6% of its response variance represented; |z| ≥ 3 in 750 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.4 | +1.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +8.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.1 | +0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +7.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +3.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +4.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.8 | -3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.5 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -4.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 120A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:75,986,831-75,994,656 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TMPIT, NET29, TACAN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXJ8](https://www.uniprot.org/uniprotkb/Q9BXJ8) (Transmembrane protein 120A):

> Multifunctional protein involved in mechanosensation, and plays an essential role in lipid metabolism and adipocyte differentiation. May function as a potential ion channel involved in sensing mechanical stimuli. Mediates the mechanosensitivity of the PKD2-TMEM120A channel complex through direct physical interaction. TMEM120A seems to affect mechanosensation by inhibiting PIEZO2 channels, possibly by altering cellular lipid content (By similarity). TMEM120A is structurally similar to a …

**Summary**, from NCBI Gene [83862](https://www.ncbi.nlm.nih.gov/gene/83862):

> Enables coenzyme A binding activity. Involved in antiviral innate immune response; fat cell differentiation; and protein complex oligomerization. Located in endoplasmic reticulum and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21697) · Entrez [83862](https://www.ncbi.nlm.nih.gov/gene/83862) · UniProt [Q9BXJ8](https://www.uniprot.org/uniprotkb/Q9BXJ8) · Ensembl [ENSG00000189077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189077)

## Data

Gene col 12087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12087); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12087]; `tensor/DDL_lfc|DDL_z.npy` [12087]; `embed/gene_vectors.npy` [12087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12087 or target_col == 12087). Every well: [[TMEM120A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM120A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
