---
symbol: "TBC1D25"
type: "gene"
col: 887
ensembl_id: "ENSG00000068354"
name: "TBC1 domain family member 25"
location: "Xp11.23"
module: 192
arm: "+"
pooled_cpm: 20.69
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 36
n_dd_up_clean: 6
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# TBC1D25

*TBC1 domain family member 25* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.49× (z +7.1, q 9e-10, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (17 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.322× (z -30.4, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHST12]] (+0.63, fdr 5e-05), [[SMIM8]] (+0.62, fdr 4e-05), [[RNF41]] (+0.62, fdr 7e-05); moves opposite to [[CDK2AP1]] (-0.59, fdr 1e-04), [[MBNL3]] (-0.59, fdr 3e-05), [[SNX5]] (-0.57, fdr 5e-05).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.49×** | +7.1 | 9e-10 | 31/46 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +5.9 | 1e-06 | 20/47 (NCI-H460, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.74×** | +5.5 | 7e-06 | 20/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +5.0 | 7e-05 | 17/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Posaconazole (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.017 | 4/48 (A549, A-172, …) | top dose only | plate-row cell shift |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.019 | 9/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Fulvestrant (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.18 | 3/47 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 20 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 887.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.322×** | -30.4 | 0e+00 | 43/47 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.404×** | -17.2 | 0e+00 | 34/40 (SW480, NCI-H2347, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.381×** | -17.0 | 0e+00 | 40/46 (SW480, H4, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.387×** | -16.7 | 0e+00 | 40/48 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.507×** | -12.0 | 6e-31 | 24/30 (NCI-H460, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.513×** | -11.7 | 1e-29 | 26/33 (Panc 03.27, HEC-1-A, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.649×** | -11.5 | 7e-29 | 29/47 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.575×** | -10.5 | 8e-24 | 34/47 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.608×** | -8.8 | 1e-16 | 27/47 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.650×** | -8.2 | 2e-14 | 28/48 (NCI-H2347, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.659×** | -7.9 | 2e-13 | 29/46 (H4, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.764×** | -7.2 | 3e-11 | 26/48 (A-172, NCI-H2030, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.704×** | -6.6 | 1e-09 | 26/48 (MIA PaCa-2, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.708×** | -6.5 | 3e-09 | 23/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.709×** | -6.5 | 3e-09 | 28/48 (KATO III, SW480, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -5.9 | 1e-07 | 20/48 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.750×** | -5.4 | 2e-06 | 22/48 (CFPAC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **0.798×** | -4.0 | 0.001 | 10/47 (KATO III, RKO, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.704×** | -3.5 | 0.009 | 12/46 (KATO III, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.832×** | -3.5 | 0.009 | 15/48 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.836× | -3.4 | 0.013 | 10/48 (NCI-H1792, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 33.8 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 28.0 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.112× (z -17.4) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.250× (z -16.8) |
| [[Hs 766T (line)]] | wt | 32.8 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -20.2) |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 26.4 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -15.0) |
| [[SNU-423 (line)]] | alt | 33.0 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -19.0) |
| [[A-172 (line)]] | wt | 23.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -16.8) |
| [[AsPC-1 (line)]] | alt | 23.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -12.3) |
| [[NCI-H1792 (line)]] | alt | 26.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -15.7) |
| [[NCI-H460 (line)]] | wt | 27.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -24.0) |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -12.9) |
| [[SW480 (line)]] | alt | 28.0 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0878× (z -27.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -18.0) |
| [[A549 (line)]] | wt | 30.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -14.7) |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.6) |
| [[H4 (line)]] | wt | 26.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0437× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0623× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -11.7) |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -13.5) |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0805× (z -11.5) |
| [[KATO III (line)]] | alt | 31.0 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -15.2) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -11.3) |
| [[A498 (line)]] | wt | 12.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -14.0) |
| [[C32 (line)]] | wt | 10.9 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0729× (z -11.9) |
| [[HCT15 (line)]] | alt | 25.4 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0578× (z -14.9) ⚠ transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0665× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 11.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -12.2) |
| [[PANC-1 (line)]] | alt | 25.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -19.5) |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0982× (z -12.1) |
| [[SW1417 (line)]] | alt | 22.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -16.2) |
| [[A-427 (line)]] | wt | 22.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -9.1) |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[C-33 A (line)]] | alt | 17.1 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.105× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[J82 (line)]] | alt | 21.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.5) |
| [[LoVo (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[LS 180 (line)]] | wt | 9.36 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 19.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 13.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -14.1) |
| [[RKO (line)]] | wt | 12.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -9.2) |
| [[SW 900 (line)]] | alt | 19.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -9.1) |
| [[SW48 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0946× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~38% of this change |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHST12]] | +0.63 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[SMIM8]] | +0.62 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[RNF41]] | +0.62 | +0.62 / +0.38 | both halves | 7e-05 |  |
| [[FBXO46]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[KCTD21]] | +0.61 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[RRAS]] | +0.61 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[VPS37C]] | +0.61 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ESS2]] | +0.61 | +0.59 / +0.36 | both halves | 1e-04 |  |
| [[TBC1D17]] | +0.60 | +0.47 / +0.48 | both halves | 2e-05 | same gene group; pathway: Rab regulation of trafficking |
| [[TBCB]] | +0.58 | +0.62 / +0.33 | both halves | 1e-04 |  |
| [[PLD3]] | +0.58 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[RTN2]] | +0.57 | +0.54 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK2AP1]] | -0.59 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[MBNL3]] | -0.59 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SNX5]] | -0.57 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[RAB11FIP2]] | -0.57 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[CRPPA]] | -0.56 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[PRDM5]] | -0.55 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[GSTCD]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[CLOCK]] | -0.55 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[MOB1A]] | -0.54 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[SEPTIN8]] | -0.54 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[NT5DC1]] | -0.53 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[PGRMC1]] | -0.52 | -0.33 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TBC1D25's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.7, 0.2); signed map (-33.9, 0.5). **Vector** length 77.2, 15.5% of its response variance represented; |z| ≥ 3 in 1,127 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +4.8 | -6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +5.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | +4.1 | -6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +3.4 | -8.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +5.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.1 | +2.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +1.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -17.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -16.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -30.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -2.9 | -6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -7.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,539,714-48,562,609 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously OATL1 |
| Gene groups (HGNC) | TBC1 domain family members |
| Reactome | 4 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3MII6](https://www.uniprot.org/uniprotkb/Q3MII6) (TBC1 domain family member 25):

> Acts as a GTPase-activating protein specific for RAB33B. Involved in the regulation of autophagosome maturation, the process in which autophagosomes fuse with endosomes and lysosomes.

**Summary**, from NCBI Gene [4943](https://www.ncbi.nlm.nih.gov/gene/4943):

> This gene encodes a protein with a TBC domain and functions as a Rab GTPase activating protein. The encoded protein is involved in the fusion of autophagosomes with endosomes and lysosomes. This gene was previously known as ornithine aminotransferase-like 1, but has no similarity to ornithine aminotransferase. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:8092](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8092) · Entrez [4943](https://www.ncbi.nlm.nih.gov/gene/4943) · UniProt [Q3MII6](https://www.uniprot.org/uniprotkb/Q3MII6) · Ensembl [ENSG00000068354](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068354)

## Data

Gene col 887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 887); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 887]; `tensor/DDL_lfc|DDL_z.npy` [887]; `embed/gene_vectors.npy` [887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 887 or target_col == 887). Every well: [[TBC1D25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
