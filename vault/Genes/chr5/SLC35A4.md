---
symbol: "SLC35A4"
type: "gene"
col: 10678
ensembl_id: "ENSG00000176087"
name: "solute carrier family 35 member A4"
location: "5q31.3"
module: 16
arm: "+"
pooled_cpm: 8.66
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# SLC35A4

*solute carrier family 35 member A4* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.00× (z +12.2, q 1e-31, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.497× (z -8.7, q 2e-15, down in 30 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.578× (z -6.8, q 3e-09, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTL6]] (+0.83, fdr 7e-06), [[TMEM185B]] (+0.73, fdr 7e-06), [[ERAL1]] (+0.73, fdr 7e-06); moves opposite to [[RPS20]] (-0.73, fdr 7e-06), [[RPLP1]] (-0.72, fdr 7e-06), [[RPS24]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10678.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +12.2 | 1e-31 | 40/45 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.48×** | +10.9 | 5e-25 | 43/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.23×** | +10.0 | 4e-21 | 40/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +9.9 | 6e-21 | 32/43 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.01×** | +8.4 | 7e-15 | 10/16 (HT-29, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.75×** | +6.9 | 4e-10 | 26/33 (A-172, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +6.1 | 1e-07 | 17/38 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.9 | 3e-07 | 19/48 (PANC-1, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +5.3 | 6e-06 | 20/47 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +5.2 | 9e-06 | 18/47 (SNU-423, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.55×** | +5.0 | 3e-05 | 11/25 (HEC-1-A, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.45×** | +4.6 | 2e-04 | 18/40 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.44×** | +4.2 | 0.001 | 13/42 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.002 | 16/48 (NCI-H2347, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.008 | 10/47 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.67×** | +3.3 | 0.027 | 5/36 (SW480, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.30×** | +3.0 | 0.070 | 5/43 (RKO, A549, …) | all doses, stronger at high dose |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +2.9 | 0.095 | 2/48 (KATO III, A498) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.26×** | +2.9 | 0.099 | 3/48 (SW1417, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10678.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -8.7 | 2e-15 | 30/44 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.578×** | -6.8 | 3e-09 | 26/47 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.644×** | -5.5 | 8e-06 | 23/46 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.708×** | -4.3 | 0.003 | 17/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.712×** | -4.1 | 0.005 | 18/44 (SNU-423, SW 900, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -3.9 | 0.008 | 20/44 (SHP-77, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Rifaximin (drug)]] 5 µM |  | **0.734×** | -3.7 | 0.017 | 12/46 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.568×** | -3.7 | 0.017 | 15/43 (HOP62, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tadalafil (drug)]] 5 µM |  | **0.768×** | -3.2 | 0.093 | 10/45 (SW1417, MIA PaCa-2, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.768×** | -3.1 | 0.093 | 7/47 (RKO, C32, …) | rises with dose | plate-row cell shift |
| [[TAK-901 (drug)]] 5 µM |  | 0.626× | -3.0 | 0.12 | 6/47 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10678. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.18 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +8.6) | [[AZD2858 (drug)]] 0.5 µM 0.0977× (z -9.4) ⚠ toxic |
| [[BT-474 (line)]] | alt | 7.17 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0897× (z -8.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 9.36 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0861× (z -8.7) |
| [[COLO 205 (line)]] | alt | 9.08 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0647× (z -10.8) |
| [[KATO III (line)]] | alt | 9.86 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -9.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 8.59 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0833× (z -11.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 8.80 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.67× (z +8.7) | — |
| [[A-172 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10678), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTL6]] | +0.83 | +0.83 / +0.79 | both halves | 7e-06 |  |
| [[TMEM185B]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[ERAL1]] | +0.73 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[DCLRE1A]] | +0.72 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[ZNF620]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.72 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[PABIR1]] | +0.72 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.71 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.70 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[ZKSCAN2]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[KLHL9]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.69 | +0.78 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS20]] | -0.73 | -0.64 / -0.73 | both halves | 7e-06 |  |
| [[RPLP1]] | -0.72 | -0.71 / -0.63 | both halves | 7e-06 |  |
| [[RPS24]] | -0.71 | -0.72 / -0.66 | both halves | 7e-06 |  |
| [[NENF]] | -0.70 | -0.78 / -0.54 | both halves | 1e-05 |  |
| [[RPL13A]] | -0.70 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[NME2]] | -0.70 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[RPLP2]] | -0.69 | -0.72 / -0.59 | both halves | 7e-06 |  |
| [[RPL27A]] | -0.69 | -0.66 / -0.66 | both halves | 7e-06 |  |
| [[RPS21]] | -0.67 | -0.76 / -0.57 | both halves | 1e-05 |  |
| [[HINT1]] | -0.67 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[KDELR1]] | -0.67 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[RPL12]] | -0.67 | -0.66 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.808). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.7, 12.5); signed map (1.3, -31.0). **Vector** length 79.9, 15.0% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.5 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.1 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.9 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -3.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -8.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -6.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member A4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,564,819-140,569,100 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Solute carrier family 35 |
| Reactome | 3 pathways, smallest: Matriglycan biosynthesis on DAG1; DAG1 glycosylations; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [L0R6Q1](https://www.uniprot.org/uniprotkb/L0R6Q1) (SLC35A4 upstream open reading frame protein):

> Required to maintain cellular respiration.

**Summary**, from NCBI Gene [113829](https://www.ncbi.nlm.nih.gov/gene/113829):

> Predicted to enable transmembrane transporter activity. Involved in positive regulation of cellular respiration and positive regulation of translation in response to stress. Located in Golgi membrane and mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20753](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20753) · Entrez [113829](https://www.ncbi.nlm.nih.gov/gene/113829) · UniProt [L0R6Q1](https://www.uniprot.org/uniprotkb/L0R6Q1) · Ensembl [ENSG00000176087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176087)

## Data

Gene col 10678: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10678); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10678, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10678]; `tensor/DDL_lfc|DDL_z.npy` [10678]; `embed/gene_vectors.npy` [10678]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10678 or target_col == 10678). Every well: [[SLC35A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
