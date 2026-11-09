---
symbol: "TCP11L1"
type: "gene"
col: 10687
ensembl_id: "ENSG00000176148"
name: "t-complex 11 like 1"
location: "11p13"
module: 62
arm: "+"
pooled_cpm: 50.06
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 35
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# TCP11L1

*t-complex 11 like 1* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[GSK1059615 (drug)]] 5 µM: 1.55× (z +5.0, q 2e-04, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (20 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.466× (z -16.6, q 0e+00, down in 45 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.544× (z -13.2, q 7e-38, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLTP3B]] (+0.58, fdr 1e-05), [[BBS7]] (+0.54, fdr 2e-04), [[UBE2Q2P1]] (+0.50, fdr 3e-05); moves opposite to [[ABCC3]] (-0.43, fdr 4e-05), [[TRA2B]] (-0.43, fdr 2e-04), [[GCLC]] (-0.42, fdr 6e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC6A14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10687.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **1.55×** | +5.0 | 2e-04 | 23/48 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +5.0 | 2e-04 | 19/48 (LoVo, NCI-H460, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.26×** | +4.9 | 2e-04 | 21/47 (RPMI-7951, NCI-H23, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.50×** | +4.6 | 5e-04 | 21/48 (A498, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.26×** | +4.6 | 5e-04 | 19/48 (NCI-H23, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.9 | 0.008 | 21/47 (SW480, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.021 | 13/48 (A498, LS 180, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.027 | 7/48 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~90% of this change | 1.17× | +3.4 | 0.038 | 13/48 (PANC-1, C-33 A, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.048 | 9/48 (LOX-IMVI, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.074 | 9/48 (J82, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10687.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.466×** | -16.6 | 0e+00 | 45/48 (SW48, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.588×** | -16.4 | 0e+00 | 38/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.512×** | -14.5 | 1e-45 | 42/48 (A549, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.498×** | -14.4 | 7e-45 | 39/48 (A549, HS-578T, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.544×** | -13.2 | 7e-38 | 44/48 (A-172, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.542×** | -12.8 | 1e-35 | 36/48 (HOP62, LOX-IMVI, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.569×** | -12.3 | 1e-32 | 36/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.569×** | -11.8 | 3e-30 | 33/47 (LoVo, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.587×** | -11.6 | 3e-29 | 38/48 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.593×** | -11.4 | 4e-28 | 35/48 (HS-578T, A549, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.415×** | -10.0 | 7e-22 | 38/49 (HOP62, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.461×** | -8.8 | 6e-17 | 34/48 (MIA PaCa-2, Hs 766T, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.657×** | -8.7 | 2e-16 | 31/48 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.707×** | -7.5 | 2e-12 | 32/48 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.699×** | -7.3 | 8e-12 | 30/48 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.728×** | -6.5 | 2e-09 | 28/48 (LoVo, SW480, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.671×** | -4.5 | 1e-04 | 19/48 (SK-MEL-2, AN3 CA, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.686×** | -4.3 | 4e-04 | 18/48 (A549, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.777×** | -3.9 | 0.002 | 10/48 (LOX-IMVI, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.881× | -3.8 | 0.002 | 13/48 (SNU-423, HOP62, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.780×** | -3.8 | 0.002 | 15/48 (LOX-IMVI, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | 0.844× | -3.7 | 0.004 | 10/48 (NCI-H1573, NCI-H661, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.838× | -3.6 | 0.005 | 15/47 (LOX-IMVI, SW48, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.742×** | -3.4 | 0.011 | 10/48 (PANC-1, SW48, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10687. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 94.0 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -27.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -12.0) |
| [[HOP62 (line)]] | alt | 66.8 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -16.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.172× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 59.8 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -24.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.134× (z -10.5) |
| [[SNU-423 (line)]] | alt | 71.4 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -15.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.339× (z -10.2) |
| [[HS-578T (line)]] | alt | 64.8 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -14.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -12.3) |
| [[A-172 (line)]] | wt | 93.1 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.311× (z -14.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.322× (z -14.5) |
| [[PANC-1 (line)]] | alt | 61.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -18.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.396× (z -14.0) |
| [[SK-MEL-2 (line)]] | alt | 69.1 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 44.7 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.381× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.490× (z -8.9) |
| [[J82 (line)]] | alt | 90.2 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -12.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 41.5 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 96.1 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.390× (z -12.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A549 (line)]] | wt | 89.3 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -15.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 26.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.349× (z -10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.399× (z -9.4) |
| [[SW48 (line)]] | wt | 89.5 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0843× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 61.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.384× (z -10.7) |
| [[H4 (line)]] | wt | 70.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -10.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HCT15 (line)]] | alt | 36.0 | 0 | 2 (2 ⚠) | — | [[NG25 (drug)]] 5 µM 0.0720× (z -9.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[HepG2_C3A (line)]] | wt | 31.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[Hs 766T (line)]] | wt | 44.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -9.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.106× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 59.1 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 36.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.244× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 45.5 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -10.6) ⚠ cell-cycle shift, explains ~91% of this change |
| [[COLO 205 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -9.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2030 (line)]] | alt | 60.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.374× (z -9.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H23 (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[RPMI-7951 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -8.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW 900 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10687), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLTP3B]] | +0.58 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[BBS7]] | +0.54 | +0.32 / +0.58 | both halves | 2e-04 |  |
| [[UBE2Q2P1]] | +0.50 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[CCDC92]] | +0.50 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[MTURN]] | +0.49 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[RRM2B]] | +0.47 | +0.27 / +0.50 | both halves | 3e-04 |  |
| [[C14orf28]] | +0.47 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[DRAM1]] | +0.47 | +0.28 / +0.52 | both halves | 3e-04 |  |
| [[NTN1]] | +0.46 | +0.24 / +0.50 | both halves | 5e-04 |  |
| [[PLPP1]] | +0.46 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[EDA2R]] | +0.46 | +0.32 / +0.46 | both halves | 2e-04 |  |
| [[PCNP]] | +0.46 | +0.40 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC3]] | -0.43 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[TRA2B]] | -0.43 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[GCLC]] | -0.42 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[ENOX1]] | -0.42 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[TBC1D8]] | -0.40 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[HMBS]] | -0.40 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[LINC00511]] | -0.40 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[SLC19A3]] | -0.39 | -0.38 / -0.27 | both halves | 3e-04 |  |
| [[LINC02320]] | -0.39 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[PRKCA]] | -0.39 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[PPARG]] | -0.38 | -0.24 / -0.41 | both halves | 5e-04 |  |
| [[CYP39A1]] | -0.38 | -0.34 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC6A14]] | B | SLC6A14 activity lowers TCP11L1's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 1.97× higher at baseline in the lines without SLC6A14 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[SLC6A14]] | B | SLC6A14 activity weakens TCP11L1's drug response | lines that do not express SLC6A14 (39) vs lines expressing it (9) | the lines without SLC6A14 respond 1.93× as strongly (z diff -2.86); strongest at Panobinostat 5 µM: 0.44x vs 0.75x (z diff -4.6) | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1; target measured in part of the lines; artifact flags |
| [[ABCC3]] | B | ABCC3 activity lowers TCP11L1's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 1.53× higher at baseline in the lines without ABCC3 | 0.044 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[GLS2]] | B | GLS2 activity lowers TCP11L1's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 1.65× higher at baseline in the lines without GLS2 | 0.065 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| [[GLS2]] | B | GLS2 activity weakens TCP11L1's drug response | lines that do not express GLS2 (14) vs lines expressing it (34) | the lines without GLS2 respond 1.73× as strongly (z diff -2.54); strongest at Belinostat 5 µM: 0.45x vs 0.65x (z diff -4.0) | 0.068 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.429). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.8, 21.3); signed map (-3.2, 0.2). **Vector** length 81.0, 19.6% of its response variance represented; |z| ≥ 3 in 1,347 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.1 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +3.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +1.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.5 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.4 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +1.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.5 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.7 | -13.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.4 | -14.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | -2.2 | -11.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.0 | -10.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.9 | -14.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -8.8 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.7 | -0.6 |
|  | [[Ritonavir (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | t-complex 11 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:33,039,417-33,105,943 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11336 |
| Matched by | ensembl_id |

UniProt [Q9NUJ3](https://www.uniprot.org/uniprotkb/Q9NUJ3) carries no function annotation.

**Summary**, from NCBI Gene [55346](https://www.ncbi.nlm.nih.gov/gene/55346):

> Predicted to be involved in signal transduction. Located in microtubule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25655) · Entrez [55346](https://www.ncbi.nlm.nih.gov/gene/55346) · UniProt [Q9NUJ3](https://www.uniprot.org/uniprotkb/Q9NUJ3) · Ensembl [ENSG00000176148](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176148)

## Data

Gene col 10687: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10687); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10687, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10687]; `tensor/DDL_lfc|DDL_z.npy` [10687]; `embed/gene_vectors.npy` [10687]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10687 or target_col == 10687). Every well: [[TCP11L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCP11L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
