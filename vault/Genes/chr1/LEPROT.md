---
symbol: "LEPROT"
type: "gene"
col: 13119
ensembl_id: "ENSG00000213625"
name: "leptin receptor overlapping transcript"
location: "1p31.3"
module: 3
arm: "-"
pooled_cpm: 33.62
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# LEPROT

*leptin receptor overlapping transcript* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.40× (z +19.8, q 0e+00, up in 41 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.23× (z +3.9, q 0.010, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.372× (z -6.9, q 1e-09, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHRAC1]] (+0.69, fdr 7e-06), [[IL6ST]] (+0.69, fdr 7e-06), [[TUG1]] (+0.66, fdr 7e-06); moves opposite to [[DPH7]] (-0.63, fdr 2e-05), [[ATG4B]] (-0.63, fdr 1e-05), [[DRD4]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13119.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.40×** | +19.8 | 0e+00 | 41/41 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.82×** | +17.3 | 0e+00 | 34/34 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.07×** | +13.9 | 1e-41 | 36/38 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.2 | 0.004 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.010 | 20/47 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.010 | 19/48 (A-172, A498, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.018 | 19/48 (A549, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.022 | 19/48 (SW480, HT-29, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.049 | 20/47 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.054 | 18/47 (A-172, A498, …) | two highest doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.054 | 19/48 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.091 | 11/48 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13119.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.372×** | -6.9 | 1e-09 | 30/47 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.580×** | -6.9 | 1e-09 | 37/48 (SK-MEL-2, A498, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.603×** | -6.8 | 2e-09 | 39/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.461×** | -5.4 | 8e-06 | 29/41 (NCI-H460, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.690×** | -5.0 | 6e-05 | 27/48 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.712×** | -4.6 | 4e-04 | 24/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.720×** | -4.3 | 0.002 | 24/48 (SHP-77, HepG2/C3A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.753×** | -3.8 | 0.009 | 22/48 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.674×** | -3.6 | 0.024 | 19/48 (NCI-H460, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.616×** | -3.4 | 0.036 | 21/48 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 56.9 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +12.8) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 53.7 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +13.7) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.355× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 45.0 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +9.1) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.0667× (z -9.1) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 45.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 37.5 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.60× (z +11.2) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.120× (z -10.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.346× (z -9.8) |
| [[A498 (line)]] | wt | 43.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.86× (z +16.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 35.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.50× (z +13.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 53.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +14.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 26.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.91× (z +13.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 36.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 45.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +12.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 28.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.64× (z +15.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 45.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.61× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 48.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.31× (z +12.5) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.232× (z -10.4) |
| [[SNU-423 (line)]] | alt | 57.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 27.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +13.8) ⚠ toxic; transcription drop | [[PH-797804 (drug)]] 5 µM 0.147× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 41.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 15.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +10.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 36.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 26.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.62× (z +10.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 48.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.95× (z +11.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 14.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +11.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 33.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 30.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.09× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 23.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.06× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.39× (z +12.1) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 21.7 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.119× (z -12.7) |
| [[C32 (line)]] | wt | 27.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +10.0) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +9.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 39.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.109× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 27.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0427× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 44.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +11.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 21.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0291× (z -10.8) |
| [[SW1417 (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 15.1 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.113× (z -8.5) |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHRAC1]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[IL6ST]] | +0.69 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[TUG1]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[NCOA4]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ERLIN2]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[RAP2C]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[NXT2]] | +0.62 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[CD164]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CCDC50]] | +0.62 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[PRKAR1A]] | +0.61 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[TMEM14C]] | +0.61 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[OSTM1]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH7]] | -0.63 | -0.68 / -0.47 | both halves | 2e-05 |  |
| [[ATG4B]] | -0.63 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[DRD4]] | -0.62 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[OSBPL7]] | -0.62 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[TRIM11]] | -0.62 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[RBAK-RBAKDN]] | -0.61 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[MRPL55]] | -0.61 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[TMEM208]] | -0.61 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[TOMM5]] | -0.60 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[PHRF1]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[CLASRP]] | -0.59 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SDHAP1-1]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LEPROT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises LEPROT's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CLDN1]] | B | CLDN1 activity raises LEPROT's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 1.23× lower at baseline in the lines without CLDN1 | 0.089 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.604). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-10.1, 1.0); signed map (16.9, -32.4). **Vector** length 108, 28.3% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +19.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +13.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +17.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | +3.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.2 | +3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.1 | +1.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.9 | -6.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.5 | -6.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.9 | -5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.7 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.7 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -2.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | leptin receptor overlapping transcript |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:65,420,587-65,436,007 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OBRGRP, OB-RGRP, VPS55, FLJ90360 |
| Matched by | ensembl_id |

**Function**, from UniProt [O15243](https://www.uniprot.org/uniprotkb/O15243) (Leptin receptor gene-related protein):

> Negatively regulates leptin receptor (LEPR) cell surface expression, and thus decreases response to leptin. Negatively regulates growth hormone (GH) receptor cell surface expression in liver. May play a role in liver resistance to GH during periods of reduced nutrient availability.

**Summary**, from NCBI Gene [54741](https://www.ncbi.nlm.nih.gov/gene/54741):

> LEPROT is associated with the Golgi complex and endosomes and has a role in cell surface expression of growth hormone receptor (GHR; MIM 600946) and leptin receptor (OBR, or LEPR; MIM 601007), thereby altering receptor-mediated cell signaling (Couturier et al., 2007 [PubMed 18042720]; Touvier et al., 2009 [PubMed 19907080]).[supplied by OMIM, Jul 2010]

**Accessions** — [HGNC:29477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29477) · Entrez [54741](https://www.ncbi.nlm.nih.gov/gene/54741) · UniProt [O15243](https://www.uniprot.org/uniprotkb/O15243) · Ensembl [ENSG00000213625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213625)

## Data

Gene col 13119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13119); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13119]; `tensor/DDL_lfc|DDL_z.npy` [13119]; `embed/gene_vectors.npy` [13119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13119 or target_col == 13119). Every well: [[LEPROT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LEPROT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
