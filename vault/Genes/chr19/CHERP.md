---
symbol: "CHERP"
type: "gene"
col: 1445
ensembl_id: "ENSG00000085872"
name: "calcium homeostasis endoplasmic reticulum protein"
location: "19p13.11"
module: 36
arm: "+"
pooled_cpm: 32.05
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 9
n_dd_up_clean: 19
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# CHERP

*calcium homeostasis endoplasmic reticulum protein* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.56× (z +20.1, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.633× (z -8.8, q 1e-15, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.738× (z -5.6, q 3e-06, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD1A]] (+0.78, fdr 7e-06), [[ZNF787]] (+0.70, fdr 7e-06), [[ZBTB9]] (+0.64, fdr 1e-05); moves opposite to [[FKBP3]] (-0.53, fdr 4e-05), [[SEPTIN7]] (-0.52, fdr 3e-05), [[PDCD6IP]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1445.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.56×** | +20.1 | 0e+00 | 48/49 (SW480, Panc 03.27, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **5.13×** | +16.3 | 0e+00 | 46/48 (SW480, Panc 03.27, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +15.4 | 0e+00 | 39/47 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +15.2 | 0e+00 | 46/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.15×** | +14.6 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.91×** | +12.3 | 1e-32 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.74×** | +10.5 | 5e-24 | 42/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +9.0 | 2e-17 | 37/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +8.3 | 6e-15 | 34/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +7.6 | 2e-12 | 29/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +7.3 | 1e-11 | 32/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +7.2 | 3e-11 | 29/48 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +7.1 | 6e-11 | 33/47 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +7.0 | 1e-10 | 35/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +5.9 | 1e-07 | 23/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.008 | 13/48 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.009 | 10/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.014 | 6/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1445.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.633×** | -8.8 | 1e-15 | 31/44 (NCI-H2030, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.724×** | -5.9 | 8e-07 | 20/38 (NCI-H460, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -5.6 | 3e-06 | 27/48 (SK-MEL-2, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.800×** | -5.6 | 3e-06 | 23/48 (SHP-77, SW480, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -4.5 | 9e-04 | 24/47 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.793×** | -4.3 | 0.002 | 19/47 (A-427, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.803×** | -4.2 | 0.002 | 18/48 (SW 1271, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.799×** | -4.2 | 0.002 | 17/47 (HS-578T, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.842× | -3.8 | 0.010 | 13/48 (MIA PaCa-2, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **0.832×** | -3.5 | 0.023 | 10/47 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.835× | -3.5 | 0.027 | 6/48 (A-427, H4, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.834× | -3.4 | 0.036 | 11/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.838× | -3.2 | 0.062 | 11/48 (NCI-H460, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.853× | -3.1 | 0.083 | 5/48 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.882× | -3.1 | 0.083 | 9/48 (A-427, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1445. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.0 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.0985× (z -20.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 29.5 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -8.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 37.0 | 7 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.87× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +13.7) | — |
| [[SHP-77 (line)]] | alt | 74.2 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.08× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +9.7) | — |
| [[A498 (line)]] | wt | 39.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -12.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 30.3 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.53× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 29.5 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.9× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.2 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.3× (z +10.6) | [[Torkinib (drug)]] 5 µM 0.0823× (z -10.3) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 25.8 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.57× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -8.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 51.5 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.4× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 30.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +10.5) | — |
| [[AsPC-1 (line)]] | alt | 28.4 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 25.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.6) | — |
| [[CHP-212 (line)]] | wt | 43.4 | 0 | 2 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0590× (z -12.9) |
| [[COLO 205 (line)]] | alt | 28.6 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 17.9× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 37.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[DTP3 (drug)]] 5 µM 0.0844× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 34.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.56× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 38.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.67× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -9.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 45.1 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 9.31× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 40.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +11.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -10.2) |
| [[A-427 (line)]] | wt | 33.8 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 7.35× (z +8.8) | — |
| [[A549 (line)]] | wt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.32× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 32.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +8.6) | — |
| [[H4 (line)]] | wt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 22.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.76× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 40.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 19.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.7× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -9.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[LOX-IMVI (line)]] | wt | 38.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 25.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +13.8) | — |
| [[RPMI-7951 (line)]] | alt | 37.1 | 0 | 1 | — | [[vincristine (drug)]] 5 µM 0.0796× (z -9.0) |
| [[SNU-1 (line)]] | wt | 29.1 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0978× (z -9.1) |
| [[SNU-423 (line)]] | alt | 30.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +12.5) | — |
| [[SW 900 (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -13.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 36.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.42× (z +8.8) | — |
| [[SW48 (line)]] | wt | 40.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1445), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD1A]] | +0.78 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ZNF787]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[ZBTB9]] | +0.64 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[BRPF1]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[YRDC]] | +0.63 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[UPF1]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ZNF384]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[RAVER1]] | +0.60 | +0.63 / +0.62 | both halves | 7e-06 | STRING 757 |
| [[TRMT44]] | +0.58 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[DDX51]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[TBRG4]] | +0.57 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[ZNF276]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP3]] | -0.53 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[SEPTIN7]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[PDCD6IP]] | -0.52 | -0.44 / -0.56 | both halves | 3e-05 | pathway: Dengue Virus-Host Interactions |
| [[CHMP2B]] | -0.51 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[TAX1BP1]] | -0.50 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[VBP1]] | -0.49 | -0.43 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.453). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-31.9, -9.3); signed map (-14.4, -25.6). **Vector** length 67.2, 13.8% of its response variance represented; |z| ≥ 3 in 1,057 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +20.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +16.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | +4.4 | +4.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +9.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.8 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +0.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +3.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -5.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | calcium homeostasis endoplasmic reticulum protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:16,517,894-16,542,437 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ERPROT213-21, DAN16 |
| Gene groups (HGNC) | G-patch domain containing; Spliceosomal A complex; CTD interacting domain containing |
| Reactome | 13 pathways, smallest: CHD1 and CHD2 subfamily; CHD chromatin remodelers; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWX8](https://www.uniprot.org/uniprotkb/Q8IWX8) (Calcium homeostasis endoplasmic reticulum protein):

> Involved in calcium homeostasis, growth and proliferation.

**Summary**, from NCBI Gene [10523](https://www.ncbi.nlm.nih.gov/gene/10523):

> Enables transmembrane transporter binding activity. Involved in positive regulation of calcineurin-NFAT signaling cascade and release of sequestered calcium ion into cytosol. Acts upstream of or within intracellular calcium ion homeostasis and negative regulation of cell population proliferation. Located in perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16930](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16930) · Entrez [10523](https://www.ncbi.nlm.nih.gov/gene/10523) · UniProt [Q8IWX8](https://www.uniprot.org/uniprotkb/Q8IWX8) · Ensembl [ENSG00000085872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085872)

## Data

Gene col 1445: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1445); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1445, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1445]; `tensor/DDL_lfc|DDL_z.npy` [1445]; `embed/gene_vectors.npy` [1445]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1445 or target_col == 1445). Every well: [[CHERP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHERP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
