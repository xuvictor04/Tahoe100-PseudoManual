---
symbol: "ATG16L2"
type: "gene"
col: 9580
ensembl_id: "ENSG00000168010"
name: "autophagy related 16 like 2"
location: "11q13.4"
module: 154
arm: "+"
pooled_cpm: 24.29
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 36
n_dd_up_clean: 7
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# ATG16L2

*autophagy related 16 like 2* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.53× (z +7.1, q 6e-10, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.341× (z -17.9, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAC2]] (+0.65, fdr 2e-05), [[CIB1]] (+0.63, fdr 4e-05), [[MPP2]] (+0.62, fdr 3e-05); moves opposite to [[GAS2]] (-0.61, fdr 1e-04), [[IQCH-AS1]] (-0.60, fdr 1e-04), [[FBXO38-DT]] (-0.57, fdr 1e-04).
> It is in [[Module 154]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +7.1 | 6e-10 | 28/48 (HT-29, A-172, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +6.4 | 5e-08 | 24/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.45×** | +6.2 | 1e-07 | 27/47 (A-427, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.41×** | +5.7 | 1e-06 | 24/48 (HT-29, AsPC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.8 | 2e-04 | 22/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.32×** | +4.7 | 3e-04 | 24/48 (PANC-1, HT-29, …) | all doses, flat |  |
| [[Methotrexate (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.009 | 17/48 (HCT15, PANC-1, …) | two highest doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.27×** | +3.8 | 0.009 | 17/48 (LoVo, A549, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.016 | 15/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.035 | 5/48 (HOP62, J82, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.23×** | +3.4 | 0.035 | 14/47 (LS 180, NCI-H460, …) | all doses, flat |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.070 | 11/48 (RKO, LS 180, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9580.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.341×** | -17.9 | 0e+00 | 42/47 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.357×** | -17.1 | 0e+00 | 44/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.518×** | -15.5 | 0e+00 | 33/47 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.415×** | -14.1 | 6e-43 | 41/45 (C-33 A, J82, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.430×** | -14.0 | 1e-42 | 41/47 (HCT15, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.451×** | -13.3 | 3e-38 | 36/47 (A-172, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.474×** | -12.4 | 1e-33 | 37/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.475×** | -11.9 | 6e-31 | 33/47 (HOP62, SNU-423, …) | two highest doses | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.494×** | -11.8 | 4e-30 | 37/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.276×** | -11.2 | 2e-27 | 41/48 (KATO III, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.306×** | -10.3 | 3e-23 | 36/46 (HOP62, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -9.6 | 3e-20 | 30/47 (HOP62, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.578×** | -8.4 | 2e-15 | 23/38 (HS-578T, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.611×** | -8.2 | 9e-15 | 31/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.633×** | -7.3 | 9e-12 | 18/32 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.783×** | -5.8 | 3e-07 | 25/48 (PANC-1, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.519×** | -5.7 | 3e-07 | 28/47 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.713×** | -5.6 | 5e-07 | 25/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.579×** | -4.8 | 5e-05 | 19/48 (SNU-423, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.819×** | -4.7 | 6e-05 | 23/48 (HOP62, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 28.1 | 0 | 12 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -16.1) |
| [[SNU-423 (line)]] | alt | 41.9 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -21.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.152× (z -13.9) |
| [[A-172 (line)]] | wt | 32.5 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.216× (z -12.5) |
| [[A549 (line)]] | wt | 21.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -14.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -12.1) |
| [[SW 900 (line)]] | alt | 31.3 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -17.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -11.7) |
| [[SW480 (line)]] | alt | 15.5 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -14.1) |
| [[H4 (line)]] | wt | 28.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 44.8 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0843× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -9.4) |
| [[J82 (line)]] | alt | 47.3 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.174× (z -13.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -11.2) |
| [[PANC-1 (line)]] | alt | 27.9 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.331× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 31.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -18.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -14.5) |
| [[HS-578T (line)]] | alt | 23.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0523× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 36.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 14.6 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.223× (z -10.7) |
| [[RKO (line)]] | wt | 33.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0938× (z -16.0) |
| [[A498 (line)]] | wt | 15.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -10.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HCT15 (line)]] | alt | 38.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0271× (z -23.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 21.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 42.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -11.7) |
| [[C-33 A (line)]] | alt | 48.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.100× (z -15.5) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 24.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.242× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -11.1) |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0755× (z -12.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.196× (z -9.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 18.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0721× (z -9.5) |
| [[LoVo (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -9.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 17.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.287× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 31.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -9.2) |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -9.8) |
| [[SNU-1 (line)]] | wt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -9.5) |
| [[A-427 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAC2]] | +0.65 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[CIB1]] | +0.63 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[MPP2]] | +0.62 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[LTBP4]] | +0.62 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[ZNRF1]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[TCIRG1]] | +0.61 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[GIPR]] | +0.61 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[ARID3B]] | +0.61 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[PBX4]] | +0.60 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[ABTB3]] | +0.60 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[SH3GL1]] | +0.60 | +0.57 / +0.43 | both halves | 4e-05 |  |
| [[CABLES2]] | +0.59 | +0.47 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAS2]] | -0.61 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[IQCH-AS1]] | -0.60 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[FBXO38-DT]] | -0.57 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[MGST1]] | -0.57 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[FBXL17]] | -0.56 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[STEAP2-AS1]] | -0.56 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[FOXG1]] | -0.55 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[INO80D]] | -0.55 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[CFAP418-AS1]] | -0.55 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[SOCS6]] | -0.55 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[ZMYND11]] | -0.55 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[ZRANB2-DT]] | -0.55 | -0.36 / -0.48 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.8, 2.8); signed map (-5.9, 47.4). **Vector** length 89.9, 22.7% of its response variance represented; |z| ≥ 3 in 1,365 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.5 | +6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.1 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.8 | +4.7 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +3.4 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.4 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.3 | +2.2 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.3 | +2.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.2 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -17.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.0 | -7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.6 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -8.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.0 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -10.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.7 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 16 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:72,814,406-72,843,674 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00012, WDR80, ATG16B |
| Gene groups (HGNC) | WD repeat domain containing; Autophagy related |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NAA4](https://www.uniprot.org/uniprotkb/Q8NAA4) (Protein Atg16l2):

> May play a role in regulating epithelial homeostasis in an ATG16L1-dependent manner.

**Summary**, from NCBI Gene [89849](https://www.ncbi.nlm.nih.gov/gene/89849):

> Predicted to be involved in macroautophagy. Predicted to act upstream of or within negative stranded viral RNA replication. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25464](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25464) · Entrez [89849](https://www.ncbi.nlm.nih.gov/gene/89849) · UniProt [Q8NAA4](https://www.uniprot.org/uniprotkb/Q8NAA4) · Ensembl [ENSG00000168010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168010)

## Data

Gene col 9580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9580); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9580]; `tensor/DDL_lfc|DDL_z.npy` [9580]; `embed/gene_vectors.npy` [9580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9580 or target_col == 9580). Every well: [[ATG16L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG16L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
