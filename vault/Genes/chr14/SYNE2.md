---
symbol: "SYNE2"
type: "gene"
col: 613
ensembl_id: "ENSG00000054654"
name: "spectrin repeat containing nuclear envelope protein 2"
location: "14q23.2"
module: 197
arm: "+"
pooled_cpm: 331.4
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 26
n_dd_up_clean: 11
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# SYNE2

*spectrin repeat containing nuclear envelope protein 2* — 14q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.57× (z +8.6, q 4e-15, up in 36 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.37× (z +5.8, q 1e-06, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.652× (z -7.7, q 6e-12, down in 36 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.748× (z -7.3, q 1e-10, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DEK]] (+0.65, fdr 7e-06), [[PCM1]] (+0.61, fdr 1e-05), [[PLCE1]] (+0.60, fdr 1e-05); moves opposite to [[PRKAG1]] (-0.58, fdr 1e-05), [[NAT9]] (-0.56, fdr 1e-05), [[RABEPK]] (-0.56, fdr 3e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 613.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +8.6 | 4e-15 | 36/48 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +7.7 | 3e-12 | 30/43 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +5.8 | 1e-06 | 32/46 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.4 | 1e-05 | 25/47 (NCI-H1792, NCI-H2347, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.79×** | +5.0 | 5e-05 | 32/49 (AsPC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +5.0 | 7e-05 | 25/47 (NCI-H460, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 4e-04 | 26/48 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.29×** | +4.5 | 4e-04 | 29/49 (NCI-H460, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.002 | 26/46 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.002 | 21/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.003 | 28/48 (LoVo, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.003 | 28/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.8 | 0.006 | 18/47 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.6 | 0.015 | 13/47 (NCI-H460, NCI-H2030, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.017 | 22/48 (Hs 766T, KATO III, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.050 | 17/47 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.070 | 17/47 (C32, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 613.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.652×** | -7.7 | 6e-12 | 36/46 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.748×** | -7.3 | 1e-10 | 32/47 (A-427, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.681×** | -7.2 | 1e-10 | 32/47 (COLO 205, KATO III, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.696×** | -6.8 | 1e-09 | 36/47 (COLO 205, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.459×** | -6.7 | 3e-09 | 38/48 (Panc 03.27, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.714×** | -6.3 | 3e-08 | 35/47 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.722×** | -6.1 | 8e-08 | 30/47 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.736×** | -5.7 | 7e-07 | 29/47 (COLO 205, KATO III, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.758×** | -4.9 | 6e-05 | 27/47 (COLO 205, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.566×** | -4.9 | 7e-05 | 33/47 (A-427, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.774×** | -4.8 | 9e-05 | 26/47 (COLO 205, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.779×** | -4.7 | 1e-04 | 27/47 (COLO 205, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.786×** | -4.5 | 3e-04 | 28/47 (A-427, MIA PaCa-2, …) | all doses, flat |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.598×** | -4.4 | 5e-04 | 32/46 (RKO, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.844× | -4.2 | 0.001 | 24/48 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.616×** | -4.1 | 0.001 | 26/47 (LoVo, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.813×** | -3.9 | 0.003 | 25/47 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.650×** | -3.7 | 0.007 | 24/47 (LoVo, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.813×** | -3.6 | 0.007 | 24/46 (SW48, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 613. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 1,259 | 0 | 16 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -20.0) |
| [[KATO III (line)]] | alt | 676 | 1 (1 ⚠) | 10 (5 ⚠) | [[Sonidegib (drug)]] 0.05 µM 2.07× (z +8.7) ⚠ unreliable plate only | [[Panobinostat (drug)]] 5 µM 0.244× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 191 | 10 (1 ⚠) | 1 | [[Trametinib (drug)]] 0.5 µM 2.22× (z +13.1) | [[Selinexor (drug)]] 5 µM 0.510× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 467 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.373× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 1,569 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -14.4) |
| [[HT-29 (line)]] | alt | 428 | 0 | 7 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.491× (z -12.8) |
| [[A-427 (line)]] | wt | 383 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -20.1) |
| [[NCI-H1573 (line)]] | alt | 130 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +17.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 640 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -23.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -17.5) |
| [[NCI-H2347 (line)]] | alt | 182 | 3 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.68× (z +10.7) | [[Selinexor (drug)]] 5 µM 0.529× (z -12.5) |
| [[SW48 (line)]] | wt | 657 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 425 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.432× (z -12.9) |
| [[PANC-1 (line)]] | alt | 272 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +11.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -9.5) ⚠ cell-cycle shift, explains ~17% of this change |
| [[RPMI-7951 (line)]] | alt | 107 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +12.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 479 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.404× (z -10.8) |
| [[A549 (line)]] | wt | 239 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.424× (z -10.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 149 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.447× (z -8.8) |
| [[BT-474 (line)]] | alt | 537 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.451× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 404 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.25× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 142 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +10.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 169 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -11.8) |
| [[HS-578T (line)]] | alt | 83.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.03× (z +8.8) | — |
| [[LoVo (line)]] | wt | 416 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.516× (z -10.1) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 119 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.30× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 250 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.425× (z -10.8) |
| [[SW480 (line)]] | alt | 194 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 142 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.495× (z -9.8) |
| [[A498 (line)]] | wt | 146 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.499× (z -10.7) |
| [[AN3 CA (line)]] | alt | 475 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.357× (z -10.7) |
| [[C32 (line)]] | wt | 326 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.469× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 163 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 96.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 132 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +9.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 331 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +11.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 204 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 325 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.90× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 311 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.192× (z -10.1) ⚠ toxic |
| [[SW 900 (line)]] | alt | 302 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.387× (z -11.0) ⚠ toxic |
| [[C-33 A (line)]] | alt | 473 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 80.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 522 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 418 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 294 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 287 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 613), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DEK]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PCM1]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PLCE1]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SMCHD1]] | +0.60 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ALCAM]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[PSIP1]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[STAG2]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 | pathway: Meiosis; STRING 509 |
| [[MAGI3]] | +0.56 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SMARCC2]] | +0.55 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[CENPU]] | +0.55 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[RAD21]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 | pathway: Meiosis; STRING 518 |
| [[MBNL1]] | +0.53 | +0.46 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAG1]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[NAT9]] | -0.56 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[RABEPK]] | -0.56 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[SNHG21]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ZNF778]] | -0.55 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[CTU1]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ZNF333]] | -0.51 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SNU13]] | -0.50 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ZBTB49]] | -0.50 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[VPS37C]] | -0.50 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ZNF526]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RPUSD2]] | -0.49 | -0.44 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers SYNE2's level | compounds that target MTOR: 4 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Temsirolimus) | 50% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds |
| [[MAP2K1]] | B | MAP2K1 activity lowers SYNE2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.1, -52.7); signed map (3.7, 7.7). **Vector** length 146, 53.1% of its response variance represented; |z| ≥ 3 in 1,891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.1 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +8.6 |
|  | [[Trametinib (drug)]] 5 µM |  | +6.0 | +4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.8 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.5 | +5.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +5.2 | +5.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.8 | +4.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.4 | -7.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.1 | -7.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | -5.5 | -4.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -5.0 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.6 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -3.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -4.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | spectrin repeat containing nuclear envelope protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.2 — chr14:63,761,899-64,226,433 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SYNE-2, DKFZP434H2235, Nesprin-2, NUANCE, NUA, KIAA1011, Nesp2 |
| Gene groups (HGNC) | Spectrin repeat containing nuclear envelope family; KASH domain containing |
| Reactome | 4 pathways, smallest: Meiotic synapsis; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXH0](https://www.uniprot.org/uniprotkb/Q8WXH0) (Nesprin-2):

> Multi-isomeric modular protein which forms a linking network between organelles and the actin cytoskeleton to maintain the subcellular spatial organization. As a component of the LINC (LInker of Nucleoskeleton and Cytoskeleton) complex involved in the connection between the nuclear lamina and the cytoskeleton. The nucleocytoplasmic interactions established by the LINC complex play an important role in the transmission of mechanical forces across the nuclear envelope and in nuclear movement and …

**Summary**, from NCBI Gene [23224](https://www.ncbi.nlm.nih.gov/gene/23224):

> The protein encoded by this gene is a nuclear outer membrane protein that binds cytoplasmic F-actin. This binding tethers the nucleus to the cytoskeleton and aids in the maintenance of the structural integrity of the nucleus. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:17084](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17084) · Entrez [23224](https://www.ncbi.nlm.nih.gov/gene/23224) · UniProt [Q8WXH0](https://www.uniprot.org/uniprotkb/Q8WXH0) · Ensembl [ENSG00000054654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054654)

## Data

Gene col 613: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 613); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 613, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 613]; `tensor/DDL_lfc|DDL_z.npy` [613]; `embed/gene_vectors.npy` [613]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 613 or target_col == 613). Every well: [[SYNE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
