---
symbol: "PLD6"
type: "gene"
col: 11046
ensembl_id: "ENSG00000179598"
name: "phospholipase D family member 6"
location: "17p11.2"
module: 68
arm: "+"
pooled_cpm: 3.68
n_lines_expressing: 48
n_dd_up: 31
n_dd_down: 2
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# PLD6

*phospholipase D family member 6* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.89× (z +26.7, q 0e+00, up in 33 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.658× (z -4.5, q 0.004, down in 17 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (A-172 0.0391×; ⚠ cell-cycle shift, explains ~2% of this change); [[Tomivosertib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0693×); [[Bentamapimod (drug)]] 0.05 µM in 1 line (SNU-1 0.0881×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[REPIN1]] (+0.71, fdr 7e-06), [[LGALSL-DT]] (+0.70, fdr 1e-05), [[TMEM192]] (+0.69, fdr 7e-06); moves opposite to [[STRAP]] (-0.64, fdr 1e-05), [[RECQL]] (-0.60, fdr 1e-05), [[GRB2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11046.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.89×** | +26.7 | 0e+00 | 33/36 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.81×** | +16.1 | 0e+00 | 34/42 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.11×** | +11.2 | 6e-27 | 25/44 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.85×** | +11.1 | 1e-26 | 25/32 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.30×** | +8.8 | 1e-16 | 29/43 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.12×** | +8.0 | 1e-13 | 24/44 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.88×** | +6.7 | 1e-09 | 21/41 (LOX-IMVI, KATO III, …) | two highest doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +6.6 | 3e-09 | 15/31 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +6.6 | 3e-09 | 1/3 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +6.5 | 5e-09 | 18/41 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.78×** | +6.1 | 5e-08 | 15/44 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +5.6 | 9e-07 | 11/21 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +5.5 | 1e-06 | 10/23 (A-172, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +5.4 | 3e-06 | 1/7 (MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +5.2 | 6e-06 | 12/43 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +4.5 | 2e-04 | 15/44 (HEC-1-A, SHP-77, …) | two highest doses | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.2 | 9e-04 | 14/36 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.47×** | +4.1 | 0.001 | 8/39 (SHP-77, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **2.01×** | +3.9 | 0.003 | 7/28 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.00×** | +3.9 | 0.003 | 6/25 (NCI-H460, SW48, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.97×** | +3.8 | 0.004 | 5/31 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11046.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (A-172 0.0391×; ⚠ cell-cycle shift, explains ~2% of this change); [[Tomivosertib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0693×); [[Bentamapimod (drug)]] 0.05 µM in 1 line (SNU-1 0.0881×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.658×** | -4.5 | 0.004 | 17/43 (LoVo, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.677×** | -4.2 | 0.008 | 11/45 (J82, A498, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.546× | -3.4 | 0.14 | 9/38 (hTERT-HPNE, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11046. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.94 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.53× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 4.68 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.7× (z +20.7) | — |
| [[A-172 (line)]] | wt | 5.88 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.0391× (z -12.5) ⚠ cell-cycle shift, explains ~2% of this change |
| [[KATO III (line)]] | alt | 3.17 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.9× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 3.83 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +15.9) | — |
| [[SHP-77 (line)]] | alt | 7.04 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +14.3) | — |
| [[Hs 766T (line)]] | wt | 3.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 3.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 1.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +8.7) | — |
| [[J82 (line)]] | alt | 4.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 4.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.86 | 0 | 1 | — | [[Tomivosertib (drug)]] 0.05 µM 0.0693× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 2.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 2.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 1 | — | [[Bentamapimod (drug)]] 0.05 µM 0.0881× (z -8.6) |
| [[SW 900 (line)]] | alt | 2.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +9.2) | — |
| [[A-427 (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11046), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REPIN1]] | +0.71 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[LGALSL-DT]] | +0.70 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[TMEM192]] | +0.69 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[THUMPD2]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.67 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[TRIP6]] | +0.67 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SLC16A9]] | +0.66 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[FAM169A]] | +0.65 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ZNF764]] | +0.62 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[UAP1L1]] | +0.62 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[CCDC102A]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[ZC3H7B]] | +0.61 | +0.63 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRAP]] | -0.64 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[RECQL]] | -0.60 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[GRB2]] | -0.60 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[TM9SF2]] | -0.60 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[ATP6AP2]] | -0.59 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[SETD3]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[MFSD14B]] | -0.57 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[RPA1]] | -0.56 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[GNB2]] | -0.56 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[STRN]] | -0.55 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[POGLUT2]] | -0.55 | -0.56 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-1.1, 9.6); signed map (18.7, -15.9). **Vector** length 65.2, 10.4% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +26.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +16.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +11.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.9 | +11.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +6.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +3.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.4 | -4.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -1.9 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -0.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.9 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase D family member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:17,200,995-17,206,333 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Zuc |
| Gene groups (HGNC) | Phospholipases |
| Reactome | 7 pathways, smallest: Synthesis of PG; PIWI-interacting RNA (piRNA) biogenesis; Synthesis of PA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2A8](https://www.uniprot.org/uniprotkb/Q8N2A8) (Mitochondrial cardiolipin hydrolase):

> Presents phospholipase and nuclease activities, depending on the different physiological conditions. Interaction with Mitoguardin (MIGA1 or MIGA2) affects the dimer conformation, facilitating the lipase activity over the nuclease activity. Plays a key role in mitochondrial fusion and fission via its phospholipase activity. In its phospholipase role, it uses the mitochondrial lipid cardiolipin as substrate to generate phosphatidate (PA or 1,2-diacyl-sn-glycero-3-phosphate), a second messenger …

**Summary**, from NCBI Gene [201164](https://www.ncbi.nlm.nih.gov/gene/201164):

> Enables cardiolipin phospholipase D activity and protein homodimerization activity. Involved in mitochondrial fusion and phospholipid biosynthetic process. Acts upstream of or within positive regulation of mitochondrial fusion. Located in mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30447](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30447) · Entrez [201164](https://www.ncbi.nlm.nih.gov/gene/201164) · UniProt [Q8N2A8](https://www.uniprot.org/uniprotkb/Q8N2A8) · Ensembl [ENSG00000179598](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179598)

## Data

Gene col 11046: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11046); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11046, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11046]; `tensor/DDL_lfc|DDL_z.npy` [11046]; `embed/gene_vectors.npy` [11046]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11046 or target_col == 11046). Every well: [[PLD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
