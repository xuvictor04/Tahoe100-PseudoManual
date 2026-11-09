---
symbol: "MCU"
type: "gene"
col: 7941
ensembl_id: "ENSG00000156026"
name: "mitochondrial calcium uniporter"
location: "10q22.1"
module: 95
arm: "-"
pooled_cpm: 204.49
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# MCU

*mitochondrial calcium uniporter* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.57× (z +11.5, q 7e-28, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.524× (z -15.9, q 0e+00, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.672× (z -10.2, q 2e-22, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMTK2]] (+0.60, fdr 3e-05), [[CYRIB]] (+0.60, fdr 2e-05), [[CDC42SE2]] (+0.57, fdr 1e-05); moves opposite to [[CYP4V2]] (-0.56, fdr 1e-04), [[TRMT13]] (-0.53, fdr 2e-04), [[KDM6B]] (-0.53, fdr 5e-05).
> It sits in the **-** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CDH1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7941.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +11.5 | 7e-28 | 41/48 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +8.6 | 3e-15 | 33/48 (RKO, A498, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +8.2 | 3e-14 | 32/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +7.8 | 9e-13 | 33/45 (RKO, SW480, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +7.5 | 5e-12 | 31/48 (A498, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.48×** | +6.0 | 2e-07 | 34/49 (RKO, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.24×** | +5.4 | 4e-06 | 25/48 (H4, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.18× | +4.2 | 0.002 | 20/48 (SW480, hTERT-HPNE, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.15× | +3.6 | 0.021 | 14/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.5 | 0.024 | 19/48 (PANC-1, HepG2/C3A, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.14× | +3.4 | 0.029 | 16/48 (J82, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.1 | 0.11 | 14/48 (NCI-H1792, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7941.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.524×** | -15.9 | 0e+00 | 39/44 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.558×** | -13.8 | 5e-41 | 38/45 (SW48, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.601×** | -13.1 | 1e-36 | 42/49 (A-427, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.672×** | -10.2 | 2e-22 | 41/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.691×** | -9.5 | 2e-19 | 40/48 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.794×** | -8.4 | 6e-15 | 25/49 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.835× | -6.6 | 4e-09 | 23/48 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.634×** | -6.1 | 7e-08 | 27/49 (KATO III, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.846× | -6.1 | 9e-08 | 19/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.644×** | -5.9 | 2e-07 | 26/38 (NCI-H2347, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.834× | -4.7 | 2e-04 | 24/48 (C32, NCI-H1573, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.900× | -3.8 | 0.006 | 3/48 (SNU-423, AsPC-1, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.878× | -3.3 | 0.037 | 13/47 (J82, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 0.05 µM |  | 0.878× | -3.1 | 0.066 | 6/48 (LS 180, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7941. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 530 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -23.3) |
| [[KATO III (line)]] | alt | 497 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -17.4) |
| [[NCI-H2347 (line)]] | alt | 321 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -22.5) |
| [[LoVo (line)]] | wt | 288 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -17.1) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -16.0) |
| [[SW1417 (line)]] | alt | 194 | 1 | 6 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -11.0) |
| [[A-427 (line)]] | wt | 156 | 1 | 5 (5 ⚠) | [[Auranofin (drug)]] 5 µM 1.80× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -20.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 252 | 1 | 5 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.86× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -12.1) |
| [[RKO (line)]] | wt | 197 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.90× (z +14.4) | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -14.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 199 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +10.8) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.82× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.474× (z -12.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 131 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.32× (z +12.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.511× (z -10.1) |
| [[A498 (line)]] | wt | 220 | 3 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.60× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 252 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.456× (z -10.0) |
| [[A-172 (line)]] | wt | 146 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.416× (z -12.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 254 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -13.3) |
| [[C32 (line)]] | wt | 140 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.14× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -12.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 244 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 130 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.495× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 201 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -12.2) |
| [[PANC-1 (line)]] | alt | 153 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.61× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.545× (z -11.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 183 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.441× (z -10.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 256 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -18.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 332 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -14.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 458 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -14.6) |
| [[H4 (line)]] | wt | 102 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.69× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -8.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 168 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.577× (z -9.0) ⚠ cell-cycle shift, explains ~69% of this change |
| [[HT-29 (line)]] | alt | 243 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.15× (z +9.0) | [[Docetaxel (drug)]] 0.05 µM 0.451× (z -9.5) ⚠ transcription drop |
| [[J82 (line)]] | alt | 90.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.16× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 162 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 1.87× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.373× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 156 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -16.4) ⚠ cell-cycle shift, explains ~69% of this change |
| [[NCI-H2030 (line)]] | alt | 130 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.600× (z -10.3) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.525× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 169 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.74× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.557× (z -9.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 103 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.16× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.431× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 199 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -12.2) |
| [[SNU-423 (line)]] | alt | 154 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.453× (z -10.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 272 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -14.5) |
| [[AN3 CA (line)]] | alt | 226 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -8.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -8.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -10.9) ⚠ cell-cycle shift, explains ~69% of this change |
| [[HS-578T (line)]] | alt | 89.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.469× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.428× (z -9.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 90.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.430× (z -9.5) |
| [[SW 1088 (line)]] | alt | 118 | 0 | 1 | — | [[Bendamustine (drug)]] 0.5 µM 0.0441× (z -13.5) |
| [[C-33 A (line)]] | alt | 173 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 209 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7941), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMTK2]] | +0.60 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[CYRIB]] | +0.60 | +0.60 / +0.47 | both halves | 2e-05 | same gene group |
| [[CDC42SE2]] | +0.57 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ABHD3]] | +0.56 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[RAD9A]] | +0.55 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[HSPA1B]] | +0.55 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[ANKRD39]] | +0.54 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[PIP4K2A]] | +0.54 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[RHPN2]] | +0.53 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[CYTH1]] | +0.53 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[MBOAT2]] | +0.52 | +0.57 / +0.39 | both halves | 6e-05 |  |
| [[UBE2H]] | +0.52 | +0.57 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP4V2]] | -0.56 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[TRMT13]] | -0.53 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[KDM6B]] | -0.53 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[MSANTD3-TMEFF1]] | -0.53 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[ZBTB2]] | -0.52 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[LINC00240]] | -0.52 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[FAM200B]] | -0.52 | -0.60 / -0.29 | both halves | 2e-04 |  |
| [[PCID2]] | -0.52 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[POLI]] | -0.52 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[ST20-MTHFS]] | -0.52 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[AMZ2]] | -0.52 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[ANAPC13]] | -0.52 | -0.60 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH1]] | B | CDH1 activity raises MCU's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 1.89× lower at baseline in the lines without CDH1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[FA2H]] | B | FA2H activity raises MCU's level | lines that do not express FA2H (27) vs lines expressing it (23) | 1.75× lower at baseline in the lines without FA2H | 0.005 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[KCNK1]] | B | KCNK1 activity raises MCU's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 1.59× lower at baseline in the lines without KCNK1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[CLDN4]] | B | CLDN4 activity raises MCU's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without CLDN4 | 0.012 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[HDAC6]] | B | HDAC6 activity lowers MCU's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers MCU's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CRYBG2]] | B | CRYBG2 activity raises MCU's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 1.51× lower at baseline in the lines without CRYBG2 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **-** arm (projection on the module's main direction -0.456). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-4.1, 35.1); signed map (-17.9, 37.8). **Vector** length 118, 35.7% of its response variance represented; |z| ≥ 3 in 1,349 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.4 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.1 | +7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.8 | +8.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.2 | +7.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +8.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.9 | +6.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +0.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.7 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.6 | -10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -8.2 | -6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.6 | -2.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -4.2 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial calcium uniporter |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:72,692,143-72,887,694 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ46135; previously C10orf42, CCDC109A |
| Gene groups (HGNC) | MicroRNA protein coding host genes; MCU complex subunits |
| Reactome | 3 pathways, smallest: Processing of SMDT1; Mitochondrial calcium ion transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NE86](https://www.uniprot.org/uniprotkb/Q8NE86) (Calcium uniporter protein, mitochondrial):

> Channel-forming and calcium-conducting subunit of the mitochondrial inner membrane calcium uniporter complex (uniplex), which mediates calcium uptake into the mitochondrial matrix. MCU channel activity is regulated by the calcium-sensor subunits of the uniplex MICU1 and MICU2 (or MICU3). Mitochondrial calcium homeostasis plays key roles in cellular physiology and regulates ATP production, cytoplasmic calcium signals and activation of cell death pathways. Involved in buffering the amplitude of …

**Summary**, from NCBI Gene [90550](https://www.ncbi.nlm.nih.gov/gene/90550):

> Enables calcium channel activity; identical protein binding activity; and uniporter activity. Involved in several processes, including cellular response to calcium ion starvation; positive regulation of mitochondrial calcium ion concentration; and positive regulation of mitochondrial fission. Located in mitochondrion. Part of uniplex complex. Is active in mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23526) · Entrez [90550](https://www.ncbi.nlm.nih.gov/gene/90550) · UniProt [Q8NE86](https://www.uniprot.org/uniprotkb/Q8NE86) · Ensembl [ENSG00000156026](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156026)

## Data

Gene col 7941: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7941); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7941, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7941]; `tensor/DDL_lfc|DDL_z.npy` [7941]; `embed/gene_vectors.npy` [7941]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7941 or target_col == 7941). Every well: [[MCU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
