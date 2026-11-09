---
symbol: "MVP"
type: "gene"
col: 269
ensembl_id: "ENSG00000013364"
name: "major vault protein"
location: "16p11.2"
module: 70
arm: "+"
pooled_cpm: 49.86
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 28
n_dd_up_clean: 11
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# MVP

*major vault protein* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.35× (z +5.8, q 5e-06, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.485× (z -14.2, q 3e-43, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAFD1]] (+0.62, fdr 3e-05), [[PSMB9]] (+0.58, fdr 1e-05), [[DCAF5]] (+0.58, fdr 1e-05); moves opposite to [[DOCK1]] (-0.58, fdr 3e-05), [[SLC4A7]] (-0.52, fdr 1e-05), [[GBX2-AS1]] (-0.51, fdr 3e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GBP2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MVP-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 269.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +5.8 | 5e-06 | 28/46 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +5.0 | 1e-04 | 22/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +5.0 | 1e-04 | 25/47 (AsPC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.25×** | +4.6 | 5e-04 | 20/48 (A-427, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 0.002 | 23/47 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +3.9 | 0.007 | 13/47 (AsPC-1, NCI-H2347, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.007 | 21/46 (NCI-H2030, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.007 | 20/47 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.007 | 16/46 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.8 | 0.007 | 17/47 (AsPC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.7 | 0.009 | 15/47 (AsPC-1, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.012 | 17/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.21×** | +3.6 | 0.013 | 17/46 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.20× | +3.6 | 0.014 | 14/47 (AsPC-1, KATO III, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.5 | 0.020 | 11/47 (AsPC-1, C32, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.027 | 17/47 (SNU-423, A549, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.029 | 8/47 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 269.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.485×** | -14.2 | 3e-43 | 44/47 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.520×** | -12.9 | 2e-35 | 43/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.534×** | -12.3 | 1e-32 | 38/47 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.565×** | -11.2 | 5e-27 | 38/47 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.594×** | -10.2 | 1e-22 | 39/47 (COLO 205, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.605×** | -9.9 | 5e-21 | 39/47 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.719×** | -9.2 | 4e-18 | 29/47 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.656×** | -8.3 | 9e-15 | 35/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.674×** | -7.7 | 6e-13 | 33/47 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.701×** | -7.0 | 2e-10 | 27/47 (RPMI-7951, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.701×** | -7.0 | 2e-10 | 32/47 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.526×** | -6.6 | 2e-09 | 31/43 (MIA PaCa-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.716×** | -6.6 | 2e-09 | 32/47 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.789×** | -6.6 | 2e-09 | 27/47 (SNU-423, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **0.727×** | -6.3 | 1e-08 | 25/45 (SK-MEL-2, LoVo, …) | inconsistent across doses | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.696×** | -6.2 | 2e-08 | 28/47 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.741×** | -5.9 | 2e-07 | 27/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.762×** | -5.1 | 8e-06 | 24/46 (H4, A-172, …) | rises with dose | position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | 0.867× | -3.9 | 0.002 | 20/47 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.822×** | -3.8 | 0.003 | 15/46 (NCI-H23, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.728×** | -3.3 | 0.022 | 16/47 (hTERT-HPNE, HCT15, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 52.1 | 0 | 10 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -16.9) |
| [[Hs 766T (line)]] | wt | 105 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 55.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -17.0) |
| [[BT-474 (line)]] | alt | 49.8 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.184× (z -13.1) |
| [[HS-578T (line)]] | alt | 56.9 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -10.4) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.520× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 37.7 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.424× (z -8.6) |
| [[A549 (line)]] | wt | 66.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.535× (z -9.2) |
| [[COLO 205 (line)]] | alt | 81.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -14.7) |
| [[H4 (line)]] | wt | 61.1 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -11.1) |
| [[HT-29 (line)]] | alt | 65.2 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.327× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 39.4 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 26.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.222× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 84.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -11.7) |
| [[SW480 (line)]] | alt | 24.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -13.2) |
| [[A-172 (line)]] | wt | 94.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.466× (z -9.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A498 (line)]] | wt | 70.3 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.459× (z -10.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HCT15 (line)]] | alt | 65.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -9.4) |
| [[LS 180 (line)]] | wt | 55.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -14.4) |
| [[RPMI-7951 (line)]] | alt | 62.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -12.0) |
| [[SW1417 (line)]] | alt | 65.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.343× (z -11.2) |
| [[A-427 (line)]] | wt | 33.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +12.1) | — |
| [[C32 (line)]] | wt | 47.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.125× (z -9.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 60.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -12.5) |
| [[HOP62 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.308× (z -8.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 77.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -12.7) ⚠ cell-cycle shift, explains ~80% of this change |
| [[PANC-1 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.450× (z -8.9) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 73.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.520× (z -9.4) |
| [[SW 900 (line)]] | alt | 50.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -10.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAFD1]] | +0.62 | +0.46 / +0.61 | both halves | 3e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[PSMB9]] | +0.58 | +0.52 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[DCAF5]] | +0.58 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.56 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[BAZ2A]] | +0.56 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[MVP-DT]] | +0.56 | +0.48 / +0.62 | both halves | 2e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[GALT]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[CDKN1B]] | +0.55 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[BAD]] | +0.54 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[YY1AP1]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[RRAGC]] | +0.53 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[EFNA1]] | +0.53 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[ZMYM5]] | +0.52 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOCK1]] | -0.58 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[SLC4A7]] | -0.52 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[GBX2-AS1]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[IPO7]] | -0.50 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[PRMT3]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | -0.49 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PRPS2]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[DCTD]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[GNL3L]] | -0.49 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[LINC02728]] | -0.49 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[SACS]] | -0.49 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[SPCS3]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP2]] | B | GBP2 activity raises MVP's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.05× lower at baseline in the lines without GBP2 | 0.003 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers MVP's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[DHRS3]] | B | DHRS3 activity strengthens MVP's drug response | lines that do not express DHRS3 (13) vs lines expressing it (34) | the lines without DHRS3 respond 0.47× as strongly (z diff +1.90); strongest at Homoharringtonine 5 µM: 1.08x vs 0.63x (z diff +5.4) | 0.060 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2; target measured in part of the lines; artifact flags |
| [[ELF3]] | B | ELF3 activity raises MVP's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 1.20× lower at baseline in the lines without ELF3 | 0.084 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MVP-DT]] | C | MVP's natural level strengthens MVP-DT's drug response | MVP's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.52; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.471). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-4.4, -37.1); signed map (-10.9, 3.4). **Vector** length 97.1, 26.2% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.7 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.3 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +3.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | -4.7 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.0 | -12.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | -3.8 | -6.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.8 | -6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -5.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | +0.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | major vault protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,820,394-29,848,039 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LRP, VAULT1 |
| Hallmark sets | PEROXISOME, INTERFERON_GAMMA_RESPONSE |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14764](https://www.uniprot.org/uniprotkb/Q14764) (Major vault protein):

> Structural component of the vault particle, which is a massive ribonucleoprotein complex that may play a role in cargo transport and signal transduction. Oligomerizes to form a cage-like vault complex, which can house several minor vault components including PARP4. Vaults may play a role in nucleo-cytoplasmic transport. Down-regulates IFNG-mediated STAT1 signaling and subsequent activation of JAK. Down-regulates SRC activity and signaling through MAP kinases.

**Summary**, from NCBI Gene [9961](https://www.ncbi.nlm.nih.gov/gene/9961):

> This gene encodes the major component of the vault complex. Vaults are multi-subunit ribonucleoprotein structures that may be involved in nucleo-cytoplasmic transport. The encoded protein may play a role in multiple cellular processes by regulating the MAP kinase, JAK/STAT and phosphoinositide 3-kinase/Akt signaling pathways. The encoded protein also plays a role in multidrug resistance, and expression of this gene may be a prognostic marker for several types of cancer. Alternatively spliced …

**Accessions** — [HGNC:7531](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7531) · Entrez [9961](https://www.ncbi.nlm.nih.gov/gene/9961) · UniProt [Q14764](https://www.uniprot.org/uniprotkb/Q14764) · Ensembl [ENSG00000013364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013364)

## Data

Gene col 269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 269); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 269]; `tensor/DDL_lfc|DDL_z.npy` [269]; `embed/gene_vectors.npy` [269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 269 or target_col == 269). Every well: [[MVP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MVP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
