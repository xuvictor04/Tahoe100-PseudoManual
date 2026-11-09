---
symbol: "TARDBP"
type: "gene"
col: 4241
ensembl_id: "ENSG00000120948"
name: "TAR DNA binding protein"
location: "1p36.22"
module: 25
arm: "+"
pooled_cpm: 66.49
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# TARDBP

*TAR DNA binding protein* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.25× (z +14.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.758× (z -5.2, q 1e-04, down in 36 of 48 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Tirabrutinib (hydrochloride) (drug)]] 5 µM: 0.802× (z -4.1, q 0.010, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOB1A]] (+0.76, fdr 7e-06), [[SMU1]] (+0.75, fdr 7e-06), [[RCN1]] (+0.74, fdr 7e-06); moves opposite to [[SNHG8]] (-0.71, fdr 1e-05), [[SNHG32]] (-0.71, fdr 1e-05), [[SMIM26]] (-0.69, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[SNHG7]] (-0.69, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4241.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.25×** | +14.9 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.87×** | +11.5 | 6e-28 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +11.1 | 3e-26 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.72×** | +10.0 | 3e-21 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +8.5 | 2e-15 | 0/49 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.34×** | +8.2 | 3e-14 | 41/48 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +8.1 | 5e-14 | 43/49 (NCI-H1573, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +7.7 | 1e-12 | 36/47 (NCI-H460, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.55×** | +7.4 | 7e-12 | 36/45 (SW480, A498, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.48×** | +7.1 | 5e-11 | 35/48 (SW480, Hs 766T, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.31×** | +6.9 | 2e-10 | 30/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.45×** | +6.8 | 6e-10 | 37/49 (RKO, H4, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.46×** | +6.6 | 2e-09 | 33/44 (A498, PANC-1, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +6.6 | 2e-09 | 40/48 (HCT15, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.41×** | +6.2 | 2e-08 | 35/48 (SW480, Hs 766T, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +6.2 | 2e-08 | 29/48 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +5.7 | 3e-07 | 35/48 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +5.5 | 1e-06 | 33/48 (HCT15, PANC-1, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 3e-04 | 30/48 (LOX-IMVI, SW48, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.3 | 4e-04 | 18/48 (A-172, NCI-H460, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +4.3 | 5e-04 | 28/47 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.012 | 21/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.19× | +2.9 | 0.070 | 13/48 (HCT15, NCI-H2347, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4241.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.758×** | -5.2 | 1e-04 | 36/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -4.1 | 0.010 | 28/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.807×** | -4.0 | 0.011 | 25/48 (SHP-77, NCI-H460, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.756×** | -3.7 | 0.027 | 23/48 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -3.4 | 0.089 | 19/48 (AN3 CA, RKO, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.845× | -3.2 | 0.12 | 16/48 (RPMI-7951, hTERT-HPNE, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.848× | -3.1 | 0.12 | 15/49 (LoVo, NCI-H23, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.849× | -3.1 | 0.12 | 13/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.849× | -3.1 | 0.12 | 16/48 (A498, BT-474, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.5 µM |  | 0.850× | -3.1 | 0.12 | 16/48 (SNU-1, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4241. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 52.6 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 69.6 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +16.3) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +11.2) | — |
| [[SW480 (line)]] | alt | 89.2 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +14.7) | — |
| [[PANC-1 (line)]] | alt | 67.2 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +13.3) | — |
| [[H4 (line)]] | wt | 62.7 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 70.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.5) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 65.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.1) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +9.4) | — |
| [[LoVo (line)]] | wt | 84.3 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 37.6 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.36× (z +10.3) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +9.6) | — |
| [[A498 (line)]] | wt | 48.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.2) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[KATO III (line)]] | alt | 64.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.51× (z +12.7) | — |
| [[LS 180 (line)]] | wt | 71.0 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +12.6) | — |
| [[RKO (line)]] | wt | 69.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 54.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.3) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +8.5) | — |
| [[A-427 (line)]] | wt | 76.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -13.9) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A549 (line)]] | wt | 47.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.4) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[AsPC-1 (line)]] | alt | 55.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[C32 (line)]] | wt | 52.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.2) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[CHP-212 (line)]] | wt | 42.6 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0689× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 49.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 48.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0982× (z -12.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 67.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SW1417 (line)]] | alt | 62.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +9.9) | — |
| [[A-172 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 73.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4241), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | +0.76 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[SMU1]] | +0.75 | +0.63 / +0.73 | both halves | 7e-06 | STRING 439 |
| [[RCN1]] | +0.74 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[PSME3]] | +0.73 | +0.63 / +0.71 | both halves | 7e-06 | STRING 506 |
| [[HCFC1]] | +0.72 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[MAPRE1]] | +0.71 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.69 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[DHFR]] | +0.68 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[NRAS]] | +0.67 | +0.41 / +0.77 | both halves | 4e-05 |  |
| [[EMC1]] | +0.67 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[U2AF2]] | +0.67 | +0.44 / +0.76 | both halves | 3e-05 | same gene group; STRING 908 |
| [[SF3B4]] | +0.66 | +0.46 / +0.74 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*54 of its nearest partners move opposite, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG8]] | -0.71 | -0.51 / -0.79 | both halves | 1e-05 |  |
| [[SNHG32]] | -0.71 | -0.54 / -0.76 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.69 | -0.56 / -0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG7]] | -0.69 | -0.46 / -0.73 | both halves | 3e-05 |  |
| [[PITPNA-AS1]] | -0.67 | -0.42 / -0.70 | both halves | 4e-05 |  |
| [[LIN7B]] | -0.67 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[RPP21]] | -0.67 | -0.43 / -0.67 | both halves | 3e-05 |  |
| [[EPB41L4A-AS1]] | -0.67 | -0.50 / -0.69 | both halves | 1e-05 |  |
| [[NSUN5P1-1]] | -0.66 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[MARCHF9]] | -0.66 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[GAS5]] | -0.66 | -0.45 / -0.72 | both halves | 3e-05 |  |
| [[SNHG6]] | -0.66 | -0.47 / -0.69 | both halves | 2e-05 |  |
| [[RPAIN]] | -0.65 | -0.38 / -0.73 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.9, -21.9); signed map (-14.7, -36.3). **Vector** length 95.0, 24.9% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +6.8 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +6.7 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +6.3 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +6.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.6 | +11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | +2.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.5 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.1 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | TAR DNA binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,012,344-11,030,528 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TDP-43, ALS10 |
| Gene groups (HGNC) | RNA binding motif containing |
| Hallmark sets | MYC_TARGETS_V1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13148](https://www.uniprot.org/uniprotkb/Q13148) (TAR DNA-binding protein 43):

> RNA-binding protein that is involved in various steps of RNA biogenesis and processing. Preferentially binds, via its two RNA recognition motifs RRM1 and RRM2, to GU-repeats on RNA molecules predominantly localized within long introns and in the 3'UTR of mRNAs. In turn, regulates the splicing of many non-coding and protein-coding RNAs including proteins involved in neuronal survival, as well as mRNAs that encode proteins relevant for neurodegenerative diseases. Plays a role in maintaining …

**Summary**, from NCBI Gene [23435](https://www.ncbi.nlm.nih.gov/gene/23435):

> HIV-1, the causative agent of acquired immunodeficiency syndrome (AIDS), contains an RNA genome that produces a chromosomally integrated DNA during the replicative cycle. Activation of HIV-1 gene expression by the transactivator Tat is dependent on an RNA regulatory element (TAR) located downstream of the transcription initiation site. The protein encoded by this gene is a transcriptional repressor that binds to chromosomally integrated TAR DNA and represses HIV-1 transcription. In addition, …

**Accessions** — [HGNC:11571](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11571) · Entrez [23435](https://www.ncbi.nlm.nih.gov/gene/23435) · UniProt [Q13148](https://www.uniprot.org/uniprotkb/Q13148) · Ensembl [ENSG00000120948](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120948)

## Data

Gene col 4241: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4241); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4241, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4241]; `tensor/DDL_lfc|DDL_z.npy` [4241]; `embed/gene_vectors.npy` [4241]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4241 or target_col == 4241). Every well: [[TARDBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TARDBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
