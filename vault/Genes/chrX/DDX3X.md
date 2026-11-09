---
symbol: "DDX3X"
type: "gene"
col: 13258
ensembl_id: "ENSG00000215301"
name: "DEAD-box helicase 3 X-linked"
location: "Xp11.4"
module: 3
arm: "-"
pooled_cpm: 149.11
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 8
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# DDX3X

*DEAD-box helicase 3 X-linked* — Xp11.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.07× (z +16.6, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.681× (z -6.2, q 2e-07, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPK]] (+0.72, fdr 7e-06), [[EIF4G2]] (+0.71, fdr 7e-06), [[YWHAE]] (+0.71, fdr 7e-06); moves opposite to [[LCMT1]] (-0.68, fdr 1e-05), [[ATP5MJ]] (-0.66, fdr 4e-05), [[ANKS3]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13258.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +16.6 | 0e+00 | 43/48 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.63×** | +15.6 | 0e+00 | 48/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.16×** | +12.4 | 4e-33 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +11.4 | 5e-28 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +9.2 | 5e-18 | 37/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +9.0 | 2e-17 | 35/49 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.80×** | +8.7 | 2e-16 | 47/49 (COLO 205, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +8.7 | 2e-16 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.38×** | +7.3 | 1e-11 | 44/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +6.5 | 5e-09 | 36/47 (COLO 205, SHP-77, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +6.4 | 1e-08 | 35/48 (A-172, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +6.0 | 1e-07 | 35/45 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.4 | 4e-06 | 32/48 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.3 | 5e-06 | 0/50 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.38×** | +5.0 | 2e-05 | 27/48 (NCI-H460, NCI-H1573, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +4.7 | 9e-05 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +4.4 | 3e-04 | 24/48 (HEC-1-A, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.020 | 24/48 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.038 | 26/48 (SW48, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.042 | 23/48 (HT-29, J82, …) | rises with dose |  |
| [[Pimozide (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.065 | 21/48 (Panc 03.27, LoVo, …) | top dose only | position effect removed |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.087 | 21/48 (SW1417, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13258.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.681×** | -6.2 | 2e-07 | 39/48 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.685×** | -6.2 | 2e-07 | 41/48 (RKO, LS 180, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.749×** | -4.7 | 5e-04 | 31/48 (NCI-H23, RKO, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.768×** | -4.3 | 0.002 | 36/48 (NCI-H2030, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.768×** | -4.3 | 0.002 | 32/48 (COLO 205, LS 180, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.788×** | -3.9 | 0.011 | 26/48 (NCI-H2030, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.791×** | -3.8 | 0.011 | 38/49 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.802×** | -3.6 | 0.024 | 26/48 (KATO III, NCI-H23, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13258. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 108 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +16.1) | — |
| [[NCI-H460 (line)]] | wt | 171 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +18.9) | — |
| [[SW480 (line)]] | alt | 222 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +14.4) | — |
| [[LoVo (line)]] | wt | 148 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +15.5) | — |
| [[KATO III (line)]] | alt | 176 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +15.9) | — |
| [[NCI-H1573 (line)]] | alt | 149 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +24.5) | — |
| [[A-172 (line)]] | wt | 76.6 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 90.3 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +24.1) | — |
| [[J82 (line)]] | alt | 140 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +11.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 140 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.4) | — |
| [[NCI-H23 (line)]] | alt | 150 | 5 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.8) | [[Belinostat (drug)]] 5 µM 0.399× (z -10.4) |
| [[PANC-1 (line)]] | alt | 103 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +14.6) | — |
| [[COLO 205 (line)]] | alt | 132 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +14.9) | — |
| [[SW48 (line)]] | wt | 163 | 5 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.01× (z +12.6) | — |
| [[A498 (line)]] | wt | 116 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +23.2) | — |
| [[BT-474 (line)]] | alt | 152 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 89.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +15.1) | — |
| [[HT-29 (line)]] | alt | 139 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 97.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +23.8) | — |
| [[NCI-H2030 (line)]] | alt | 124 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 127 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +18.5) | — |
| [[LS 180 (line)]] | wt | 140 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +15.0) | — |
| [[C32 (line)]] | wt | 102 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +14.9) | — |
| [[CFPAC-1 (line)]] | alt | 142 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +15.9) | — |
| [[H4 (line)]] | wt | 109 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 202 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.2) | — |
| [[HepG2_C3A (line)]] | wt | 115 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 147 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 98.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +16.4) | — |
| [[NCI-H2347 (line)]] | alt | 220 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 172 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +16.3) | — |
| [[RKO (line)]] | wt | 228 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 153 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 187 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 112 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +9.7) | — |
| [[A549 (line)]] | wt | 160 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 179 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 98.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +20.1) | — |
| [[SNU-1 (line)]] | wt | 116 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +9.2) | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 1 | — | [[Erlotinib (drug)]] 0.05 µM 0.0885× (z -8.5) |
| [[SW1417 (line)]] | alt | 213 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.3) | — |
| [[A-427 (line)]] | wt | 242 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 162 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 296 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13258), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | +0.72 | +0.62 / +0.62 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 757 |
| [[EIF4G2]] | +0.71 | +0.63 / +0.64 | both halves | 7e-06 | STRING 773 |
| [[YWHAE]] | +0.71 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[U2AF2]] | +0.71 | +0.53 / +0.66 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 544 |
| [[SRSF1]] | +0.70 | +0.51 / +0.66 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 570 |
| [[MAPRE1]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[SFPQ]] | +0.68 | +0.56 / +0.70 | both halves | 1e-05 | STRING 662 |
| [[EWSR1]] | +0.68 | +0.54 / +0.67 | both halves | 1e-05 | STRING 550 |
| [[HNRNPL]] | +0.67 | +0.54 / +0.60 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 403 |
| [[TUG1]] | +0.67 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[HNRNPM]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 656 |
| [[MOB1A]] | +0.65 | +0.46 / +0.67 | both halves | 2e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 9 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | -0.68 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ATP5MJ]] | -0.66 | -0.41 / -0.67 | both halves | 4e-05 |  |
| [[ANKS3]] | -0.65 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[RPP21]] | -0.65 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[LIN7B]] | -0.65 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[POLR2I]] | -0.65 | -0.46 / -0.59 | both halves | 3e-05 | pathway: Dengue Virus-Host Interactions |
| [[MPG]] | -0.65 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[MRPL41]] ⚠ | -0.65 | -0.30 / -0.67 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[COMMD6]] | -0.64 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[MALSU1]] | -0.64 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[ATP5MK]] | -0.61 | -0.39 / -0.64 | both halves | 5e-05 | STRING 444 |
| [[RNF181]] | -0.61 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[SEC22A]] | -0.61 | -0.49 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises DDX3X's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.755). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.3, -24.0); signed map (15.4, -38.1). **Vector** length 117, 40.8% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA 3'-end processing* (reactome, mean cos +0.58 to 12); *mRNA Polyadenylation* (reactome, mean cos +0.60 to 11); *mRNA Splicing - Major Pathway* (reactome, mean cos +0.59 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +9.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.3 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.1 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.7 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +6.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.5 | -6.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.4 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.0 | -6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.0 | -0.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -4.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.5 | -1.3 |
|  | [[EX229 (drug)]] 0.5 µM |  | -3.4 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 3 X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.4 — chrX:41,333,348-41,364,472 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DBX, HLP2, DDX14, CAP-Rf; previously DDX3 |
| Gene groups (HGNC) | DEAD-box helicases |
| Reactome | 6 pathways, smallest: Dengue virus activates/modulates innate and adaptive immune responses; Dengue Virus-Host Interactions; Dengue Virus Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [O00571](https://www.uniprot.org/uniprotkb/O00571) (ATP-dependent RNA helicase DDX3X):

> Multifunctional ATP-dependent RNA helicase. The ATPase activity can be stimulated by various ribo-and deoxynucleic acids indicative for a relaxed substrate specificity. In vitro can unwind partially double-stranded DNA with a preference for 5'-single-stranded DNA overhangs. Binds RNA G-quadruplex (rG4s) structures, including those located in the 5'-UTR of NRAS mRNA. Involved in many cellular processes, which do not necessarily require its ATPase/helicase catalytic activities (Probable). …

**Summary**, from NCBI Gene [1654](https://www.ncbi.nlm.nih.gov/gene/1654):

> The protein encoded by this gene is a member of the large DEAD-box protein family, that is defined by the presence of the conserved Asp-Glu-Ala-Asp (DEAD) motif, and has ATP-dependent RNA helicase activity. This protein has been reported to display a high level of RNA-independent ATPase activity, and unlike most DEAD-box helicases, the ATPase activity is thought to be stimulated by both RNA and DNA. This protein has multiple conserved domains and is thought to play roles in both the nucleus and …

**Accessions** — [HGNC:2745](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2745) · Entrez [1654](https://www.ncbi.nlm.nih.gov/gene/1654) · UniProt [O00571](https://www.uniprot.org/uniprotkb/O00571) · Ensembl [ENSG00000215301](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215301)

## Data

Gene col 13258: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13258); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13258, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13258]; `tensor/DDL_lfc|DDL_z.npy` [13258]; `embed/gene_vectors.npy` [13258]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13258 or target_col == 13258). Every well: [[DDX3X — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX3X.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
