---
symbol: "AFAP1"
type: "gene"
col: 12229
ensembl_id: "ENSG00000196526"
name: "actin filament associated protein 1"
location: "4p16.1"
module: 84
arm: "+"
pooled_cpm: 144.85
n_lines_expressing: 45
n_dd_up: 5
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# AFAP1

*actin filament associated protein 1* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.82× (z +12.4, q 3e-32, up in 27 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.511× (z -19.5, q 0e+00, down in 37 of 44 measured lines).
> Its strongest partners by |cos| (63 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 37 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPP5F]] (+0.63, fdr 5e-05), [[CADM4]] (+0.62, fdr 2e-04), [[FCHO1]] (+0.60, fdr 0.002, ⚠ one half only (not replicated)), [[SLC9A7]] (+0.58, fdr 3e-05); moves opposite to [[FAIM]] (-0.58, fdr 5e-04), [[DDX59]] (-0.55, fdr 5e-04), [[NIPAL2]] (-0.55, fdr 9e-04, ⚠ not reproduced), [[CCAR1]] (-0.55, fdr 1e-04).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC00869-1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12229.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +12.4 | 3e-32 | 27/43 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +9.1 | 2e-17 | 26/43 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +8.9 | 7e-17 | 26/43 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +5.0 | 9e-05 | 21/43 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.6 | 5e-04 | 17/43 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.019 | 9/43 (SW1417, HS-578T, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.025 | 14/44 (A498, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.040 | 11/43 (NCI-H2347, COLO 205, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.12 | 8/42 (A498, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12229.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -19.5 | 0e+00 | 37/44 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.573×** | -16.2 | 0e+00 | 32/43 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.521×** | -12.9 | 1e-35 | 32/43 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.584×** | -11.1 | 2e-26 | 35/43 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -9.7 | 3e-20 | 30/43 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -9.1 | 1e-17 | 33/43 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.652×** | -8.8 | 1e-16 | 30/43 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -8.8 | 1e-16 | 32/45 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.649×** | -8.6 | 8e-16 | 26/42 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.650×** | -8.5 | 1e-15 | 27/38 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.672×** | -8.2 | 2e-14 | 30/43 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.722×** | -6.7 | 1e-09 | 28/43 (SK-MEL-2, RPMI-7951, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.741×** | -6.2 | 3e-08 | 26/43 (PANC-1, C32, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.749×** | -5.9 | 1e-07 | 22/43 (C32, SNU-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.752×** | -5.9 | 2e-07 | 21/43 (SNU-1, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.831×** | -5.4 | 3e-06 | 21/43 (HOP62, A-172, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.637×** | -4.9 | 4e-05 | 24/43 (PANC-1, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.652×** | -4.6 | 1e-04 | 19/43 (PANC-1, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.693×** | -3.9 | 0.002 | 19/44 (PANC-1, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.837× | -3.7 | 0.006 | 19/43 (SNU-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.841× | -3.6 | 0.009 | 18/44 (NCI-H460, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12229. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 569 | 0 | 24 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -29.3) |
| [[C32 (line)]] | wt | 271 | 0 | 20 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -25.4) |
| [[RPMI-7951 (line)]] | alt | 419 | 0 | 14 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -23.4) |
| [[J82 (line)]] | alt | 353 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -18.5) |
| [[SK-MEL-2 (line)]] | alt | 93.2 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.0) |
| [[SNU-1 (line)]] | wt | 133 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -15.2) |
| [[A-172 (line)]] | wt | 229 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -18.4) |
| [[A549 (line)]] | wt | 150 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -17.1) |
| [[CFPAC-1 (line)]] | alt | 240 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -15.8) |
| [[HOP62 (line)]] | alt | 187 | 0 | 7 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 211 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -21.3) |
| [[LoVo (line)]] | wt | 53.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 171 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -23.7) |
| [[Panc 03.27 (line)]] | alt | 328 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -14.4) |
| [[A498 (line)]] | wt | 57.4 | 3 | 2 | [[Belinostat (drug)]] 5 µM 2.69× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.8) |
| [[Hs 766T (line)]] | wt | 292 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -14.7) |
| [[HS-578T (line)]] | alt | 209 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -18.5) |
| [[KATO III (line)]] | alt | 72.5 | 2 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.40× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -20.0) |
| [[HEC-1-A (line)]] | alt | 52.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 58.8 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.216× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 60.7 | 2 | 2 | [[Panobinostat (drug)]] 0.5 µM 3.09× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -11.3) |
| [[SW1417 (line)]] | alt | 63.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -13.0) |
| [[BT-474 (line)]] | alt | 90.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -12.9) |
| [[LOX-IMVI (line)]] | wt | 113 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -14.7) |
| [[A-427 (line)]] | wt | 36.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 193 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 39.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +16.8) | — |
| [[NCI-H460 (line)]] | wt | 119 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -10.3) |
| [[H4 (line)]] | wt | 207 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -8.6) |
| [[LS 180 (line)]] | wt | 88.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.412× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 37.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.282× (z -10.0) |
| [[SNU-423 (line)]] | alt | 184 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -13.9) |
| [[SW 1271 (line)]] | alt | 69.8 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0854× (z -8.6) |
| [[AN3 CA (line)]] | alt | 115 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 30.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12229), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP5F]] | +0.63 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[CADM4]] | +0.62 | +0.51 / +0.32 | both halves | 2e-04 |  |
| [[FCHO1]] | +0.60 | +0.53 / +0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[SLC9A7]] | +0.58 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[RASA3]] | +0.58 | +0.52 / +0.41 | both halves | 4e-05 | same gene group |
| [[IL1RAP]] | +0.58 | +0.60 / +0.38 | both halves | 6e-05 |  |
| [[DNAAF3]] | +0.57 | +0.40 / +0.23 | both halves | 5e-04 |  |
| [[ADAM19]] | +0.57 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[SLC6A6]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.57 | +0.47 / +0.22 | both halves | 6e-04 |  |
| [[PODXL]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[GRK5]] | +0.56 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[KIF21B]] | +0.56 | +0.51 / +0.20 | both halves | 7e-04 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 23 of them with an alert (⚠; 23 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAIM]] | -0.58 | -0.50 / -0.24 | both halves | 5e-04 |  |
| [[DDX59]] | -0.55 | -0.42 / -0.23 | both halves | 5e-04 |  |
| [[NIPAL2]] | -0.55 | -0.39 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[CCAR1]] | -0.55 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[LINC00869-1]] | -0.54 | -0.51 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[TTC32]] | -0.54 | -0.51 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[CREBBP]] | -0.54 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[PBLD]] | -0.54 | -0.48 / -0.06 | ⚠ not reproduced | 0.004 |  |
| [[OARD1]] | -0.54 | -0.51 / -0.27 | both halves | 3e-04 |  |
| [[HOXB7]] | -0.54 | -0.39 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[ATAD2B]] | -0.54 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[UNK]] | -0.54 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[CARD8]] | -0.53 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[WDR33]] | -0.53 | -0.40 / -0.23 | both halves | 5e-04 |  |
| [[COBLL1]] | -0.53 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[ZBTB8A]] | -0.53 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[DECR1]] | -0.52 | -0.42 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises AFAP1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NAV2]] | B | NAV2 activity raises AFAP1's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 2.18× lower at baseline in the lines without NAV2 | 0.038 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[HDAC6]] | B | HDAC6 activity lowers AFAP1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LOXL2]] | B | LOXL2 activity raises AFAP1's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 2.65× lower at baseline in the lines without LOXL2 | 0.059 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[TESC]] | B | TESC activity lowers AFAP1's level | lines that do not express TESC (23) vs lines expressing it (27) | 2.35× higher at baseline in the lines without TESC | 0.079 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1 |
| [[ITGB3]] | B | ITGB3 activity raises AFAP1's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 2.36× lower at baseline in the lines without ITGB3 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[FLNB]] | C | FLNB activity raises AFAP1's level | lines that do not express FLNB (3) vs lines expressing it (47) | 3.40× lower at baseline in the lines without FLNB | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00869-1]] | B | AFAP1 activity lowers LINC00869-1's level | lines that do not express AFAP1 (5) vs lines expressing it (45) | 2.63× higher at baseline in the lines without AFAP1 | 0.095 | ⚠ within organs, on part of the lines; also absent: RBM43; maybe low, not absent |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.6, 1.0); signed map (-8.6, 49.6). **Vector** length 105, 28.1% of its response variance represented; |z| ≥ 3 in 1,470 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +7.5 | +8.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.2 | +12.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.0 | +9.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +5.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | -0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -19.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -9.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -2.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.1 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.1 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.0 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | actin filament associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:7,758,714-7,939,926 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AFAP-110, AFAP |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N556](https://www.uniprot.org/uniprotkb/Q8N556) (Actin filament-associated protein 1):

> Can cross-link actin filaments into both network and bundle structures (By similarity). May modulate changes in actin filament integrity and induce lamellipodia formation. May function as an adapter molecule that links other proteins, such as SRC and PKC to the actin cytoskeleton. Seems to play a role in the development and progression of prostate adenocarcinoma by regulating cell-matrix adhesions and migration in the cancer cells.

**Summary**, from NCBI Gene [60312](https://www.ncbi.nlm.nih.gov/gene/60312):

> The protein encoded by this gene is a Src binding partner. It may represent a potential modulator of actin filament integrity in response to cellular signals, and may function as an adaptor protein by linking Src family members and/or other signaling proteins to actin filaments. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:24017](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24017) · Entrez [60312](https://www.ncbi.nlm.nih.gov/gene/60312) · UniProt [Q8N556](https://www.uniprot.org/uniprotkb/Q8N556) · Ensembl [ENSG00000196526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196526)

## Data

Gene col 12229: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12229); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12229, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12229]; `tensor/DDL_lfc|DDL_z.npy` [12229]; `embed/gene_vectors.npy` [12229]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12229 or target_col == 12229). Every well: [[AFAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
