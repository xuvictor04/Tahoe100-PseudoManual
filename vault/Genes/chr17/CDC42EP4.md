---
symbol: "CDC42EP4"
type: "gene"
col: 11048
ensembl_id: "ENSG00000179604"
name: "CDC42 effector protein 4"
location: "17q25.1"
module: 4
arm: "-"
pooled_cpm: 27.69
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CDC42EP4

*CDC42 effector protein 4* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +12.7, q 2e-34, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.436× (z -16.6, q 0e+00, down in 44 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.451× (z -8.3, q 1e-14, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMIZ1]] (+0.63, fdr 1e-05), [[TLE3]] (+0.61, fdr 3e-05), [[TFEB]] (+0.60, fdr 1e-05); moves opposite to [[ZNF202]] (-0.55, fdr 3e-05), [[GNL3L]] (-0.53, fdr 3e-05), [[TAF2]] (-0.53, fdr 2e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11048.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +12.7 | 2e-34 | 35/44 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +7.8 | 1e-12 | 25/46 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +7.7 | 3e-12 | 29/45 (J82, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +6.8 | 1e-09 | 22/43 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +6.5 | 1e-08 | 24/47 (SW1417, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.3 | 0.002 | 15/47 (NCI-H2347, SW480, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.009 | 9/47 (SW1417, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.015 | 10/47 (HCT15, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.20× | +3.6 | 0.020 | 8/47 (SW480, SHP-77, …) | all doses, flat |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.19× | +3.4 | 0.045 | 8/47 (A498, HT-29, …) | top dose only | plate-row cell shift |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.3 | 0.046 | 7/46 (Hs 766T, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.046 | 14/47 (SW1417, Panc 03.27, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.17× | +3.2 | 0.057 | 15/47 (NCI-H2347, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11048.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.436×** | -16.6 | 0e+00 | 44/47 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -12.0 | 6e-31 | 26/34 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.560×** | -11.6 | 9e-29 | 32/40 (Hs 766T, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.578×** | -10.1 | 6e-22 | 28/37 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.451×** | -8.3 | 1e-14 | 33/46 (SK-MEL-2, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.454×** | -8.3 | 1e-14 | 31/45 (LoVo, PANC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.485×** | -7.6 | 3e-12 | 29/45 (KATO III, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.492×** | -7.4 | 8e-12 | 29/45 (KATO III, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.706×** | -5.0 | 4e-05 | 19/47 (KATO III, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.634×** | -4.8 | 1e-04 | 16/43 (SW1417, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.643×** | -4.6 | 2e-04 | 16/47 (LOX-IMVI, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.852× | -4.5 | 3e-04 | 19/47 (Panc 03.27, A549, …) | rises with dose | low cells (technical?) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.732×** | -4.5 | 4e-04 | 13/47 (LoVo, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.821×** | -4.0 | 0.003 | 11/47 (Panc 03.27, COLO 205, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.823×** | -3.9 | 0.004 | 11/46 (AsPC-1, SW 900, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.814×** | -3.9 | 0.004 | 11/46 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.823×** | -3.7 | 0.006 | 13/46 (AsPC-1, Panc 03.27, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.774×** | -3.7 | 0.007 | 15/47 (HCT15, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.834× | -3.6 | 0.007 | 15/45 (LS 180, NCI-H1792, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.828×** | -3.6 | 0.007 | 14/46 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.880× | -3.6 | 0.007 | 10/47 (NCI-H1792, LS 180, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11048. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 66.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -17.4) |
| [[A498 (line)]] | wt | 48.6 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -10.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 28.2 | 3 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 7.07× (z +17.1) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.386× (z -8.7) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 38.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -12.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 46.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -13.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 32.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 30.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -13.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 27.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0948× (z -19.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 30.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -13.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 23.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 28.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -10.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 26.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 37.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -13.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 26.7 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0806× (z -9.5) |
| [[CHP-212 (line)]] | wt | 83.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0436× (z -16.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 42.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.284× (z -8.5) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.145× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[HS-578T (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -10.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0819× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +9.7) | — |
| [[RKO (line)]] | wt | 8.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 0 | 1 | — | [[Abemaciclib (drug)]] 5 µM 0.0389× (z -11.5) |
| [[SNU-423 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -8.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 22.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.4) | — |
| [[A-427 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11048), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMIZ1]] | +0.63 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[TLE3]] | +0.61 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[TFEB]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[GPRC5C]] | +0.58 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[SSBP3]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ING1]] | +0.56 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[EFNB1]] | +0.54 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[GATA2]] | +0.54 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[GRB7]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.53 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[TESK2]] | +0.52 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[YPEL2]] | +0.51 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF202]] | -0.55 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[GNL3L]] | -0.53 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[TAF2]] | -0.53 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[AGK]] | -0.53 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[DNAJC24]] | -0.52 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[COMMD10]] | -0.52 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[LDAH]] | -0.52 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[PTPN11]] | -0.52 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[MRRF]] | -0.52 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[COMT]] | -0.51 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[SUCLG2]] | -0.51 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[PUM3]] | -0.51 | -0.41 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CDC42EP4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZMIZ1]] | C | ZMIZ1 activity raises CDC42EP4's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 2.63× lower at baseline in the lines without ZMIZ1 | 0.024 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.8, 31.9); signed map (-4.1, 27.0). **Vector** length 103, 23.3% of its response variance represented; |z| ≥ 3 in 1,006 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +12.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.0 | +6.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.0 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +2.3 | +2.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.7 | +3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.2 | -16.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.6 | -8.3 |
|  | [[EX229 (drug)]] 5 µM |  | -5.4 | -7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | -11.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.0 | -7.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.6 | -8.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.5 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | CDC42 effector protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:73,283,624-73,312,005 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CEP4, KAIA1777, BORG4, MGC3740, MGC17125 |
| Gene groups (HGNC) | CDC42 effector proteins |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 7 pathways, smallest: RHOQ GTPase cycle; RAC2 GTPase cycle; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3Q1](https://www.uniprot.org/uniprotkb/Q9H3Q1) (Cdc42 effector protein 4):

> Probably involved in the organization of the actin cytoskeleton. May act downstream of CDC42 to induce actin filament assembly leading to cell shape changes. Induces pseudopodia formation, when overexpressed in fibroblasts.

**Summary**, from NCBI Gene [23580](https://www.ncbi.nlm.nih.gov/gene/23580):

> The product of this gene is a member of the CDC42-binding protein family. Members of this family interact with Rho family GTPases and regulate the organization of the actin cytoskeleton. This protein has been shown to bind both CDC42 and TC10 GTPases in a GTP-dependent manner. When overexpressed in fibroblasts, this protein was able to induce pseudopodia formation, which suggested a role in inducing actin filament assembly and cell shape control. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17147](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17147) · Entrez [23580](https://www.ncbi.nlm.nih.gov/gene/23580) · UniProt [Q9H3Q1](https://www.uniprot.org/uniprotkb/Q9H3Q1) · Ensembl [ENSG00000179604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179604)

## Data

Gene col 11048: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11048); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11048, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11048]; `tensor/DDL_lfc|DDL_z.npy` [11048]; `embed/gene_vectors.npy` [11048]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11048 or target_col == 11048). Every well: [[CDC42EP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC42EP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
