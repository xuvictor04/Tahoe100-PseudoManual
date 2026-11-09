---
symbol: "MAP1S"
type: "gene"
col: 5070
ensembl_id: "ENSG00000130479"
name: "microtubule associated protein 1S"
location: "19p13.12"
module: 20
arm: "-"
pooled_cpm: 18.96
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# MAP1S

*microtubule associated protein 1S* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.97× (z +11.6, q 1e-28, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.448× (z -13.8, q 7e-41, down in 37 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.639× (z -10.9, q 2e-25, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCE1]] (+0.69, fdr 1e-05), [[SIGIRR]] (+0.65, fdr 3e-05), [[LRRC8E]] (+0.64, fdr 2e-05); moves opposite to [[PAPOLA]] (-0.64, fdr 1e-04), [[SELENOF]] (-0.61, fdr 5e-05), [[NNT]] (-0.61, fdr 4e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5070.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +11.6 | 1e-28 | 43/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.59×** | +11.4 | 2e-27 | 33/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +10.6 | 5e-24 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +9.5 | 5e-19 | 35/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +8.0 | 9e-14 | 28/47 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +6.6 | 5e-09 | 24/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +6.3 | 3e-08 | 23/43 (NCI-H2030, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.7 | 9e-07 | 26/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.1 | 2e-05 | 20/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.33×** | +5.0 | 4e-05 | 18/44 (HS-578T, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.007 | 18/48 (A498, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.25×** | +3.8 | 0.007 | 17/46 (SW480, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.25×** | +3.8 | 0.007 | 16/47 (HOP62, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +3.7 | 0.008 | 15/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.7 | 0.008 | 16/48 (SNU-423, J82, …) | top dose only | low cells (technical?) |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.014 | 5/47 (SNU-423, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.039 | 12/47 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.073 | 5/47 (SW480, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.073 | 16/47 (HS-578T, NCI-H1573, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5070.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.448×** | -13.8 | 7e-41 | 37/41 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.479×** | -12.2 | 9e-32 | 28/32 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -10.9 | 2e-25 | 32/46 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -6.7 | 2e-09 | 27/48 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.672×** | -6.3 | 3e-08 | 21/38 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -5.7 | 1e-06 | 25/46 (A-172, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.803×** | -3.6 | 0.021 | 13/47 (SNU-423, BT-474, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.804×** | -3.6 | 0.021 | 16/47 (LoVo, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.805×** | -3.5 | 0.027 | 15/48 (LoVo, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.832×** | -3.2 | 0.087 | 7/47 (A-427, SK-MEL-2, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5070. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 34.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0397× (z -28.7) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 21.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 17.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -13.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 23.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -11.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 30.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -12.9) |
| [[LoVo (line)]] | wt | 22.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 13.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 13.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 5 µM 0.165× (z -13.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 34.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -8.5) |
| [[PANC-1 (line)]] | alt | 10.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.15× (z +10.2) | — |
| [[A498 (line)]] | wt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -11.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -10.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[H4 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -9.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -8.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -9.2) |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -11.4) |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -11.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -15.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0992× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -11.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 19.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -8.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -14.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0586× (z -18.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -9.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -9.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -17.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5070), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCE1]] | +0.69 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[SIGIRR]] | +0.65 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[LRRC8E]] | +0.64 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[CDC34]] | +0.64 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[PLIN3]] | +0.64 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[KLHL26]] | +0.63 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[C15orf39]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[NSUN5]] | +0.61 | +0.37 / +0.66 | both halves | 8e-05 |  |
| [[TRAPPC4]] | +0.61 | +0.36 / +0.60 | both halves | 1e-04 |  |
| [[R3HCC1]] | +0.61 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[PDRG1]] | +0.61 | +0.39 / +0.69 | both halves | 6e-05 |  |
| [[RELA]] | +0.61 | +0.65 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPOLA]] | -0.64 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[SELENOF]] | -0.61 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[NNT]] | -0.61 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[CRPPA]] | -0.59 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[PTGR2]] | -0.59 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[CMPK1]] | -0.58 | -0.29 / -0.67 | both halves | 3e-04 |  |
| [[IRAK4]] | -0.58 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[LYRM1]] | -0.58 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[CSDE1]] | -0.58 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[DECR1]] | -0.56 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[SETD7]] | -0.56 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[STRADB]] | -0.56 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MAP1S's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CAMSAP3]] | B | CAMSAP3 activity raises MAP1S's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 1.16× lower at baseline in the lines without CAMSAP3 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-47.5, 15.8); signed map (-27.8, 14.8). **Vector** length 98.6, 21.6% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +11.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +10.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.7 | +9.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | +4.4 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +1.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +3.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.9 | -13.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.4 | -6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -12.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -3.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein 1S |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:17,719,242-17,734,513 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10669, MAP8; previously C19orf5, VCY2IP1, BPY2IP1 |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q66K74](https://www.uniprot.org/uniprotkb/Q66K74) (Microtubule-associated protein 1S):

> Microtubule-associated protein that mediates aggregation of mitochondria resulting in cell death and genomic destruction (MAGD). Plays a role in anchoring the microtubule organizing center to the centrosomes. Binds to DNA. Plays a role in apoptosis. Involved in the formation of microtubule bundles (By similarity). Stabilizes microtubules in neuronal dendrites; CDKL5-dependent phosphorylation dissociates MAP1S from microtubules, promoting microtubule plus-end dynamic instability and supporting …

**Summary**, from NCBI Gene [55201](https://www.ncbi.nlm.nih.gov/gene/55201):

> Enables DNA binding activity; WD40-repeat domain binding activity; and cytoskeletal protein binding activity. Involved in metaphase chromosome alignment; microtubule cytoskeleton organization; and neuron projection morphogenesis. Located in several cellular components, including microtubule cytoskeleton; nuclear lumen; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15715) · Entrez [55201](https://www.ncbi.nlm.nih.gov/gene/55201) · UniProt [Q66K74](https://www.uniprot.org/uniprotkb/Q66K74) · Ensembl [ENSG00000130479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130479)

## Data

Gene col 5070: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5070); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5070, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5070]; `tensor/DDL_lfc|DDL_z.npy` [5070]; `embed/gene_vectors.npy` [5070]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5070 or target_col == 5070). Every well: [[MAP1S — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP1S.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
