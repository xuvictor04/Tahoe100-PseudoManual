---
symbol: "TNPO3"
type: "gene"
col: 746
ensembl_id: "ENSG00000064419"
name: "transportin 3"
location: "7q32.1"
module: 142
arm: "+"
pooled_cpm: 189.51
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# TNPO3

*transportin 3* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.55× (z +12.9, q 2e-35, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.633× (z -12.4, q 1e-32, down in 37 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.826× (z -8.0, q 3e-13, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAP130]] (+0.73, fdr 7e-06), [[NFATC3]] (+0.73, fdr 1e-05), [[SNHG30]] (+0.71, fdr 7e-06); moves opposite to [[LIG4]] (-0.65, fdr 7e-06), [[VEZF1]] (-0.65, fdr 8e-06), [[HIVEP2]] (-0.61, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 746.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +12.9 | 2e-35 | 47/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +11.5 | 4e-28 | 45/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +10.1 | 8e-22 | 40/48 (HT-29, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +10.1 | 1e-21 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +9.7 | 4e-20 | 35/48 (BT-474, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +9.6 | 6e-20 | 43/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +9.3 | 1e-18 | 39/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +8.6 | 6e-16 | 39/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +7.3 | 3e-11 | 32/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +7.2 | 3e-11 | 32/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.41×** | +7.1 | 5e-11 | 40/49 (NCI-H460, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +6.4 | 5e-09 | 34/45 (J82, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.21×** | +5.7 | 6e-07 | 25/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.13× | +5.1 | 2e-05 | 17/49 (AsPC-1, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | 1.18× | +4.7 | 8e-05 | 22/47 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.068 | 13/48 (NCI-H460, RKO, …) | two highest doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.11× | +3.1 | 0.068 | 3/48 (NCI-H23, SW 900, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.068 | 14/47 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.083 | 4/49 (HOP62, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 746.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.633×** | -12.4 | 1e-32 | 37/45 (SW48, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -9.2 | 1e-17 | 0/50 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.826×** | -8.0 | 3e-13 | 27/48 (AsPC-1, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.832×** | -7.7 | 3e-12 | 25/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.768×** | -7.5 | 9e-12 | 27/44 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.771×** | -7.4 | 2e-11 | 33/47 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.775×** | -7.2 | 5e-11 | 28/48 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.824×** | -5.7 | 9e-07 | 25/48 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.840× | -4.9 | 5e-05 | 24/49 (A549, AsPC-1, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -4.4 | 6e-04 | 19/48 (A-172, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.867× | -4.2 | 0.001 | 18/49 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.873× | -4.0 | 0.003 | 15/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.890× | -3.4 | 0.026 | 7/48 (NCI-H1792, C32, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.886× | -3.4 | 0.026 | 5/47 (COLO 205, SNU-1, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.857× | -3.2 | 0.045 | 13/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | 0.926× | -3.2 | 0.047 | 1/48 (CHP-212) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.930× | -3.0 | 0.082 | 0/48 | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 746. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 240 | 8 (3 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +19.5) | [[Dinaciclib (drug)]] 0.05 µM 0.592× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.633× (z -9.2) |
| [[SW480 (line)]] | alt | 182 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +14.5) | — |
| [[HT-29 (line)]] | alt | 196 | 6 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.40× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.582× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 297 | 6 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.03× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.456× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 165 | 5 (3 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.05 µM 1.79× (z +10.7) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.75× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.423× (z -14.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 224 | 1 (1 ⚠) | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +11.9) ⚠ cell-cycle shift, explains ~13% of this change | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -16.8) |
| [[A-172 (line)]] | wt | 105 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.439× (z -13.0) |
| [[LoVo (line)]] | wt | 166 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.29× (z +14.3) | — |
| [[RKO (line)]] | wt | 250 | 4 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.98× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 136 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.89× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 288 | 1 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.58× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.583× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 185 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.511× (z -11.3) |
| [[A549 (line)]] | wt | 192 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 170 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.13× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.531× (z -10.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 166 | 1 | 2 | [[Ixazomib citrate (drug)]] 5 µM 1.87× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.634× (z -9.0) |
| [[SW48 (line)]] | wt | 228 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.17× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -16.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 250 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -13.4) |
| [[BT-474 (line)]] | alt | 155 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.52× (z +12.8) | — |
| [[C-33 A (line)]] | alt | 255 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.420× (z -12.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 382 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.416× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 274 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.531× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.593× (z -8.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 141 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.616× (z -10.6) |
| [[KATO III (line)]] | alt | 180 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.74× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 252 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.546× (z -8.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 194 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.517× (z -9.1) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.661× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 168 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.04× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 221 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.518× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 157 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.36× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 159 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 206 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 124 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 153 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 208 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 746), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAP130]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[NFATC3]] | +0.73 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[SNHG30]] | +0.71 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.66 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[ZCCHC17]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[RARS2]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[PPHLN1]] | +0.65 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[MBOAT7]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[MFN1]] | +0.65 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[RNF4]] | +0.65 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[TUSC2]] | +0.64 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[UQCRH]] | +0.63 | +0.68 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIG4]] | -0.65 | -0.75 / -0.61 | both halves | 7e-06 |  |
| [[VEZF1]] | -0.65 | -0.61 / -0.58 | both halves | 8e-06 |  |
| [[HIVEP2]] | -0.61 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.61 | -0.70 / -0.53 | both halves | 1e-05 |  |
| [[ZNF776]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[SYNPO]] | -0.60 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[NHLRC2]] | -0.59 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ZNF260]] | -0.59 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.59 | -0.66 / -0.57 | both halves | 8e-06 |  |
| [[BCL3]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ZC3H7B]] | -0.58 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[NEK9]] | -0.58 | -0.63 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.750). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.0, -7.5); signed map (-43.1, 2.8). **Vector** length 113, 34.9% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.1 | +9.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +12.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.7 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +4.9 | +5.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.8 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -12.2 | -8.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -11.4 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.9 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.6 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.2 | -12.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -7.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | transportin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:128,954,180-129,055,173 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRN-SR, MTR10A, TRN-SR2, IPO12; previously LGMD1F |
| Gene groups (HGNC) | Importins; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5L0](https://www.uniprot.org/uniprotkb/Q9Y5L0) (Transportin-3):

> Importin, which transports target proteins into the nucleus. Specifically mediates the nuclear import of splicing factor serine/arginine (SR) proteins, such as RBM4, SFRS1 and SFRS2, by recognizing phosphorylated SR domains. Also mediates the nuclear import of serine/arginine (SR) protein CPSF6, independently of CPSF6 phosphorylation. The nuclear import process is regulated by the small GTPase Ran that partitions between cytoplasm and nucleus in the predominantly GDP- and GTP-bound form, …

**Summary**, from NCBI Gene [23534](https://www.ncbi.nlm.nih.gov/gene/23534):

> The protein encoded by this gene is a nuclear import receptor for serine/arginine-rich (SR) proteins such as the splicing factors SFRS1 and SFRS2. The encoded protein has also been shown to be involved in HIV-1 infection, apparently through interaction with the HIV-1 capsid protein. Several protein-coding and non-coding transcript variants have been found for this gene. [provided by RefSeq, Apr 2020]

**Accessions** — [HGNC:17103](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17103) · Entrez [23534](https://www.ncbi.nlm.nih.gov/gene/23534) · UniProt [Q9Y5L0](https://www.uniprot.org/uniprotkb/Q9Y5L0) · Ensembl [ENSG00000064419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064419)

## Data

Gene col 746: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 746); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 746, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 746]; `tensor/DDL_lfc|DDL_z.npy` [746]; `embed/gene_vectors.npy` [746]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 746 or target_col == 746). Every well: [[TNPO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNPO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
