---
symbol: "FAM161A"
type: "gene"
col: 9922
ensembl_id: "ENSG00000170264"
name: "FAM161 centrosomal protein A"
location: "2p15"
module: 175
arm: "+"
pooled_cpm: 15.66
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 11
n_dd_up_clean: 14
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# FAM161A

*FAM161 centrosomal protein A* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.28× (z +15.9, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.553× (z -7.9, q 2e-12, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (75 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KATNAL1]] (+0.57, fdr 1e-04), [[FXYD6]] (+0.56, fdr 4e-05), [[MNS1]] (+0.51, fdr 2e-05); moves opposite to [[MOB3B]] (-0.43, fdr 0.001, ⚠ not reproduced), [[TRAPPC12]] (-0.43, fdr 4e-04), [[ZNG1F]] (-0.43, fdr 3e-04), [[ZNG1C]] (-0.42, fdr 1e-04).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[BOLA3-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9922.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.28×** | +15.9 | 0e+00 | 45/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.18×** | +14.9 | 0e+00 | 20/23 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.87×** | +14.1 | 6e-43 | 46/47 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.72×** | +13.4 | 7e-39 | 34/38 (PANC-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.48×** | +12.2 | 6e-32 | 40/46 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +10.3 | 1e-22 | 31/46 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.04×** | +9.6 | 1e-19 | 40/47 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.14×** | +9.4 | 3e-19 | 21/29 (A-427, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +7.0 | 2e-10 | 25/47 (RKO, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.72×** | +7.0 | 2e-10 | 25/40 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +6.9 | 4e-10 | 26/46 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.58×** | +6.1 | 4e-08 | 26/46 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.32×** | +5.9 | 2e-07 | 22/47 (PANC-1, KATO III, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +5.8 | 3e-07 | 26/46 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +5.8 | 3e-07 | 26/47 (LoVo, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +5.1 | 1e-05 | 22/47 (HepG2/C3A, HOP62, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.3 | 6e-04 | 17/47 (HOP62, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.002 | 15/47 (J82, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.056 | 4/44 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.056 | 15/46 (C32, A-172, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.39×** | +2.9 | 0.094 | 6/45 (NCI-H460, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9922.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.553×** | -7.9 | 2e-12 | 30/46 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.596×** | -6.9 | 1e-09 | 29/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.603×** | -6.7 | 3e-09 | 27/46 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.637×** | -6.0 | 3e-07 | 25/44 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.443×** | -5.7 | 2e-06 | 21/44 (MIA PaCa-2, NCI-H1792, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.525×** | -4.5 | 7e-04 | 20/47 (A-427, C-33 A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.803×** | -4.1 | 0.003 | 15/47 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.749×** | -3.8 | 0.009 | 19/46 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.752×** | -3.8 | 0.009 | 15/47 (PANC-1, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.764×** | -3.6 | 0.019 | 13/46 (A-427, A-172, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -3.4 | 0.041 | 4/47 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.786×** | -3.2 | 0.063 | 13/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9922. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 21.0 | 5 (4 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.51× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.30× (z +10.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 45.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.03× (z +11.6) ⚠ toxic; transcription drop | [[TAK-901 (drug)]] 5 µM 0.0978× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 36.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.244× (z -10.6) |
| [[SHP-77 (line)]] | alt | 33.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.99× (z +9.2) ⚠ toxic; transcription drop | [[AZD2858 (drug)]] 0.5 µM 0.0952× (z -10.6) ⚠ toxic · without an alert: [[Temsirolimus (drug)]] 0.5 µM 0.292× (z -8.6) |
| [[SW480 (line)]] | alt | 22.1 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -9.8) |
| [[A498 (line)]] | wt | 17.8 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.06× (z +10.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.71× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 5.52 | 0 | 2 | — | [[Naproxen (drug)]] 5 µM 0.0891× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 16.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Digitoxin (drug)]] 5 µM 0.282× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 7.39 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.65× (z +8.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 10.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.07× (z +8.6) | — |
| [[LoVo (line)]] | wt | 5.11 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 4.41 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 23.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -10.0) ⚠ cell-cycle shift, explains ~84% of this change |
| [[NCI-H661 (line)]] | alt | 39.9 | 0 | 1 | — | [[MK-8353 (drug)]] 0.05 µM 0.0737× (z -8.5) |
| [[SNU-423 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.56× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[AN3 CA (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9922), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 20 of them with an alert (⚠; 20 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KATNAL1]] | +0.57 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[FXYD6]] | +0.56 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[MNS1]] | +0.51 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[FAM13B]] | +0.48 | +0.20 / +0.56 | both halves | 7e-04 |  |
| [[CYB5RL]] | +0.48 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ANKRD36C]] | +0.47 | +0.34 / +0.32 | both halves | 2e-04 |  |
| [[CTSV]] | +0.47 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[MAST1]] | +0.47 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[TMEM14A]] | +0.45 | +0.24 / +0.60 | both halves | 4e-04 |  |
| [[PSIP1]] | +0.45 | +0.45 / +0.36 | both halves | 9e-05 |  |
| [[DYNC2H1]] | +0.45 | +0.39 / +0.45 | both halves | 6e-05 |  |
| [[PLEKHH2]] | +0.45 | +0.32 / +0.54 | both halves | 2e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB3B]] | -0.43 | -0.15 / -0.25 | ⚠ not reproduced | 0.001 |  |
| [[TRAPPC12]] | -0.43 | -0.25 / -0.41 | both halves | 4e-04 |  |
| [[ZNG1F]] | -0.43 | -0.29 / -0.36 | both halves | 3e-04 |  |
| [[ZNG1C]] | -0.42 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[ZNG1E]] | -0.42 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[NSF]] | -0.42 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[RUNDC1]] | -0.41 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[ATP6V0A2]] | -0.40 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[MED27]] | -0.40 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[AP4E1]] | -0.40 | -0.17 / -0.34 | ⚠ not reproduced | 0.001 |  |
| [[ATR]] | -0.39 | -0.21 / -0.33 | both halves | 6e-04 |  |
| [[SRP19]] | -0.38 | -0.15 / -0.27 | ⚠ not reproduced | 0.001 |  |
| [[MTOR]] | -0.38 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[HDAC4]] | -0.38 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[TASOR2]] | -0.38 | -0.24 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3-DT]] | B | BOLA3-DT activity raises FAM161A's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 2.21× lower at baseline in the lines without BOLA3-DT | 0.030 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[APBB1]] | B | APBB1 activity raises FAM161A's level | lines that do not express APBB1 (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without APBB1 | 0.043 | ⚠ within organs, on part of the lines; also absent: C14orf132, WNT9A, TTC7B; maybe low, not absent |
| [[KIF3C]] | B | KIF3C activity raises FAM161A's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 2.71× lower at baseline in the lines without KIF3C | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1; its own permutation p |
| [[CHD5]] | B | CHD5 activity raises FAM161A's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.48× lower at baseline in the lines without CHD5 | 0.092 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[VAT1]] | C | VAT1 activity raises FAM161A's level | lines that do not express VAT1 (3) vs lines expressing it (47) | 3.02× lower at baseline in the lines without VAT1 | 0.079 | ⚠ few lines (3 vs 47); across organs; also absent: SH2B3, C12orf75, SKAP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.111). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.5, -1.3); signed map (-26.6, 32.1). **Vector** length 65.0, 11.9% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.5 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +2.9 | +13.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.5 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +2.3 | +9.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.0 | +2.4 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +5.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.3 | +1.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -3.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -6.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -4.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | FAM161 centrosomal protein A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:61,824,848-61,854,143 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13305; previously RP28 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3B820](https://www.uniprot.org/uniprotkb/Q3B820) (Protein FAM161A):

> Involved in ciliogenesis.

**Summary**, from NCBI Gene [84140](https://www.ncbi.nlm.nih.gov/gene/84140):

> This gene belongs to the FAM161 family. It is expressed mainly in the retina. Mouse studies suggested that this gene is involved in development of retinal progenitors during embryogenesis, and that its activity is restricted to mature photoreceptors after birth. Mutations in this gene cause autosomal recessive retinitis pigmentosa-28. Alternatively spliced transcript variants have been identified.[provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:25808](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25808) · Entrez [84140](https://www.ncbi.nlm.nih.gov/gene/84140) · UniProt [Q3B820](https://www.uniprot.org/uniprotkb/Q3B820) · Ensembl [ENSG00000170264](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170264)

## Data

Gene col 9922: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9922); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9922, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9922]; `tensor/DDL_lfc|DDL_z.npy` [9922]; `embed/gene_vectors.npy` [9922]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9922 or target_col == 9922). Every well: [[FAM161A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM161A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
