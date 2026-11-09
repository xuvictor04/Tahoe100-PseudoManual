---
symbol: "SH3BGRL"
type: "gene"
col: 5181
ensembl_id: "ENSG00000131171"
name: "SH3 domain binding glutamate rich protein like"
location: "Xq21.1"
module: 29
arm: "+"
pooled_cpm: 47.62
n_lines_expressing: 46
n_dd_up: 20
n_dd_down: 36
n_dd_up_clean: 15
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# SH3BGRL

*SH3 domain binding glutamate rich protein like* — Xq21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.19× (z +16.2, q 0e+00, up in 37 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.44× (z +7.3, q 4e-11, up in 31 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.375× (z -28.6, q 0e+00, down in 41 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCP2]] (+0.75, fdr 7e-06), [[SCARB2]] (+0.71, fdr 7e-06), [[TSPAN6]] (+0.70, fdr 7e-06); moves opposite to [[MPP3]] (-0.60, fdr 1e-05), [[PLEKHN1]] (-0.60, fdr 1e-05), [[ZXDC]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 4 go from it, the strongest it → [[DECR1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5181.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +16.2 | 0e+00 | 37/43 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +14.4 | 7e-45 | 33/37 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +11.2 | 6e-27 | 32/41 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +7.3 | 4e-11 | 31/43 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.89×** | +6.8 | 9e-10 | 34/43 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +6.8 | 9e-10 | 24/44 (LS 180, KATO III, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +6.4 | 1e-08 | 32/44 (HOP62, KATO III, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +6.2 | 4e-08 | 26/44 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +5.8 | 5e-07 | 25/44 (Hs 766T, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +5.4 | 3e-06 | 25/44 (LS 180, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +5.4 | 3e-06 | 24/43 (C32, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +5.2 | 9e-06 | 23/44 (SK-MEL-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +5.0 | 3e-05 | 15/44 (SW480, C32, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.29×** | +5.0 | 3e-05 | 22/44 (Hs 766T, C32, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +4.8 | 8e-05 | 14/44 (AsPC-1, C32, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +4.7 | 8e-05 | 18/44 (SK-MEL-2, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 1e-04 | 19/44 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.001 | 17/44 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5181.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.375×** | -28.6 | 0e+00 | 41/44 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.381×** | -19.9 | 0e+00 | 38/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.532×** | -13.0 | 2e-36 | 37/44 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.535×** | -12.9 | 7e-36 | 37/44 (SW480, SW 1088, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.551×** | -11.8 | 3e-30 | 37/44 (NCI-H460, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.572×** | -11.5 | 1e-28 | 38/44 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.579×** | -10.6 | 2e-24 | 34/44 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.613×** | -10.1 | 5e-22 | 34/44 (SW480, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.641×** | -9.1 | 4e-18 | 34/44 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.644×** | -9.1 | 7e-18 | 29/44 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.662×** | -8.5 | 9e-16 | 35/44 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -8.3 | 6e-15 | 24/44 (CHP-212, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.669×** | -8.3 | 6e-15 | 29/44 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.685×** | -7.8 | 3e-13 | 26/44 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.694×** | -7.5 | 2e-12 | 29/44 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.698×** | -7.4 | 4e-12 | 27/44 (NCI-H460, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.701×** | -7.3 | 8e-12 | 27/44 (KATO III, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5181. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 68.5 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -32.1) |
| [[SW480 (line)]] | alt | 50.4 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -14.6) |
| [[PANC-1 (line)]] | alt | 79.9 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +14.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -19.9) |
| [[Hs 766T (line)]] | wt | 84.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 69.9 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -22.7) |
| [[SNU-423 (line)]] | alt | 103 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -19.0) |
| [[AN3 CA (line)]] | alt | 138 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.140× (z -13.6) |
| [[HOP62 (line)]] | alt | 54.9 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -15.2) |
| [[SHP-77 (line)]] | alt | 45.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -14.3) |
| [[SK-MEL-2 (line)]] | alt | 98.4 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -11.8) |
| [[A498 (line)]] | wt | 33.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.6) |
| [[A549 (line)]] | wt | 58.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -17.2) |
| [[H4 (line)]] | wt | 63.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -20.3) |
| [[LS 180 (line)]] | wt | 54.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 25.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.83× (z +12.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 47.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -18.0) |
| [[C32 (line)]] | wt | 51.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 40.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 59.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 31.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -13.6) |
| [[KATO III (line)]] | alt | 43.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -14.1) |
| [[LoVo (line)]] | wt | 14.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.13× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 80.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 59.2 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.333× (z -10.6) |
| [[A-427 (line)]] | wt | 57.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.360× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 22.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -8.7) |
| [[COLO 205 (line)]] | alt | 34.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.5) |
| [[HS-578T (line)]] | alt | 27.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +10.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 45.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -11.3) |
| [[RKO (line)]] | wt | 51.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -9.4) |
| [[SW 900 (line)]] | alt | 43.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -14.9) |
| [[A-172 (line)]] | wt | 32.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -12.4) |
| [[CHP-212 (line)]] | wt | 68.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -12.8) |
| [[HCT15 (line)]] | alt | 39.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 48.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -12.0) |
| [[SNU-1 (line)]] | wt | 52.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -8.8) |
| [[SW 1088 (line)]] | alt | 87.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0603× (z -10.5) |
| [[SW 1271 (line)]] | alt | 43.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0600× (z -8.7) |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 53.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5181), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCP2]] | +0.75 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[SCARB2]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[TSPAN6]] | +0.70 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ATRAID]] | +0.67 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ITM2B]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PRDX3]] | +0.65 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[PPT1]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[MANEA]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[LANCL1]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[PON2]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[NNT]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[TMEM123]] | +0.62 | +0.49 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP3]] | -0.60 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[PLEKHN1]] | -0.60 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[ZXDC]] | -0.58 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[BCAR1]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[FAM131A]] | -0.57 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[CLCF1]] | -0.57 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[GAN]] | -0.56 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[KCTD5]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[FBXL18]] | -0.56 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[RRP7A]] | -0.56 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ORAI1]] | -0.56 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[RDH13]] | -0.56 | -0.45 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers SH3BGRL's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[RHOBTB3]] | B | RHOBTB3 activity raises SH3BGRL's level | lines that do not express RHOBTB3 (10) vs lines expressing it (40) | 1.66× lower at baseline in the lines without RHOBTB3 | 0.071 | ⚠ within organs, on part of the lines; also absent: FYN, POGLUT3; maybe low, not absent |
| [[NNT]] | B | NNT activity raises SH3BGRL's level | lines that do not express NNT (6) vs lines expressing it (44) | 2.05× lower at baseline in the lines without NNT | 0.093 | ⚠ within organs, on part of the lines; co-absent genes |
| [[HMGN5]] | C | HMGN5 activity raises SH3BGRL's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 4.16× lower at baseline in the lines without HMGN5 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DECR1]] | C | SH3BGRL activity raises DECR1's level | lines that do not express SH3BGRL (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without SH3BGRL | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HMGN5, HIPK2, ATP10D |
| [[KLF16]] | C | SH3BGRL activity lowers KLF16's level | lines that do not express SH3BGRL (4) vs lines expressing it (46) | 1.50× higher at baseline in the lines without SH3BGRL | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HMGN5, HIPK2, ATP10D |
| [[HMGN5]] | C | SH3BGRL activity raises HMGN5's level | lines that do not express SH3BGRL (4) vs lines expressing it (46) | 3.65× lower at baseline in the lines without SH3BGRL | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HMGN5, HIPK2, ATP10D; co-absent with the target |
| [[EIF5B]] | C | SH3BGRL activity lowers EIF5B's level | lines that do not express SH3BGRL (4) vs lines expressing it (46) | 1.53× higher at baseline in the lines without SH3BGRL | 0.054 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HMGN5, HIPK2, ATP10D |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.2, -19.8); signed map (-21.5, -39.8). **Vector** length 106, 30.9% of its response variance represented; |z| ≥ 3 in 1,380 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.9 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +16.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +11.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.4 | +7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +5.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.0 | +5.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -7.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.3 | -7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -7.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.7 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain binding glutamate rich protein like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.1 — chrX:81,202,102-81,298,547 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC117402 |
| Matched by | ensembl_id |

**Function**, from UniProt [O75368](https://www.uniprot.org/uniprotkb/O75368) (Adapter SH3BGRL):

> Appears to function as an adapter protein that bridges proteins together or proteins with mRNAs. May function as a ubiquitin ligase-substrate adapter. Additionally, associates with translating cytoplasmic ribosomes and may promote the expression of specific mRNAs.

**Summary**, from NCBI Gene [6451](https://www.ncbi.nlm.nih.gov/gene/6451):

> Enables protein-RNA adaptor activity and ubiquitin-like ligase-substrate adaptor activity. Involved in positive regulation of cytoplasmic translational initiation and proteasome-mediated ubiquitin-dependent protein catabolic process. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10823](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10823) · Entrez [6451](https://www.ncbi.nlm.nih.gov/gene/6451) · UniProt [O75368](https://www.uniprot.org/uniprotkb/O75368) · Ensembl [ENSG00000131171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131171)

## Data

Gene col 5181: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5181); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5181, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5181]; `tensor/DDL_lfc|DDL_z.npy` [5181]; `embed/gene_vectors.npy` [5181]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5181 or target_col == 5181). Every well: [[SH3BGRL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3BGRL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
