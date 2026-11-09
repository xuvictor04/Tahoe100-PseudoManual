---
symbol: "SARAF"
type: "gene"
col: 5483
ensembl_id: "ENSG00000133872"
name: "store-operated calcium entry associated regulatory factor"
location: "8p12"
module: 76
arm: "+"
pooled_cpm: 85.04
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 12
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# SARAF

*store-operated calcium entry associated regulatory factor* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.68× (z +10.6, q 2e-23, up in 37 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.61× (z +9.7, q 9e-20, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.482× (z -14.9, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.719× (z -9.5, q 6e-19, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRIPT]] (+0.71, fdr 7e-06), [[KIZ]] (+0.70, fdr 7e-06), [[CRELD1]] (+0.65, fdr 7e-06); moves opposite to [[GPATCH4]] (-0.67, fdr 7e-06), [[UTP15]] (-0.63, fdr 1e-05), [[PAK1IP1]] (-0.63, fdr 7e-06).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5483.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +10.6 | 2e-23 | 37/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +9.7 | 9e-20 | 42/48 (LoVo, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +8.5 | 5e-15 | 36/48 (LoVo, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +8.2 | 2e-14 | 35/48 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +8.0 | 2e-13 | 28/43 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +7.2 | 4e-11 | 40/48 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +6.2 | 4e-08 | 35/48 (A498, A-172, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.70×** | +5.7 | 1e-06 | 40/47 (LoVo, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +5.6 | 1e-06 | 31/48 (A-172, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +5.6 | 1e-06 | 33/48 (A-172, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +5.4 | 4e-06 | 24/45 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +5.3 | 7e-06 | 25/48 (A-172, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +5.2 | 1e-05 | 30/49 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 9e-05 | 30/48 (NCI-H1573, Panc 03.27, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +4.4 | 5e-04 | 24/49 (A-172, Panc 03.27, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 1.19× | +3.4 | 0.027 | 13/49 (HOP62, AsPC-1, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.18× | +3.2 | 0.045 | 16/48 (AsPC-1, HOP62, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.059 | 15/48 (HOP62, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5483.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.482×** | -14.9 | 0e+00 | 48/48 (NCI-H460, HS-578T, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.719×** | -9.5 | 6e-19 | 33/48 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.707×** | -7.1 | 3e-10 | 30/48 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.724×** | -6.3 | 4e-08 | 36/48 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.575×** | -5.9 | 4e-07 | 31/48 (HS-578T, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.576×** | -5.9 | 4e-07 | 33/48 (SW 900, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.750×** | -5.9 | 4e-07 | 34/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.593×** | -5.6 | 2e-06 | 32/48 (SW 900, HS-578T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.630×** | -4.9 | 5e-05 | 30/48 (SW48, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.635×** | -4.8 | 7e-05 | 29/48 (RPMI-7951, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.723×** | -4.7 | 1e-04 | 30/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.798×** | -4.4 | 4e-04 | 23/48 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.809×** | -4.1 | 0.002 | 25/48 (HepG2/C3A, LoVo, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.775×** | -3.7 | 0.009 | 23/49 (SW48, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.824×** | -3.7 | 0.010 | 21/47 (HS-578T, CHP-212, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.827×** | -3.6 | 0.010 | 20/47 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 75.9 | 4 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.34× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -10.8) |
| [[HS-578T (line)]] | alt | 143 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -16.5) |
| [[NCI-H2347 (line)]] | alt | 112 | 2 (2 ⚠) | 4 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.52× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -16.3) |
| [[SNU-423 (line)]] | alt | 55.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -10.0) |
| [[A498 (line)]] | wt | 97.3 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.453× (z -10.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.620× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 98.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.407× (z -10.5) |
| [[C32 (line)]] | wt | 50.0 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.82× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 152 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -10.0) |
| [[LoVo (line)]] | wt | 102 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.36× (z +11.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.425× (z -11.3) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 83.6 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.330× (z -13.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.618× (z -8.5) |
| [[PANC-1 (line)]] | alt | 23.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +11.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 72.0 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.97× (z +11.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.393× (z -9.7) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 122 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -15.1) |
| [[SW 900 (line)]] | alt | 114 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.362× (z -11.2) |
| [[A-427 (line)]] | wt | 72.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -9.4) |
| [[A549 (line)]] | wt | 84.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.437× (z -8.9) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 90.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 68.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.56× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 81.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.405× (z -8.5) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 120 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.39× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 96.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.339× (z -11.2) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 47.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 93.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.479× (z -9.8) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 57.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -10.6) |
| [[SHP-77 (line)]] | alt | 112 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 81.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.452× (z -8.6) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.348× (z -10.8) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 177 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 125 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRIPT]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[KIZ]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[CRELD1]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[FTL]] | +0.64 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[RTN3]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ECT2L]] | +0.63 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[PSAP]] | +0.62 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[SNX3]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[PJA2]] | +0.62 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ADIPOR1]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[HSPA5]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH4]] | -0.67 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[UTP15]] | -0.63 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[PAK1IP1]] | -0.63 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[NIP7]] | -0.63 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[FJX1]] | -0.62 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[PPRC1]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[RRS1]] | -0.62 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[NOC3L]] | -0.62 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[MRTO4]] | -0.61 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[DHX37]] | -0.61 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[WDR4]] | -0.60 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[ZC3H7B]] | -0.60 | -0.61 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.1, -45.8); signed map (-21.3, 10.1). **Vector** length 134, 40.6% of its response variance represented; |z| ≥ 3 in 1,092 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.0 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +8.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +5.5 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +9.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.2 | +6.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.7 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.3 | -14.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.7 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.1 | -6.3 |
|  | [[EX229 (drug)]] 5 µM |  | -7.1 | -5.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.6 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.5 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.4 | -4.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.2 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | store-operated calcium entry associated regulatory factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:30,063,003-30,083,208 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC8721; previously TMEM66 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BY9](https://www.uniprot.org/uniprotkb/Q96BY9) (Store-operated calcium entry-associated regulatory factor):

> Negative regulator of store-operated Ca(2+) entry (SOCE) involved in protecting cells from Ca(2+) overfilling. In response to cytosolic Ca(2+) elevation after endoplasmic reticulum Ca(2+) refilling, promotes a slow inactivation of STIM (STIM1 or STIM2)-dependent SOCE activity: possibly act by facilitating the deoligomerization of STIM to efficiently turn off ORAI when the endoplasmic reticulum lumen is filled with the appropriate Ca(2+) levels, and thus preventing the overload of the cell with …

**Summary**, from NCBI Gene [51669](https://www.ncbi.nlm.nih.gov/gene/51669):

> Involved in regulation of store-operated calcium entry. Located in endoplasmic reticulum membrane and endoplasmic reticulum-plasma membrane contact site. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28789](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28789) · Entrez [51669](https://www.ncbi.nlm.nih.gov/gene/51669) · UniProt [Q96BY9](https://www.uniprot.org/uniprotkb/Q96BY9) · Ensembl [ENSG00000133872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133872)

## Data

Gene col 5483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5483); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5483]; `tensor/DDL_lfc|DDL_z.npy` [5483]; `embed/gene_vectors.npy` [5483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5483 or target_col == 5483). Every well: [[SARAF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SARAF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
