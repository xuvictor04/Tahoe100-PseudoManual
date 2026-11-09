---
symbol: "DNAJC2"
type: "gene"
col: 2670
ensembl_id: "ENSG00000105821"
name: "DnaJ heat shock protein family (Hsp40) member C2"
location: "7q22.1"
module: 12
arm: "+"
pooled_cpm: 128.65
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 5
n_dd_up_clean: 23
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# DNAJC2

*DnaJ heat shock protein family (Hsp40) member C2* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.24× (z +15.3, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.96× (z +14.6, q 1e-45, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.764× (z -5.2, q 1e-04, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM25]] (+0.70, fdr 7e-06), [[NSRP1]] (+0.67, fdr 7e-06), [[UBXN4]] (+0.66, fdr 1e-05); moves opposite to [[BSG]] (-0.72, fdr 7e-06), [[MED14]] (-0.67, fdr 1e-05), [[ITM2C]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2670.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.24×** | +15.3 | 0e+00 | 47/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.96×** | +14.6 | 1e-45 | 48/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.86×** | +14.1 | 5e-43 | 48/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.40×** | +11.8 | 8e-30 | 48/48 (PANC-1, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.23×** | +10.2 | 3e-22 | 48/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.97×** | +8.7 | 2e-16 | 48/48 (NCI-H1573, LS 180, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +7.8 | 5e-13 | 42/48 (C32, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.70×** | +7.1 | 1e-10 | 44/48 (SW480, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.65×** | +6.7 | 1e-09 | 43/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.93×** | +6.3 | 2e-08 | 44/49 (PANC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +6.2 | 3e-08 | 43/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +6.1 | 6e-08 | 43/48 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.55×** | +5.6 | 9e-07 | 42/47 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.10×** | +5.2 | 9e-06 | 39/45 (J82, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.7 | 8e-05 | 36/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +4.5 | 2e-04 | 33/49 (RPMI-7951, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.56×** | +4.2 | 7e-04 | 40/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.77×** | +4.0 | 0.002 | 39/48 (MIA PaCa-2, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.004 | 27/49 (COLO 205, AN3 CA, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.71×** | +3.8 | 0.004 | 38/48 (SW1417, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +3.5 | 0.011 | 27/48 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.011 | 33/48 (HEC-1-A, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2670.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.764×** | -5.2 | 1e-04 | 37/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.733×** | -4.2 | 0.005 | 35/48 (A498, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.733×** | -4.2 | 0.005 | 30/49 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.749×** | -3.9 | 0.011 | 34/48 (A498, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.750×** | -3.9 | 0.011 | 36/48 (KATO III, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 109 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 97.4 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +20.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.80× (z +18.2) | — |
| [[LS 180 (line)]] | wt | 106 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.42× (z +12.5) | — |
| [[SW480 (line)]] | alt | 164 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.67× (z +10.2) | — |
| [[C32 (line)]] | wt | 175 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.21× (z +14.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 193 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.37× (z +11.7) | — |
| [[NCI-H23 (line)]] | alt | 136 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +13.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.17× (z +13.6) | — |
| [[PANC-1 (line)]] | alt | 135 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +18.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.90× (z +14.6) | — |
| [[A-172 (line)]] | wt | 97.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +14.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.06× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 101 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +15.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.87× (z +12.9) | — |
| [[H4 (line)]] | wt | 108 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +15.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.24× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 124 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.21× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 107 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.30× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 135 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.68× (z +13.2) | — |
| [[SNU-423 (line)]] | alt | 86.8 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.85× (z +13.4) | — |
| [[A-427 (line)]] | wt | 115 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.79× (z +12.2) | — |
| [[HEC-1-A (line)]] | alt | 87.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[HOP62 (line)]] | alt | 71.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +15.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.91× (z +15.1) | — |
| [[SW 900 (line)]] | alt | 103 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +14.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.43× (z +10.9) | — |
| [[A498 (line)]] | wt | 258 | 1 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.01× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -10.7) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.453× (z -9.9) |
| [[COLO 205 (line)]] | alt | 72.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +12.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.82× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 120 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +13.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.99× (z +11.9) | — |
| [[J82 (line)]] | alt | 120 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +9.1) | — |
| [[KATO III (line)]] | alt | 137 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.43× (z +12.2) | — |
| [[LOX-IMVI (line)]] | wt | 90.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.40× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 61.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.85× (z +12.2) | — |
| [[NCI-H2030 (line)]] | alt | 114 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.92× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 169 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.50× (z +11.4) | — |
| [[RPMI-7951 (line)]] | alt | 121 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.49× (z +10.8) | — |
| [[A549 (line)]] | wt | 112 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 160 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.23× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 96.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.48× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 76.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.41× (z +9.1) | — |
| [[RKO (line)]] | wt | 211 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 161 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 201 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.32× (z +10.3) | — |
| [[SW48 (line)]] | wt | 203 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.27× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 213 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.91× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HepG2_C3A (line)]] | wt | 90.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 132 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 78.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 114 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[C-33 A (line)]] | alt | 103 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM25]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[NSRP1]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[UBXN4]] | +0.66 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[MPHOSPH10]] | +0.66 | +0.81 / +0.66 | both halves | 7e-06 | STRING 401 |
| [[DDX27]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ZRANB2]] | +0.65 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[DNAJC7]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 | same gene group; pathway: Cellular response to heat stress; STRING 446 |
| [[GOSR1]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[TATDN1]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[TYW3]] | +0.63 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[NOL8]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.63 | +0.68 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BSG]] | -0.72 | -0.68 / -0.69 | both halves | 7e-06 |  |
| [[MED14]] | -0.67 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[ITM2C]] | -0.67 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[PKM]] | -0.66 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[CALM3]] | -0.66 | -0.72 / -0.52 | both halves | 1e-05 |  |
| [[TWSG1]] | -0.64 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[NAGA]] | -0.64 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[AGPAT1]] | -0.63 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[CFL1]] | -0.63 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[LSM4]] | -0.62 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[TAGLN2]] | -0.62 | -0.60 / -0.58 | both halves | 8e-06 |  |
| [[PRKACA]] | -0.62 | -0.61 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DNAJC2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[APLP1]] | B | APLP1 activity raises DNAJC2's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.25× lower at baseline in the lines without APLP1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-39.9, -1.2); signed map (-2.2, -17.2). **Vector** length 97.0, 39.6% of its response variance represented; |z| ≥ 3 in 1,311 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.1 | +10.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.8 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +14.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.3 | +15.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +7.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.3 | +6.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +4.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.7 | +3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.1 | +6.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -4.3 | +7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.8 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | +3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:103,312,289-103,344,830 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MPP11, MPHOSPH11, ZUO1, zuotin; previously ZRF1 |
| Gene groups (HGNC) | Myb/SANT domain containing; DNAJ (HSP40) heat shock proteins |
| Reactome | 4 pathways, smallest: Regulation of HSF1-mediated heat shock response; Cellular response to heat stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99543](https://www.uniprot.org/uniprotkb/Q99543) (DnaJ homolog subfamily C member 2):

> Acts both as a chaperone in the cytosol and as a chromatin regulator in the nucleus. When cytosolic, acts as a molecular chaperone: component of the ribosome-associated complex (RAC), a complex involved in folding or maintaining nascent polypeptides in a folding-competent state. In the RAC complex, stimulates the ATPase activity of the ribosome-associated pool of Hsp70-type chaperones HSPA14 that bind to the nascent polypeptide chain. When nuclear, mediates the switching from polycomb-repressed …

**Summary**, from NCBI Gene [27000](https://www.ncbi.nlm.nih.gov/gene/27000):

> This gene is a member of the M-phase phosphoprotein (MPP) family. The gene encodes a phosphoprotein with a J domain and a Myb DNA-binding domain which localizes to both the nucleus and the cytosol. The protein is capable of forming a heterodimeric complex that associates with ribosomes, acting as a molecular chaperone for nascent polypeptide chains as they exit the ribosome. This protein was identified as a leukemia-associated antigen and expression of the gene is upregulated in leukemic …

**Accessions** — [HGNC:13192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13192) · Entrez [27000](https://www.ncbi.nlm.nih.gov/gene/27000) · UniProt [Q99543](https://www.uniprot.org/uniprotkb/Q99543) · Ensembl [ENSG00000105821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105821)

## Data

Gene col 2670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2670); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2670]; `tensor/DDL_lfc|DDL_z.npy` [2670]; `embed/gene_vectors.npy` [2670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2670 or target_col == 2670). Every well: [[DNAJC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
