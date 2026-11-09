---
symbol: "ABTB1"
type: "gene"
col: 3567
ensembl_id: "ENSG00000114626"
name: "ankyrin repeat and BTB domain containing 1"
location: "3q21.3"
module: 76
arm: "+"
pooled_cpm: 6.4
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 50
n_dd_up_clean: 12
n_dd_down_clean: 42
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# ABTB1

*ankyrin repeat and BTB domain containing 1* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[GSK1059615 (drug)]] 0.5 µM: 2.25× (z +5.8, q 4e-06, up in 21 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.128× (z -20.6, q 0e+00, down in 45 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.273× (z -18.4, q 0e+00, down in 38 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOB2]] (+0.76, fdr 7e-06), [[SPSB3]] (+0.71, fdr 1e-05), [[MTMR14]] (+0.71, fdr 7e-06); moves opposite to [[MEIS2]] (-0.59, fdr 2e-05), [[SNX5]] (-0.58, fdr 3e-05), [[MYLK-AS1]] (-0.57, fdr 2e-04).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[REPS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3567.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.25×** | +5.8 | 4e-06 | 21/38 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[DTP3 (drug)]] 5 µM |  | **2.34×** | +4.3 | 0.004 | 15/34 (J82, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.52×** | +3.9 | 0.015 | 8/46 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Rapamycin (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.019 | 12/46 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.022 | 12/37 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[4EGI-1 (drug)]] 5 µM |  | **1.97×** | +3.5 | 0.048 | 7/33 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.40×** | +3.3 | 0.062 | 10/45 (PANC-1, HS-578T, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.062 | 11/45 (PANC-1, Panc 03.27, …) | all doses, flat |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.063 | 6/40 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.063 | 10/37 (RKO, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.57×** | +3.2 | 0.068 | 6/32 (HT-29, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.073 | 8/43 (HT-29, SW48, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.53× | +3.0 | 0.10 | 5/34 (HOP62, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Larotrectinib sulfate (drug)]] 5 µM | ⚠ unreliable plate only | 1.35× | +3.0 | 0.10 | 9/46 (PANC-1, HEC-1-A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3567.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.128×** | -20.6 | 0e+00 | 45/46 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.273×** | -18.4 | 0e+00 | 38/38 (J82, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.246×** | -14.1 | 1e-42 | 43/47 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.294×** | -12.3 | 2e-32 | 34/38 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.312×** | -11.7 | 2e-29 | 32/36 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.302×** | -11.5 | 7e-29 | 37/44 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.337×** | -10.9 | 1e-25 | 35/42 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.465×** | -10.9 | 1e-25 | 32/40 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.180×** | -8.8 | 1e-16 | 34/39 (NCI-H23, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.314×** | -8.3 | 6e-15 | 34/47 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.209×** | -8.0 | 7e-14 | 30/41 (J82, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.431×** | -8.0 | 7e-14 | 33/43 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.221×** | -7.7 | 6e-13 | 33/36 (KATO III, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.476×** | -7.4 | 4e-12 | 31/43 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[EX229 (drug)]] 5 µM |  | **0.266×** | -6.8 | 5e-10 | 28/34 (SW480, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.275×** | -6.6 | 1e-09 | 28/42 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.518×** | -6.6 | 1e-09 | 27/45 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3567. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 10.9 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0641× (z -19.4) |
| [[AsPC-1 (line)]] | alt | 16.6 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0916× (z -18.0) |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -13.9) |
| [[PANC-1 (line)]] | alt | 3.32 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0565× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.184× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 8.24 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -13.5) |
| [[KATO III (line)]] | alt | 16.2 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0965× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0212× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 9.68 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0299× (z -15.2) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 7.87 | 0 | 4 | — | [[Digitoxin (drug)]] 0.5 µM 0.0282× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 3.04 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0719× (z -10.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.175× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -13.5) |
| [[HS-578T (line)]] | alt | 7.94 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0620× (z -12.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.164× (z -11.5) |
| [[HT-29 (line)]] | alt | 6.07 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0647× (z -10.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.185× (z -9.3) |
| [[LoVo (line)]] | wt | 7.07 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0568× (z -14.1) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 6.27 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0463× (z -11.3) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.0595× (z -10.0) |
| [[SW480 (line)]] | alt | 4.05 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -15.3) |
| [[A-172 (line)]] | wt | 7.30 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0927× (z -10.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.232× (z -8.7) |
| [[A498 (line)]] | wt | 4.00 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0729× (z -11.2) |
| [[A549 (line)]] | wt | 6.93 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0970× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 5.12 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -8.5) |
| [[HOP62 (line)]] | alt | 5.68 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0669× (z -17.0) |
| [[Hs 766T (line)]] | wt | 7.19 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 5.27 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 6.92 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0745× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 4.19 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0618× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.163× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0654× (z -12.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.189× (z -10.7) |
| [[SW 900 (line)]] | alt | 4.66 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -9.1) |
| [[RKO (line)]] | wt | 3.29 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0373× (z -9.1) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 8.63 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0567× (z -11.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 5.97 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0964× (z -9.8) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 8.53 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0512× (z -9.4) |
| [[A-427 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3567), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB2]] | +0.76 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.71 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[MTMR14]] | +0.71 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[INPP5K]] | +0.70 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[CCNDBP1]] | +0.68 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[HDAC11]] | +0.67 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.66 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ATG2A]] | +0.66 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[WIPI2]] | +0.66 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[CRIPT]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[YPEL3]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 | STRING 540 |
| [[MARF1]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEIS2]] | -0.59 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SNX5]] | -0.58 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[MYLK-AS1]] | -0.57 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[ZNF827]] | -0.56 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[AFG1L]] | -0.53 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[MBNL3]] | -0.52 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[GTF2I]] | -0.52 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[NAALADL2]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[FUBP1]] | -0.51 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[PLCH1]] | -0.51 | -0.52 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[REPS2]] | B | REPS2 activity raises ABTB1's level | lines that do not express REPS2 (12) vs lines expressing it (38) | 1.57× lower at baseline in the lines without REPS2 | 0.024 | ⚠ within organs, on part of the lines; also absent: GALNT9, ENSG00000227486, PLPP2; maybe low, not absent |
| [[MTOR]] | B | MTOR activity lowers ABTB1's level | compounds that target MTOR: 4 of 8 raise it (GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 50% of the class's compounds vs 2.8% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AHNAK2]] | B | AHNAK2 activity raises ABTB1's level | lines that do not express AHNAK2 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without AHNAK2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CAV1, CAV2, ITGA2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ABTB1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.8% of all compounds | 0.038 | ⚠ off-target possible; 4 compounds |
| [[TOP2A]] | B | TOP2A activity raises ABTB1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.4, -44.3); signed map (-20.0, 11.8). **Vector** length 94.1, 22.3% of its response variance represented; |z| ≥ 3 in 1,286 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | +2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | -0.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +2.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.7 | +3.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.6 | +5.8 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[DTP3 (drug)]] 5 µM |  | +2.3 | +4.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.1 | -20.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.0 | -8.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.6 | -5.6 |
|  | [[EX229 (drug)]] 5 µM |  | -6.3 | -6.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.9 | -7.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.2 | -8.0 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and BTB domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:127,672,935-127,680,926 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BPOZ, EF1ABP, Btb3, BTBD21, BPOZ-2 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969K4](https://www.uniprot.org/uniprotkb/Q969K4) (Ankyrin repeat and BTB/POZ domain-containing protein 1):

> May act as a mediator of the PTEN growth-suppressive signaling pathway. May play a role in developmental processes.

**Summary**, from NCBI Gene [80325](https://www.ncbi.nlm.nih.gov/gene/80325):

> This gene encodes a protein with an ankyrin repeat region and two BTB/POZ domains, which are thought to be involved in protein-protein interactions. Expression of this gene is activated by the phosphatase and tensin homolog, a tumor suppressor. Alternate splicing results in three transcript variants. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:18275](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18275) · Entrez [80325](https://www.ncbi.nlm.nih.gov/gene/80325) · UniProt [Q969K4](https://www.uniprot.org/uniprotkb/Q969K4) · Ensembl [ENSG00000114626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114626)

## Data

Gene col 3567: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3567); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3567, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3567]; `tensor/DDL_lfc|DDL_z.npy` [3567]; `embed/gene_vectors.npy` [3567]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3567 or target_col == 3567). Every well: [[ABTB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABTB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
