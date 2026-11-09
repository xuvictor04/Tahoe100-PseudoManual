---
symbol: "CRK"
type: "gene"
col: 9433
ensembl_id: "ENSG00000167193"
name: "CRK proto-oncogene, adaptor protein"
location: "17p13.3"
module: 182
arm: "-"
pooled_cpm: 107.3
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# CRK

*CRK proto-oncogene, adaptor protein* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.69× (z +14.0, q 1e-41, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.737× (z -8.1, q 2e-13, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C11orf91]] (+0.70, fdr 7e-06), [[SETX]] (+0.69, fdr 7e-06), [[KCNJ14]] (+0.68, fdr 7e-06); moves opposite to [[CAT]] (-0.68, fdr 7e-06), [[KDM1A]] (-0.61, fdr 1e-05), [[HSF2]] (-0.61, fdr 7e-06).
> It sits in the **-** arm of [[Module 182]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9433.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +14.0 | 1e-41 | 40/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +7.9 | 6e-13 | 36/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +7.0 | 6e-10 | 36/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +6.9 | 8e-10 | 34/48 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.9 | 4e-07 | 35/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +5.8 | 6e-07 | 37/48 (SW480, HCT15, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.34×** | +5.5 | 4e-06 | 34/48 (LS 180, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.31×** | +5.1 | 3e-05 | 26/48 (LS 180, HCT15, …) | two highest doses | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.4 | 8e-04 | 0/50 | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.26×** | +4.3 | 9e-04 | 29/49 (NCI-H23, NCI-H2347, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | 1.18× | +3.1 | 0.096 | 20/48 (HCT15, LS 180, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.18× | +3.1 | 0.096 | 21/48 (SNU-423, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9433.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.737×** | -8.1 | 2e-13 | 39/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.750×** | -5.4 | 2e-05 | 36/48 (NCI-H23, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.783×** | -4.6 | 7e-04 | 26/49 (A549, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.789×** | -4.5 | 0.001 | 31/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.795×** | -4.3 | 0.002 | 29/48 (A-172, NCI-H2030, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.801×** | -4.0 | 0.004 | 23/47 (AsPC-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.665×** | -4.0 | 0.004 | 31/47 (NCI-H23, H4, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.802×** | -4.0 | 0.004 | 25/47 (HS-578T, C32, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.868× | -3.8 | 0.010 | 8/48 (HOP62, A549, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.815×** | -3.6 | 0.020 | 22/45 (SW48, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | 0.877× | -3.5 | 0.023 | 16/48 (RKO, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.859× | -3.3 | 0.040 | 13/48 (NCI-H23, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.857× | -3.2 | 0.060 | 18/49 (CHP-212, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.867× | -3.1 | 0.074 | 13/48 (SW480, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.846× | -3.0 | 0.088 | 19/47 (NCI-H23, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9433. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 64.7 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.13× (z +13.5) | [[Lonafarnib (drug)]] 5 µM 0.0720× (z -13.1) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 96.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +23.6) | [[Dinaciclib (drug)]] 0.5 µM 0.514× (z -9.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 101 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.07× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -13.4) |
| [[HCT15 (line)]] | alt | 148 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +8.7) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.367× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 89.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +9.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.507× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 125 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +24.6) | [[Selinexor (drug)]] 5 µM 0.498× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 105 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -10.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 98.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +20.0) | — |
| [[A549 (line)]] | wt | 155 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -14.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 142 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -8.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 113 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +17.3) | — |
| [[HS-578T (line)]] | alt | 89.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.7) | — |
| [[KATO III (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -13.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 115 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.6) | [[Lonafarnib (drug)]] 5 µM 0.198× (z -9.9) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 75.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +16.0) | — |
| [[NCI-H23 (line)]] | alt | 189 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 93.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +23.4) | — |
| [[SK-MEL-2 (line)]] | alt | 60.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +18.1) | — |
| [[SNU-1 (line)]] | wt | 90.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +11.7) | — |
| [[SW48 (line)]] | wt | 133 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -9.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 114 | 0 | 1 | — | [[Osimertinib (mesylate) (drug)]] 5 µM 0.416× (z -8.7) |
| [[C-33 A (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -10.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 47.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 85.3 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +8.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 84.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +18.6) | — |
| [[Hs 766T (line)]] | wt | 87.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +13.5) | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.3) | — |
| [[LoVo (line)]] | wt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 69.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 82.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.133× (z -11.6) ⚠ toxic |
| [[RKO (line)]] | wt | 139 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.525× (z -10.3) |
| [[SNU-423 (line)]] | alt | 68.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +17.6) | — |
| [[SW 1088 (line)]] | alt | 86.2 | 0 | 1 | — | [[Levobupivacaine (hydrochloride) (drug)]] 0.5 µM 0.0918× (z -8.5) |
| [[SW 900 (line)]] | alt | 147 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.4) | — |
| [[SW480 (line)]] | alt | 138 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.25× (z +11.7) | — |
| [[A-172 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 128 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 96.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 89.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9433), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf91]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[SETX]] | +0.69 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[KCNJ14]] | +0.68 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[DMPK]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[REXO1]] | +0.65 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[TUT7]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[C3orf62]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[FBXL18]] | +0.63 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[TLNRD1]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[METTL2B]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[UCKL1-AS1]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[RAB35]] | +0.62 | +0.48 / +0.69 | both halves | 2e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAT]] | -0.68 | -0.71 / -0.63 | both halves | 7e-06 |  |
| [[KDM1A]] | -0.61 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[HSF2]] | -0.61 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[LTA4H]] | -0.60 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[TMEM185A]] | -0.60 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[ATP5F1C]] | -0.60 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[C20orf96]] | -0.60 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[USP3]] | -0.59 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[HBS1L]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[METTL17]] | -0.58 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[MINDY3]] | -0.58 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[PREPL]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **-** arm (projection on the module's main direction -0.751). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (4.4, -9.7); signed map (8.2, 13.1). **Vector** length 137, 43.2% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.8 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +7.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.0 | +5.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.9 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +14.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +1.3 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | +2.9 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.3 | -8.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.9 | -5.4 |
|  | [[NG25 (drug)]] 5 µM |  | -5.7 | -4.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.6 | -4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.3 | -3.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -5.0 | -4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.1 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | CRK proto-oncogene, adaptor protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,420,689-1,463,162 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SH2 domain containing; SH3 domain containing |
| Reactome | 34 pathways, smallest: ARMS-mediated activation; MET receptor recycling; MET activates RAP1 and RAC1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P46108](https://www.uniprot.org/uniprotkb/P46108) (Adapter molecule crk):

> Involved in cell branching and adhesion mediated by BCAR1-CRK-RAPGEF1 signaling and activation of RAP1.; [Isoform Crk-II]: Regulates cell adhesion, spreading and migration. Mediates attachment-induced MAPK8 activation, membrane ruffling and cell motility in a Rac-dependent manner. Involved in phagocytosis of apoptotic cells and cell motility via its interaction with DOCK1 and DOCK4. May regulate the EFNA5-EPHA3 signaling (By similarity).

**Summary**, from NCBI Gene [1398](https://www.ncbi.nlm.nih.gov/gene/1398):

> This gene encodes a member of an adapter protein family that binds to several tyrosine-phosphorylated proteins. The product of this gene has several SH2 and SH3 domains (src-homology domains) and is involved in several signaling pathways, recruiting cytoplasmic proteins in the vicinity of tyrosine kinase through SH2-phosphotyrosine interaction. The N-terminal SH2 domain of this protein functions as a positive regulator of transformation whereas the C-terminal SH3 domain functions as a negative …

**Accessions** — [HGNC:2362](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2362) · Entrez [1398](https://www.ncbi.nlm.nih.gov/gene/1398) · UniProt [P46108](https://www.uniprot.org/uniprotkb/P46108) · Ensembl [ENSG00000167193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167193)

## Data

Gene col 9433: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9433); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9433, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9433]; `tensor/DDL_lfc|DDL_z.npy` [9433]; `embed/gene_vectors.npy` [9433]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9433 or target_col == 9433). Every well: [[CRK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
