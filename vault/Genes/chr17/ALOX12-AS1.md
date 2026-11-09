---
symbol: "ALOX12-AS1"
type: "gene"
col: 13243
ensembl_id: "ENSG00000215067"
name: "mir-497-195 cluster host gene"
location: "17p13.1"
module: 26
arm: "+"
pooled_cpm: 28.37
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 14
n_dd_up_clean: 27
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# ALOX12-AS1

*mir-497-195 cluster host gene* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.93× (z +16.7, q 0e+00, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.538× (z -6.8, q 6e-09, down in 24 of 47 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.585× (z -5.9, q 8e-07, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC90B-AS1]] (+0.73, fdr 7e-06), [[ALG1L9P]] (+0.72, fdr 7e-06), [[PSMD7-DT]] (+0.72, fdr 7e-06); moves opposite to [[ZNF30]] (-0.65, fdr 2e-04), [[SDHAF3]] (-0.63, fdr 4e-05), [[C17orf58]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 2 with an alert ⚠; shown: the 15 strongest. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13243.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.93×** | +16.7 | 0e+00 | 42/45 (SW 900, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +13.5 | 6e-39 | 30/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.25×** | +12.6 | 7e-34 | 40/47 (SW1417, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.52×** | +10.1 | 5e-22 | 40/47 (SW 900, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.21×** | +8.7 | 3e-16 | 35/47 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +8.7 | 4e-16 | 39/46 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +6.8 | 8e-10 | 34/47 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +5.9 | 3e-07 | 27/47 (SK-MEL-2, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.64×** | +5.3 | 9e-06 | 31/45 (NCI-H23, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +4.8 | 1e-04 | 23/47 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.52×** | +4.6 | 2e-04 | 26/46 (SW480, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +4.5 | 3e-04 | 26/47 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.001 | 23/47 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.30×** | +4.0 | 0.003 | 20/47 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **2.00×** | +4.0 | 0.003 | 20/46 (SW480, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13243.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.538×** | -6.8 | 6e-09 | 24/47 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.558×** | -6.1 | 2e-07 | 30/47 (SW480, AN3 CA, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.585×** | -5.9 | 8e-07 | 28/47 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.593×** | -5.7 | 1e-06 | 27/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.604×** | -5.5 | 4e-06 | 30/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.387×** | -5.4 | 5e-06 | 28/46 (COLO 205, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.665×** | -4.5 | 6e-04 | 26/47 (SW480, COLO 205, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.492×** | -4.1 | 0.003 | 22/47 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.705×** | -3.8 | 0.008 | 22/47 (SW480, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.701×** | -3.7 | 0.010 | 22/43 (COLO 205, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.711×** | -3.7 | 0.010 | 18/47 (C32, BT-474, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.810×** | -3.3 | 0.054 | 17/47 (COLO 205, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.748×** | -3.2 | 0.067 | 18/47 (SW480, SW 1271, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.589×** | -3.0 | 0.099 | 17/43 (H4, SHP-77, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 29.5 | 2 | 9 (6 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.07× (z +11.0) | [[Harringtonine (drug)]] 0.5 µM 0.228× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 13.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +25.4) | — |
| [[SK-MEL-2 (line)]] | alt | 41.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.0) | — |
| [[C32 (line)]] | wt | 29.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 90.4 | 0 | 3 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0599× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 16.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +17.9) | — |
| [[PANC-1 (line)]] | alt | 16.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.253× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SW 900 (line)]] | alt | 11.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +14.5) | — |
| [[A-172 (line)]] | wt | 53.9 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.03× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 13.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.76× (z +13.5) | — |
| [[HCT15 (line)]] | alt | 71.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0719× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 12.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +10.7) | — |
| [[J82 (line)]] | alt | 11.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.92× (z +14.0) | — |
| [[NCI-H2030 (line)]] | alt | 16.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 25.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +15.2) | — |
| [[RKO (line)]] | wt | 15.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +11.0) | [[Hydroxyurea (drug)]] 0.05 µM 0.0777× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 67.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 23.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 12.9 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 5.17× (z +11.4) | — |
| [[A498 (line)]] | wt | 32.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +9.5) | — |
| [[A549 (line)]] | wt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 43.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[AsPC-1 (line)]] | alt | 17.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.72× (z +13.8) | — |
| [[C-33 A (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.34× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +10.7) | — |
| [[HEC-1-A (line)]] | alt | 20.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.04× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 54.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +9.9) | — |
| [[KATO III (line)]] | alt | 17.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +9.9) | — |
| [[LoVo (line)]] | wt | 94.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -9.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LOX-IMVI (line)]] | wt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 8.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.77× (z +9.6) | — |
| [[A-427 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC90B-AS1]] | +0.73 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[ALG1L9P]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.72 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[ZCWPW2]] | +0.70 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[CFAP43]] | +0.69 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[CCDC30]] | +0.68 | +0.72 / +0.57 | both halves | 8e-06 |  |
| [[CELF6]] | +0.68 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[LINC02646]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MGAM]] | +0.68 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[HCG17]] | +0.67 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[ST8SIA5]] | +0.67 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[EFCAB6]] | +0.65 | +0.73 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF30]] | -0.65 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[SDHAF3]] | -0.63 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[C17orf58]] | -0.63 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[NR2C1]] | -0.60 | -0.65 / -0.39 | both halves | 6e-05 |  |
| [[PET117]] | -0.58 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[WASF3]] | -0.57 | -0.70 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[RSAD1]] | -0.57 | -0.54 / -0.29 | both halves | 2e-04 |  |
| [[GNPTAB]] | -0.56 | -0.51 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ALOX12-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ESRRB]] | B | ESRRB activity raises ALOX12-AS1's level | lines that do not express ESRRB (5) vs lines expressing it (45) | 2.33× lower at baseline in the lines without ESRRB | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC02932, DYNLRB2-AS1, ARHGAP15; maybe low, not absent |
| [[LINC00907]] | C | LINC00907 activity raises ALOX12-AS1's level | lines that do not express LINC00907 (3) vs lines expressing it (47) | 2.94× lower at baseline in the lines without LINC00907 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAH6, ABHD12B, ESRRB; maybe low, not absent; its own permutation p |
| [[FBXO38-DT]] | C | FBXO38-DT activity raises ALOX12-AS1's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 2.66× lower at baseline in the lines without FBXO38-DT | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.757). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.1, 18.1); signed map (23.7, -2.0). **Vector** length 87.8, 21.8% of its response variance represented; |z| ≥ 3 in 1,224 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +13.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +16.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +12.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +8.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +5.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.9 | +2.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | +0.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.6 | +5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.4 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | mir-497-195 cluster host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17p13.1 — chr17:6,875,232-7,019,659 (-) |
| Ensembl biotype | lncRNA |
| Also known as | MIR195HG; previously ALOX12-AS1 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | prev_symbol |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:39523](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39523) · Entrez [100506755](https://www.ncbi.nlm.nih.gov/gene/100506755) · Ensembl [ENSG00000215067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215067)

## Data

Gene col 13243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13243); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13243]; `tensor/DDL_lfc|DDL_z.npy` [13243]; `embed/gene_vectors.npy` [13243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13243 or target_col == 13243). Every well: [[ALOX12-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALOX12-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
