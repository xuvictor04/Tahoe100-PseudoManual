---
symbol: "GET1"
type: "gene"
col: 11237
ensembl_id: "ENSG00000182093"
name: "guided entry of tail-anchored proteins factor 1"
location: "21q22.2"
module: 30
arm: "+"
pooled_cpm: 21.13
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 28
n_dd_up_clean: 9
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# GET1

*guided entry of tail-anchored proteins factor 1* — 21q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.71× (z +10.4, q 9e-23, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.350× (z -28.8, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NTAN1]] (+0.70, fdr 7e-06), [[CDS2]] (+0.70, fdr 9e-06), [[ADIPOR1]] (+0.69, fdr 1e-05); moves opposite to [[PATL2]] (-0.67, fdr 2e-05), [[UTP3]] (-0.66, fdr 7e-06), [[ZFX]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11237.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +10.4 | 9e-23 | 35/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +10.1 | 2e-21 | 39/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +9.4 | 7e-19 | 40/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +5.8 | 9e-07 | 25/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.36×** | +5.7 | 1e-06 | 23/47 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +5.6 | 2e-06 | 23/48 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +4.9 | 8e-05 | 11/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 3e-04 | 19/47 (SNU-423, H4, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.006 | 10/48 (LS 180, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.21×** | +3.7 | 0.010 | 12/48 (LS 180, KATO III, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.069 | 8/48 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.1 | 0.085 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11237.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.350×** | -28.8 | 0e+00 | 46/47 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.363×** | -18.9 | 0e+00 | 42/47 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.420×** | -16.8 | 0e+00 | 36/47 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.586×** | -10.4 | 4e-23 | 38/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.606×** | -9.7 | 3e-20 | 30/46 (H4, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.627×** | -9.1 | 1e-17 | 31/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.433×** | -8.5 | 2e-15 | 29/48 (H4, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.664×** | -7.9 | 1e-13 | 31/48 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.669×** | -7.8 | 4e-13 | 29/48 (A-172, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.671×** | -7.7 | 6e-13 | 27/48 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.679×** | -7.5 | 3e-12 | 27/48 (HT-29, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.546×** | -6.1 | 4e-08 | 22/46 (C32, LOX-IMVI, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.815×** | -5.6 | 8e-07 | 26/48 (A-427, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.760×** | -5.3 | 4e-06 | 19/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **0.783×** | -4.6 | 2e-04 | 20/46 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.640×** | -4.5 | 2e-04 | 17/48 (PANC-1, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.723×** | -4.5 | 2e-04 | 13/48 (MIA PaCa-2, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.800×** | -4.3 | 4e-04 | 18/48 (CFPAC-1, HCT15, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.657×** | -4.3 | 6e-04 | 17/48 (RPMI-7951, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.814×** | -4.0 | 0.002 | 16/48 (A-172, H4, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.679×** | -3.9 | 0.002 | 16/46 (CFPAC-1, A549, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11237. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 31.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0761× (z -31.1) |
| [[NCI-H460 (line)]] | wt | 17.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -15.8) |
| [[C32 (line)]] | wt | 23.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -18.0) |
| [[A498 (line)]] | wt | 23.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -14.0) |
| [[A549 (line)]] | wt | 19.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -14.9) |
| [[HOP62 (line)]] | alt | 27.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -18.5) |
| [[NCI-H1573 (line)]] | alt | 13.4 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -13.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.211× (z -9.9) |
| [[PANC-1 (line)]] | alt | 20.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -18.1) |
| [[H4 (line)]] | wt | 41.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.243× (z -11.5) |
| [[HCT15 (line)]] | alt | 33.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 49.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.6) |
| [[SNU-423 (line)]] | alt | 20.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -16.3) |
| [[A-427 (line)]] | wt | 21.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 30.4 | 0 | 2 | — | [[Roxadustat (drug)]] 0.05 µM 0.209× (z -9.0) |
| [[HS-578T (line)]] | alt | 25.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -15.8) |
| [[J82 (line)]] | alt | 12.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 26.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.4) |
| [[NCI-H1792 (line)]] | alt | 22.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 28.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.7) |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -15.5) |
| [[SW480 (line)]] | alt | 20.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -15.5) |
| [[CFPAC-1 (line)]] | alt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -18.0) |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.5) |
| [[Hs 766T (line)]] | wt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -13.7) |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -8.5) |
| [[KATO III (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 18.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -12.2) |
| [[SNU-1 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -13.5) ⚠ cell-cycle shift, explains ~95% of this change |
| [[AN3 CA (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11237), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTAN1]] | +0.70 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[CDS2]] | +0.70 | +0.78 / +0.57 | both halves | 9e-06 |  |
| [[ADIPOR1]] | +0.69 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.69 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[GET1-SH3BGR]] | +0.68 | +0.66 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RAB40B]] | +0.68 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[TPRG1L]] | +0.67 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[LINC01881]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[MAX]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[STX7]] | +0.67 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[SDHAP1]] | +0.66 | +0.76 / +0.49 | both halves | 2e-05 |  |
| [[HSPB11]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[GGCX]] | +0.66 | +0.62 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATL2]] | -0.67 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[UTP3]] | -0.66 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[ZFX]] | -0.66 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ZNF462]] | -0.66 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[PBDC1]] | -0.65 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[ZC3H4]] | -0.64 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[METTL18]] | -0.64 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.64 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[ZNF518A]] | -0.64 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.64 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[FJX1]] | -0.64 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[GPATCH4]] | -0.63 | -0.67 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GET1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers GET1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.729). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (3.8, -13.7); signed map (-39.0, -1.6). **Vector** length 86.8, 18.3% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.3 | +9.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +10.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +10.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.7 | +5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +4.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | -0.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.4 | -28.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.0 | -18.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -16.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -3.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | guided entry of tail-anchored proteins factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.2 — chr21:39,377,698-39,428,528 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CHD5; previously WRB |
| Gene groups (HGNC) | Guided entry of tail-anchored proteins complex subunits |
| Reactome | 2 pathways, smallest: Insertion of tail-anchored proteins into the endoplasmic reticulum membrane; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [O00258](https://www.uniprot.org/uniprotkb/O00258) (Guided entry of tail-anchored proteins factor 1):

> Required for the post-translational delivery of tail-anchored (TA) proteins to the endoplasmic reticulum (ER). Together with CAMLG/GET2, acts as a membrane receptor for soluble GET3/TRC40, which recognizes and selectively binds the transmembrane domain of TA proteins in the cytosol. Required to ensure correct topology and ER insertion of CAMLG.

**Summary**, from NCBI Gene [7485](https://www.ncbi.nlm.nih.gov/gene/7485):

> This gene is located in the candidate region for congenital heart disease (CHD) in Down syndrome (DS). It encodes a basic protein that functions as a receptor that promotes insertion of tail-anchored proteins in the endoplasmic reticulum membrane. This gene is located at a maternally-methylated differentially methylated region (DMR); however, its transcription may be biallelic, not imprinted. Alternative splicing results in different transcript variants. A pseudogene has been defined on …

**Accessions** — [HGNC:12790](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12790) · Entrez [7485](https://www.ncbi.nlm.nih.gov/gene/7485) · UniProt [O00258](https://www.uniprot.org/uniprotkb/O00258) · Ensembl [ENSG00000182093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182093)

## Data

Gene col 11237: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11237); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11237, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11237]; `tensor/DDL_lfc|DDL_z.npy` [11237]; `embed/gene_vectors.npy` [11237]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11237 or target_col == 11237). Every well: [[GET1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GET1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
