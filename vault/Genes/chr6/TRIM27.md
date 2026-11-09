---
symbol: "TRIM27"
type: "gene"
col: 12916
ensembl_id: "ENSG00000204713"
name: "tripartite motif containing 27"
location: "6p22.1"
module: 33
arm: "+"
pooled_cpm: 42.8
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# TRIM27

*tripartite motif containing 27* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.13× (z +8.8, q 7e-16, up in 2 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.00× (z +7.6, q 6e-12, up in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CFPAC-1 2.92×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.536× (z -16.2, q 0e+00, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRM]] (+0.72, fdr 7e-06), [[SRPRB]] (+0.72, fdr 7e-06), [[RABEPK]] (+0.66, fdr 7e-06); moves opposite to [[ATP6V0C]] (-0.54, fdr 1e-04), [[STAG2]] (-0.53, fdr 3e-05), [[SMARCA1]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12916.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CFPAC-1 2.92×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +8.8 | 7e-16 | 2/48 (H4, NCI-H661) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +7.6 | 6e-12 | 32/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 0.002 | 18/48 (NCI-H1573, SW 900, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | **1.22×** | +3.9 | 0.011 | 16/47 (NCI-H2030, AsPC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +3.4 | 0.087 | 10/48 (NCI-H460, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12916.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.536×** | -16.2 | 0e+00 | 37/48 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.572×** | -11.8 | 8e-30 | 36/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.648×** | -9.2 | 7e-18 | 32/47 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -7.9 | 4e-13 | 19/39 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.693×** | -7.8 | 9e-13 | 27/48 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.746×** | -6.2 | 5e-08 | 27/46 (J82, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.778×** | -6.1 | 7e-08 | 28/48 (J82, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.775×** | -5.2 | 1e-05 | 25/48 (PANC-1, A-172, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.796×** | -4.8 | 8e-05 | 22/48 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.820×** | -4.8 | 9e-05 | 20/48 (SK-MEL-2, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.816×** | -4.3 | 9e-04 | 22/48 (KATO III, NCI-H460, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.728×** | -3.5 | 0.020 | 17/47 (C32, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.885× | -3.4 | 0.031 | 17/48 (HOP62, J82, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.877× | -3.3 | 0.031 | 15/48 (NCI-H23, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -3.3 | 0.031 | 14/48 (SW48, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.862× | -3.2 | 0.056 | 11/48 (LoVo, A-427, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.863× | -3.1 | 0.056 | 11/48 (RPMI-7951, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.856× | -3.0 | 0.072 | 8/47 (A-172, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | 0.877× | -3.0 | 0.083 | 11/48 (LoVo, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 106 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -15.1) |
| [[A498 (line)]] | wt | 44.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 62.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -15.1) |
| [[A-172 (line)]] | wt | 37.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.365× (z -11.2) |
| [[HOP62 (line)]] | alt | 56.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -10.9) |
| [[PANC-1 (line)]] | alt | 53.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -18.1) |
| [[SK-MEL-2 (line)]] | alt | 44.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -16.2) |
| [[HS-578T (line)]] | alt | 34.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.5) |
| [[LoVo (line)]] | wt | 43.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.368× (z -10.0) |
| [[LS 180 (line)]] | wt | 45.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.340× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 84.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -16.7) |
| [[NCI-H460 (line)]] | wt | 27.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -14.2) |
| [[NCI-H661 (line)]] | alt | 36.5 | 0 | 2 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0757× (z -8.9) |
| [[RKO (line)]] | wt | 51.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.381× (z -8.6) |
| [[SNU-1 (line)]] | wt | 42.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -8.9) |
| [[A-427 (line)]] | wt | 44.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -17.6) |
| [[AN3 CA (line)]] | alt | 48.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 45.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[C32 (line)]] | wt | 36.7 | 0 | 1 (1 ⚠) | — | [[NG25 (drug)]] 5 µM 0.0460× (z -12.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.92× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 34.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.1) |
| [[KATO III (line)]] | alt | 41.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.332× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 46.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 42.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.1) |
| [[SW1417 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.384× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 51.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -10.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 43.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.443× (z -10.3) |
| [[A549 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRM]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[SRPRB]] | +0.72 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[RABEPK]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[EARS2]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[DDX31]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[DNAJA3]] | +0.64 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ATAD3B]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[NSUN2]] | +0.63 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[POLR1B]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TIMM23]] | +0.62 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[WDR3]] | +0.62 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[POLR3A]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V0C]] | -0.54 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[STAG2]] | -0.53 | -0.44 / -0.49 | both halves | 3e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[SMARCA1]] | -0.53 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.53 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[FMR1]] | -0.53 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[BDH2]] | -0.52 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-5.3, -29.3); signed map (-44.7, -18.6). **Vector** length 109, 26.4% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +2.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.4 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.2 | -16.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -6.4 | -6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.8 | -11.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.5 | -2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:28,903,002-28,923,988 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF76; previously RFP |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 11 pathways, smallest: Suppression of apoptosis; Response of Mtb to phagocytosis; Infection with Mycobacterium tuberculosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P14373](https://www.uniprot.org/uniprotkb/P14373) (Zinc finger protein RFP):

> E3 ubiquitin-protein ligase that mediates ubiquitination of various substrates and thereby plays a role in diffent processes including proliferation, innate immunity, apoptosis, immune response or autophagy. Ubiquitinates PIK3C2B and inhibits its activity by mediating the formation of 'Lys-48'-linked polyubiquitin chains; the function inhibits CD4 T-cell activation. Acts as a regulator of retrograde transport: together with MAGEL2, mediates the formation of 'Lys-63'-linked polyubiquitin chains …

**Summary**, from NCBI Gene [5987](https://www.ncbi.nlm.nih.gov/gene/5987):

> This gene encodes a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. This protein localizes to the nuclear matrix. It interacts with the enhancer of polycomb protein and represses gene transcription. It is also thought to be involved in the differentiation of male germ cells. Fusion of the N-terminus of this protein with the truncated C-terminus of the RET gene product has been …

**Accessions** — [HGNC:9975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9975) · Entrez [5987](https://www.ncbi.nlm.nih.gov/gene/5987) · UniProt [P14373](https://www.uniprot.org/uniprotkb/P14373) · Ensembl [ENSG00000204713](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204713)

## Data

Gene col 12916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12916); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12916]; `tensor/DDL_lfc|DDL_z.npy` [12916]; `embed/gene_vectors.npy` [12916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12916 or target_col == 12916). Every well: [[TRIM27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
