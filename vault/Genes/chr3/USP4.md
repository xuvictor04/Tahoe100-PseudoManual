---
symbol: "USP4"
type: "gene"
col: 3539
ensembl_id: "ENSG00000114316"
name: "ubiquitin specific peptidase 4"
location: "3p21.31"
module: 129
arm: "+"
pooled_cpm: 70.35
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# USP4

*ubiquitin specific peptidase 4* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.27× (z +6.6, q 2e-08, up in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~17% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.24× (z +5.8, q 2e-06, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.588× (z -20.5, q 0e+00, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTRES1]] (+0.66, fdr 2e-05), [[TECPR1]] (+0.60, fdr 2e-05), [[METTL2A]] (+0.60, fdr 3e-05); moves opposite to [[SUMO3]] (-0.60, fdr 2e-05), [[PGRMC1]] (-0.60, fdr 1e-05), [[ITM2B]] (-0.56, fdr 3e-05).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3539.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.27×** | +6.6 | 2e-08 | 24/48 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +5.8 | 2e-06 | 22/48 (SNU-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.17× | +4.1 | 0.009 | 18/47 (SW480, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.7 | 0.035 | 13/48 (LoVo, NCI-H2030, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.13× | +3.2 | 0.13 | 10/48 (Panc 03.27, NCI-H1573, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | 1.12× | +3.1 | 0.19 | 5/48 (CFPAC-1, A498, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.19 | 3/48 (SW480, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.12× | +3.0 | 0.19 | 16/48 (PANC-1, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3539.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.588×** | -20.5 | 0e+00 | 41/49 (SW1417, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.629×** | -12.2 | 7e-32 | 38/48 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -10.7 | 1e-24 | 35/50 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.804×** | -8.4 | 5e-15 | 25/48 (A-427, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.850× | -6.3 | 4e-08 | 19/48 (NCI-H2347, NCI-H1792, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.858× | -5.9 | 3e-07 | 19/48 (SW1417, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.808×** | -5.8 | 4e-07 | 24/48 (RKO, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.810×** | -5.8 | 6e-07 | 24/48 (AsPC-1, A-427, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.825×** | -5.1 | 2e-05 | 21/47 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.845× | -4.6 | 2e-04 | 19/49 (HOP62, AsPC-1, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.799×** | -4.3 | 1e-03 | 19/47 (SNU-1, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.846× | -4.2 | 0.001 | 17/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.850× | -4.1 | 0.002 | 14/48 (HOP62, NCI-H23, …) | all doses, flat |  |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | 0.865× | -4.0 | 0.003 | 13/48 (SNU-423, HEC-1-A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.766×** | -3.8 | 0.005 | 15/44 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.914× | -3.5 | 0.014 | 3/48 (NCI-H2347, NCI-H23, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.882× | -3.4 | 0.016 | 13/47 (A549, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.883× | -3.4 | 0.016 | 15/48 (LS 180, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3539. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 60.8 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.364× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -14.3) |
| [[HOP62 (line)]] | alt | 70.1 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -12.0) |
| [[HS-578T (line)]] | alt | 85.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -15.2) |
| [[J82 (line)]] | alt | 87.0 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -11.8) |
| [[LoVo (line)]] | wt | 64.4 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.482× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 80.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -14.7) |
| [[SW1417 (line)]] | alt | 107 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -17.4) |
| [[SW480 (line)]] | alt | 90.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -14.3) |
| [[A-172 (line)]] | wt | 70.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -9.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -8.7) |
| [[A-427 (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -27.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 75.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 89.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.465× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -8.9) |
| [[LS 180 (line)]] | wt | 65.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -13.4) |
| [[NCI-H23 (line)]] | alt | 82.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -14.3) |
| [[NCI-H2347 (line)]] | alt | 80.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 87.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -12.8) |
| [[A549 (line)]] | wt | 57.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.1) |
| [[C-33 A (line)]] | alt | 72.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 39.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.4) |
| [[HCT15 (line)]] | alt | 77.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HT-29 (line)]] | alt | 50.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 63.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -11.3) |
| [[KATO III (line)]] | alt | 52.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 71.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 60.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 66.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 53.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -8.8) |
| [[NCI-H661 (line)]] | alt | 54.9 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0697× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 93.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -12.1) |
| [[SW 900 (line)]] | alt | 54.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -9.3) |
| [[SW48 (line)]] | wt | 93.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -8.7) |
| [[A498 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 69.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 85.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3539), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTRES1]] | +0.66 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[TECPR1]] | +0.60 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[METTL2A]] | +0.60 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[EIF5B]] | +0.58 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[MTMR9]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[EIF2B3]] | +0.58 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[C3orf62]] | +0.57 | +0.50 / +0.63 | both halves | 1e-05 | ⚠ **readthrough risk**: C3orf62 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[ZNF212]] | +0.57 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[UBE2W]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[REXO4]] | +0.56 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[ZNF696]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[NSUN5]] | +0.55 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[ZC3H18]] | +0.55 | +0.48 / +0.69 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUMO3]] | -0.60 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PGRMC1]] | -0.60 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ITM2B]] | -0.56 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[BCO2]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PLBD1]] | -0.52 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[C5orf15]] | -0.51 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[EEF1A1P5]] | -0.50 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[PRCP]] | -0.50 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[CIAO2A]] | -0.50 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[ANKRD30BL]] | -0.50 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[STT3B]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[GNAS]] | -0.49 | -0.35 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises USP4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CRTAP]] | C | CRTAP activity raises USP4's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.41× lower at baseline in the lines without CRTAP | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.518). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.1, -2.3); signed map (-12.0, -21.3). **Vector** length 105, 24.6% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.7 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | -1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.9 | -3.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +0.8 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.2 | +1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.9 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -20.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -12.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -4.7 | -8.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~1% of this change | -4.6 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -5.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,277,144-49,340,712 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Unph; previously UNP |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 7 pathways, smallest: TNFR1-induced proapoptotic signaling; TNFR1-induced NF-kappa-B signaling pathway; Regulation of TNFR1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13107](https://www.uniprot.org/uniprotkb/Q13107) (Ubiquitin carboxyl-terminal hydrolase 4):

> Deubiquitinating enzyme that removes conjugated ubiquitin from target proteins. Deubiquitinates PDPK1. Deubiquitinates TRIM21. Deubiquitinates receptor ADORA2A which increases the amount of functional receptor at the cell surface. Deubiquitinates HAS2. Deubiquitinates MAVs leading to maintain MAVS protein stability, resulting in increased production of type I interferons (IFN-I) and enhanced antiviral innate immune responses against viral infections. Deubiquitinates RHEB in response to EGF …

**Summary**, from NCBI Gene [7375](https://www.ncbi.nlm.nih.gov/gene/7375):

> The protein encoded by this gene is a protease that deubiquitinates target proteins such as ADORA2A and TRIM21. The encoded protein shuttles between the nucleus and cytoplasm and is involved in maintaining operational fidelity in the endoplasmic reticulum. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:12627](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12627) · Entrez [7375](https://www.ncbi.nlm.nih.gov/gene/7375) · UniProt [Q13107](https://www.uniprot.org/uniprotkb/Q13107) · Ensembl [ENSG00000114316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114316)

## Data

Gene col 3539: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3539); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3539, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3539]; `tensor/DDL_lfc|DDL_z.npy` [3539]; `embed/gene_vectors.npy` [3539]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3539 or target_col == 3539). Every well: [[USP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
