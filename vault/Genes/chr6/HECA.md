---
symbol: "HECA"
type: "gene"
col: 3368
ensembl_id: "ENSG00000112406"
name: "HECA ribonucleoprotein granule regulator"
location: "6q24.1"
module: 69
arm: "+"
pooled_cpm: 32.34
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 18
n_dd_up_clean: 16
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# HECA

*HECA ribonucleoprotein granule regulator* — 6q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +16.4, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.366× (z -15.2, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.258× (z -10.7, q 3e-24, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YPEL5]] (+0.69, fdr 7e-06), [[MTURN]] (+0.68, fdr 7e-06), [[MOB2]] (+0.66, fdr 2e-05); moves opposite to [[RBM26]] (-0.66, fdr 1e-05), [[FASTKD2]] (-0.56, fdr 1e-05), [[PAK1IP1]] (-0.55, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3368.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +16.4 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +6.1 | 3e-07 | 31/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +5.4 | 1e-05 | 32/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +5.1 | 5e-05 | 28/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.0 | 5e-05 | 26/47 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.80×** | +4.6 | 3e-04 | 22/47 (LoVo, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 0.001 | 21/48 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.002 | 20/47 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.69×** | +4.1 | 0.002 | 20/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.0 | 0.004 | 23/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.28×** | +3.8 | 0.009 | 19/48 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.29×** | +3.7 | 0.012 | 22/47 (LoVo, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.017 | 17/47 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.021 | 18/47 (SW480, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.022 | 17/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.022 | 18/48 (SNU-1, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.030 | 5/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.032 | 19/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3368.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.366×** | -15.2 | 0e+00 | 47/48 (AsPC-1, LoVo, …) | inconsistent across doses | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.258×** | -10.7 | 3e-24 | 46/47 (LoVo, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.325×** | -8.9 | 2e-16 | 43/48 (COLO 205, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.338×** | -8.6 | 2e-15 | 40/47 (LoVo, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.349×** | -8.3 | 1e-14 | 38/47 (RKO, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.354×** | -8.2 | 2e-14 | 43/47 (AsPC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.683×** | -5.4 | 5e-06 | 25/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.583×** | -5.1 | 2e-05 | 30/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -5.1 | 2e-05 | 30/46 (CHP-212, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.539×** | -4.9 | 7e-05 | 30/46 (SW48, NCI-H1573, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.601×** | -4.8 | 8e-05 | 30/48 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.613×** | -4.6 | 2e-04 | 30/48 (LoVo, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -4.2 | 0.001 | 1/49 (CHP-212) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.749×** | -4.2 | 0.001 | 24/48 (AN3 CA, HT-29, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.760×** | -4.1 | 0.001 | 22/44 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Radotinib (drug)]] 5 µM |  | 0.863× | -3.1 | 0.052 | 20/48 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Filgotinib (drug)]] 0.5 µM |  | **0.813×** | -3.1 | 0.053 | 18/48 (HepG2/C3A, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.1 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 10.4 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +12.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.261× (z -8.9) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 50.9 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.255× (z -12.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.118× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 56.2 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.166× (z -14.2) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0856× (z -10.2) |
| [[LoVo (line)]] | wt | 41.4 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.287× (z -12.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0965× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 30.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.358× (z -9.1) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 37.2 | 0 | 2 (1 ⚠) | — | [[venetoclax (drug)]] 5 µM 0.0568× (z -10.9) |
| [[SW48 (line)]] | wt | 43.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 22.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.260× (z -10.3) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 38.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.6) | — |
| [[A498 (line)]] | wt | 24.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.8) | — |
| [[A549 (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.172× (z -11.6) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0690× (z -10.1) |
| [[COLO 205 (line)]] | alt | 32.2 | 0 | 1 | — | [[Abemaciclib (drug)]] 5 µM 0.0576× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.101× (z -9.0) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 25.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 1 | — | [[TAK-733 (drug)]] 5 µM 0.0541× (z -9.9) |
| [[HT-29 (line)]] | alt | 50.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -11.0) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 37.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.8) | — |
| [[KATO III (line)]] | alt | 46.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.272× (z -11.2) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 34.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.266× (z -8.9) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 43.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 33.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.227× (z -12.4) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 64.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.226× (z -10.9) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 81.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.363× (z -8.8) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL5]] | +0.69 | +0.58 / +0.77 | both halves | 7e-06 | STRING 469 |
| [[MTURN]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[MOB2]] | +0.66 | +0.48 / +0.74 | both halves | 2e-05 |  |
| [[WIPI2]] | +0.65 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[REPS2]] | +0.62 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[INSR]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[SERINC1]] | +0.61 | +0.35 / +0.72 | both halves | 1e-04 |  |
| [[TCP11L2]] | +0.59 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[PDCD4]] | +0.59 | +0.37 / +0.69 | both halves | 9e-05 |  |
| [[KLHL24]] | +0.59 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[CCDC28A]] | +0.59 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[CALCOCO1]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM26]] | -0.66 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[FASTKD2]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[PAK1IP1]] | -0.55 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[AFG1L]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[LTV1]] | -0.54 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[AGK]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[SMARCAD1]] | -0.54 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[MRPS9]] | -0.54 | -0.37 / -0.60 | both halves | 9e-05 |  |
| [[MRPL1]] | -0.53 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[TCERG1]] | -0.53 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ACBD6]] | -0.52 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[THUMPD2]] | -0.51 | -0.41 / -0.57 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.3, -45.1); signed map (-17.6, 11.0). **Vector** length 118, 32.5% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +16.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.6 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | -0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +4.4 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +3.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.6 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.1 | -15.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.9 | -10.7 |
|  | [[EX229 (drug)]] 5 µM |  | -8.5 | -8.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.9 | -8.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.5 | -8.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.0 | -8.9 |

## What is on record

|  |  |
|---|---|
| Name | HECA ribonucleoprotein granule regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.1 — chr6:139,135,080-139,180,802 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HDCL, hHDC, HDC, dJ225E12.1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBI9](https://www.uniprot.org/uniprotkb/Q9UBI9) (Headcase protein homolog):

> May play an important role in some human cancers. May be part of the regulatory mechanism in the development of epithelial tube networks such as the circulatory system and lungs.

**Summary**, from NCBI Gene [51696](https://www.ncbi.nlm.nih.gov/gene/51696):

> This gene encodes the homolog of the Drosophila headcase protein, a highly basic, cytoplasmic protein that regulates the re-entry of imaginal cells into the mitotic cycle during adult morphogenesis. In Drosophila, the encoded protein also inhibits terminal branching of neighboring cells during tracheal development. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21041) · Entrez [51696](https://www.ncbi.nlm.nih.gov/gene/51696) · UniProt [Q9UBI9](https://www.uniprot.org/uniprotkb/Q9UBI9) · Ensembl [ENSG00000112406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112406)

## Data

Gene col 3368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3368); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3368]; `tensor/DDL_lfc|DDL_z.npy` [3368]; `embed/gene_vectors.npy` [3368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3368 or target_col == 3368). Every well: [[HECA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HECA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
