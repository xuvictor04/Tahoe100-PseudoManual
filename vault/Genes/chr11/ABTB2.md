---
symbol: "ABTB2"
type: "gene"
col: 9225
ensembl_id: "ENSG00000166016"
name: "ankyrin repeat and BTB domain containing 2"
location: "11p13"
module: 14
arm: "+"
pooled_cpm: 234.05
n_lines_expressing: 43
n_dd_up: 48
n_dd_down: 6
n_dd_up_clean: 37
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 15
direction_downstream: 14
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ABTB2

*ankyrin repeat and BTB domain containing 2* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.46× (z +25.6, q 0e+00, up in 40 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.359× (z -14.2, q 8e-43, down in 29 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.457× (z -6.0, q 4e-07, down in 36 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCH1]] (+0.55, fdr 3e-05), [[ELOVL7]] (+0.53, fdr 1e-05), [[STX11]] (+0.52, fdr 4e-05); moves opposite to [[CEP20]] (-0.51, fdr 4e-05), [[SHPRH]] (-0.48, fdr 5e-05), [[TMLHE]] (-0.47, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[KPNA7]] → it (grade B ⚠); 14 go from it, the strongest it → [[MYO1E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9225.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.46×** | +25.6 | 0e+00 | 40/41 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.95×** | +20.0 | 0e+00 | 40/41 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.11×** | +16.4 | 0e+00 | 38/41 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.92×** | +15.6 | 0e+00 | 40/41 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.88×** | +14.6 | 0e+00 | 40/41 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.17×** | +12.5 | 4e-34 | 40/42 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +10.4 | 2e-23 | 38/41 (SW480, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +10.1 | 5e-22 | 36/41 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +9.8 | 9e-21 | 27/42 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +8.3 | 7e-15 | 31/41 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +7.9 | 1e-13 | 33/42 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.70×** | +7.7 | 8e-13 | 30/41 (BT-474, PANC-1, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +7.4 | 6e-12 | 30/40 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +7.4 | 7e-12 | 35/41 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +6.7 | 1e-09 | 28/41 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +6.6 | 2e-09 | 32/41 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9225.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.359×** | -14.2 | 8e-43 | 29/37 (SK-MEL-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.601×** | -7.5 | 2e-11 | 27/42 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.457×** | -6.0 | 4e-07 | 36/41 (A549, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.737×** | -4.5 | 0.001 | 23/41 (HT-29, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.743×** | -4.4 | 0.001 | 26/41 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.821×** | -4.1 | 0.004 | 21/41 (NCI-H1792, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -3.1 | 0.17 | 2/43 (NCI-H1792, NCI-H1573) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9225. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 226 | 6 (2 ⚠) | 14 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.50× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.71× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.189× (z -11.3) |
| [[LS 180 (line)]] | wt | 104 | 13 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +18.6) | — |
| [[NCI-H460 (line)]] | wt | 83.2 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +16.8) | — |
| [[H4 (line)]] | wt | 64.1 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +18.6) | — |
| [[SK-MEL-2 (line)]] | alt | 377 | 1 | 11 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.45× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.0981× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.327× (z -10.9) |
| [[SW480 (line)]] | alt | 114 | 12 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.81× (z +21.8) | — |
| [[PANC-1 (line)]] | alt | 185 | 10 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +20.1) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -11.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 207 | 9 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 213 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -9.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 103 | 8 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.81× (z +13.8) | [[Ponatinib (drug)]] 5 µM 0.341× (z -9.5) |
| [[RKO (line)]] | wt | 103 | 9 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +18.5) | — |
| [[SW1417 (line)]] | alt | 451 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -14.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 115 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +26.1) | — |
| [[HS-578T (line)]] | alt | 92.3 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +25.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 147 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +14.5) | — |
| [[Panc 03.27 (line)]] | alt | 603 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +21.5) | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -23.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 269 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +16.8) | — |
| [[J82 (line)]] | alt | 275 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 470 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -24.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -11.2) |
| [[A-172 (line)]] | wt | 133 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -10.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 430 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +23.2) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -16.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 398 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.20× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 184 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.79× (z +13.2) | — |
| [[SW 900 (line)]] | alt | 107 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +20.3) | — |
| [[A549 (line)]] | wt | 524 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -14.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 61.3 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 12.0× (z +15.6) | — |
| [[NCI-H23 (line)]] | alt | 87.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.59× (z +13.2) | — |
| [[RPMI-7951 (line)]] | alt | 188 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.7) | — |
| [[SW48 (line)]] | wt | 81.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 8.92× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 629 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -9.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 238 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +20.5) | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -13.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 290 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -18.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 538 | 0 | 3 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.221× (z -12.8) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 94.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -10.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 97.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +11.5) | — |
| [[C32 (line)]] | wt | 426 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -10.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 343 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 540 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 243 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.4) | — |
| [[SW 1088 (line)]] | alt | 132 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +12.4) | — |
| [[SW 1271 (line)]] | alt | 332 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +9.6) | — |
| [[A-427 (line)]] | wt | 33.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 28.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 37.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 28.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 45.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9225), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCH1]] | +0.55 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[ELOVL7]] | +0.53 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[STX11]] | +0.52 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[RND1]] | +0.52 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[TICAM1]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[RNF19B]] | +0.52 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[KPNA7]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CDKN2B]] | +0.51 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[SDC4]] | +0.51 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[RAP1B]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[FGD6]] | +0.51 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[IGSF3]] | +0.51 | +0.36 / +0.57 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP20]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[SHPRH]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[TMLHE]] | -0.47 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PPWD1]] | -0.46 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[ARL5A]] | -0.45 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[PDSS2]] | -0.44 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[SMARCAD1]] | -0.44 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[XPNPEP3]] | -0.44 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[TAS2R14]] | -0.43 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[ZCCHC4]] | -0.43 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[TUBGCP4]] | -0.43 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[ZNF566]] | -0.43 | -0.36 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KPNA7]] | B | KPNA7 activity raises ABTB2's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 2.68× lower at baseline in the lines without KPNA7 | 0.006 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[IRF6]] | B | IRF6 activity raises ABTB2's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without IRF6 | 0.013 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[MYO1E]] | B | MYO1E activity raises ABTB2's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 3.05× lower at baseline in the lines without MYO1E | 0.019 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[BIK]] | B | BIK activity raises ABTB2's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.25× lower at baseline in the lines without BIK | 0.024 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[CYP3A5]] | B | CYP3A5 activity raises ABTB2's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.00× lower at baseline in the lines without CYP3A5 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[LAMC2]] | B | LAMC2 activity raises ABTB2's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.72× lower at baseline in the lines without LAMC2 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[RNF223]] | B | RNF223 activity raises ABTB2's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 1.89× lower at baseline in the lines without RNF223 | 0.064 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[NFATC2]] | B | NFATC2 activity raises ABTB2's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 2.31× lower at baseline in the lines without NFATC2 | 0.065 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[TRIB1]] | B | TRIB1 activity raises ABTB2's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.82× lower at baseline in the lines without TRIB1 | 0.066 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[CYP3A5]] | B | CYP3A5 activity weakens ABTB2's drug response | lines that do not express CYP3A5 (25) vs lines expressing it (17) | the lines without CYP3A5 respond 1.14× as strongly (z diff -0.78); strongest at Homoharringtonine 0.5 µM: 2.66x vs 1.62x (z diff -2.5) | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A; target measured in part of the lines; artifact flags |
| [[DAPP1]] | B | DAPP1 activity raises ABTB2's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 2.01× lower at baseline in the lines without DAPP1 | 0.077 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[SDC4]] | B | SDC4 activity raises ABTB2's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 3.41× lower at baseline in the lines without SDC4 | 0.082 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2 |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 12, C 2. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1E]] | B | ABTB2 activity raises MYO1E's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 3.32× lower at baseline in the lines without ABTB2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[TNFAIP8]] | B | ABTB2 activity raises TNFAIP8's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without ABTB2 | 0.015 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[SDC4]] | B | ABTB2 activity raises SDC4's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 3.77× lower at baseline in the lines without ABTB2 | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[EHD1]] | B | ABTB2 activity raises EHD1's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 2.07× lower at baseline in the lines without ABTB2 | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[MED15]] | B | ABTB2 activity raises MED15's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 1.44× lower at baseline in the lines without ABTB2 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[IER3]] | B | ABTB2 activity raises IER3's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without ABTB2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[TRIB1]] | B | ABTB2 activity raises TRIB1's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 2.41× lower at baseline in the lines without ABTB2 | 0.057 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[IFFO2]] | B | ABTB2 activity raises IFFO2's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without ABTB2 | 0.077 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[BAIAP2L1]] | B | ABTB2 activity raises BAIAP2L1's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 2.76× lower at baseline in the lines without ABTB2 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[SLC25A45]] | B | ABTB2 activity raises SLC25A45's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 1.88× lower at baseline in the lines without ABTB2 | 0.088 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| cells under [[Filgotinib (drug)]] 0.05 µM | B | ABTB2 activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express ABTB2 (7) vs lines expressing it (41) | the lines without ABTB2: 1.15× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| cells under [[Tolcapone (drug)]] 5 µM | B | ABTB2 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express ABTB2 (7) vs lines expressing it (41) | the lines without ABTB2: 0.82× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.400). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.2, 4.0); signed map (5.8, 21.8). **Vector** length 114, 39.9% of its response variance represented; |z| ≥ 3 in 1,685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +7.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.7 | +6.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.5 | +5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +8.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.0 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.1 |
|  | [[Auranofin (drug)]] 0.5 µM |  | +2.2 | +1.5 |
| fall | [[NG25 (drug)]] 5 µM |  | -7.3 | -6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -14.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.1 | +6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.9 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.6 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and BTB domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:34,150,987-34,358,010 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586C1619, BTBD22, ABTB2A |
| Gene groups (HGNC) | Ankyrin repeat domain containing; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N961](https://www.uniprot.org/uniprotkb/Q8N961) (Ankyrin repeat and BTB/POZ domain-containing protein 2):

> May be involved in the initiation of hepatocyte growth.

**Summary**, from NCBI Gene [25841](https://www.ncbi.nlm.nih.gov/gene/25841):

> Predicted to enable protein heterodimerization activity. Predicted to act upstream of or within cellular response to toxic substance. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23842](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23842) · Entrez [25841](https://www.ncbi.nlm.nih.gov/gene/25841) · UniProt [Q8N961](https://www.uniprot.org/uniprotkb/Q8N961) · Ensembl [ENSG00000166016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166016)

## Data

Gene col 9225: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9225); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9225, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9225]; `tensor/DDL_lfc|DDL_z.npy` [9225]; `embed/gene_vectors.npy` [9225]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9225 or target_col == 9225). Every well: [[ABTB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABTB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
