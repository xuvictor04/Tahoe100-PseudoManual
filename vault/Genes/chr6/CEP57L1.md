---
symbol: "CEP57L1"
type: "gene"
col: 11373
ensembl_id: "ENSG00000183137"
name: "centrosomal protein 57 like 1"
location: "6q21"
module: 67
arm: "+"
pooled_cpm: 46.55
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CEP57L1

*centrosomal protein 57 like 1* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.91× (z +16.3, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.640× (z -11.2, q 2e-26, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP85]] (+0.74, fdr 7e-06), [[CENPI]] (+0.74, fdr 7e-06), [[SKA1]] (+0.74, fdr 7e-06); moves opposite to [[LINC00571]] (-0.65, fdr 4e-05), [[ZFHX2-AS1]] (-0.63, fdr 5e-05), [[LINC02955]] (-0.63, fdr 6e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZNF341-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11373.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +16.3 | 0e+00 | 44/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +15.7 | 0e+00 | 42/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +15.4 | 0e+00 | 47/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +8.6 | 1e-15 | 35/48 (RKO, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +7.6 | 4e-12 | 33/48 (AsPC-1, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +4.7 | 3e-04 | 14/48 (KATO III, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.17× | +3.9 | 0.008 | 13/48 (HT-29, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.7 | 0.018 | 18/48 (LoVo, RKO, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.037 | 10/47 (LoVo, NCI-H2347, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | 1.14× | +3.3 | 0.046 | 19/47 (RKO, A549, …) | inconsistent across doses | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.046 | 8/48 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.072 | 5/48 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.1 | 0.076 | 7/48 (SW480, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.082 | 8/48 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.1 | 0.082 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11373.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.640×** | -11.2 | 2e-26 | 38/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -8.8 | 3e-16 | 29/48 (HEC-1-A, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.784×** | -8.6 | 1e-15 | 24/48 (H4, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.738×** | -7.6 | 4e-12 | 30/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.750×** | -7.2 | 5e-11 | 25/48 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.579×** | -7.2 | 7e-11 | 29/48 (PANC-1, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.750×** | -6.9 | 3e-10 | 27/47 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.837× | -6.3 | 2e-08 | 20/48 (HEC-1-A, SW 1271, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.788×** | -6.0 | 1e-07 | 23/48 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.638×** | -5.9 | 2e-07 | 18/36 (HS-578T, H4, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.792×** | -5.6 | 1e-06 | 24/48 (AN3 CA, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.800×** | -5.6 | 1e-06 | 26/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.656×** | -5.5 | 1e-06 | 23/48 (A-172, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.802×** | -5.5 | 1e-06 | 21/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.811×** | -5.3 | 5e-06 | 20/48 (J82, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -5.1 | 1e-05 | 23/48 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.888× | -4.2 | 7e-04 | 16/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.846× | -4.2 | 8e-04 | 19/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.747×** | -3.8 | 0.004 | 13/48 (HEC-1-A, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 45.4 | 3 | 2 | [[Belinostat (drug)]] 5 µM 2.39× (z +11.7) | [[Auranofin (drug)]] 5 µM 0.499× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 45.8 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.435× (z -10.2) |
| [[RKO (line)]] | wt | 43.8 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.31× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.130× (z -16.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 46.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -14.5) |
| [[BT-474 (line)]] | alt | 51.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.68× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 31.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +10.4) | — |
| [[KATO III (line)]] | alt | 33.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +10.3) | — |
| [[LoVo (line)]] | wt | 31.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.90× (z +11.4) | — |
| [[LS 180 (line)]] | wt | 32.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.07× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.333× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 34.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.299× (z -12.9) |
| [[PANC-1 (line)]] | alt | 127 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 1.69× (z +9.5) | [[TAK-901 (drug)]] 5 µM 0.382× (z -9.1) |
| [[A-172 (line)]] | wt | 67.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -10.1) |
| [[H4 (line)]] | wt | 37.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -15.6) |
| [[J82 (line)]] | alt | 42.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.409× (z -8.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.547× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 64.9 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.43× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -15.1) |
| [[A-427 (line)]] | wt | 70.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.450× (z -10.1) |
| [[A549 (line)]] | wt | 33.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -9.5) |
| [[AN3 CA (line)]] | alt | 77.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 24.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.196× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 46.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 42.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -8.6) |
| [[NCI-H2122 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Raltitrexed (drug)]] 5 µM 0.235× (z -9.8) ⚠ cell-cycle shift, explains ~62% of this change |
| [[RPMI-7951 (line)]] | alt | 59.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -10.1) |
| [[SHP-77 (line)]] | alt | 60.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 36.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -8.8) |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.209× (z -14.4) ⚠ cell-cycle shift, explains ~58% of this change |
| [[SW48 (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP85]] | +0.74 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[CENPI]] | +0.74 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[SKA1]] | +0.74 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[CEP192]] | +0.73 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[PBK]] | +0.73 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[MPHOSPH9]] | +0.72 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[CCDC150]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[UBE2T]] | +0.72 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[PARPBP]] | +0.72 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[NUF2]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[CIT]] | +0.71 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[TTK]] | +0.70 | +0.65 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00571]] | -0.65 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ZFHX2-AS1]] | -0.63 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[LINC02955]] | -0.63 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[LINC01762]] | -0.61 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[BCL10-AS1]] | -0.60 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CCDC90B-AS1]] | -0.60 | -0.32 / -0.44 | both halves | 1e-04 |  |
| [[MMADHC-DT]] | -0.60 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[ZNF341-AS1]] | -0.60 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[C1orf54]] | -0.60 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[C2orf49-DT]] | -0.59 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[CPEB2-DT]] | -0.59 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[NEK8]] | -0.59 | -0.44 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity lowers CEP57L1's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.67× higher at baseline in the lines without ZNF341-AS1 | 0.047 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers CEP57L1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC00571]] | B | LINC00571 activity lowers CEP57L1's level | lines that do not express LINC00571 (5) vs lines expressing it (45) | 1.85× higher at baseline in the lines without LINC00571 | 0.069 | ⚠ within organs, on part of the lines; also absent: KIFC3, NDRG1, DELEC1; maybe low, not absent |
| [[PBK]] | C | PBK activity raises CEP57L1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.14× lower at baseline in the lines without PBK | 0.047 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.8, -53.5); signed map (-46.0, -40.0). **Vector** length 101, 24.8% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.61 to 12); *G2/M checkpoint* (hallmark, mean cos +0.59 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.62 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.5 | +15.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.6 | +15.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +16.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +7.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +8.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.8 | +3.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.8 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.3 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.5 | -8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.2 | -11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | -6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -2.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.3 | -3.6 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 57 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:109,095,110-109,174,418 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA487F23.2, MGC21731; previously C6orf182 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYX8](https://www.uniprot.org/uniprotkb/Q8IYX8) (Centrosomal protein CEP57L1):

> Centrosomal protein which may be required for microtubule attachment to centrosomes.

**Summary**, from NCBI Gene [285753](https://www.ncbi.nlm.nih.gov/gene/285753):

> Enables identical protein binding activity. Predicted to be located in microtubule. Predicted to be active in centrosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21561](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21561) · Entrez [285753](https://www.ncbi.nlm.nih.gov/gene/285753) · UniProt [Q8IYX8](https://www.uniprot.org/uniprotkb/Q8IYX8) · Ensembl [ENSG00000183137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183137)

## Data

Gene col 11373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11373); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11373]; `tensor/DDL_lfc|DDL_z.npy` [11373]; `embed/gene_vectors.npy` [11373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11373 or target_col == 11373). Every well: [[CEP57L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP57L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
