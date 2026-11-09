---
symbol: "LAMP2"
type: "gene"
col: 93
ensembl_id: "ENSG00000005893"
name: "lysosome associated membrane protein 2"
location: "Xq24"
module: 29
arm: "+"
pooled_cpm: 128.96
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# LAMP2

*lysosome associated membrane protein 2* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.41× (z +17.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.754× (z -5.5, q 2e-05, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNS]] (+0.84, fdr 7e-06), [[SCARB2]] (+0.74, fdr 7e-06), [[LAMP1]] (+0.74, fdr 7e-06); moves opposite to [[SURF6]] (-0.68, fdr 7e-06), [[ZNF593]] (-0.66, fdr 1e-05), [[CCDC137]] (-0.65, fdr 2e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 93.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.41×** | +17.8 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +15.3 | 0e+00 | 47/49 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +14.8 | 0e+00 | 43/44 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +13.4 | 5e-39 | 45/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +12.6 | 3e-34 | 47/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +12.0 | 4e-31 | 40/45 (C-33 A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +11.7 | 1e-29 | 46/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +10.7 | 7e-25 | 41/48 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.61×** | +9.5 | 1e-19 | 44/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +8.4 | 3e-15 | 38/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +6.5 | 4e-09 | 31/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +6.1 | 5e-08 | 29/48 (J82, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.26×** | +5.7 | 6e-07 | 28/49 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +5.6 | 8e-07 | 35/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +5.2 | 7e-06 | 37/49 (SW480, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 2e-04 | 25/48 (LOX-IMVI, A-427, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.011 | 16/48 (C32, MIA PaCa-2, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.3 | 0.024 | 13/48 (SW1417, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.028 | 22/49 (NCI-H1573, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.046 | 13/48 (HOP62, SW1417, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.054 | 18/49 (C32, SK-MEL-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 93.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.754×** | -5.5 | 2e-05 | 31/49 (SK-MEL-2, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.822×** | -4.0 | 0.017 | 24/48 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.757×** | -3.8 | 0.033 | 25/48 (HT-29, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.838× | -3.6 | 0.043 | 21/48 (A-427, CHP-212, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.835× | -3.4 | 0.073 | 21/47 (SHP-77, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.850× | -3.3 | 0.073 | 17/48 (C32, NCI-H661, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.782×** | -3.3 | 0.073 | 21/49 (A498, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.862× | -3.0 | 0.17 | 17/48 (CHP-212, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 93. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 111 | 12 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.57× (z +27.8) | — |
| [[SW480 (line)]] | alt | 106 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +16.1) | — |
| [[KATO III (line)]] | alt | 140 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +16.0) | — |
| [[LOX-IMVI (line)]] | wt | 72.9 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 190 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +17.1) | — |
| [[SW1417 (line)]] | alt | 164 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +13.7) | — |
| [[HT-29 (line)]] | alt | 107 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +13.6) | — |
| [[LoVo (line)]] | wt | 54.4 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +11.2) | — |
| [[C32 (line)]] | wt | 188 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +12.7) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 204 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 83.4 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 57.4 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.99× (z +15.3) | — |
| [[NCI-H23 (line)]] | alt | 102 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +13.2) | — |
| [[BT-474 (line)]] | alt | 92.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +14.1) | — |
| [[COLO 205 (line)]] | alt | 70.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 86.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.06× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 81.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +10.9) | — |
| [[A549 (line)]] | wt | 100 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.22× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 97.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.9) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 186 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +11.6) | — |
| [[J82 (line)]] | alt | 140 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 135 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 1.80× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 491 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +14.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 489 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 88.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +10.3) | — |
| [[A498 (line)]] | wt | 146 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 91.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 119 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +12.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 124 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.7) | — |
| [[A-172 (line)]] | wt | 67.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 55.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.69× (z +10.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 94.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.18× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 85.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0771× (z -15.6) |
| [[H4 (line)]] | wt | 136 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 72.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +9.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 113 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.03× (z +9.0) | — |
| [[RKO (line)]] | wt | 95.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.388× (z -9.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 54.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 78.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 168 | 0 | 1 | — | [[Apalutamide (drug)]] 0.05 µM 0.0814× (z -10.2) |
| [[SW48 (line)]] | wt | 79.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +11.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 131 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 93), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNS]] | +0.84 | +0.77 / +0.87 | both halves | 7e-06 | STRING 426 |
| [[SCARB2]] | +0.74 | +0.65 / +0.79 | both halves | 7e-06 | STRING 654 |
| [[LAMP1]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 | same gene group; STRING 999 |
| [[ATP6AP1]] | +0.72 | +0.72 / +0.63 | both halves | 7e-06 | STRING 465 |
| [[PPT1]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 416 |
| [[TMEM30A]] | +0.70 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[CREG1]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CRTAP]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[MMGT1]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[PCYOX1]] | +0.68 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[PSAP]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 476 |
| [[ITM2B]] | +0.67 | +0.75 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SURF6]] | -0.68 | -0.58 / -0.72 | both halves | 7e-06 |  |
| [[ZNF593]] | -0.66 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[CCDC137]] | -0.65 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[FBXO45]] | -0.63 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[BRIX1]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[PPP1R35]] ⚠ | -0.61 | -0.52 / -0.66 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FBXL6]] | -0.60 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[NIFK]] | -0.60 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[DHRS7B]] | -0.60 | -0.43 / -0.70 | both halves | 3e-05 |  |
| [[MRM2]] | -0.59 | -0.45 / -0.69 | both halves | 3e-05 |  |
| [[MTG2]] | -0.59 | -0.47 / -0.71 | both halves | 2e-05 |  |
| [[MRPL46]] | -0.58 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[FAM32A]] | -0.57 | -0.49 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-22.9, -20.3); signed map (-23.7, -37.1). **Vector** length 131, 45.6% of its response variance represented; |z| ≥ 3 in 1,215 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +14.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.3 | +17.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +12.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +5.7 | +9.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.6 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.8 | +3.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.7 | +2.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.6 | +1.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.5 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.2 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.1 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.9 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.4 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.4 | -3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.0 | -3.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.8 | -3.3 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -3.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | lysosome associated membrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:120,426,148-120,469,365 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD107b |
| Gene groups (HGNC) | CD molecules; Lysosome associated membrane proteins |
| Hallmark sets | PROTEIN_SECRETION, COAGULATION, COMPLEMENT, HEME_METABOLISM |
| Reactome | 8 pathways, smallest: Chaperone Mediated Autophagy; Platelet degranulation; Response to elevated platelet cytosolic Ca2+ |
| Matched by | ensembl_id |

**Function**, from UniProt [P13473](https://www.uniprot.org/uniprotkb/P13473) (Lysosome-associated membrane glycoprotein 2):

> Lysosomal membrane glycoprotein which plays an important role in lysosome biogenesis, lysosomal pH regulation and autophagy. Acts as an important regulator of lysosomal lumen pH regulation by acting as a direct inhibitor of the proton channel TMEM175, facilitating lysosomal acidification for optimal hydrolase activity. Plays an important role in chaperone-mediated autophagy, a process that mediates lysosomal degradation of proteins in response to various stresses and as part of the normal …

**Summary**, from NCBI Gene [3920](https://www.ncbi.nlm.nih.gov/gene/3920):

> The protein encoded by this gene is a member of a family of membrane glycoproteins. This glycoprotein provides selectins with carbohydrate ligands. It may play a role in tumor cell metastasis. It may also function in the protection, maintenance, and adhesion of the lysosome. Alternative splicing of this gene results in multiple transcript variants encoding distinct proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6501](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6501) · Entrez [3920](https://www.ncbi.nlm.nih.gov/gene/3920) · UniProt [P13473](https://www.uniprot.org/uniprotkb/P13473) · Ensembl [ENSG00000005893](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005893)

## Data

Gene col 93: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 93); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 93, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 93]; `tensor/DDL_lfc|DDL_z.npy` [93]; `embed/gene_vectors.npy` [93]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 93 or target_col == 93). Every well: [[LAMP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
