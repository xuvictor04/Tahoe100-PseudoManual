---
symbol: "ASL"
type: "gene"
col: 4742
ensembl_id: "ENSG00000126522"
name: "argininosuccinate lyase"
location: "7q11.21"
module: 218
arm: "+"
pooled_cpm: 41.09
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 28
n_dd_up_clean: 6
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/218"]
generated_by: "tahoemap"
---

# ASL

*argininosuccinate lyase* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.28× (z +13.3, q 1e-37, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.550× (z -13.6, q 3e-39, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCDH]] (+0.73, fdr 1e-05), [[CLTCL1]] (+0.69, fdr 1e-05), [[NANS]] (+0.66, fdr 9e-06); moves opposite to [[C5orf15]] (-0.64, fdr 2e-05), [[RAB11FIP2]] (-0.63, fdr 2e-05), [[DECR1]] (-0.62, fdr 1e-04).
> It is in [[Module 218]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MYO1E]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4742.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.28×** | +13.3 | 1e-37 | 43/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.14×** | +12.3 | 3e-32 | 39/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +8.2 | 4e-14 | 29/46 (SW480, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.22×** | +4.6 | 5e-04 | 20/45 (SW480, AsPC-1, …) | top dose only | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.70×** | +4.5 | 7e-04 | 27/46 (SW480, RKO, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.57×** | +3.8 | 0.013 | 21/46 (SW480, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.061 | 15/45 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.31× | +3.1 | 0.13 | 8/45 (SHP-77, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4742.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.550×** | -13.6 | 3e-39 | 40/46 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.564×** | -8.8 | 3e-16 | 39/46 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.570×** | -8.7 | 7e-16 | 35/45 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.383×** | -8.1 | 1e-13 | 36/47 (NCI-H1792, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -7.2 | 9e-11 | 33/46 (COLO 205, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.693×** | -5.9 | 4e-07 | 26/46 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.774×** | -5.8 | 6e-07 | 28/46 (HOP62, A498, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.504×** | -5.8 | 6e-07 | 30/46 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.700×** | -5.7 | 7e-07 | 26/46 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.725×** | -5.1 | 2e-05 | 30/46 (HT-29, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.734×** | -4.9 | 4e-05 | 25/45 (HOP62, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.734×** | -4.9 | 4e-05 | 27/46 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.723×** | -4.8 | 7e-05 | 26/46 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.746×** | -4.7 | 1e-04 | 26/46 (A-172, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -4.4 | 4e-04 | 3/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.765×** | -4.1 | 0.001 | 22/45 (J82, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.781×** | -3.9 | 0.002 | 22/45 (HS-578T, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.786×** | -3.8 | 0.004 | 21/46 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4742. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 51.0 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -13.1) |
| [[A-427 (line)]] | wt | 20.3 | 3 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 4.00× (z +9.6) | [[PH-797804 (drug)]] 5 µM 0.0706× (z -9.5) |
| [[HOP62 (line)]] | alt | 46.9 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.7) ⚠ cell-cycle shift, explains ~19% of this change | [[Digitoxin (drug)]] 5 µM 0.238× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.511× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 62.7 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.60× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -13.4) |
| [[PANC-1 (line)]] | alt | 28.7 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 2.64× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -13.3) |
| [[SW1417 (line)]] | alt | 57.0 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.76× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -11.9) |
| [[SW480 (line)]] | alt | 36.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.71× (z +14.6) | — |
| [[COLO 205 (line)]] | alt | 44.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -10.0) |
| [[LoVo (line)]] | wt | 32.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.8) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.13× (z +10.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.337× (z -9.2) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 76.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -11.8) |
| [[A-172 (line)]] | wt | 46.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.355× (z -9.0) |
| [[A498 (line)]] | wt | 65.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -10.1) |
| [[C32 (line)]] | wt | 37.2 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -11.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -10.2) |
| [[CHP-212 (line)]] | wt | 84.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 26.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.0) ⚠ cell-cycle shift, explains ~19% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 47.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0879× (z -17.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 30.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -10.8) |
| [[A549 (line)]] | wt | 28.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.295× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 61.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.1) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[CFPAC-1 (line)]] | alt | 57.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.4) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[HCT15 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -9.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -10.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.4) ⚠ cell-cycle shift, explains ~19% of this change |
| [[KATO III (line)]] | alt | 47.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 58.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -11.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 28.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 36.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -11.5) |
| [[AN3 CA (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.97 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.25 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4742), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCDH]] | +0.73 | +0.54 / +0.68 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[CLTCL1]] | +0.69 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[NANS]] | +0.66 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[NOSIP]] | +0.65 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[MLXIP]] | +0.63 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[SPATA2L]] | +0.62 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[OGG1]] | +0.62 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[MYO1E]] | +0.62 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[GP6-AS1]] | +0.61 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[METRNL]] | +0.61 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[MT1X]] | +0.61 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[KLHL26]] | +0.61 | +0.54 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C5orf15]] | -0.64 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[RAB11FIP2]] | -0.63 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[DECR1]] | -0.62 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[SUMO3]] | -0.61 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[MYLK-AS1]] | -0.59 | -0.47 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[EPM2A]] | -0.58 | -0.52 / -0.11 | ⚠ one half (not replicated) | 0.002 | pathway: Diseases of metabolism |
| [[AMER1]] | -0.58 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[GAS2]] | -0.58 | -0.39 / -0.26 | both halves | 4e-04 |  |
| [[ZNF362]] | -0.58 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[CRPPA]] | -0.57 | -0.41 / -0.29 | both halves | 3e-04 |  |
| [[MSL3]] | -0.57 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[FOXJ2]] | -0.57 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ANGEL2]] | -0.56 | -0.46 / -0.26 | both halves | 3e-04 |  |
| [[HFE]] | -0.56 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1E]] | B | MYO1E activity raises ASL's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without MYO1E | 0.031 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ASL's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers ASL's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FLNB]] | C | FLNB activity raises ASL's level | lines that do not express FLNB (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without FLNB | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 218]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.6, 2.9); signed map (-26.7, 16.7). **Vector** length 131, 37.7% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +9.0 | +13.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.8 | +12.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.6 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +6.0 | +4.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.0 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.3 | +1.3 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -8.1 | -5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -13.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -7.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.7 | -8.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.5 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.8 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | argininosuccinate lyase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.21 — chr7:66,075,800-66,094,697 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ASAL |
| Gene groups (HGNC) | Carbon-nitrogen lyases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 4 pathways, smallest: Diseases of the urea cycle; Urea cycle; Diseases of metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P04424](https://www.uniprot.org/uniprotkb/P04424) (Argininosuccinate lyase):

> Catalyzes the reversible cleavage of L-argininosuccinate to fumarate and L-arginine, an intermediate step reaction in the urea cycle mostly providing for hepatic nitrogen detoxification into excretable urea as well as de novo L-arginine synthesis in nonhepatic tissues. Essential regulator of intracellular and extracellular L-arginine pools. As part of citrulline-nitric oxide cycle, forms tissue-specific multiprotein complexes with argininosuccinate synthase ASS1, transport protein SLC7A1 and …

**Summary**, from NCBI Gene [435](https://www.ncbi.nlm.nih.gov/gene/435):

> This gene encodes a member of the lyase 1 family. The encoded protein forms a cytosolic homotetramer and primarily catalyzes the reversible hydrolytic cleavage of argininosuccinate into arginine and fumarate, an essential step in the liver in detoxifying ammonia via the urea cycle. Mutations in this gene result in the autosomal recessive disorder argininosuccinic aciduria, or argininosuccinic acid lyase deficiency. A nontranscribed pseudogene is also located on the long arm of chromosome 22. …

**Accessions** — [HGNC:746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:746) · Entrez [435](https://www.ncbi.nlm.nih.gov/gene/435) · UniProt [P04424](https://www.uniprot.org/uniprotkb/P04424) · Ensembl [ENSG00000126522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126522)

## Data

Gene col 4742: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4742); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4742, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4742]; `tensor/DDL_lfc|DDL_z.npy` [4742]; `embed/gene_vectors.npy` [4742]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4742 or target_col == 4742). Every well: [[ASL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
