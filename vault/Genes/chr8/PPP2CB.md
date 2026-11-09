---
symbol: "PPP2CB"
type: "gene"
col: 2485
ensembl_id: "ENSG00000104695"
name: "protein phosphatase 2 catalytic subunit beta"
location: "8p12"
module: 39
arm: "+"
pooled_cpm: 116.31
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 9
n_dd_up_clean: 20
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# PPP2CB

*protein phosphatase 2 catalytic subunit beta* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.02× (z +14.1, q 4e-42, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.660× (z -8.3, q 4e-14, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BIRC6-AS2-1]] (+0.58, fdr 1e-05), [[SOS2]] (+0.58, fdr 1e-05), [[PHKG1]] (+0.58, fdr 1e-05); moves opposite to [[AIFM1]] (-0.55, fdr 5e-05), [[MTHFD1]] (-0.53, fdr 4e-05), [[DNMT1]] (-0.51, fdr 3e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2485.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +14.1 | 4e-42 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.59×** | +13.4 | 2e-38 | 45/49 (NCI-H1573, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +11.3 | 2e-27 | 43/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +10.8 | 8e-25 | 46/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.68×** | +10.3 | 6e-23 | 45/48 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.44×** | +10.3 | 6e-23 | 35/48 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +10.0 | 2e-21 | 43/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +8.9 | 4e-17 | 42/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +8.8 | 1e-16 | 44/48 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +8.5 | 7e-16 | 31/49 (AsPC-1, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +8.4 | 2e-15 | 44/48 (KATO III, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +7.9 | 2e-13 | 33/48 (A-427, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +7.5 | 3e-12 | 38/47 (SNU-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.66×** | +7.2 | 2e-11 | 43/49 (KATO III, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +6.6 | 1e-09 | 31/49 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.40×** | +6.5 | 2e-09 | 37/47 (HT-29, CFPAC-1, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +5.4 | 2e-06 | 28/48 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.28×** | +5.0 | 1e-05 | 32/47 (HT-29, COLO 205, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2485.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.660×** | -8.3 | 4e-14 | 38/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.699×** | -7.2 | 2e-10 | 31/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.700×** | -7.2 | 2e-10 | 33/48 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.702×** | -6.8 | 1e-09 | 27/44 (SW48, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.751×** | -5.7 | 1e-06 | 33/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.759×** | -5.5 | 3e-06 | 33/48 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.773×** | -5.2 | 2e-05 | 26/49 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.781×** | -4.6 | 3e-04 | 24/45 (SW48, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -4.0 | 0.004 | 2/50 (NCI-H23, MIA PaCa-2) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.695×** | -3.8 | 0.008 | 20/49 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -3.6 | 0.019 | 21/48 (HepG2/C3A, NCI-H23, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.841× | -3.5 | 0.026 | 18/48 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.841× | -3.3 | 0.035 | 16/48 (NCI-H2347, SNU-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.847× | -3.3 | 0.035 | 17/48 (HepG2/C3A, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.891× | -3.2 | 0.052 | 8/48 (NCI-H2347, NCI-H23, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.890× | -3.2 | 0.052 | 13/49 (Hs 766T, LS 180, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.895× | -3.2 | 0.054 | 9/48 (LOX-IMVI, A498, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.858× | -3.1 | 0.069 | 15/48 (A-427, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2485. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 89.7 | 10 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.449× (z -9.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 228 | 7 (2 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +16.1) | [[Panobinostat (drug)]] 5 µM 0.465× (z -10.4) |
| [[KATO III (line)]] | alt | 121 | 9 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.17× (z +14.0) | — |
| [[LoVo (line)]] | wt | 134 | 8 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.16× (z +15.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +15.5) | — |
| [[NCI-H460 (line)]] | wt | 101 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.56× (z +17.9) | — |
| [[HepG2_C3A (line)]] | wt | 161 | 4 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -8.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.460× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 114 | 5 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 5.83× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.433× (z -10.2) |
| [[PANC-1 (line)]] | alt | 45.3 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.11× (z +16.0) | — |
| [[SNU-1 (line)]] | wt | 138 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.72× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 157 | 3 | 1 | [[Auranofin (drug)]] 5 µM 2.07× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.550× (z -9.0) |
| [[A498 (line)]] | wt | 118 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 166 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -11.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 135 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -12.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 171 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.20× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.468× (z -11.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 152 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.59× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 152 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -9.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 58.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +10.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 132 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.05× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 58.7 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +8.8) | — |
| [[RKO (line)]] | wt | 163 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -9.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 72.0 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.78× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 123 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 117 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 93.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.431× (z -8.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 89.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 55.6 | 0 | 1 | — | [[Arbutin (drug)]] 0.05 µM 0.0672× (z -8.6) |
| [[SW1417 (line)]] | alt | 58.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +8.6) | — |
| [[A-172 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 138 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 156 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2485), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIRC6-AS2-1]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SOS2]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[PHKG1]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[CCDC181]] | +0.57 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[MFSD2B]] | +0.57 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[GSK3B-DT]] | +0.56 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[OOEP]] | +0.55 | +0.28 / +0.43 | both halves | 3e-04 |  |
| [[IL12RB2]] | +0.55 | +0.28 / +0.44 | both halves | 3e-04 |  |
| [[SYCE1L]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[NOXRED1]] | +0.54 | +0.41 / +0.39 | both halves | 5e-05 |  |
| [[SPATA1]] | +0.54 | +0.27 / +0.47 | both halves | 3e-04 |  |
| [[LRIF1]] | +0.54 | +0.41 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIFM1]] | -0.55 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[MTHFD1]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[DNMT1]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[MADD]] | -0.50 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[HOOK1]] | -0.50 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[MDM1]] | -0.49 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[DLD]] | -0.47 | -0.21 / -0.50 | both halves | 6e-04 | pathway: HALLMARK_GLYCOLYSIS |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PPP2CB's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.418). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.7, -19.2); signed map (10.3, 9.8). **Vector** length 97.7, 32.3% of its response variance represented; |z| ≥ 3 in 1,443 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.2 | +8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.7 | +7.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +7.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.6 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +0.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +0.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.6 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | -7.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | +10.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.0 | -0.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 catalytic subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:30,774,457-30,814,314 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP2Abeta |
| Gene groups (HGNC) | Protein phosphatase catalytic subunits; STRIPAK complex |
| Hallmark sets | COMPLEMENT, GLYCOLYSIS |
| Reactome | 119 pathways, smallest: PP2A-mediated dephosphorylation of key metabolic factors; MASTL Facilitates Mitotic Progression; Regulation of glycolysis by fructose 2,6-bisphosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P62714](https://www.uniprot.org/uniprotkb/P62714) (Serine/threonine-protein phosphatase 2A catalytic subunit beta isoform):

> Catalytic subunit of protein phosphatase 2A (PP2A), a serine/threonine phosphatase involved in the regulation of a wide variety of enzymes, signal transduction pathways, and cellular events (Probable). PP2A can modulate the activity of phosphorylase B kinase, casein kinase 2, mitogen-stimulated S6 kinase, and MAP-2 kinase. Part of the striatin-interacting phosphatase and kinase (STRIPAK) complexes. STRIPAK complexes have critical roles in protein (de)phosphorylation and are regulators of …

**Summary**, from NCBI Gene [5516](https://www.ncbi.nlm.nih.gov/gene/5516):

> This gene encodes the phosphatase 2A catalytic subunit. Protein phosphatase 2A is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory subunits. This gene encodes a beta isoform of the catalytic subunit. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:9300](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9300) · Entrez [5516](https://www.ncbi.nlm.nih.gov/gene/5516) · UniProt [P62714](https://www.uniprot.org/uniprotkb/P62714) · Ensembl [ENSG00000104695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104695)

## Data

Gene col 2485: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2485); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2485, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2485]; `tensor/DDL_lfc|DDL_z.npy` [2485]; `embed/gene_vectors.npy` [2485]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2485 or target_col == 2485). Every well: [[PPP2CB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2CB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
