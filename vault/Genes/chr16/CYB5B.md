---
symbol: "CYB5B"
type: "gene"
col: 2302
ensembl_id: "ENSG00000103018"
name: "cytochrome b5 type B"
location: "16q22.1"
module: 29
arm: "+"
pooled_cpm: 81.98
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CYB5B

*cytochrome b5 type B* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.71× (z +12.5, q 4e-33, up in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.63× (z +6.0, q 3e-07, up in 24 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 9 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 4 lines (NCI-H1573 2.79×, HT-29 2.76×, SK-MEL-2 2.90×, A498 1.94×; ⚠ cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (J82 2.39×, A-427 2.49×, NCI-H1573 2.44×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H1573 2.72×, HT-29 2.79×; ⚠ cell-cycle shift, explains ~39% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.788× (z -7.8, q 3e-12, down in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~21% of this change. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 0.806× (z -5.1, q 1e-04, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BANF1]] (+0.55, fdr 2e-05), [[HDAC1]] (+0.52, fdr 3e-05), [[ARF3]] (+0.52, fdr 1e-05); moves opposite to [[ATF4]] (-0.60, fdr 1e-05), [[WASHC1]] (-0.54, fdr 4e-05), [[SNHG32]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 19 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2302.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 9 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 4 lines (NCI-H1573 2.79×, HT-29 2.76×, SK-MEL-2 2.90×, A498 1.94×; ⚠ cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (J82 2.39×, A-427 2.49×, NCI-H1573 2.44×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H1573 2.72×, HT-29 2.79×; ⚠ cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.71×** | +12.5 | 4e-33 | 38/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.64×** | +11.6 | 1e-28 | 37/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.43×** | +8.4 | 8e-15 | 35/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.40×** | +7.8 | 8e-13 | 30/49 (J82, A-427, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +6.0 | 3e-07 | 24/49 (A498, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **1.30×** | +5.8 | 6e-07 | 25/42 (J82, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.28×** | +5.6 | 2e-06 | 28/48 (SK-MEL-2, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +5.4 | 6e-06 | 26/48 (HT-29, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.54×** | +5.3 | 8e-06 | 27/48 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.18× | +5.2 | 1e-05 | 20/48 (MIA PaCa-2, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.17× | +5.2 | 1e-05 | 19/48 (NCI-H2030, A549, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | 1.17× | +5.1 | 2e-05 | 18/49 (NCI-H2030, C-33 A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.21×** | +4.4 | 5e-04 | 20/48 (NCI-H23, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.21×** | +4.4 | 5e-04 | 19/48 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 1.19× | +3.9 | 0.003 | 19/50 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.8 | 0.005 | 11/48 (LoVo, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +2.9 | 0.082 | 14/47 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2302.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.788×** | -7.8 | 3e-12 | 27/48 (SNU-1, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.806×** | -5.1 | 1e-04 | 24/48 (SNU-1, KATO III, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.806×** | -4.9 | 2e-04 | 24/47 (COLO 205, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.778×** | -4.7 | 4e-04 | 22/48 (COLO 205, SNU-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.761×** | -4.6 | 5e-04 | 20/48 (LS 180, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.810×** | -3.9 | 0.008 | 18/48 (HCT15, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 0.847× | -3.6 | 0.023 | 16/47 (CHP-212, SW 1271, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.899× | -3.5 | 0.030 | 17/49 (LS 180, COLO 205, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | 0.776× | -3.1 | 0.11 | 13/46 (LS 180, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~11% of this change | 0.879× | -3.0 | 0.13 | 17/48 (SW 1088, SW1417, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2302. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 173 | 1 (1 ⚠) | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.84× (z +8.9) ⚠ cell-cycle shift, explains <1% of this change | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -14.8) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.415× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 34.7 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +10.4) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[AsPC-1 (line)]] | alt | 178 | 1 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.95× (z +8.6) ⚠ cell-cycle shift, explains <1% of this change | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.0) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.350× (z -9.7) |
| [[HT-29 (line)]] | alt | 43.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.79× (z +9.8) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[J82 (line)]] | alt | 63.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[LS 180 (line)]] | wt | 116 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -13.2) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.378× (z -9.5) |
| [[SNU-1 (line)]] | wt | 284 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -19.8) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.369× (z -8.6) |
| [[A-427 (line)]] | wt | 77.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.88× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 64.4 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.94× (z +8.9) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[COLO 205 (line)]] | alt | 127 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -15.5) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SW1417 (line)]] | alt | 205 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -14.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A549 (line)]] | wt | 59.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.33× (z +8.5) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[C-33 A (line)]] | alt | 56.4 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.39× (z +9.3) ⚠ toxic; cell-cycle shift, explains ~41% of this change | — |
| [[CFPAC-1 (line)]] | alt | 74.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -12.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[CHP-212 (line)]] | wt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0870× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -12.2) ⚠ cell-cycle shift, explains ~21% of this change |
| [[LoVo (line)]] | wt | 86.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H1792 (line)]] | alt | 50.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.2) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[NCI-H2030 (line)]] | alt | 154 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.605× (z -8.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H23 (line)]] | alt | 44.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.49× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 44.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +9.5) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SW480 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -11.4) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A-172 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 61.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 108 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2302), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BANF1]] | +0.55 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[HDAC1]] | +0.52 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[ARF3]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[CDK2]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[RFC5]] | +0.51 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[PABIR2]] | +0.51 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[PHB1]] | +0.51 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[ILRUN]] | +0.51 | +0.58 / +0.38 | both halves | 6e-05 |  |
| [[RTTN]] | +0.50 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[TECR]] | +0.50 | +0.53 / +0.36 | both halves | 9e-05 |  |
| [[USP54]] | +0.50 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[FKBP1A]] | +0.50 | +0.46 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF4]] | -0.60 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[WASHC1]] | -0.54 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[SNHG32]] | -0.54 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[NSRP1]] | -0.52 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[DNAJB2]] | -0.51 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[EIF1]] | -0.50 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[SNHG12]] | -0.50 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[CDV3]] | -0.49 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[GPS2]] | -0.48 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[NPIPP1]] | -0.48 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[SNHG8]] | -0.47 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[AK6]] | -0.47 | -0.50 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.478). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-38.6, -30.1); signed map (-28.6, -35.8). **Vector** length 114, 28.7% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | +6.0 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | +5.4 | +7.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | +4.0 | +5.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.8 | +12.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +3.8 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.6 | +5.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +1.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.2 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -7.9 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.0 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -3.5 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.4 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.3 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome b5 type B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:69,398,402-69,466,264 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CYB5-M |
| Gene groups (HGNC) | Cytochrome b5 domain containing |
| Hallmark sets | UV_RESPONSE_UP, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: eNOS activation; Metabolism of nitric oxide: NOS3 activation and regulation; Sphingolipid de novo biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O43169](https://www.uniprot.org/uniprotkb/O43169) (Cytochrome b5 type B):

> Cytochrome b5 is a membrane-bound hemoprotein functioning as an electron carrier for several membrane-bound oxygenases.

**Summary**, from NCBI Gene [80777](https://www.ncbi.nlm.nih.gov/gene/80777):

> Enables heme binding activity. Contributes to nitrite reductase (NO-forming) activity. Involved in nitric oxide biosynthetic process. Located in membrane. Part of nitric-oxide synthase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24374](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24374) · Entrez [80777](https://www.ncbi.nlm.nih.gov/gene/80777) · UniProt [O43169](https://www.uniprot.org/uniprotkb/O43169) · Ensembl [ENSG00000103018](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103018)

## Data

Gene col 2302: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2302); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2302, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2302]; `tensor/DDL_lfc|DDL_z.npy` [2302]; `embed/gene_vectors.npy` [2302]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2302 or target_col == 2302). Every well: [[CYB5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYB5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
