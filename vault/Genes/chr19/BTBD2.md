---
symbol: "BTBD2"
type: "gene"
col: 5432
ensembl_id: "ENSG00000133243"
name: "BTB domain containing 2"
location: "19p13.3"
module: 129
arm: "+"
pooled_cpm: 27.27
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# BTBD2

*BTB domain containing 2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 1.30× (z +4.9, q 6e-04, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.414× (z -23.5, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTLL1]] (+0.64, fdr 1e-05), [[KLHL26]] (+0.63, fdr 3e-05), [[SMIM8]] (+0.62, fdr 5e-05); moves opposite to [[PGRMC1]] (-0.61, fdr 1e-05), [[LINC01829]] (-0.56, fdr 1e-04), [[ARSB]] (-0.53, fdr 2e-04).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5432.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.30×** | +4.9 | 6e-04 | 22/47 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +4.8 | 6e-04 | 19/46 (PANC-1, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.3 | 0.004 | 20/43 (RPMI-7951, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.013 | 18/47 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.025 | 11/48 (HOP62, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.025 | 13/48 (KATO III, PANC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.4 | 0.058 | 11/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.066 | 10/47 (Panc 03.27, HS-578T, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.3 | 0.066 | 11/48 (MIA PaCa-2, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.066 | 14/48 (NCI-H2030, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.081 | 15/37 (PANC-1, LOX-IMVI, …) | two highest doses | composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | 1.12× | +3.1 | 0.090 | 11/48 (CFPAC-1, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5432.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.414×** | -23.5 | 0e+00 | 46/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.604×** | -9.5 | 7e-19 | 34/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -9.3 | 3e-18 | 29/47 (HOP62, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.636×** | -8.5 | 3e-15 | 33/47 (Panc 03.27, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -8.2 | 2e-14 | 32/48 (Panc 03.27, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.652×** | -8.0 | 8e-14 | 32/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.660×** | -7.5 | 5e-12 | 28/48 (Panc 03.27, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.715×** | -6.3 | 2e-08 | 25/47 (SNU-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.708×** | -6.2 | 3e-08 | 27/47 (COLO 205, SNU-423, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.727×** | -6.0 | 1e-07 | 26/48 (NCI-H2030, C-33 A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.806×** | -5.7 | 5e-07 | 23/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.739×** | -5.7 | 6e-07 | 23/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.745×** | -5.5 | 1e-06 | 25/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.753×** | -5.3 | 4e-06 | 24/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.792×** | -4.4 | 5e-04 | 22/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.801×** | -4.2 | 0.001 | 17/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.817×** | -3.8 | 0.004 | 14/48 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Furosemide (drug)]] 0.5 µM |  | **0.822×** | -3.7 | 0.007 | 12/48 (A-172, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 46.6 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -23.9) |
| [[Panc 03.27 (line)]] | alt | 47.7 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -18.2) |
| [[A-427 (line)]] | wt | 38.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -18.4) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -10.1) |
| [[A498 (line)]] | wt | 25.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +34.6) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 24.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -12.6) |
| [[A-172 (line)]] | wt | 44.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -13.1) |
| [[C32 (line)]] | wt | 23.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -10.2) |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.198× (z -9.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 52.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -13.9) |
| [[HOP62 (line)]] | alt | 25.8 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 30.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 29.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.7) ⚠ cell-cycle shift, explains ~12% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 50.5 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 23.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -17.1) |
| [[SW480 (line)]] | alt | 24.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -15.3) |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0968× (z -8.6) |
| [[BT-474 (line)]] | alt | 27.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -8.9) |
| [[C-33 A (line)]] | alt | 36.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 21.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -9.6) |
| [[HS-578T (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.1) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[HT-29 (line)]] | alt | 18.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -10.5) |
| [[KATO III (line)]] | alt | 18.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.2) |
| [[LoVo (line)]] | wt | 27.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -11.5) |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 16.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 22.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -11.3) |
| [[SNU-423 (line)]] | alt | 25.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -9.2) |
| [[SW 900 (line)]] | alt | 18.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -9.3) |
| [[SW48 (line)]] | wt | 40.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -10.6) |
| [[A549 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL1]] | +0.64 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[KLHL26]] | +0.63 | +0.58 / +0.45 | both halves | 3e-05 | same gene group |
| [[SMIM8]] | +0.62 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[ZNF559]] | +0.61 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[SNRNP70]] | +0.61 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[CRTC1]] | +0.60 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[DDX19B]] | +0.60 | +0.37 / +0.54 | both halves | 9e-05 |  |
| [[PKN1]] | +0.60 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[MOB3A]] | +0.60 | +0.58 / +0.44 | both halves | 3e-05 | ⚠ same locus (36.2 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF559-ZNF177]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[TOMM20]] | +0.59 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[TAMM41]] | +0.58 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[BRAT1]] | +0.58 | +0.48 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGRMC1]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[LINC01829]] | -0.56 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[ARSB]] | -0.53 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[EIF4G2]] | -0.53 | -0.29 / -0.53 | both halves | 2e-04 |  |
| [[ERAP1]] | -0.52 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[RNF217-AS1]] | -0.52 | -0.21 / -0.41 | both halves | 7e-04 |  |
| [[SLC5A3]] | -0.50 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[CRPPA]] | -0.50 | -0.21 / -0.40 | both halves | 6e-04 |  |
| [[PI4K2B]] | -0.49 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[ATP11C]] | -0.49 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[LNPEP]] | -0.49 | -0.32 / -0.42 | both halves | 1e-04 |  |
| [[TAX1BP3]] | -0.48 | -0.31 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BTBD2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-31.8, -4.9); signed map (-18.7, -15.2). **Vector** length 86.0, 17.9% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -0.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.2 | +4.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.2 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.3 | -23.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -4.1 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -0.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | BTB domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,985,438-2,034,881 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

UniProt [Q9BX70](https://www.uniprot.org/uniprotkb/Q9BX70) carries no function annotation.

**Summary**, from NCBI Gene [55643](https://www.ncbi.nlm.nih.gov/gene/55643):

> The C-terminus of the protein encoded by this gene binds topoisomerase I. The N-terminus contains a proline-rich region and a BTB/POZ domain (broad-complex, Tramtrack and bric a brac/Pox virus and Zinc finger), both of which are typically involved in protein-protein interactions. Subcellularly, the protein localizes to cytoplasmic bodies. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15504) · Entrez [55643](https://www.ncbi.nlm.nih.gov/gene/55643) · UniProt [Q9BX70](https://www.uniprot.org/uniprotkb/Q9BX70) · Ensembl [ENSG00000133243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133243)

## Data

Gene col 5432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5432); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5432]; `tensor/DDL_lfc|DDL_z.npy` [5432]; `embed/gene_vectors.npy` [5432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5432 or target_col == 5432). Every well: [[BTBD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTBD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
