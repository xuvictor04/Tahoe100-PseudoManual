---
symbol: "INTS6"
type: "gene"
col: 2272
ensembl_id: "ENSG00000102786"
name: "integrator complex subunit 6"
location: "13q14.3"
module: 38
arm: "+"
pooled_cpm: 234.53
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# INTS6

*integrator complex subunit 6* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +13.3, q 1e-37, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.581× (z -8.0, q 1e-12, down in 33 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.776× (z -5.5, q 5e-06, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM72]] (+0.76, fdr 7e-06), [[PILRA]] (+0.74, fdr 7e-06), [[SEMA4A]] (+0.71, fdr 7e-06); moves opposite to [[RPP30]] (-0.61, fdr 1e-05), [[MRS2]] (-0.58, fdr 1e-05), [[ACTR5]] (-0.58, fdr 2e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[C21orf91-OT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2272.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +13.3 | 1e-37 | 40/48 (A498, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +11.6 | 8e-29 | 42/49 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +8.4 | 9e-15 | 38/48 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +6.1 | 2e-07 | 2/50 (NCI-H1792, SW 1271) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.5 | 7e-04 | 27/48 (C32, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +3.8 | 0.014 | 27/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.022 | 26/48 (SW48, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.23× | +3.1 | 0.15 | 24/50 (SW48, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | 1.46× | +3.0 | 0.15 | 25/49 (SW480, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2272.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.581×** | -8.0 | 1e-12 | 33/44 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.611×** | -7.5 | 1e-11 | 36/49 (HCT15, A-172, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.611×** | -7.0 | 6e-10 | 32/45 (A-172, J82, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.661×** | -6.3 | 4e-08 | 40/48 (KATO III, PANC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.776×** | -5.5 | 5e-06 | 36/48 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.533×** | -5.0 | 4e-05 | 38/49 (A-427, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.720×** | -5.0 | 4e-05 | 31/48 (BT-474, HCT15, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.546×** | -4.8 | 1e-04 | 28/38 (Panc 03.27, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.557×** | -4.7 | 2e-04 | 38/47 (SW48, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.743×** | -4.5 | 3e-04 | 36/48 (SNU-1, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.753×** | -4.3 | 7e-04 | 32/48 (LoVo, SW 900, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.745×** | -4.3 | 7e-04 | 31/48 (SNU-423, J82, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.761×** | -4.2 | 0.001 | 30/48 (A-427, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.782×** | -3.8 | 0.007 | 28/48 (HCT15, BT-474, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.803×** | -3.4 | 0.030 | 27/48 (HEC-1-A, HepG2/C3A, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.804×** | -3.1 | 0.058 | 22/47 (A-427, PANC-1, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 277 | 7 (5 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.39× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -12.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 229 | 6 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.409× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 197 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +30.1) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -9.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 153 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +18.0) | — |
| [[hTERT-HPNE (line)]] | wt | 298 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -10.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 139 | 5 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.41× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -9.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 105 | 5 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +13.7) | [[NG25 (drug)]] 5 µM 0.109× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 202 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -13.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 249 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 525 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +25.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 223 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -13.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 268 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -13.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 205 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -17.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 168 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.01× (z +15.9) | — |
| [[COLO 205 (line)]] | alt | 650 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -8.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 309 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -14.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 140 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.41× (z +11.4) | [[Lonafarnib (drug)]] 5 µM 0.160× (z -9.2) ⚠ toxic |
| [[KATO III (line)]] | alt | 219 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -12.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 300 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.434× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 337 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.6) | [[Lonafarnib (drug)]] 5 µM 0.122× (z -9.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 396 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -14.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 122 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 193 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +14.2) | — |
| [[CFPAC-1 (line)]] | alt | 165 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +13.9) | — |
| [[HepG2_C3A (line)]] | wt | 236 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -10.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 290 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -11.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 345 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -11.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 150 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +15.1) | — |
| [[PANC-1 (line)]] | alt | 216 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -11.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 215 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 98.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.351× (z -9.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 145 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +10.0) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 242 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -12.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 388 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 154 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.35× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 118 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.8) | — |
| [[SNU-1 (line)]] | wt | 209 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 133 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.7) | — |
| [[A-427 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 199 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 330 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 228 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM72]] | +0.76 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[PILRA]] | +0.74 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[SEMA4A]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[THUMPD3-AS1]] | +0.71 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PPIEL-1]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[LRRC23]] | +0.69 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[NLGN3]] | +0.69 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[FGF18]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.67 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[BOLA1]] | +0.67 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PPIEL]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP30]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[MRS2]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[ACTR5]] | -0.58 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[STX7]] | -0.57 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[VPS33B]] | -0.57 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[TBC1D13]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[CDC16]] | -0.57 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[TERF1]] | -0.56 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[UBAC1]] | -0.56 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[HEATR6]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[SAAL1]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C21orf91-OT1]] | B | C21orf91-OT1 activity raises INTS6's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.69× lower at baseline in the lines without C21orf91-OT1 | 0.026 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[FER1L4]] | B | FER1L4 activity raises INTS6's level | lines that do not express FER1L4 (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without FER1L4 | 0.051 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |
| [[ASGR1]] | B | ASGR1 activity raises INTS6's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.40× lower at baseline in the lines without ASGR1 | 0.062 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.7, -17.1); signed map (15.3, 11.3). **Vector** length 147, 49.5% of its response variance represented; |z| ≥ 3 in 1,118 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.3 | +8.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +13.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +4.5 | +6.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.3 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +3.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | +3.2 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +1.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.9 | +1.3 |
| fall | [[Radotinib (drug)]] 5 µM |  | -7.2 | -5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.1 | -3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.9 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.5 | -5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -2.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -5.2 | -5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.0 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.3 — chr13:51,354,077-51,454,264 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DICE1, HDB, Notchl2, DBI-1, DDX26A, INT6; previously DDX26 |
| Gene groups (HGNC) | Integrator complex |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL03](https://www.uniprot.org/uniprotkb/Q9UL03) (Integrator complex subunit 6):

> Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol II subunit POLR2A …

**Summary**, from NCBI Gene [26512](https://www.ncbi.nlm.nih.gov/gene/26512):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. The protein encoded by this gene is a DEAD box protein that is part of a complex that interacts with the C-terminus of RNA polymerase II and is involved in 3' end processing of snRNAs. In addition, this gene is a candidate tumor suppressor and is located in the critical region of loss of heterozygosity (LOH). Multiple transcript variants encoding different isoforms have been found for …

**Accessions** — [HGNC:14879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14879) · Entrez [26512](https://www.ncbi.nlm.nih.gov/gene/26512) · UniProt [Q9UL03](https://www.uniprot.org/uniprotkb/Q9UL03) · Ensembl [ENSG00000102786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102786)

## Data

Gene col 2272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2272); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2272]; `tensor/DDL_lfc|DDL_z.npy` [2272]; `embed/gene_vectors.npy` [2272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2272 or target_col == 2272). Every well: [[INTS6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
