---
symbol: "NT5DC3"
type: "gene"
col: 3264
ensembl_id: "ENSG00000111696"
name: "5'-nucleotidase domain containing 3"
location: "12q23.3"
module: 77
arm: "+"
pooled_cpm: 78.34
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# NT5DC3

*5'-nucleotidase domain containing 3* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.13× (z +10.1, q 3e-21, up in 44 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.50× (z +5.4, q 2e-05, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.518× (z -8.8, q 5e-16, down in 36 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.555× (z -7.9, q 6e-13, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPAT]] (+0.65, fdr 7e-06), [[TMEM120B]] (+0.62, fdr 1e-05), [[URI1]] (+0.61, fdr 3e-05); moves opposite to [[BAZ2B]] (-0.64, fdr 1e-05), [[C11orf58]] (-0.64, fdr 1e-05), [[CARD6]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3264.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.13×** | +10.1 | 3e-21 | 44/48 (NCI-H460, C32, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +5.4 | 2e-05 | 31/48 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[EX229 (drug)]] 5 µM |  | **1.88×** | +4.4 | 0.002 | 35/48 (C32, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +4.3 | 0.002 | 28/48 (C32, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.38×** | +4.3 | 0.002 | 26/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.68×** | +3.6 | 0.027 | 25/48 (C32, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.044 | 26/48 (NCI-H1792, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.29×** | +3.4 | 0.052 | 22/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +3.2 | 0.087 | 16/48 (LoVo, KATO III, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3264.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.518×** | -8.8 | 5e-16 | 36/49 (NCI-H23, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.555×** | -7.9 | 6e-13 | 39/48 (HS-578T, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.549×** | -7.8 | 1e-12 | 35/48 (SW48, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.536×** | -7.8 | 1e-12 | 34/44 (RKO, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.622×** | -6.2 | 8e-08 | 30/42 (A-427, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.695×** | -4.9 | 9e-05 | 26/48 (C-33 A, SW48, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.707×** | -4.7 | 2e-04 | 31/48 (A-172, HOP62, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.786×** | -4.6 | 3e-04 | 30/48 (SW1417, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.804×** | -4.2 | 0.002 | 26/49 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.739×** | -4.1 | 0.002 | 25/48 (HT-29, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.737×** | -3.8 | 0.007 | 25/47 (HS-578T, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.758×** | -3.6 | 0.014 | 26/48 (MIA PaCa-2, HCT15, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.767×** | -3.6 | 0.014 | 25/48 (LoVo, SNU-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.778×** | -3.4 | 0.028 | 20/48 (SW48, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **0.784×** | -3.3 | 0.038 | 21/49 (NCI-H460, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3264. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 213 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -18.6) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.122× (z -14.6) |
| [[HS-578T (line)]] | alt | 131 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.182× (z -14.9) |
| [[HT-29 (line)]] | alt | 212 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 137 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -13.4) |
| [[RKO (line)]] | wt | 50.8 | 1 (1 ⚠) | 5 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.18× (z +10.0) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.346× (z -9.3) |
| [[A-172 (line)]] | wt | 69.1 | 1 (1 ⚠) | 4 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.17× (z +9.8) ⚠ unreliable plate only | [[Harringtonine (drug)]] 0.5 µM 0.188× (z -14.2) |
| [[C32 (line)]] | wt | 127 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.0) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 68.0 | 1 (1 ⚠) | 3 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.17× (z +8.6) ⚠ unreliable plate only | [[Harringtonine (drug)]] 5 µM 0.308× (z -12.7) |
| [[HOP62 (line)]] | alt | 67.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.281× (z -11.6) |
| [[LS 180 (line)]] | wt | 84.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 54.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.89× (z +9.3) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.216× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 115 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -9.6) |
| [[A-427 (line)]] | wt | 49.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.324× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 118 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.0) ⚠ cell-cycle shift, explains ~21% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -10.4) |
| [[C-33 A (line)]] | alt | 66.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -12.4) |
| [[HCT15 (line)]] | alt | 164 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -10.9) |
| [[KATO III (line)]] | alt | 51.7 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.63× (z +8.6) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -9.8) |
| [[LoVo (line)]] | wt | 119 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.349× (z -9.3) |
| [[A498 (line)]] | wt | 87.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -10.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 69.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -12.4) ⚠ cell-cycle shift, explains ~21% of this change |
| [[J82 (line)]] | alt | 84.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 31.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.10× (z +9.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 47.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.57× (z +9.8) ⚠ unreliable plate only | — |
| [[NCI-H2030 (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 72.6 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.23× (z +12.1) ⚠ unreliable plate only | — |
| [[RPMI-7951 (line)]] | alt | 79.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -9.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 88.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 97.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0646× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 89.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -10.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 72.8 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.16× (z +9.1) ⚠ unreliable plate only | — |
| [[A549 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 78.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3264), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPAT]] | +0.65 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[TMEM120B]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[URI1]] | +0.61 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[SMG1P2]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[PHKA2]] | +0.59 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[L2HGDH]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[EEF2K]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[NANS]] | +0.58 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[TAF5L]] | +0.58 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[GNL3]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[LPCAT1]] | +0.57 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[IMPDH1]] | +0.57 | +0.56 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.64 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.64 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[CARD6]] | -0.58 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[WBP4]] | -0.57 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[ZBED5]] | -0.57 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[PAXIP1-AS2]] | -0.56 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[RIPK2-DT]] | -0.55 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[GGPS1]] | -0.55 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[RAB30-DT]] | -0.55 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[TIA1]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ZDHHC1]] | -0.54 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[YIPF4]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers NT5DC3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-2.0, 1.5); signed map (-49.4, -2.0). **Vector** length 137, 43.5% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.7 | +10.1 |
|  | [[EX229 (drug)]] 5 µM |  | +5.4 | +4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.7 | +4.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.7 | +5.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.5 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.3 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +2.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.8 | +3.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.7 | -7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.4 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -5.3 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.3 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -3.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | 5'-nucleotidase domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:103,770,453-103,841,234 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TU12B1-TY, FLJ11266 |
| Matched by | ensembl_id |

UniProt [Q86UY8](https://www.uniprot.org/uniprotkb/Q86UY8) carries no function annotation.

**Summary**, from NCBI Gene [51559](https://www.ncbi.nlm.nih.gov/gene/51559):

> Predicted to enable 5'-nucleotidase activity. Located in mitochondrion. Part of signaling receptor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30826) · Entrez [51559](https://www.ncbi.nlm.nih.gov/gene/51559) · UniProt [Q86UY8](https://www.uniprot.org/uniprotkb/Q86UY8) · Ensembl [ENSG00000111696](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111696)

## Data

Gene col 3264: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3264); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3264, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3264]; `tensor/DDL_lfc|DDL_z.npy` [3264]; `embed/gene_vectors.npy` [3264]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3264 or target_col == 3264). Every well: [[NT5DC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NT5DC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
