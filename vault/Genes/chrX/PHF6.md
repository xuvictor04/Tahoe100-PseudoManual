---
symbol: "PHF6"
type: "gene"
col: 7995
ensembl_id: "ENSG00000156531"
name: "PHD finger protein 6"
location: "Xq26.2"
module: 25
arm: "+"
pooled_cpm: 54.2
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# PHF6

*PHD finger protein 6* — Xq26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.80× (z +15.2, q 0e+00, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.51× (z +10.6, q 5e-24, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.719× (z -12.1, q 8e-31, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSX2IP]] (+0.70, fdr 7e-06), [[HLTF]] (+0.68, fdr 1e-05), [[ALG10]] (+0.66, fdr 7e-06); moves opposite to [[ST7-AS2]] (-0.65, fdr 3e-05), [[DENND6A-AS1]] (-0.65, fdr 4e-05), [[LINC02951]] (-0.64, fdr 6e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZHX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7995.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.80×** | +15.2 | 0e+00 | 43/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.79×** | +15.0 | 0e+00 | 43/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.74×** | +14.3 | 2e-44 | 39/48 (SNU-423, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.69×** | +13.6 | 1e-39 | 40/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.56×** | +10.6 | 2e-24 | 33/45 (MIA PaCa-2, A-172, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +10.6 | 5e-24 | 41/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +9.2 | 2e-18 | 35/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.44×** | +9.0 | 1e-17 | 28/43 (SNU-423, NCI-H460, …) | all doses, flat | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +6.7 | 2e-09 | 25/48 (AsPC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.29×** | +6.3 | 2e-08 | 21/47 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.21×** | +4.9 | 5e-05 | 23/48 (NCI-H23, HT-29, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.6 | 2e-04 | 17/48 (NCI-H1792, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +4.3 | 7e-04 | 18/48 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.18× | +4.1 | 0.002 | 20/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | 1.17× | +4.0 | 0.002 | 15/48 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.025 | 9/48 (SNU-423, PANC-1, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.028 | 12/48 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.10× | +3.3 | 0.028 | 6/48 (MIA PaCa-2, SW48, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.14× | +3.2 | 0.031 | 5/48 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.12× | +3.0 | 0.069 | 14/48 (C32, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7995.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -12.1 | 8e-31 | 34/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.746×** | -7.6 | 9e-12 | 29/48 (NCI-H23, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.768×** | -6.9 | 1e-09 | 27/48 (NCI-H23, SW 1088, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.794×** | -6.0 | 3e-07 | 26/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.648×** | -5.9 | 5e-07 | 29/49 (NCI-H1573, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.846× | -4.3 | 0.001 | 18/47 (Panc 03.27, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.891× | -4.3 | 0.002 | 16/48 (NCI-H2347, Hs 766T, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.756×** | -3.8 | 0.011 | 16/48 (Panc 03.27, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.870× | -3.3 | 0.059 | 8/48 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Bergenin (drug)]] 0.5 µM |  | 0.882× | -3.3 | 0.059 | 11/48 (HCT15, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7995. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 33.2 | 5 (5 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.25× (z +12.8) ⚠ cell-cycle shift, explains ~39% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 55.3 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 69.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 43.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -11.1) |
| [[PANC-1 (line)]] | alt | 83.4 | 2 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 1.78× (z +8.9) ⚠ cell-cycle shift, explains ~39% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.661× (z -9.2) |
| [[C32 (line)]] | wt | 30.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.08× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.327× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 48.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -8.5) |
| [[J82 (line)]] | alt | 57.8 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.05× (z +9.3) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 82.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.449× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 82.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -9.7) |
| [[SNU-423 (line)]] | alt | 60.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[SW1417 (line)]] | alt | 55.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.4) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 24.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | — |
| [[A-427 (line)]] | wt | 78.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 47.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 28.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 32.3 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.12× (z +8.6) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[Panc 03.27 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.413× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 54.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -9.0) |
| [[SW48 (line)]] | wt | 41.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | — |
| [[SW480 (line)]] | alt | 122 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -14.8) |
| [[AN3 CA (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 72.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 74.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7995), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*34 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSX2IP]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[HLTF]] | +0.68 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ALG10]] | +0.66 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[CDCA7L]] | +0.66 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MOCS2]] | +0.65 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ELMOD2]] | +0.65 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[ZDHHC21]] | +0.63 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[IPO8]] | +0.63 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[DLD]] | +0.61 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[LRRCC1]] | +0.61 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[ECHS1]] | +0.61 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[FIGNL1]] | +0.60 | +0.42 / +0.56 | both halves | 4e-05 | pathway: DNA Double-Strand Break Repair |

## Genes that move opposite

*66 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST7-AS2]] | -0.65 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[DENND6A-AS1]] | -0.65 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[LINC02951]] | -0.64 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[SLC23A1]] | -0.64 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[ZBTB20-AS5]] | -0.63 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[SPATA1]] | -0.63 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[EHBP1-AS1]] | -0.63 | -0.36 / -0.64 | both halves | 9e-05 |  |
| [[CNPY2-AS1]] | -0.63 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[MED28-DT]] | -0.63 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[SPATC1]] | -0.63 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[CHMP3-AS1]] | -0.62 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[PCF11-AS1]] | -0.61 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZHX2]] | B | ZHX2 activity lowers PHF6's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.57× higher at baseline in the lines without ZHX2 | 0.057 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[HDAC6]] | B | HDAC6 activity lowers PHF6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.0, -36.2); signed map (-33.5, -35.1). **Vector** length 97.7, 22.8% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.2 | +15.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.7 | +9.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +10.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.5 | +4.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +2.5 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.8 | -12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.0 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.8 | -7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.7 | -1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.2 — chrX:134,373,288-134,428,791 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1823, MGC14797, CENP-31; previously BFLS, BORJ |
| Gene groups (HGNC) | PHD finger proteins |
| Reactome | 16 pathways, smallest: RNA Polymerase I Promoter Opening; SWI/SNF chromatin remodelers; RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWS0](https://www.uniprot.org/uniprotkb/Q8IWS0) (PHD finger protein 6):

> Transcriptional regulator that associates with ribosomal RNA promoters and suppresses ribosomal RNA (rRNA) transcription.

**Summary**, from NCBI Gene [84295](https://www.ncbi.nlm.nih.gov/gene/84295):

> This gene is a member of the plant homeodomain (PHD)-like finger (PHF) family. It encodes a protein with two PHD-type zinc finger domains, indicating a potential role in transcriptional regulation, that localizes to the nucleolus. Mutations affecting the coding region of this gene or the splicing of the transcript have been associated with Borjeson-Forssman-Lehmann syndrome (BFLS), a disorder characterized by cognitive disability, epilepsy, hypogonadism, hypometabolism, obesity, swelling of …

**Accessions** — [HGNC:18145](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18145) · Entrez [84295](https://www.ncbi.nlm.nih.gov/gene/84295) · UniProt [Q8IWS0](https://www.uniprot.org/uniprotkb/Q8IWS0) · Ensembl [ENSG00000156531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156531)

## Data

Gene col 7995: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7995); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7995, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7995]; `tensor/DDL_lfc|DDL_z.npy` [7995]; `embed/gene_vectors.npy` [7995]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7995 or target_col == 7995). Every well: [[PHF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
