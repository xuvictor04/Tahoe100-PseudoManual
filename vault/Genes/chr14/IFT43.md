---
symbol: "IFT43"
type: "gene"
col: 4090
ensembl_id: "ENSG00000119650"
name: "intraflagellar transport 43"
location: "14q24.3"
module: 185
arm: "+"
pooled_cpm: 73.76
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 26
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# IFT43

*intraflagellar transport 43* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.77× (z +10.7, q 6e-24, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.521× (z -12.3, q 7e-32, down in 41 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.649× (z -8.1, q 4e-14, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ULK4]] (+0.70, fdr 7e-06), [[KATNIP]] (+0.67, fdr 7e-06), [[CDKAL1]] (+0.67, fdr 1e-05); moves opposite to [[TSPAN12]] (-0.54, fdr 4e-05), [[GPR63]] (-0.50, fdr 1e-04), [[ENTREP1]] (-0.49, fdr 4e-05).
> It is in [[Module 185]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4090.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +10.7 | 6e-24 | 47/48 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +8.5 | 7e-15 | 45/48 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +7.9 | 4e-13 | 42/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.27×** | +4.5 | 0.001 | 23/48 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 0.001 | 23/48 (SNU-423, NCI-H1792, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.1 | 0.003 | 1/50 (NCI-H1792) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.010 | 20/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.15× | +3.6 | 0.019 | 16/48 (NCI-H1573, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.22×** | +3.5 | 0.026 | 16/48 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.033 | 16/48 (HS-578T, AsPC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.4 | 0.040 | 19/48 (BT-474, RPMI-7951, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.048 | 12/49 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.20× | +3.1 | 0.075 | 19/48 (NCI-H23, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4090.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.521×** | -12.3 | 7e-32 | 41/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.538×** | -10.7 | 3e-24 | 37/47 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.565×** | -10.5 | 2e-23 | 41/49 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.591×** | -9.9 | 5e-21 | 41/48 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.614×** | -8.4 | 4e-15 | 29/43 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.649×** | -8.1 | 4e-14 | 36/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.657×** | -7.7 | 9e-13 | 36/48 (MIA PaCa-2, SW480, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.665×** | -7.1 | 1e-10 | 36/47 (HT-29, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.499×** | -6.8 | 5e-10 | 33/49 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.699×** | -6.7 | 1e-09 | 30/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.783×** | -6.5 | 4e-09 | 32/48 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.535×** | -6.2 | 3e-08 | 29/48 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.735×** | -5.8 | 3e-07 | 31/48 (COLO 205, HOP62, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.718×** | -5.8 | 3e-07 | 27/45 (C-33 A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.751×** | -5.4 | 3e-06 | 32/49 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.821×** | -5.3 | 5e-06 | 23/49 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.816×** | -3.7 | 0.006 | 25/48 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.824×** | -3.6 | 0.007 | 21/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.825×** | -3.6 | 0.008 | 23/48 (A-427, RKO, …) | all doses, flat |  |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.822×** | -3.4 | 0.016 | 12/48 (SW48, A-172, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.835× | -3.4 | 0.016 | 21/48 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.823×** | -3.4 | 0.017 | 18/48 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.827×** | -3.3 | 0.022 | 14/49 (NCI-H460, A498, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4090. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 85.1 | 0 | 10 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -23.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.253× (z -20.5) |
| [[KATO III (line)]] | alt | 78.1 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -20.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.483× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 70.8 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.233× (z -19.2) |
| [[COLO 205 (line)]] | alt | 92.9 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0948× (z -24.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 75.2 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -13.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 65.3 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.32× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.295× (z -12.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.376× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 87.0 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.387× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 113 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.517× (z -10.8) |
| [[HCT15 (line)]] | alt | 98.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -12.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 49.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 69.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -25.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 62.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.351× (z -9.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 60.8 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -15.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.463× (z -10.2) |
| [[A-427 (line)]] | wt | 86.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.456× (z -10.3) |
| [[C-33 A (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -13.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 86.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -10.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 35.4 | 0 | 2 (1 ⚠) | — | [[Cilostazol (drug)]] 0.05 µM 0.169× (z -10.5) |
| [[HOP62 (line)]] | alt | 81.7 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.114× (z -13.1) ⚠ toxic |
| [[HT-29 (line)]] | alt | 64.2 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.340× (z -11.2) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 76.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -16.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 95.8 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.139× (z -10.1) ⚠ toxic |
| [[RKO (line)]] | wt | 68.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -15.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 62.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 95.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -10.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -10.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 64.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.309× (z -9.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 77.8 | 0 | 1 (1 ⚠) | — | [[NG25 (drug)]] 5 µM 0.0880× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.376× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SHP-77 (line)]] | alt | 81.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 72.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -15.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 61.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -10.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 77.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 85.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4090), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ULK4]] | +0.70 | +0.58 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[KATNIP]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[CDKAL1]] | +0.67 | +0.54 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[UMAD1]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[NUP214]] | +0.63 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[VPS13B]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[NSMCE2]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[VTI1A]] | +0.59 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[METTL15]] | +0.58 | +0.36 / +0.65 | both halves | 1e-04 |  |
| [[TTLL5]] | +0.58 | +0.35 / +0.60 | both halves | 1e-04 | STRING 489; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LINC00630]] | +0.57 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[TNKS]] | +0.57 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[SMG6]] | +0.56 | +0.42 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN12]] | -0.54 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[GPR63]] | -0.50 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[ENTREP1]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[OGFRL1]] | -0.49 | -0.29 / -0.48 | both halves | 3e-04 |  |
| [[DSC3]] | -0.48 | -0.18 / -0.43 | ⚠ not reproduced | 9e-04 |  |
| [[NPTXR]] | -0.48 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[TRIM36]] | -0.48 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[TMEM64]] | -0.46 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[TLCD4]] | -0.46 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[RCAN3]] | -0.46 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ZDHHC2]] | -0.45 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[SLC35G1]] | -0.44 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[SLC25A30]] | -0.44 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers IFT43's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-26.8, -11.9); signed map (-19.4, 2.4). **Vector** length 84.9, 24.0% of its response variance represented; |z| ≥ 3 in 1,181 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | -1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | +4.6 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -1.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.6 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +10.7 |
|  | [[Thymol (drug)]] 5 µM |  | +1.3 | +0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.0 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.0 | +4.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -13.2 | -6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -10.7 | -5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.3 | -7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.0 | -5.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.2 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:75,902,136-76,084,585 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32173, MGC16028; previously C14orf179 |
| Gene groups (HGNC) | IFT-A complex |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FT9](https://www.uniprot.org/uniprotkb/Q96FT9) (Intraflagellar transport protein 43 homolog):

> As a component of IFT complex A (IFT-A), a complex required for retrograde ciliary transport and entry into cilia of G protein-coupled receptors (GPCRs), it is involved in ciliogenesis. Involved in retrograde ciliary transport along microtubules from the ciliary tip to the base.

**Summary**, from NCBI Gene [112752](https://www.ncbi.nlm.nih.gov/gene/112752):

> This gene encodes a subunit of the intraflagellar transport complex A (IFT-A). IFT-A is a multiprotein complex that plays an important role in cilia assembly and maintenance by mediating retrograde ciliary transport. Mutations in this gene are a cause of cranioectodermal dysplasia-3 (CED3), also known as Sensenbrenner syndrome. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:29669](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29669) · Entrez [112752](https://www.ncbi.nlm.nih.gov/gene/112752) · UniProt [Q96FT9](https://www.uniprot.org/uniprotkb/Q96FT9) · Ensembl [ENSG00000119650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119650)

## Data

Gene col 4090: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4090); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4090, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4090]; `tensor/DDL_lfc|DDL_z.npy` [4090]; `embed/gene_vectors.npy` [4090]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4090 or target_col == 4090). Every well: [[IFT43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFT43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
