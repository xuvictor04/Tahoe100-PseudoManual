---
symbol: "TOM1"
type: "gene"
col: 1911
ensembl_id: "ENSG00000100284"
name: "target of myb1 membrane trafficking protein"
location: "22q12.3"
module: 59
arm: "+"
pooled_cpm: 38.11
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 23
n_dd_up_clean: 13
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# TOM1

*target of myb1 membrane trafficking protein* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.81× (z +9.8, q 4e-20, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.492× (z -11.7, q 7e-29, down in 35 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.700× (z -5.9, q 4e-07, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAT2]] (+0.70, fdr 7e-06), [[BLVRB]] (+0.64, fdr 7e-06), [[TBC1D17]] (+0.64, fdr 7e-06); moves opposite to [[NEMP2]] (-0.61, fdr 1e-05), [[IPO7]] (-0.59, fdr 1e-05), [[EPB41L2]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1911.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +9.8 | 4e-20 | 30/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +8.0 | 4e-13 | 36/48 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +7.0 | 4e-10 | 28/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +6.7 | 3e-09 | 32/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +5.5 | 5e-06 | 24/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +5.4 | 5e-06 | 24/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.38×** | +5.4 | 6e-06 | 30/48 (C32, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.32×** | +4.8 | 9e-05 | 22/49 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 5e-04 | 22/48 (HEC-1-A, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +4.5 | 5e-04 | 24/48 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 9e-04 | 24/48 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.19× | +3.9 | 0.004 | 22/48 (KATO III, COLO 205, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.024 | 17/47 (NCI-H460, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.036 | 16/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.043 | 12/49 (NCI-H460, J82, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.043 | 14/49 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.071 | 12/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1911.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.492×** | -11.7 | 7e-29 | 35/44 (NCI-H2347, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.506×** | -10.8 | 1e-24 | 26/37 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.543×** | -9.7 | 6e-20 | 39/48 (SNU-423, HS-578T, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.532×** | -9.6 | 8e-20 | 29/38 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.610×** | -7.8 | 5e-13 | 34/49 (SNU-423, HS-578T, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.700×** | -5.9 | 4e-07 | 27/48 (COLO 205, A549, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.779×** | -5.8 | 7e-07 | 31/49 (NCI-H1792, A498, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.722×** | -5.4 | 6e-06 | 21/48 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.736×** | -5.0 | 3e-05 | 24/48 (NCI-H1573, A498, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.831×** | -4.2 | 0.001 | 20/48 (SW 900, NCI-H2030, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.777×** | -4.2 | 0.002 | 21/48 (H4, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -4.1 | 0.002 | 21/48 (NCI-H661, NCI-H460, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.836× | -4.1 | 0.002 | 17/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.786×** | -4.0 | 0.003 | 21/48 (A549, COLO 205, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.791×** | -3.8 | 0.004 | 19/48 (LS 180, Hs 766T, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.796×** | -3.7 | 0.006 | 17/49 (HS-578T, A498, …) | inconsistent across doses | position effect removed |
| [[Brimonidine (drug)]] 5 µM |  | **0.802×** | -3.6 | 0.009 | 10/48 (LoVo, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.803×** | -3.6 | 0.009 | 18/48 (SNU-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.808×** | -3.5 | 0.012 | 15/48 (SNU-1, KATO III, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.815×** | -3.2 | 0.030 | 15/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.812×** | -3.2 | 0.036 | 18/47 (A549, Panc 03.27, …) | all doses, flat | low cells (technical?) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.825×** | -3.2 | 0.036 | 12/48 (RKO, PANC-1, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.870× | -3.1 | 0.042 | 14/48 (NCI-H1573, SW480, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.841× | -2.8 | 0.086 | 11/48 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1911. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 79.1 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[CFPAC-1 (line)]] | alt | 59.3 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.451× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 53.6 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H460 (line)]] | wt | 37.0 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HS-578T (line)]] | alt | 66.6 | 0 | 4 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -12.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 66.0 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -13.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SW 900 (line)]] | alt | 64.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[A549 (line)]] | wt | 35.5 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.246× (z -10.1) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.298× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 70.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H1792 (line)]] | alt | 54.4 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -17.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[PANC-1 (line)]] | alt | 24.8 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.95× (z +12.9) | — |
| [[HepG2_C3A (line)]] | wt | 60.7 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.199× (z -11.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 26.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.4) | — |
| [[KATO III (line)]] | alt | 39.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.9) | — |
| [[C32 (line)]] | wt | 74.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -9.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[COLO 205 (line)]] | alt | 82.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.258× (z -10.7) |
| [[HCT15 (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[Hs 766T (line)]] | wt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0773× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[hTERT-HPNE (line)]] | wt | 41.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[Panc 03.27 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -10.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[RPMI-7951 (line)]] | alt | 51.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0820× (z -8.8) |
| [[SW1417 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1911), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAT2]] | +0.70 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[BLVRB]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[TBC1D17]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 | same gene group |
| [[MAP2K2]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SLC26A11]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SIRT2]] | +0.62 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[TSC1]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[PTOV1]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 | same gene group |
| [[NEU1]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PIAS4]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[GABARAP]] ⚠ | +0.59 | +0.58 / +0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PLD3]] | +0.59 | +0.67 / +0.61 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEMP2]] | -0.61 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[IPO7]] | -0.59 | -0.66 / -0.57 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.59 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.59 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[DDAH1]] | -0.59 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[NME1]] | -0.58 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[CCND1]] | -0.58 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[ATIC]] | -0.56 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[CPSF3]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[DARS2]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.55 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.55 | -0.56 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TOM1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PTGES]] | B | PTGES activity raises TOM1's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.58× lower at baseline in the lines without PTGES | 0.039 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[PTGES]] | B | PTGES activity strengthens TOM1's drug response | lines that do not express PTGES (17) vs lines expressing it (32) | the lines without PTGES respond 0.70× as strongly (z diff +1.31); strongest at Dinaciclib 5 µM: 0.72x vs 0.39x (z diff +4.1) | 0.076 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.587). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-38.7, -26.4); signed map (-25.6, 8.7). **Vector** length 114, 31.5% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.7 | +8.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +4.6 | +4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.2 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.8 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.7 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -5.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.4 | -9.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.2 | -7.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.0 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -0.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.6 | -3.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | target of myb1 membrane trafficking protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:35,299,275-35,347,992 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O60784](https://www.uniprot.org/uniprotkb/O60784) (Target of Myb1 membrane trafficking protein):

> Adapter protein that plays a role in the intracellular membrane trafficking of ubiquitinated proteins, thereby participating in autophagy, ubiquitination-dependent signaling and receptor recycling pathways. Acts as a MYO6/Myosin VI adapter protein that targets MYO6 to endocytic structures. Together with MYO6, required for autophagosomal delivery of endocytic cargo, the maturation of autophagosomes and their fusion with lysosomes. MYO6 links TOM1 with autophagy receptors, such as TAX1BP1; …

**Summary**, from NCBI Gene [10043](https://www.ncbi.nlm.nih.gov/gene/10043):

> This gene was identified as a target of the v-myb oncogene. The encoded protein shares its N-terminal domain in common with proteins associated with vesicular trafficking at the endosome. It is recruited to the endosomes by its interaction with endofin. Several alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:11982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11982) · Entrez [10043](https://www.ncbi.nlm.nih.gov/gene/10043) · UniProt [O60784](https://www.uniprot.org/uniprotkb/O60784) · Ensembl [ENSG00000100284](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100284)

## Data

Gene col 1911: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1911); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1911, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1911]; `tensor/DDL_lfc|DDL_z.npy` [1911]; `embed/gene_vectors.npy` [1911]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1911 or target_col == 1911). Every well: [[TOM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
