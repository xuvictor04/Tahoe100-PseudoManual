---
symbol: "KRCC1"
type: "gene"
col: 10210
ensembl_id: "ENSG00000172086"
name: "lysine rich coiled-coil 1"
location: "2p11.2"
module: 10
arm: "+"
pooled_cpm: 31.07
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 25
n_dd_up_clean: 26
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# KRCC1

*lysine rich coiled-coil 1* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.29× (z +9.0, q 2e-16, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.204× (z -17.1, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB30-DT]] (+0.81, fdr 7e-06), [[MZF1-AS1]] (+0.81, fdr 7e-06), [[PPP3CB-AS1]] (+0.81, fdr 7e-06); moves opposite to [[PIK3R2]] (-0.74, fdr 7e-06), [[AP1S1]] (-0.72, fdr 8e-05), [[FAM118A]] (-0.72, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LACC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10210.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +9.0 | 2e-16 | 40/46 (LoVo, A-427, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.81×** | +6.4 | 3e-08 | 39/48 (A-172, H4, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +6.4 | 3e-08 | 36/48 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.8 | 2e-04 | 25/45 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +4.3 | 0.002 | 27/48 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.002 | 24/47 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.002 | 29/48 (KATO III, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.003 | 23/47 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.47×** | +3.9 | 0.007 | 22/46 (A549, RKO, …) | all doses, flat | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.007 | 21/48 (A-427, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +3.8 | 0.007 | 21/45 (CFPAC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.007 | 18/48 (CFPAC-1, SW1417, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.009 | 24/47 (LoVo, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.018 | 18/47 (SNU-423, SW480, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.020 | 15/48 (CFPAC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.023 | 21/48 (A-427, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10210.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.204×** | -17.1 | 0e+00 | 46/48 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.246×** | -15.2 | 0e+00 | 46/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.289×** | -13.4 | 1e-38 | 41/47 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.324×** | -12.2 | 7e-32 | 44/48 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.325×** | -12.1 | 7e-32 | 45/48 (H4, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.343×** | -11.6 | 7e-29 | 46/48 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.346×** | -11.4 | 2e-28 | 42/48 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.253×** | -7.8 | 6e-13 | 35/45 (COLO 205, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.273×** | -7.3 | 1e-11 | 42/48 (COLO 205, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.515×** | -7.2 | 4e-11 | 33/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.555×** | -6.3 | 1e-08 | 33/48 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.542×** | -6.2 | 3e-08 | 30/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.556×** | -6.0 | 1e-07 | 32/47 (HS-578T, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.559×** | -5.9 | 2e-07 | 29/47 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.624×** | -4.9 | 4e-05 | 26/45 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.635×** | -4.9 | 4e-05 | 32/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.643×** | -4.5 | 3e-04 | 27/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10210. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 76.9 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0398× (z -21.8) |
| [[LoVo (line)]] | wt | 27.9 | 3 | 5 | [[Homoharringtonine (drug)]] 0.5 µM 5.66× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 46.0 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0895× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -13.1) |
| [[PANC-1 (line)]] | alt | 25.1 | 0 | 8 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0941× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -17.6) |
| [[HT-29 (line)]] | alt | 31.3 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0907× (z -15.4) |
| [[SW480 (line)]] | alt | 24.6 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -12.6) |
| [[KATO III (line)]] | alt | 46.1 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -14.2) |
| [[LS 180 (line)]] | wt | 35.8 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -11.8) |
| [[A-172 (line)]] | wt | 47.7 | 1 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.68× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.186× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.200× (z -11.6) |
| [[A549 (line)]] | wt | 44.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.186× (z -10.7) |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0718× (z -12.7) |
| [[J82 (line)]] | alt | 15.7 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.160× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 39.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.134× (z -14.7) |
| [[SK-MEL-2 (line)]] | alt | 30.5 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.187× (z -10.8) |
| [[A-427 (line)]] | wt | 19.0 | 1 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 6.24× (z +10.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -9.6) |
| [[BT-474 (line)]] | alt | 32.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.206× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 48.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.29× (z +10.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.246× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -9.4) |
| [[HOP62 (line)]] | alt | 37.9 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.30× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.237× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 33.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.194× (z -10.3) |
| [[C32 (line)]] | wt | 25.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0744× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -8.5) |
| [[H4 (line)]] | wt | 32.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0330× (z -16.8) |
| [[HCT15 (line)]] | alt | 33.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -8.7) |
| [[HS-578T (line)]] | alt | 22.4 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.147× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 19.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0808× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.177× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 20.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 34.4 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.181× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 25.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -9.1) |
| [[Hs 766T (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0226× (z -18.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.101× (z -9.7) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 29.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.177× (z -10.6) |
| [[RKO (line)]] | wt | 16.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.152× (z -9.3) |
| [[SNU-1 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0635× (z -9.1) ⚠ transcription drop |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -10.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 20.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.154× (z -10.7) |
| [[A498 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10210), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB30-DT]] | +0.81 | +0.84 / +0.63 | both halves | 7e-06 |  |
| [[MZF1-AS1]] | +0.81 | +0.82 / +0.60 | both halves | 7e-06 |  |
| [[PPP3CB-AS1]] | +0.81 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.81 | +0.86 / +0.50 | both halves | 1e-05 |  |
| [[LINC02340]] | +0.81 | +0.86 / +0.60 | both halves | 7e-06 |  |
| [[GABPB2]] | +0.80 | +0.83 / +0.55 | both halves | 1e-05 |  |
| [[PDCL3P4]] | +0.79 | +0.87 / +0.55 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.79 | +0.83 / +0.51 | both halves | 1e-05 |  |
| [[AK9]] | +0.79 | +0.83 / +0.51 | both halves | 1e-05 |  |
| [[BCDIN3D]] | +0.79 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.78 | +0.81 / +0.55 | both halves | 1e-05 |  |
| [[ZNF407-AS1]] | +0.77 | +0.84 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3R2]] | -0.74 | -0.71 / -0.65 | both halves | 7e-06 |  |
| [[AP1S1]] | -0.72 | -0.80 / -0.37 | both halves | 8e-05 |  |
| [[FAM118A]] | -0.72 | -0.72 / -0.42 | both halves | 4e-05 |  |
| [[GNA12]] | -0.71 | -0.75 / -0.41 | both halves | 4e-05 |  |
| [[IGSF8]] | -0.70 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[LPCAT4]] | -0.70 | -0.73 / -0.45 | both halves | 3e-05 |  |
| [[L2HGDH]] | -0.70 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[SHQ1]] | -0.68 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[MAST3]] | -0.68 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[RPA1]] | -0.68 | -0.72 / -0.58 | both halves | 8e-06 |  |
| [[AP3M2]] | -0.67 | -0.66 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LACC1]] | B | LACC1 activity raises KRCC1's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.67× lower at baseline in the lines without LACC1 | 0.035 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[TOP2A]] | B | TOP2A activity lowers KRCC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.799). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.8, 13.6); signed map (26.5, -11.0). **Vector** length 117, 38.5% of its response variance represented; |z| ≥ 3 in 1,316 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +13.5 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +12.3 | +4.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.6 | +4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +10.5 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +9.0 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.9 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +3.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -8.3 | -11.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.7 | -11.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.3 | -12.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.5 | -4.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.9 | -4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.8 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | -3.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -3.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | lysine rich coiled-coil 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:88,027,205-88,064,252 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22333 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPI7](https://www.uniprot.org/uniprotkb/Q9NPI7) (Lysine-rich coiled-coil protein 1):

> Regulates CHEK1-mediated cell cycle checkpoint. Facilitates efficient recombination and homologous recombination repair. Required for proper S-phase progression and mitotic entry.

**Summary**, from NCBI Gene [51315](https://www.ncbi.nlm.nih.gov/gene/51315):

> Predicted to be involved in DNA damage response. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28039](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28039) · Entrez [51315](https://www.ncbi.nlm.nih.gov/gene/51315) · UniProt [Q9NPI7](https://www.uniprot.org/uniprotkb/Q9NPI7) · Ensembl [ENSG00000172086](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172086)

## Data

Gene col 10210: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10210); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10210, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10210]; `tensor/DDL_lfc|DDL_z.npy` [10210]; `embed/gene_vectors.npy` [10210]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10210 or target_col == 10210). Every well: [[KRCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
