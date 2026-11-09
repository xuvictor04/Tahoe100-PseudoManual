---
symbol: "PSMC6"
type: "gene"
col: 1977
ensembl_id: "ENSG00000100519"
name: "proteasome 26S subunit, ATPase 6"
location: "14q22.1"
module: 72
arm: "+"
pooled_cpm: 77.43
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PSMC6

*proteasome 26S subunit, ATPase 6* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.80× (z +21.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Filgotinib (drug)]] 5 µM: 0.785× (z -3.8, q 0.067, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNL1]] (+0.81, fdr 7e-06), [[PSMA3]] (+0.74, fdr 7e-06), [[PSMA6]] (+0.71, fdr 7e-06); moves opposite to [[MYL12A]] (-0.53, fdr 3e-05), [[ENTR1]] (-0.48, fdr 3e-05), [[SKI]] (-0.47, fdr 4e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1977.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.80×** | +21.3 | 0e+00 | 48/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.34×** | +19.3 | 0e+00 | 48/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.31×** | +18.1 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.04×** | +11.4 | 5e-28 | 42/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.77×** | +11.1 | 1e-26 | 47/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +10.5 | 6e-24 | 42/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.56×** | +10.0 | 8e-22 | 34/48 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.29×** | +9.5 | 2e-19 | 47/49 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.85×** | +8.8 | 1e-16 | 42/48 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +8.1 | 4e-14 | 32/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.43×** | +7.4 | 6e-12 | 42/45 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.48×** | +6.3 | 1e-08 | 29/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.48×** | +6.1 | 6e-08 | 33/48 (LoVo, NCI-H460, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.46×** | +5.9 | 2e-07 | 37/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +5.8 | 3e-07 | 34/48 (LoVo, C32, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.023 | 13/49 (RKO, HOP62, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.079 | 11/49 (MIA PaCa-2, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1977.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **0.785×** | -3.8 | 0.067 | 24/48 (CFPAC-1, C32, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -3.7 | 0.071 | 24/48 (C32, NCI-H2030, …) | top dose only | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.794×** | -3.5 | 0.076 | 23/49 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -3.4 | 0.080 | 0/50 | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.803×** | -3.4 | 0.086 | 20/48 (NCI-H1792, SW48, …) | top dose only | plate-row cell shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.789×** | -3.2 | 0.086 | 19/48 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.818×** | -3.2 | 0.086 | 19/48 (HEC-1-A, NCI-H1792, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.818×** | -3.2 | 0.086 | 20/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.868× | -3.2 | 0.086 | 13/48 (SW1417, SW 900, …) | top dose only | position effect removed |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.811×** | -3.2 | 0.086 | 14/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.822×** | -3.1 | 0.086 | 19/48 (NCI-H1573, J82, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.870× | -3.1 | 0.086 | 15/48 (SK-MEL-2, A498, …) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **0.826×** | -3.0 | 0.092 | 14/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Meloxicam (drug)]] 0.5 µM |  | **0.827×** | -3.0 | 0.092 | 19/48 (SW 1271, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.818×** | -3.0 | 0.092 | 19/48 (NCI-H2030, C32, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.874× | -3.0 | 0.092 | 9/48 (C-33 A, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1977. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 55.5 | 12 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.14× (z +20.0) | — |
| [[NCI-H460 (line)]] | wt | 65.5 | 10 (6 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.60× (z +15.9) | — |
| [[PANC-1 (line)]] | alt | 53.7 | 10 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.68× (z +18.2) | — |
| [[SW480 (line)]] | alt | 65.8 | 9 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.84× (z +17.5) | — |
| [[NCI-H23 (line)]] | alt | 76.4 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.51× (z +14.1) | — |
| [[Panc 03.27 (line)]] | alt | 93.2 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.94× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 140 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.97× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 83.5 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.90× (z +15.1) | — |
| [[NCI-H1573 (line)]] | alt | 107 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.51× (z +15.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.79× (z +14.6) | — |
| [[NCI-H1792 (line)]] | alt | 69.3 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.39× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 54.9 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.29× (z +13.9) | — |
| [[KATO III (line)]] | alt | 56.4 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.42× (z +14.5) | — |
| [[A498 (line)]] | wt | 52.3 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.52× (z +11.0) | — |
| [[A549 (line)]] | wt | 68.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.67× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 52.9 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.39× (z +14.8) | — |
| [[SK-MEL-2 (line)]] | alt | 56.1 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.00× (z +12.5) | — |
| [[A-172 (line)]] | wt | 44.6 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.23× (z +10.5) | — |
| [[A-427 (line)]] | wt | 93.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.43× (z +14.3) | — |
| [[C32 (line)]] | wt | 73.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.14× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 181 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.27× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 47.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.86× (z +13.6) | — |
| [[H4 (line)]] | wt | 71.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.74× (z +12.3) | — |
| [[HCT15 (line)]] | alt | 71.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.38× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 56.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.34× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 61.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.56× (z +13.8) | — |
| [[HS-578T (line)]] | alt | 53.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.79× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 57.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.64× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 78.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.41× (z +11.3) | — |
| [[RKO (line)]] | wt | 67.6 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.41× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 82.2 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.30× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 59.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.77× (z +13.0) | — |
| [[C-33 A (line)]] | alt | 78.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.29× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 176 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.08× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 67.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.66× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 63.4 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.15× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 47.5 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.122× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 85.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 68.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.54× (z +9.5) | — |
| [[J82 (line)]] | alt | 52.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.79× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 150 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.38× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 96.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.60× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 93.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.02× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 90.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1977), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNL1]] | +0.81 | +0.86 / +0.73 | both halves | 7e-06 | STRING 528 |
| [[PSMA3]] | +0.74 | +0.76 / +0.66 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |
| [[PSMA6]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[PSMA2]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[PSMA1]] | +0.65 | +0.70 / +0.57 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RTCA]] | +0.64 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[PSMB2]] | +0.63 | +0.61 / +0.67 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[PSMC2]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |
| [[CDC40]] | +0.62 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.62 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[FXR1]] | +0.61 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[TENT2]] | +0.61 | +0.61 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYL12A]] | -0.53 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[ENTR1]] | -0.48 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[SKI]] | -0.47 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[KDSR]] | -0.47 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[DDX19A]] | -0.47 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[PKP4]] | -0.47 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[ZBTB9]] | -0.47 | -0.43 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.5, -10.0); signed map (-26.6, -23.8). **Vector** length 83.6, 26.2% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.62 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.8 | +19.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.7 | +21.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.3 | +18.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.6 | +7.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.2 | +9.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +5.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -6.5 | +6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.0 | +11.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -5.8 | +5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | +10.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | +1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -0.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | +1.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.6 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, ATPase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:52,707,178-52,728,590 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p42, RPT5 |
| Gene groups (HGNC) | AAA ATPases; Proteasome |
| Hallmark sets | MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 173 pathways, smallest: SARS-CoV-1 targets host intracellular signalling and regulatory pathways; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P62333](https://www.uniprot.org/uniprotkb/P62333) (26S proteasome regulatory subunit 10B):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair. PSMC6 belongs to …

**Summary**, from NCBI Gene [5706](https://www.ncbi.nlm.nih.gov/gene/5706):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9553](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9553) · Entrez [5706](https://www.ncbi.nlm.nih.gov/gene/5706) · UniProt [P62333](https://www.uniprot.org/uniprotkb/P62333) · Ensembl [ENSG00000100519](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100519)

## Data

Gene col 1977: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1977); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1977, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1977]; `tensor/DDL_lfc|DDL_z.npy` [1977]; `embed/gene_vectors.npy` [1977]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1977 or target_col == 1977). Every well: [[PSMC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
