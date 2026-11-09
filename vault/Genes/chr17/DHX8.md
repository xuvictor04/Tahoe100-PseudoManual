---
symbol: "DHX8"
type: "gene"
col: 864
ensembl_id: "ENSG00000067596"
name: "DEAH-box helicase 8"
location: "17q21.31"
module: 145
arm: "+"
pooled_cpm: 65.41
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 19
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# DHX8

*DEAH-box helicase 8* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.19× (z +21.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.615× (z -13.4, q 2e-38, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.666× (z -5.9, q 1e-06, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GATAD2B]] (+0.70, fdr 3e-05), [[MARK2]] (+0.64, fdr 7e-06), [[SUPT4H1]] (+0.60, fdr 1e-05); moves opposite to [[GLS]] (-0.47, fdr 4e-05), [[PITRM1]] (-0.46, fdr 6e-05), [[OGT]] (-0.45, fdr 9e-05).
> It is in [[Module 145]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +21.7 | 0e+00 | 48/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +21.4 | 0e+00 | 43/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +20.5 | 0e+00 | 48/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.42×** | +17.8 | 0e+00 | 46/49 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +17.6 | 0e+00 | 47/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.54×** | +13.5 | 2e-39 | 40/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +12.7 | 5e-35 | 43/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +12.4 | 2e-33 | 39/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +12.3 | 3e-33 | 38/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +12.2 | 2e-32 | 36/49 (HEC-1-A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +10.3 | 3e-23 | 38/48 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +10.1 | 2e-22 | 37/48 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +9.7 | 2e-20 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +9.6 | 2e-20 | 31/48 (SW480, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.40×** | +9.2 | 9e-19 | 34/48 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +7.5 | 2e-12 | 33/48 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +7.3 | 1e-11 | 24/48 (HOP62, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 864.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.615×** | -13.4 | 2e-38 | 47/48 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.666×** | -5.9 | 1e-06 | 25/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.697×** | -5.2 | 3e-05 | 20/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.726×** | -4.6 | 5e-04 | 23/48 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.765×** | -3.9 | 0.012 | 18/48 (SW1417, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.828×** | -3.7 | 0.018 | 12/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.960× | -3.7 | 0.021 | 0/49 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.784×** | -3.5 | 0.031 | 17/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.884× | -3.4 | 0.044 | 5/48 (BT-474, LoVo, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | 0.850× | -3.2 | 0.072 | 9/49 (NCI-H460, A498, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.921× | -3.2 | 0.072 | 6/48 (SNU-1, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 78.4 | 10 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.28× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.582× (z -9.1) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 35.9 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +13.5) | — |
| [[NCI-H23 (line)]] | alt | 74.3 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 49.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.4) | — |
| [[KATO III (line)]] | alt | 78.2 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +12.8) | — |
| [[NCI-H460 (line)]] | wt | 65.6 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.47× (z +14.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.505× (z -10.7) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 98.0 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.54× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 74.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.99× (z +14.1) | — |
| [[LOX-IMVI (line)]] | wt | 63.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +16.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 53.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.9) | — |
| [[A-427 (line)]] | wt | 77.8 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 86.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +14.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.568× (z -8.8) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 70.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.7) | — |
| [[HS-578T (line)]] | alt | 64.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +14.8) | — |
| [[SK-MEL-2 (line)]] | alt | 86.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 93.7 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.82× (z +8.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.463× (z -11.2) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 66.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.37× (z +10.2) | — |
| [[LoVo (line)]] | wt | 54.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 65.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.391× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 91.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.13× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.414× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 54.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +10.4) | — |
| [[COLO 205 (line)]] | alt | 75.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.00× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 61.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.15× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.439× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 63.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 46.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 59.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.41× (z +8.6) ⚠ toxic; cell-cycle shift, explains ~1% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 44.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.19× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 87.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.355× (z -9.4) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 66.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0734× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 68.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.7) | — |
| [[CHP-212 (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0853× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 38.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 52.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.6) | — |
| [[HepG2_C3A (line)]] | wt | 80.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 92.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 53.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +28.8) | — |
| [[NCI-H2347 (line)]] | alt | 65.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 59.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +13.8) | — |
| [[SNU-1 (line)]] | wt | 57.1 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.280× (z -10.2) |
| [[SW 1271 (line)]] | alt | 84.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 14 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2B]] | +0.70 | +0.44 / +0.71 | both halves | 3e-05 | **novel candidate** |
| [[MARK2]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[SUPT4H1]] | +0.60 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[GPKOW]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ZNF707]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[BRD8]] | +0.55 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[ZER1]] | +0.55 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[RSBN1L]] | +0.54 | +0.36 / +0.64 | both halves | 1e-04 |  |
| [[TNRC6B]] | +0.54 | +0.32 / +0.58 | both halves | 2e-04 |  |
| [[RTF1]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 | STRING 483 |
| [[IK]] | +0.53 | +0.40 / +0.63 | both halves | 4e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 445 |
| [[SYF2]] | +0.52 | +0.42 / +0.54 | both halves | 4e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 997 |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLS]] | -0.47 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[PITRM1]] | -0.46 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[OGT]] | -0.45 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[STK26]] | -0.43 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[NETO2]] | -0.42 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[ADK]] | -0.42 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[WDR41]] | -0.41 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[CYCS]] | -0.41 | -0.26 / -0.37 | both halves | 3e-04 |  |
| [[LINC00910]] | -0.41 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[KIF21A]] | -0.40 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[DESI2]] | -0.40 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[ACAD11]] | -0.40 | -0.13 / -0.47 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.5, -41.8); signed map (-4.6, -4.9). **Vector** length 80.2, 19.2% of its response variance represented; |z| ≥ 3 in 1,273 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +17.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +13.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~93% of this change | +3.7 | +2.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +7.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +4.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | -0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.0 | -13.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.0 | -4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.5 | -5.9 |
|  | [[EX229 (drug)]] 5 µM |  | -5.3 | -5.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.1 | -3.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | DEAH-box helicase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:43,483,865-43,610,338 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HRH1, Prp22, PRPF22, Dhr2; previously DDX8 |
| Gene groups (HGNC) | DEAH-box helicases; SSU processome; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14562](https://www.uniprot.org/uniprotkb/Q14562) (ATP-dependent RNA helicase DHX8):

> Involved in pre-mRNA splicing as component of the spliceosome. Facilitates nuclear export of spliced mRNA by releasing the RNA from the spliceosome.

**Summary**, from NCBI Gene [1659](https://www.ncbi.nlm.nih.gov/gene/1659):

> This gene is a member of the DEAH box polypeptide family. The encoded protein contains the DEAH (Asp-Glu-Ala-His) motif which is characteristic of all DEAH box proteins, and is thought to function as an ATP-dependent RNA helicase that regulates the release of spliced mRNAs from spliceosomes prior to their export from the nucleus. This protein may be required for the replication of human immunodeficiency virus type 1 (HIV-1). Alternative splicing results in multiple transcript variants. …

**Accessions** — [HGNC:2749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2749) · Entrez [1659](https://www.ncbi.nlm.nih.gov/gene/1659) · UniProt [Q14562](https://www.uniprot.org/uniprotkb/Q14562) · Ensembl [ENSG00000067596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067596)

## Data

Gene col 864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 864); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 864]; `tensor/DDL_lfc|DDL_z.npy` [864]; `embed/gene_vectors.npy` [864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 864 or target_col == 864). Every well: [[DHX8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
