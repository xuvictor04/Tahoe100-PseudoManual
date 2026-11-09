---
symbol: "DPYSL2"
type: "gene"
col: 1714
ensembl_id: "ENSG00000092964"
name: "dihydropyrimidinase like 2"
location: "8p21.2"
module: 11
arm: "-"
pooled_cpm: 157.17
n_lines_expressing: 45
n_dd_up: 2
n_dd_down: 36
n_dd_up_clean: 0
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# DPYSL2

*dihydropyrimidinase like 2* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.65× (z +9.4, q 5e-18, up in 29 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 2.51×, KATO III 2.96×, A549 2.11×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 3.48×, KATO III 2.44×, SW1417 2.66×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LOX-IMVI 3.05×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.163× (z -49.6, q 0e+00, down in 42 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYH10]] (+0.60, fdr 2e-05), [[EHBP1L1]] (+0.58, fdr 1e-05), [[PAPSS1]] (+0.57, fdr 4e-05); moves opposite to [[FBXO6]] (-0.61, fdr 4e-05), [[SCAMP1-AS1]] (-0.60, fdr 1e-05), [[ZCCHC10]] (-0.59, fdr 2e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[PLCXD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1714.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 2.51×, KATO III 2.96×, A549 2.11×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 3.48×, KATO III 2.44×, SW1417 2.66×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LOX-IMVI 3.05×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +9.4 | 5e-18 | 29/40 (SHP-77, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +6.9 | 2e-09 | 28/44 (SK-MEL-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | 1.15× | +3.9 | 0.020 | 15/43 (SNU-1, LS 180, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.33 | 10/43 (C32, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1714.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.163×** | -49.6 | 0e+00 | 42/43 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.181×** | -33.0 | 0e+00 | 42/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.193×** | -30.6 | 0e+00 | 42/43 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.417×** | -16.9 | 0e+00 | 40/43 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.433×** | -15.5 | 0e+00 | 38/42 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.451×** | -15.3 | 0e+00 | 38/43 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.458×** | -15.1 | 0e+00 | 38/43 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.645×** | -12.0 | 4e-31 | 35/44 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.561×** | -11.1 | 6e-27 | 36/43 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.565×** | -11.0 | 2e-26 | 35/43 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.596×** | -10.0 | 1e-21 | 39/43 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.609×** | -9.5 | 6e-20 | 30/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.601×** | -9.4 | 2e-19 | 30/42 (NCI-H23, C-33 A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.608×** | -9.1 | 5e-18 | 35/43 (NCI-H460, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.640×** | -8.6 | 3e-16 | 32/43 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.648×** | -8.4 | 2e-15 | 38/43 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.694×** | -7.0 | 7e-11 | 32/43 (MIA PaCa-2, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.780×** | -6.7 | 4e-10 | 29/43 (PANC-1, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.781×** | -4.8 | 5e-05 | 24/43 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1714. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 166 | 0 | 25 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -39.2) |
| [[NCI-H460 (line)]] | wt | 176 | 0 | 20 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -35.6) |
| [[NCI-H23 (line)]] | alt | 211 | 0 | 19 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0818× (z -37.1) |
| [[PANC-1 (line)]] | alt | 173 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -48.1) |
| [[H4 (line)]] | wt | 203 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -27.5) |
| [[LoVo (line)]] | wt | 163 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -29.7) |
| [[AsPC-1 (line)]] | alt | 293 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0344× (z -41.2) |
| [[NCI-H1573 (line)]] | alt | 79.0 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -34.0) |
| [[KATO III (line)]] | alt | 167 | 2 (2 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.96× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -32.0) |
| [[MIA PaCa-2 (line)]] | alt | 351 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0478× (z -45.8) |
| [[A-172 (line)]] | wt | 407 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -22.0) |
| [[A-427 (line)]] | wt | 157 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0801× (z -43.5) |
| [[A549 (line)]] | wt | 171 | 1 (1 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.11× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0815× (z -43.4) |
| [[CFPAC-1 (line)]] | alt | 112 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -32.0) |
| [[Panc 03.27 (line)]] | alt | 131 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -27.7) |
| [[C-33 A (line)]] | alt | 180 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -18.8) |
| [[HOP62 (line)]] | alt | 122 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -31.7) |
| [[hTERT-HPNE (line)]] | wt | 316 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -25.6) |
| [[J82 (line)]] | alt | 96.5 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -12.1) |
| [[C32 (line)]] | wt | 94.8 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -18.6) |
| [[Hs 766T (line)]] | wt | 311 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0411× (z -41.2) |
| [[NCI-H2030 (line)]] | alt | 172 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0827× (z -38.1) |
| [[HCT15 (line)]] | alt | 176 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0823× (z -23.3) |
| [[LOX-IMVI (line)]] | wt | 47.6 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.05 µM 3.05× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -16.7) |
| [[NCI-H2347 (line)]] | alt | 186 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0775× (z -39.9) |
| [[SNU-1 (line)]] | wt | 84.6 | 1 (1 ⚠) | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.75× (z +9.0) ⚠ cell-cycle shift, explains ~18% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.107× (z -16.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -14.6) |
| [[SW 900 (line)]] | alt | 94.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -30.7) |
| [[LS 180 (line)]] | wt | 106 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -27.6) |
| [[RPMI-7951 (line)]] | alt | 203 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -23.1) |
| [[SW1417 (line)]] | alt | 65.3 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -21.5) |
| [[COLO 205 (line)]] | alt | 77.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -22.9) |
| [[HS-578T (line)]] | alt | 490 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -20.6) |
| [[SNU-423 (line)]] | alt | 116 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -15.0) |
| [[A498 (line)]] | wt | 120 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -22.1) |
| [[NCI-H1792 (line)]] | alt | 74.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -22.3) |
| [[SHP-77 (line)]] | alt | 155 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.51× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -13.3) |
| [[SW48 (line)]] | wt | 188 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0660× (z -24.5) |
| [[HepG2_C3A (line)]] | wt | 65.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -17.3) |
| [[SK-MEL-2 (line)]] | alt | 59.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -11.0) |
| [[SW 1088 (line)]] | alt | 296 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -14.1) |
| [[SW 1271 (line)]] | alt | 63.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -9.2) |
| [[CHP-212 (line)]] | wt | 81.3 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.180× (z -9.3) |
| [[AN3 CA (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 36.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 31.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 38.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1714), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYH10]] | +0.60 | +0.55 / +0.47 | both halves | 2e-05 | pathway: Semaphorin interactions |
| [[EHBP1L1]] | +0.58 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[PAPSS1]] | +0.57 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[SMS]] | +0.57 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[PNMA2]] | +0.56 | +0.66 / +0.46 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SUN1]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[FAM117B]] | +0.56 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[DPP9]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[BNIP3L]] | +0.54 | +0.58 / +0.56 | both halves | 1e-05 | ⚠ same locus (8.4 kb, same strand: neighbours can correlate without regulation) |
| [[MXRA7]] | +0.54 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[CALU]] | +0.54 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[LPCAT2]] | +0.53 | +0.51 / +0.36 | both halves | 9e-05 |  |
| [[C12orf75]] | +0.53 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[FHL1]] | +0.52 | +0.45 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO6]] | -0.61 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[SCAMP1-AS1]] | -0.60 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ZCCHC10]] | -0.59 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[RPP38]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ZC3HC1]] | -0.57 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[WARS2]] | -0.57 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[MRPL32]] | -0.56 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[NFYC]] | -0.56 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[FBXW4]] | -0.55 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[DDX28]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ATAD2B]] | -0.54 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[YTHDF2]] | -0.54 | -0.46 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCXD1]] | B | DPYSL2 activity lowers PLCXD1's level | lines that do not express DPYSL2 (5) vs lines expressing it (45) | 2.07× higher at baseline in the lines without DPYSL2 | 0.048 | ⚠ within organs, on part of the lines; also absent: PHLDA1, PARP3; maybe low, not absent |
| [[BNIP3L]] | B | DPYSL2 activity raises BNIP3L's level | lines that do not express DPYSL2 (5) vs lines expressing it (45) | 1.92× lower at baseline in the lines without DPYSL2 | 0.083 | ⚠ within organs, on part of the lines; also absent: PHLDA1, PARP3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (14.0, -9.6); signed map (-8.7, 43.0). **Vector** length 110, 34.6% of its response variance represented; |z| ≥ 3 in 1,633 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.1 | +2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.1 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +2.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +4.7 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.7 | -16.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.6 | -15.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.2 | -9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.6 | -7.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.4 | -6.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -2.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.0 | -4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | dihydropyrimidinase like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:26,514,031-26,658,178 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DRP-2, DHPRP2, CRMP2, DRP2 |
| Gene groups (HGNC) | M38 metallopeptidases; Spectrin repeat containing |
| Hallmark sets | HEDGEHOG_SIGNALING |
| Reactome | 6 pathways, smallest: CRMPs in Sema3A signaling; Recycling pathway of L1; Semaphorin interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16555](https://www.uniprot.org/uniprotkb/Q16555) (Dihydropyrimidinase-related protein 2):

> Plays a role in neuronal development and polarity, as well as in axon growth and guidance, neuronal growth cone collapse and cell migration. Necessary for signaling by class 3 semaphorins and subsequent remodeling of the cytoskeleton. May play a role in endocytosis.

**Summary**, from NCBI Gene [1808](https://www.ncbi.nlm.nih.gov/gene/1808):

> This gene encodes a member of the collapsin response mediator protein family. Collapsin response mediator proteins form homo- and hetero-tetramers and facilitate neuron guidance, growth and polarity. The encoded protein promotes microtubule assembly and is required for Sema3A-mediated growth cone collapse, and also plays a role in synaptic signaling through interactions with calcium channels. This gene has been implicated in multiple neurological disorders, and hyperphosphorylation of the …

**Accessions** — [HGNC:3014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3014) · Entrez [1808](https://www.ncbi.nlm.nih.gov/gene/1808) · UniProt [Q16555](https://www.uniprot.org/uniprotkb/Q16555) · Ensembl [ENSG00000092964](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092964)

## Data

Gene col 1714: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1714); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1714, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1714]; `tensor/DDL_lfc|DDL_z.npy` [1714]; `embed/gene_vectors.npy` [1714]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1714 or target_col == 1714). Every well: [[DPYSL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPYSL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
