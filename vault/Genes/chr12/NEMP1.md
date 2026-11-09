---
symbol: "NEMP1"
type: "gene"
col: 9376
ensembl_id: "ENSG00000166881"
name: "nuclear envelope integral membrane protein 1"
location: "12q13.3"
module: 22
arm: "+"
pooled_cpm: 46.65
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# NEMP1

*nuclear envelope integral membrane protein 1* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.10× (z +15.6, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.606× (z -7.4, q 6e-11, down in 38 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.534× (z -4.9, q 2e-04, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KNTC1]] (+0.70, fdr 7e-06), [[STMN1]] (+0.68, fdr 7e-06), [[RAD51AP1]] (+0.68, fdr 7e-06); moves opposite to [[NOL7]] (-0.62, fdr 1e-05, ⚠ NOL7 in the vector space only through flagged drug-doses), [[RBM27]] (-0.60, fdr 1e-05), [[MPHOSPH10]] (-0.59, fdr 1e-05), [[NDUFB9]] (-0.56, fdr 4e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +15.6 | 0e+00 | 40/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +13.9 | 3e-41 | 43/48 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +10.4 | 4e-23 | 40/47 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.98×** | +10.1 | 6e-22 | 40/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.86×** | +9.2 | 6e-18 | 40/48 (BT-474, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.76×** | +8.3 | 7e-15 | 39/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.68×** | +7.7 | 1e-12 | 36/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.67×** | +7.3 | 3e-11 | 34/48 (HS-578T, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +6.9 | 4e-10 | 34/48 (BT-474, A-172, …) | all doses, flat | cell-cycle shift (explains ~23% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +6.4 | 8e-09 | 29/48 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.52×** | +6.2 | 3e-08 | 32/47 (NCI-H460, BT-474, …) | all doses, flat | cell-cycle shift (explains ~13% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.51×** | +6.1 | 7e-08 | 30/47 (KATO III, BT-474, …) | all doses, flat | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +6.0 | 7e-08 | 28/48 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.51×** | +5.9 | 2e-07 | 27/41 (SW 900, NCI-H2347, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.44×** | +5.4 | 3e-06 | 28/48 (BT-474, A-172, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.001 | 23/48 (SNU-423, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9376.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.606×** | -7.4 | 6e-11 | 38/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.534×** | -4.9 | 2e-04 | 29/47 (Hs 766T, C32, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.794×** | -4.8 | 2e-04 | 26/48 (A-427, LS 180, …) | rises with dose | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.536×** | -4.8 | 2e-04 | 32/48 (Hs 766T, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.706×** | -4.5 | 8e-04 | 23/48 (HCT15, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.582×** | -4.2 | 0.002 | 27/47 (HCT15, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -4.2 | 0.002 | 0/48 | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.598×** | -4.0 | 0.005 | 26/48 (LOX-IMVI, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.631×** | -3.6 | 0.023 | 22/48 (SW480, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.685×** | -3.5 | 0.024 | 21/48 (A-427, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.823×** | -3.2 | 0.060 | 16/48 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.709×** | -3.2 | 0.064 | 12/48 (NCI-H460, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.810×** | -3.1 | 0.079 | 17/48 (HOP62, LOX-IMVI, …) | two highest doses |  |
| [[Arbutin (drug)]] 5 µM |  | **0.806×** | -3.1 | 0.085 | 13/48 (Panc 03.27, SNU-423, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 57.4 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +18.7) | [[Bortezomib (drug)]] 5 µM 0.0948× (z -10.3) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 32.7 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +8.8) | [[vincristine (drug)]] 5 µM 0.0636× (z -9.5) |
| [[KATO III (line)]] | alt | 26.0 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.99× (z +11.2) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 33.4 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +12.5) | — |
| [[BT-474 (line)]] | alt | 31.8 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.44× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 27.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +12.0) | — |
| [[J82 (line)]] | alt | 77.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.9) | — |
| [[NCI-H2347 (line)]] | alt | 29.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +14.3) | — |
| [[NCI-H460 (line)]] | wt | 41.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +19.8) | — |
| [[A498 (line)]] | wt | 47.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 23.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +10.2) | — |
| [[C32 (line)]] | wt | 27.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 37.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 50.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 29.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +16.7) | — |
| [[Panc 03.27 (line)]] | alt | 60.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 44.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +13.0) | — |
| [[SW480 (line)]] | alt | 65.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +9.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-427 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.457× (z -9.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[CFPAC-1 (line)]] | alt | 25.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.3) | — |
| [[CHP-212 (line)]] | wt | 38.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0865× (z -10.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HepG2_C3A (line)]] | wt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 32.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +9.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 30.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +9.8) | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Raltitrexed (drug)]] 5 µM 0.202× (z -16.3) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 65.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 48.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 36.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +10.5) | — |
| [[SW 900 (line)]] | alt | 26.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 40.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.8) | — |
| [[A549 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KNTC1]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 | STRING 441 |
| [[STMN1]] | +0.68 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[RAD51AP1]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[MCM7]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[CENPH]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[MYBL1]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[NUSAP1]] | +0.64 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[ESPL1]] | +0.64 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[ESCO2]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[NCAPD2]] | +0.63 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[FOXM1]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[RMI2]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOL7]] ⚠ | -0.62 | -0.55 / -0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RBM27]] | -0.60 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[MPHOSPH10]] | -0.59 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[NDUFB9]] | -0.56 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[MRPL21]] | -0.56 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[PUS3]] | -0.56 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[RWDD1]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[CCDC12]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[SNRPB2]] | -0.55 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[MTDH]] | -0.54 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[MRPS26]] | -0.53 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[PCGF1]] ⚠ | -0.53 | -0.39 / -0.53 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NEMP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises NEMP1's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 2.42× lower at baseline in the lines without C21orf58, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.1, -49.7); signed map (-45.4, -47.3). **Vector** length 124, 37.6% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.6 | +9.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.2 | +7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | +4.6 | +5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.5 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +6.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.3 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +2.0 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.1 | +2.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -6.4 | -4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -6.3 | -4.8 |
|  | [[EX229 (drug)]] 5 µM |  | -6.0 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.9 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.6 | -0.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.3 | -4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | nuclear envelope integral membrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,055,643-57,088,063 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0286; previously TMEM194, TMEM194A |
| Matched by | ensembl_id |

**Function**, from UniProt [O14524](https://www.uniprot.org/uniprotkb/O14524) (Nuclear envelope integral membrane protein 1):

> Together with EMD, contributes to nuclear envelope stiffness in germ cells. Required for female fertility (By similarity). Essential for normal erythropoiesis (By similarity). Required for efficient nuclear envelope opening and enucleation during the late stages of erythroblast maturation (By similarity).

**Summary**, from NCBI Gene [23306](https://www.ncbi.nlm.nih.gov/gene/23306):

> Involved in nuclear membrane organization. Predicted to be located in nuclear inner membrane. Predicted to be active in nuclear envelope. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29001) · Entrez [23306](https://www.ncbi.nlm.nih.gov/gene/23306) · UniProt [O14524](https://www.uniprot.org/uniprotkb/O14524) · Ensembl [ENSG00000166881](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166881)

## Data

Gene col 9376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9376); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9376]; `tensor/DDL_lfc|DDL_z.npy` [9376]; `embed/gene_vectors.npy` [9376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9376 or target_col == 9376). Every well: [[NEMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
