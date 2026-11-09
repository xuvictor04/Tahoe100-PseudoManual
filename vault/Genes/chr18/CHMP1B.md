---
symbol: "CHMP1B"
type: "gene"
col: 14917
ensembl_id: "ENSG00000255112"
name: "charged multivesicular body protein 1B"
location: "18p11.21"
module: 74
arm: "+"
pooled_cpm: 51.36
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 10
n_dd_up_clean: 19
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# CHMP1B

*charged multivesicular body protein 1B* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.87× (z +10.6, q 2e-23, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.489× (z -12.1, q 5e-31, down in 44 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.468× (z -6.7, q 4e-09, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPH2]] (+0.57, fdr 7e-06), [[CDKN2B]] (+0.57, fdr 1e-05), [[SLU7]] (+0.56, fdr 9e-05); moves opposite to [[NFXL1]] (-0.60, fdr 2e-05), [[ZYG11A]] (-0.58, fdr 5e-05), [[EEF2K]] (-0.56, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14917.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.87×** | +10.6 | 2e-23 | 42/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.91×** | +10.5 | 2e-23 | 36/48 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +9.8 | 3e-20 | 40/48 (A-172, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +9.7 | 3e-20 | 37/45 (AsPC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +8.9 | 9e-17 | 39/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +8.7 | 3e-16 | 39/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +8.3 | 1e-14 | 32/42 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.41×** | +8.2 | 1e-14 | 28/47 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +7.5 | 4e-12 | 41/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +7.4 | 6e-12 | 38/47 (HOP62, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +6.2 | 3e-08 | 29/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +5.9 | 2e-07 | 29/47 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +5.8 | 2e-07 | 33/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.43×** | +5.8 | 3e-07 | 27/42 (HEC-1-A, NCI-H1792, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.38×** | +5.5 | 1e-06 | 26/46 (HOP62, Hs 766T, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.41×** | +5.4 | 3e-06 | 28/47 (hTERT-HPNE, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.70×** | +4.7 | 7e-05 | 27/49 (SK-MEL-2, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.6 | 2e-04 | 17/48 (BT-474, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +4.5 | 2e-04 | 21/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +4.2 | 8e-04 | 22/49 (NCI-H460, LOX-IMVI, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +4.1 | 0.001 | 19/48 (HOP62, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14917.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.489×** | -12.1 | 5e-31 | 44/48 (LOX-IMVI, SW480, …) | all doses, flat | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.468×** | -6.7 | 4e-09 | 35/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.469×** | -6.7 | 4e-09 | 37/48 (NCI-H460, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.473×** | -6.6 | 5e-09 | 36/47 (KATO III, CHP-212, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.489×** | -6.3 | 3e-08 | 39/47 (NCI-H2347, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.515×** | -5.9 | 4e-07 | 26/48 (NCI-H1573, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.602×** | -5.4 | 5e-06 | 33/48 (NCI-H460, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.774×** | -4.1 | 0.003 | 23/48 (LoVo, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 5 µM |  | **0.679×** | -3.4 | 0.038 | 13/48 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **0.811×** | -3.4 | 0.045 | 19/47 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.881× | -3.0 | 0.12 | 15/48 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 129 | 10 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.60× (z +14.9) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Selinexor (drug)]] 5 µM 2.33× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 68.2 | 7 (6 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.44× (z +12.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.33× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.295× (z -12.3) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 50.0 | 7 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.56× (z +14.4) | — |
| [[AsPC-1 (line)]] | alt | 49.9 | 5 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.93× (z +12.4) | — |
| [[SK-MEL-2 (line)]] | alt | 50.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +15.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.56× (z +13.7) | — |
| [[SW480 (line)]] | alt | 54.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.362× (z -12.9) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 26.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +13.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.88× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 37.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 52.3 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.91× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 71.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +14.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.87× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 23.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +9.0) ⚠ toxic; transcription drop | [[Pimozide (drug)]] 0.5 µM 0.189× (z -8.7) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 43.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.8) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.23× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 70.2 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.55× (z +9.6) | — |
| [[J82 (line)]] | alt | 36.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.13× (z +8.9) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.295× (z -10.3) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 49.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.2) ⚠ cell-cycle shift, explains ~49% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.377× (z -8.8) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 76.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 49.8 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.86× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 56.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.309× (z -8.7) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 91.4 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.71× (z +8.7) | — |
| [[KATO III (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.337× (z -10.3) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 53.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.253× (z -13.1) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 53.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.08× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.258× (z -11.0) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 48.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.409× (z -9.7) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 52.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.3) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SNU-423 (line)]] | alt | 40.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +8.7) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[A-427 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPH2]] | +0.57 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CDKN2B]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[SLU7]] | +0.56 | +0.37 / +0.65 | both halves | 9e-05 |  |
| [[ZBTB20]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[NBR1]] | +0.55 | +0.36 / +0.67 | both halves | 1e-04 |  |
| [[GABARAPL1]] | +0.55 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[NR3C1]] | +0.55 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[OTUD1]] | +0.54 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[MAFK]] | +0.54 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[SDAD1P1]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[RB1CC1]] | +0.53 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[PNRC2]] | +0.52 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFXL1]] | -0.60 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[ZYG11A]] | -0.58 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[EEF2K]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[IQCB1]] | -0.55 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[GLMN]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[L2HGDH]] | -0.53 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[NOD1]] | -0.53 | -0.62 / -0.38 | both halves | 7e-05 |  |
| [[GPR180]] | -0.53 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[PDIA5]] | -0.53 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[MYO19]] | -0.52 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[NAA35]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[GK5]] | -0.51 | -0.57 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.471). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.4, -32.6); signed map (-8.4, 12.4). **Vector** length 106, 28.6% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +6.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +9.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.3 | +3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.9 | -12.1 |
|  | [[EX229 (drug)]] 5 µM |  | -7.3 | -6.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.7 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.4 | -5.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.3 | -6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.2 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | charged multivesicular body protein 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:11,851,413-11,854,444 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CHMP1.5, C18orf2, Vps46B |
| Gene groups (HGNC) | Charged multivesicular body proteins; ESCRT-III associated factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7LBR1](https://www.uniprot.org/uniprotkb/Q7LBR1) (Charged multivesicular body protein 1b):

> Probable peripherally associated component of the endosomal sorting required for transport complex III (ESCRT-III) which is involved in multivesicular bodies (MVBs) formation and sorting of endosomal cargo proteins into MVBs. MVBs contain intraluminal vesicles (ILVs) that are generated by invagination and scission from the limiting membrane of the endosome and mostly are delivered to lysosomes enabling degradation of membrane proteins, such as stimulated growth factor receptors, lysosomal …

**Summary**, from NCBI Gene [57132](https://www.ncbi.nlm.nih.gov/gene/57132):

> CHMP1B belongs to the chromatin-modifying protein/charged multivesicular body protein (CHMP) family. These proteins are components of ESCRT-III (endosomal sorting complex required for transport III), a complex involved in degradation of surface receptor proteins and formation of endocytic multivesicular bodies (MVBs). Some CHMPs have both nuclear and cytoplasmic/vesicular distributions, and one such CHMP, CHMP1A (MIM 164010), is required for both MVB formation and regulation of cell cycle …

**Accessions** — [HGNC:24287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24287) · Entrez [57132](https://www.ncbi.nlm.nih.gov/gene/57132) · UniProt [Q7LBR1](https://www.uniprot.org/uniprotkb/Q7LBR1) · Ensembl [ENSG00000255112](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255112)

## Data

Gene col 14917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14917); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14917]; `tensor/DDL_lfc|DDL_z.npy` [14917]; `embed/gene_vectors.npy` [14917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14917 or target_col == 14917). Every well: [[CHMP1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHMP1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
