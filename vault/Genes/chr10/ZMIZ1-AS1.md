---
symbol: "ZMIZ1-AS1"
type: "gene"
col: 13407
ensembl_id: "ENSG00000224596"
name: "ZMIZ1 antisense RNA 1"
location: "10q22.3"
module: 100
arm: "+"
pooled_cpm: 8.06
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 30
n_dd_up_clean: 10
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# ZMIZ1-AS1

*ZMIZ1 antisense RNA 1* — 10q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +8.3, q 8e-14, up in 28 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (14 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.313× (z -12.3, q 3e-32, down in 36 of 45 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.447× (z -8.6, q 1e-15, down in 26 of 43 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPN12]] (+0.55, fdr 3e-05), [[ITGA7]] (+0.52, fdr 3e-05), [[SPTBN4]] (+0.51, fdr 5e-05); moves opposite to [[DROSHA]] (-0.50, fdr 6e-05), [[ARMC1]] (-0.47, fdr 5e-05), [[NIPSNAP2]] (-0.45, fdr 4e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RMDN2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13407.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +8.3 | 8e-14 | 28/39 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +7.0 | 8e-10 | 23/44 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +5.4 | 1e-05 | 20/41 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +4.2 | 0.004 | 17/40 (C32, SW480, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.47×** | +4.1 | 0.004 | 11/41 (A549, LS 180, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.058 | 11/44 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.076 | 12/41 (LS 180, A-427, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.081 | 4/44 (SW 900, C32, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.090 | 8/42 (A-427, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.090 | 4/43 (A-427, HCT15, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13407.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.313×** | -12.3 | 3e-32 | 36/45 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.376×** | -10.4 | 6e-23 | 30/42 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.535×** | -9.4 | 1e-18 | 28/41 (LS 180, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.415×** | -9.0 | 4e-17 | 27/43 (SW480, LS 180, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.443×** | -8.6 | 7e-16 | 28/39 (HT-29, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.447×** | -8.6 | 1e-15 | 26/43 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.449×** | -8.5 | 2e-15 | 30/42 (LS 180, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.454×** | -8.4 | 4e-15 | 29/43 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.471×** | -8.0 | 8e-14 | 25/40 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.314×** | -6.4 | 7e-09 | 23/40 (A-427, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.527×** | -6.4 | 7e-09 | 24/41 (SK-MEL-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.347×** | -5.9 | 2e-07 | 23/41 (LS 180, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.578×** | -5.8 | 3e-07 | 19/43 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.585×** | -5.5 | 2e-06 | 19/36 (LS 180, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.598×** | -5.4 | 2e-06 | 25/44 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.382×** | -5.3 | 3e-06 | 19/40 (SW480, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.610×** | -5.2 | 5e-06 | 24/41 (PANC-1, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.650×** | -4.6 | 2e-04 | 18/41 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.740×** | -4.5 | 2e-04 | 20/42 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.446×** | -4.5 | 2e-04 | 17/41 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.455×** | -4.4 | 3e-04 | 15/39 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.513×** | -3.7 | 0.005 | 14/39 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.730×** | -3.3 | 0.019 | 16/40 (HT-29, NCI-H23, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.647×** | -3.3 | 0.021 | 14/44 (NCI-H460, SW48, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13407. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.5 | 0 | 13 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0916× (z -13.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0976× (z -13.4) |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 9 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0283× (z -17.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0786× (z -12.6) |
| [[HT-29 (line)]] | alt | 12.2 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -16.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0874× (z -12.6) |
| [[SW480 (line)]] | alt | 6.82 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -14.3) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.173× (z -9.7) |
| [[LoVo (line)]] | wt | 5.70 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.0603× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -13.2) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.125× (z -10.0) |
| [[A549 (line)]] | wt | 6.37 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -9.1) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0926× (z -9.0) |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0960× (z -8.8) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 9.21 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -12.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H460 (line)]] | wt | 6.11 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.104× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 2 (1 ⚠) | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0951× (z -9.0) |
| [[SNU-423 (line)]] | alt | 34.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0393× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +8.9) | — |
| [[A-427 (line)]] | wt | 7.62 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0590× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 6.68 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -9.5) |
| [[C-33 A (line)]] | alt | 8.57 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0630× (z -9.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -10.1) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H1792 (line)]] | alt | 8.44 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.121× (z -8.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 3.54 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0507× (z -8.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H23 (line)]] | alt | 5.25 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0595× (z -9.2) |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0765× (z -9.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[AN3 CA (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13407), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN12]] | +0.55 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[ITGA7]] | +0.52 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[SPTBN4]] | +0.51 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[AATK]] | +0.50 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[SEC1P]] | +0.49 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[RIPOR3]] | +0.49 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[ZMIZ1]] | +0.49 | +0.38 / +0.51 | both halves | 7e-05 | ⚠ same locus (1.1 kb: neighbours can correlate without regulation) |
| [[KNDC1]] | +0.49 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[LHX4]] | +0.49 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[ATP13A3-DT]] | +0.48 | +0.25 / +0.59 | both halves | 4e-04 |  |
| [[COL9A3]] | +0.48 | +0.31 / +0.42 | both halves | 2e-04 |  |
| [[CCDC3]] | +0.48 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[ZNF774]] | +0.47 | +0.37 / +0.49 | both halves | 7e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DROSHA]] | -0.50 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[ARMC1]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[NIPSNAP2]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[GNB4]] | -0.45 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[ZYG11B]] | -0.44 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[ARMC8]] | -0.44 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[MRPL35]] | -0.44 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[EIF2B4]] | -0.44 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[BLTP1]] | -0.43 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[C5orf22]] | -0.43 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[C3orf14]] | -0.42 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[PWP1]] | -0.42 | -0.31 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RMDN2-AS1]] | B | RMDN2-AS1 activity raises ZMIZ1-AS1's level | lines that do not express RMDN2-AS1 (14) vs lines expressing it (36) | 1.49× lower at baseline in the lines without RMDN2-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: EHD3, PLOD2, ZNF43; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.470). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.6, 34.6); signed map (25.5, 19.0). **Vector** length 63.2, 10.5% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | -1.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -8.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -6.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -5.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | ZMIZ1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q22.3 — chr10:78,943,328-79,067,895 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27433](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27433) · Entrez [283050](https://www.ncbi.nlm.nih.gov/gene/283050) · Ensembl [ENSG00000224596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224596)

## Data

Gene col 13407: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13407); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13407, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13407]; `tensor/DDL_lfc|DDL_z.npy` [13407]; `embed/gene_vectors.npy` [13407]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13407 or target_col == 13407). Every well: [[ZMIZ1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMIZ1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
