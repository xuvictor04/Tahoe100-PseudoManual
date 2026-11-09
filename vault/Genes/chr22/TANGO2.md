---
symbol: "TANGO2"
type: "gene"
col: 11421
ensembl_id: "ENSG00000183597"
name: "transport and golgi organization 2 homolog"
location: "22q11.21"
module: 72
arm: "+"
pooled_cpm: 15.52
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# TANGO2

*transport and golgi organization 2 homolog* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 3.16× (z +16.7, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.551× (z -12.9, q 2e-35, down in 35 of 46 measured lines) ⚠ cell-cycle shift, explains ~64% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.315× (z -9.3, q 3e-18, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD39]] (+0.74, fdr 7e-06), [[UFD1]] (+0.73, fdr 7e-06), [[HERC2P2]] (+0.73, fdr 7e-06); moves opposite to [[ZNF608]] (-0.63, fdr 7e-06), [[TIFA]] (-0.59, fdr 1e-05), [[FAM200B]] (-0.58, fdr 4e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11421.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **3.16×** | +16.7 | 0e+00 | 43/45 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.85×** | +16.1 | 0e+00 | 43/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.70×** | +15.3 | 0e+00 | 43/47 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.63×** | +14.9 | 0e+00 | 44/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.53×** | +14.3 | 3e-44 | 46/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.19×** | +12.1 | 1e-31 | 41/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.77×** | +6.3 | 3e-08 | 25/48 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.98×** | +5.5 | 3e-06 | 22/38 (LS 180, NCI-H460, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +5.0 | 3e-05 | 21/47 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 0.001 | 14/44 (LS 180, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +4.0 | 0.003 | 10/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.003 | 17/45 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +3.5 | 0.021 | 6/48 (C32, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 14 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11421.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.551×** | -12.9 | 2e-35 | 35/46 (SK-MEL-2, HS-578T, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.488×** | -11.0 | 7e-26 | 41/48 (PANC-1, HS-578T, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.315×** | -9.3 | 3e-18 | 36/47 (KATO III, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.551×** | -9.2 | 7e-18 | 32/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.494×** | -8.9 | 6e-17 | 28/47 (A549, NCI-H23, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.638×** | -6.9 | 5e-10 | 26/46 (A-172, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.647×** | -6.7 | 2e-09 | 26/47 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.496×** | -5.6 | 1e-06 | 19/44 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.709×** | -5.3 | 8e-06 | 24/46 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.666×** | -5.1 | 2e-05 | 22/41 (HS-578T, A498, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.795×** | -5.0 | 3e-05 | 19/48 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.732×** | -4.4 | 4e-04 | 16/34 (NCI-H460, BT-474, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **0.771×** | -4.0 | 0.003 | 19/37 (SK-MEL-2, SHP-77, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.6 | 0.012 | 20/48 (SK-MEL-2, SW480, …) | top dose only | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.793×** | -3.6 | 0.014 | 15/47 (SW480, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11421. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.0 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.36× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.175× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 16.4 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.9) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.230× (z -9.5) |
| [[KATO III (line)]] | alt | 15.1 | 4 | 1 | [[Ixazomib citrate (drug)]] 5 µM 4.62× (z +10.0) | [[TAK-901 (drug)]] 5 µM 0.0840× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 11.3 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.71× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 12.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.59× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 10.0 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.80× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.3) ⚠ cell-cycle shift, explains ~62% of this change |
| [[HS-578T (line)]] | alt | 29.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -14.2) ⚠ cell-cycle shift, explains ~64% of this change |
| [[HT-29 (line)]] | alt | 38.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.07× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 17.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.3) ⚠ cell-cycle shift, explains ~64% of this change |
| [[LoVo (line)]] | wt | 16.0 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.77× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.274× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LS 180 (line)]] | wt | 17.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.13× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 15.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.78× (z +9.1) | — |
| [[A498 (line)]] | wt | 17.8 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.91× (z +9.5) | — |
| [[A549 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.6) ⚠ cell-cycle shift, explains ~64% of this change |
| [[AsPC-1 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -12.2) ⚠ cell-cycle shift, explains ~62% of this change |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -9.1) ⚠ cell-cycle shift, explains ~64% of this change |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.130× (z -8.7) |
| [[J82 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.5) ⚠ cell-cycle shift, explains ~64% of this change |
| [[NCI-H2347 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -9.9) ⚠ cell-cycle shift, explains ~62% of this change |
| [[RKO (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -10.7) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -14.5) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SNU-423 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.0) ⚠ cell-cycle shift, explains ~64% of this change |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11421), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD39]] | +0.74 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[UFD1]] | +0.73 | +0.75 / +0.68 | both halves | 7e-06 | STRING 536 |
| [[HERC2P2]] | +0.73 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[PCYT1A]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[SNX29]] | +0.70 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[PWWP3A]] | +0.68 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[SAMD4B]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[HERC2P3]] | +0.67 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[EPS15L1]] | +0.67 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[KCTD21]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ZFAND2A]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF608]] | -0.63 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[TIFA]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[FAM200B]] | -0.58 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[AGL]] | -0.58 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[BMI1]] | -0.58 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[REL]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[LEKR1]] | -0.57 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[CAV1]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[CPNE1]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[PER2]] | -0.55 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[ANAPC13]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TANGO2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers TANGO2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.7, -8.0); signed map (-27.7, -25.8). **Vector** length 109, 27.5% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +12.2 | +16.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +11.6 | +16.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.7 | +15.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +5.5 | +5.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.8 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -8.1 | -12.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.1 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -5.4 | -8.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.1 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -5.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | transport and golgi organization 2 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,017,014-20,067,164 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761P1121; previously C22orf25 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ICL3](https://www.uniprot.org/uniprotkb/Q6ICL3) (Transport and Golgi organization protein 2 homolog):

> May be involved in lipid homeostasis.

**Summary**, from NCBI Gene [128989](https://www.ncbi.nlm.nih.gov/gene/128989):

> This gene belongs to the transport and Golgi organization family, whose members are predicted to play roles in secretory protein loading in the endoplasmic reticulum. Depletion of this gene in Drosophila S2 cells causes fusion of the Golgi with the ER. In mouse tissue culture cells, this protein co-localizes with a mitochondrially targeted mCherry protein and displays very low levels of co-localization with Golgi and peroxisomes. Allelic variants of this gene are associated with rhabdomyolysis, …

**Accessions** — [HGNC:25439](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25439) · Entrez [128989](https://www.ncbi.nlm.nih.gov/gene/128989) · UniProt [Q6ICL3](https://www.uniprot.org/uniprotkb/Q6ICL3) · Ensembl [ENSG00000183597](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183597)

## Data

Gene col 11421: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11421); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11421, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11421]; `tensor/DDL_lfc|DDL_z.npy` [11421]; `embed/gene_vectors.npy` [11421]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11421 or target_col == 11421). Every well: [[TANGO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TANGO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
