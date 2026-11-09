---
symbol: "EHD1"
type: "gene"
col: 3105
ensembl_id: "ENSG00000110047"
name: "EH domain containing 1"
location: "11q13.1"
module: 141
arm: "+"
pooled_cpm: 44.59
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 34
n_dd_up_clean: 15
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 36
direction_downstream: 0
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# EHD1

*EH domain containing 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.77× (z +19.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (5 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.599× (z -7.2, q 5e-10, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHB]] (+0.79, fdr 7e-06), [[HBEGF]] (+0.73, fdr 7e-06), [[FAM107B]] (+0.70, fdr 7e-06); moves opposite to [[SNX13]] (-0.60, fdr 1e-05), [[CHPT1]] (-0.59, fdr 1e-05), [[PAIP1]] (-0.55, fdr 2e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 36 arrows point to it, the strongest [[SOX9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3105.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.77×** | +19.4 | 0e+00 | 48/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.36×** | +17.7 | 0e+00 | 43/47 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **8.61×** | +16.4 | 0e+00 | 46/49 (Panc 03.27, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.98×** | +16.0 | 0e+00 | 47/48 (J82, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.69×** | +14.5 | 1e-45 | 47/48 (J82, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.56×** | +13.8 | 4e-41 | 43/47 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.45×** | +12.6 | 1e-34 | 42/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +11.1 | 1e-26 | 37/47 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +8.5 | 2e-15 | 35/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.71×** | +7.6 | 2e-12 | 33/47 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +6.9 | 4e-10 | 35/48 (C32, SW480, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +6.7 | 9e-10 | 31/47 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +6.6 | 1e-09 | 30/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.41×** | +5.0 | 2e-05 | 26/48 (Panc 03.27, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.84×** | +4.7 | 1e-04 | 26/47 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.001 | 26/48 (C32, Panc 03.27, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.015 | 13/48 (Panc 03.27, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.016 | 19/48 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3105.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.599×** | -7.2 | 5e-10 | 30/47 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.650×** | -6.2 | 1e-07 | 33/48 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.648×** | -6.1 | 2e-07 | 23/34 (HCT15, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.659×** | -6.0 | 2e-07 | 30/49 (NCI-H1573, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.747×** | -6.0 | 3e-07 | 25/48 (A549, A-172, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.713×** | -5.8 | 7e-07 | 31/48 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.665×** | -5.7 | 1e-06 | 34/48 (A549, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.743×** | -5.2 | 1e-05 | 26/48 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.769×** | -5.0 | 3e-05 | 27/48 (A549, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.693×** | -4.9 | 5e-05 | 27/48 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.717×** | -4.8 | 7e-05 | 27/47 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.722×** | -4.7 | 1e-04 | 25/48 (A549, HS-578T, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.726×** | -4.6 | 2e-04 | 26/48 (J82, A-172, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.742×** | -4.5 | 3e-04 | 24/48 (A549, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.559×** | -4.4 | 4e-04 | 25/47 (SW 900, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.748×** | -4.2 | 1e-03 | 27/49 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -4.1 | 0.001 | 21/48 (NCI-H1792, Panc 03.27, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.760×** | -4.0 | 0.002 | 22/48 (HOP62, J82, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3105. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 72.0 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +13.0) | [[Cobimetinib (drug)]] 5 µM 0.310× (z -9.7) |
| [[HOP62 (line)]] | alt | 63.5 | 7 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +17.0) | [[Clobetasol propionate (drug)]] 0.05 µM 0.356× (z -9.1) |
| [[HS-578T (line)]] | alt | 58.7 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +14.7) | [[Clobetasol propionate (drug)]] 0.05 µM 0.371× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 39.8 | 4 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.225× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 60.7 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +18.7) | — |
| [[J82 (line)]] | alt | 61.5 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.52× (z +16.7) | — |
| [[LOX-IMVI (line)]] | wt | 22.0 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +13.8) | — |
| [[SNU-423 (line)]] | alt | 24.4 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.28× (z +18.8) | — |
| [[AsPC-1 (line)]] | alt | 80.1 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 41.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +15.7) | — |
| [[PANC-1 (line)]] | alt | 55.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +21.5) | — |
| [[SW480 (line)]] | alt | 33.3 | 5 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.47× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -10.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 30.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +18.5) | — |
| [[CFPAC-1 (line)]] | alt | 82.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -12.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 56.6 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 25.6× (z +13.1) | — |
| [[NCI-H460 (line)]] | wt | 20.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 36.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +10.3) | — |
| [[A-427 (line)]] | wt | 18.3 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.37× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 59.5 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 56.5 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.9× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 56.2 | 2 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.95× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 47.5 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 45.4 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.79× (z +10.1) | — |
| [[A-172 (line)]] | wt | 57.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 13.1× (z +11.8) | — |
| [[BT-474 (line)]] | alt | 53.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +12.3) | — |
| [[HCT15 (line)]] | alt | 63.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.38× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -14.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 30.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +13.3) | — |
| [[LoVo (line)]] | wt | 37.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 71.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.21× (z +10.4) | [[Adagrasib (drug)]] 0.05 µM 0.620× (z -14.9) ⚠ position not correctable |
| [[NCI-H1792 (line)]] | alt | 40.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +12.8) | [[Adagrasib (drug)]] 0.05 µM 0.635× (z -10.3) ⚠ position not correctable |
| [[NCI-H23 (line)]] | alt | 21.4 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +8.9) | — |
| [[C32 (line)]] | wt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +10.2) | — |
| [[COLO 205 (line)]] | alt | 38.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 52.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 22.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 78.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.4× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3105), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHB]] | +0.79 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[HBEGF]] | +0.73 | +0.76 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[FAM107B]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[MAP2K3]] | +0.69 | +0.75 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[KRT15]] | +0.69 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[PLAUR]] | +0.69 | +0.59 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[STK10]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[FOSL1]] | +0.68 | +0.73 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SYNJ2]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[DPF3]] | +0.67 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[WNT7B]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.66 | +0.69 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX13]] | -0.60 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[CHPT1]] | -0.59 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[PAIP1]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 34, C 2. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOX9]] | B | SOX9 activity raises EHD1's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.38× lower at baseline in the lines without SOX9 | 0.002 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[ITGA3]] | B | ITGA3 activity raises EHD1's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 2.06× lower at baseline in the lines without ITGA3 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[LAMC2]] | B | LAMC2 activity raises EHD1's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.77× lower at baseline in the lines without LAMC2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[PTK6]] | B | PTK6 activity raises EHD1's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 1.79× lower at baseline in the lines without PTK6 | 0.005 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[SMAD3]] | B | SMAD3 activity raises EHD1's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 2.30× lower at baseline in the lines without SMAD3 | 0.005 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[WNT7B]] | B | WNT7B activity raises EHD1's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without WNT7B | 0.007 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[CDCP1]] | B | CDCP1 activity raises EHD1's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without CDCP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[ADAM8]] | B | ADAM8 activity raises EHD1's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.56× lower at baseline in the lines without ADAM8 | 0.007 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[PHLDA2]] | B | PHLDA2 activity raises EHD1's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.26× lower at baseline in the lines without PHLDA2 | 0.010 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[CSF2]] | B | CSF2 activity raises EHD1's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 1.50× lower at baseline in the lines without CSF2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[LINC01589]] | B | LINC01589 activity raises EHD1's level | lines that do not express LINC01589 (23) vs lines expressing it (27) | 1.49× lower at baseline in the lines without LINC01589 | 0.012 | ⚠ within organs, on part of the lines; also absent: HNF1B, ENSG00000279806, GOLT1A |
| [[PDGFB]] | B | PDGFB activity raises EHD1's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 1.69× lower at baseline in the lines without PDGFB | 0.012 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.727). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.5, 0.2); signed map (2.3, 44.7). **Vector** length 124, 40.4% of its response variance represented; |z| ≥ 3 in 1,663 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.8 | +16.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +19.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +16.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +8.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.1 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +7.6 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +2.7 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.8 |
| fall | [[NG25 (drug)]] 5 µM |  | -6.3 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -1.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -5.9 | -6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.9 | -1.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.7 | -6.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.6 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.1 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.1 | -4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.0 | -4.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -5.0 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | EH domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,851,642-64,888,296 (-) |
| Ensembl biotype | protein_coding |
| Also known as | H-PAST, HPAST1, FLJ42622, FLJ44618; previously PAST1 |
| Gene groups (HGNC) | EF-hand domain containing |
| Hallmark sets | COMPLEMENT, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 2 pathways, smallest: Factors involved in megakaryocyte development and platelet production; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4M9](https://www.uniprot.org/uniprotkb/Q9H4M9) (EH domain-containing protein 1):

> ATP- and membrane-binding protein that controls membrane reorganization/tubulation upon ATP hydrolysis. In vitro causes vesiculation of endocytic membranes. Acts in early endocytic membrane fusion and membrane trafficking of recycling endosomes. Recruited to endosomal membranes upon nerve growth factor stimulation, indirectly regulates neurite outgrowth (By similarity). Plays a role in myoblast fusion (By similarity). Involved in the unidirectional retrograde dendritic transport of endocytosed …

**Summary**, from NCBI Gene [10938](https://www.ncbi.nlm.nih.gov/gene/10938):

> This gene belongs to a highly conserved gene family encoding EPS15 homology (EH) domain-containing proteins. The protein-binding EH domain was first noted in EPS15, a substrate for the epidermal growth factor receptor. The EH domain has been shown to be an important motif in proteins involved in protein-protein interactions and in intracellular sorting. The protein encoded by this gene is thought to play a role in the endocytosis of IGF1 receptors. Alternatively spliced transcript variants have …

**Accessions** — [HGNC:3242](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3242) · Entrez [10938](https://www.ncbi.nlm.nih.gov/gene/10938) · UniProt [Q9H4M9](https://www.uniprot.org/uniprotkb/Q9H4M9) · Ensembl [ENSG00000110047](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110047)

## Data

Gene col 3105: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3105); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3105, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3105]; `tensor/DDL_lfc|DDL_z.npy` [3105]; `embed/gene_vectors.npy` [3105]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3105 or target_col == 3105). Every well: [[EHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
