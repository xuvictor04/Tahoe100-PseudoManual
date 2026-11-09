---
symbol: "RIN2"
type: "gene"
col: 5356
ensembl_id: "ENSG00000132669"
name: "Ras and Rab interactor 2"
location: "20p11.23"
module: 120
arm: "+"
pooled_cpm: 127.45
n_lines_expressing: 41
n_dd_up: 3
n_dd_down: 54
n_dd_up_clean: 0
n_dd_down_clean: 41
in_vector_space: true
direction_upstream: 13
direction_downstream: 10
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# RIN2

*Ras and Rab interactor 2* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.86× (z +8.6, q 3e-15, up in 23 of 35 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (J82 4.62×, SW 900 3.80×, HOP62 4.08×, SHP-77 3.54×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (J82 5.41×, SW 900 3.85×, HOP62 3.70×, AsPC-1 3.06×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (J82 3.47×, SW 900 3.33×, HOP62 3.50×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 54 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.238× (z -30.5, q 0e+00, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPM1]] (+0.53, fdr 3e-05), [[AMIGO2]] (+0.51, fdr 3e-05), [[PRSS23]] (+0.51, fdr 4e-05); moves opposite to [[ANK2]] (-0.52, fdr 2e-05), [[LONRF1]] (-0.52, fdr 2e-04), [[PHF20]] (-0.47, fdr 7e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[ATP1B1]] → it (grade B ⚠); 10 go from it, the strongest it → [[PCED1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5356.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (J82 4.62×, SW 900 3.80×, HOP62 4.08×, SHP-77 3.54×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (J82 5.41×, SW 900 3.85×, HOP62 3.70×, AsPC-1 3.06×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (J82 3.47×, SW 900 3.33×, HOP62 3.50×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +8.6 | 3e-15 | 23/35 (J82, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +5.1 | 1e-04 | 19/34 (J82, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.8 | 3e-04 | 19/40 (J82, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | 1.18× | +3.5 | 0.065 | 8/39 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.13 | 12/39 (HS-578T, NCI-H2030, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 1.24× | +3.1 | 0.17 | 15/39 (NCI-H460, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 61 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 54 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5356.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.238×** | -30.5 | 0e+00 | 37/39 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.216×** | -23.0 | 0e+00 | 39/39 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.270×** | -19.7 | 0e+00 | 39/39 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.279×** | -19.2 | 0e+00 | 39/39 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.302×** | -18.0 | 0e+00 | 35/39 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.309×** | -17.6 | 0e+00 | 39/39 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.336×** | -16.4 | 0e+00 | 35/39 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.358×** | -14.8 | 0e+00 | 36/39 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.375×** | -14.7 | 0e+00 | 37/39 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.391×** | -13.3 | 9e-39 | 35/39 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.568×** | -12.0 | 2e-31 | 33/40 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.455×** | -11.8 | 1e-30 | 37/39 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.478×** | -11.1 | 7e-27 | 33/39 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.482×** | -11.0 | 2e-26 | 37/39 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.510×** | -10.1 | 2e-22 | 33/39 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.559×** | -8.7 | 1e-16 | 33/39 (LoVo, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.594×** | -7.2 | 2e-11 | 26/39 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5356. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 222 | 3 (3 ⚠) | 17 (5 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.08× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -24.9) |
| [[PANC-1 (line)]] | alt | 173 | 0 | 20 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -29.2) |
| [[LoVo (line)]] | wt | 233 | 1 (1 ⚠) | 17 (4 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.45× (z +9.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.0643× (z -32.4) |
| [[NCI-H1573 (line)]] | alt | 216 | 0 | 17 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0437× (z -37.3) |
| [[NCI-H460 (line)]] | wt | 130 | 0 | 17 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0886× (z -38.4) |
| [[LS 180 (line)]] | wt | 248 | 0 | 16 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -23.2) |
| [[A549 (line)]] | wt | 413 | 0 | 14 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0375× (z -32.3) |
| [[COLO 205 (line)]] | alt | 174 | 0 | 14 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -30.6) |
| [[SW 900 (line)]] | alt | 149 | 3 (3 ⚠) | 11 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.85× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -19.4) |
| [[H4 (line)]] | wt | 102 | 0 | 13 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.132× (z -14.2) |
| [[HT-29 (line)]] | alt | 166 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -24.7) |
| [[NCI-H23 (line)]] | alt | 42.9 | 0 | 13 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.190× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 136 | 1 (1 ⚠) | 11 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.06× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -15.8) |
| [[CFPAC-1 (line)]] | alt | 310 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0804× (z -33.0) |
| [[Hs 766T (line)]] | wt | 447 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -20.7) |
| [[SNU-423 (line)]] | alt | 114 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -17.1) |
| [[KATO III (line)]] | alt | 220 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -27.5) |
| [[BT-474 (line)]] | alt | 94.8 | 0 | 10 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.167× (z -16.3) |
| [[NCI-H2030 (line)]] | alt | 114 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0684× (z -27.4) |
| [[Panc 03.27 (line)]] | alt | 109 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -21.8) |
| [[A-172 (line)]] | wt | 117 | 0 | 8 | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -14.2) |
| [[J82 (line)]] | alt | 83.9 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 5.41× (z +16.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.247× (z -14.4) |
| [[RPMI-7951 (line)]] | alt | 145 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -23.6) |
| [[HEC-1-A (line)]] | alt | 77.5 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -20.4) |
| [[HepG2_C3A (line)]] | wt | 134 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -19.5) |
| [[hTERT-HPNE (line)]] | wt | 128 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -15.2) |
| [[HS-578T (line)]] | alt | 130 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -16.5) |
| [[A498 (line)]] | wt | 93.8 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.05 µM 2.75× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -10.5) |
| [[SHP-77 (line)]] | alt | 48.5 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 3.54× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.302× (z -10.1) |
| [[AN3 CA (line)]] | alt | 101 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 84.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -16.4) |
| [[SW 1088 (line)]] | alt | 189 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -10.8) |
| [[SW48 (line)]] | wt | 49.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.160× (z -11.8) |
| [[C32 (line)]] | wt | 40.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -12.2) |
| [[SW 1271 (line)]] | alt | 184 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -12.1) |
| [[A-427 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.93 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.0 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 21.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5356), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPM1]] | +0.53 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[AMIGO2]] | +0.51 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[PRSS23]] | +0.51 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[TM4SF18]] | +0.49 | +0.23 / +0.58 | both halves | 5e-04 |  |
| [[F2R]] | +0.48 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[WWTR1]] | +0.48 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[ENC1]] | +0.47 | +0.34 / +0.43 | both halves | 1e-04 |  |
| [[LAMA4]] | +0.47 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[SERPINB9]] | +0.47 | +0.40 / +0.44 | both halves | 4e-05 |  |
| [[LAMC1]] | +0.46 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[F2RL1]] | +0.46 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[CMTM6]] | +0.46 | +0.26 / +0.43 | both halves | 3e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANK2]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[LONRF1]] | -0.52 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[PHF20]] | -0.47 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[FOXO3B]] | -0.46 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[IL17RA]] | -0.45 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[PDCD5]] | -0.45 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[RBM20]] | -0.44 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[AGTPBP1]] | -0.44 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[GTF2IRD1]] | -0.43 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[KANSL3]] | -0.42 | -0.22 / -0.39 | both halves | 6e-04 |  |
| [[NR2C2AP]] | -0.42 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[ANO4]] | -0.41 | -0.44 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP1B1]] | B | ATP1B1 activity raises RIN2's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 3.61× lower at baseline in the lines without ATP1B1 | 0.004 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[PCED1B]] | B | PCED1B activity raises RIN2's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 3.20× lower at baseline in the lines without PCED1B | 0.011 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[AMIGO2]] | B | AMIGO2 activity raises RIN2's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 2.68× lower at baseline in the lines without AMIGO2 | 0.011 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[LXN]] | B | LXN activity raises RIN2's level | lines that do not express LXN (19) vs lines expressing it (31) | 2.48× lower at baseline in the lines without LXN | 0.020 | ⚠ within organs, on part of the lines; also absent: GPX3, CYP4F11, SLPI; maybe low, not absent |
| [[ANK2]] | B | ANK2 activity lowers RIN2's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 2.79× higher at baseline in the lines without ANK2 | 0.023 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[LXN]] | B | LXN activity strengthens RIN2's drug response | lines that do not express LXN (13) vs lines expressing it (26) | the lines without LXN respond 0.74× as strongly (z diff +1.85); strongest at Bortezomib 0.05 µM: 0.55x vs 0.37x (z diff +3.1) | 0.035 | ⚠ within organs, on part of the lines; also absent: GPX3, CYP4F11, SLPI; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TNFRSF21]] | B | TNFRSF21 activity raises RIN2's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 2.16× lower at baseline in the lines without TNFRSF21 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[RAB27B]] | B | RAB27B activity raises RIN2's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 2.85× lower at baseline in the lines without RAB27B | 0.070 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[PMEPA1]] | B | PMEPA1 activity raises RIN2's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 2.27× lower at baseline in the lines without PMEPA1 | 0.087 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[FAM107B]] | B | FAM107B activity raises RIN2's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.23× lower at baseline in the lines without FAM107B | 0.093 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[ITGA3]] | B | ITGA3 activity raises RIN2's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 2.67× lower at baseline in the lines without ITGA3 | 0.099 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[ANTXR2]] | C | ANTXR2 activity raises RIN2's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 4.00× lower at baseline in the lines without ANTXR2 | 0.010 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCED1B]] | B | RIN2 activity raises PCED1B's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 3.10× lower at baseline in the lines without RIN2 | 0.012 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[AMIGO2]] | B | RIN2 activity raises AMIGO2's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 2.57× lower at baseline in the lines without RIN2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[RBM20]] | B | RIN2 activity lowers RBM20's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 4.58× higher at baseline in the lines without RIN2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[ANK2]] | B | RIN2 activity lowers ANK2's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 2.82× higher at baseline in the lines without RIN2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[ATP1B1]] | B | RIN2 activity raises ATP1B1's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 2.27× lower at baseline in the lines without RIN2 | 0.070 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[COL17A1]] | B | RIN2 activity raises COL17A1's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 2.23× lower at baseline in the lines without RIN2 | 0.077 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[LXN]] | B | RIN2 activity raises LXN's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 1.85× lower at baseline in the lines without RIN2 | 0.083 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[TNFRSF21]] | B | RIN2 activity raises TNFRSF21's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 1.73× lower at baseline in the lines without RIN2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[RAB27B]] | B | RIN2 activity raises RAB27B's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 3.28× lower at baseline in the lines without RIN2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[SMAD3]] | B | RIN2 activity raises SMAD3's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 2.45× lower at baseline in the lines without RIN2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.331). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.1, 15.5); signed map (20.7, 42.0). **Vector** length 87.4, 26.8% of its response variance represented; |z| ≥ 3 in 1,598 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +5.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | -6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | -3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Busulfan (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | +1.2 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.0 | -11.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.5 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -5.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.2 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | Ras and Rab interactor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:19,757,606-20,002,457 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RASSF4 |
| Gene groups (HGNC) | VPS9 domain containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYP3](https://www.uniprot.org/uniprotkb/Q8WYP3) (Ras and Rab interactor 2):

> Ras effector protein. May function as an upstream activator and/or downstream effector for RAB5B in endocytic pathway. May function as a guanine nucleotide exchange (GEF) of RAB5B, required for activating the RAB5 proteins by exchanging bound GDP for free GTP.

**Summary**, from NCBI Gene [54453](https://www.ncbi.nlm.nih.gov/gene/54453):

> The RAB5 protein is a small GTPase involved in membrane trafficking in the early endocytic pathway. The protein encoded by this gene binds the GTP-bound form of the RAB5 protein preferentially over the GDP-bound form, and functions as a guanine nucleotide exchange factor for RAB5. The encoded protein is found primarily as a tetramer in the cytoplasm and does not bind other members of the RAB family. Mutations in this gene cause macrocephaly alopecia cutis laxa and scoliosis (MACS) syndrome, an …

**Accessions** — [HGNC:18750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18750) · Entrez [54453](https://www.ncbi.nlm.nih.gov/gene/54453) · UniProt [Q8WYP3](https://www.uniprot.org/uniprotkb/Q8WYP3) · Ensembl [ENSG00000132669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132669)

## Data

Gene col 5356: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5356); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5356, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5356]; `tensor/DDL_lfc|DDL_z.npy` [5356]; `embed/gene_vectors.npy` [5356]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5356 or target_col == 5356). Every well: [[RIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
