---
symbol: "FAS"
type: "gene"
col: 369
ensembl_id: "ENSG00000026103"
name: "Fas cell surface death receptor"
location: "10q23.31"
module: 62
arm: "+"
pooled_cpm: 27.96
n_lines_expressing: 42
n_dd_up: 38
n_dd_down: 11
n_dd_up_clean: 28
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 13
direction_downstream: 12
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# FAS

*Fas cell surface death receptor* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.37× (z +18.6, q 0e+00, up in 34 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.216× (z -23.5, q 0e+00, down in 40 of 40 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTA2]] (+0.86, fdr 7e-06, ⚠ same locus), [[SPATA18]] (+0.79, fdr 7e-06), [[MDM2]] (+0.77, fdr 7e-06), [[ZMAT3]] (+0.72, fdr 7e-06); moves opposite to [[TPST2]] (-0.60, fdr 3e-05), [[ST6GALNAC4]] (-0.59, fdr 5e-05), [[RNF216]] (-0.57, fdr 2e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[DRAM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 12 with an alert ⚠; shown: the 15 strongest. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 369.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +18.6 | 0e+00 | 34/38 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +15.4 | 0e+00 | 27/39 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.78×** | +15.1 | 0e+00 | 32/40 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.03×** | +12.9 | 6e-36 | 34/39 (NCI-H2347, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +11.3 | 2e-27 | 25/39 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +10.1 | 3e-22 | 30/40 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +8.2 | 1e-14 | 27/40 (A498, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.9 | 2e-13 | 19/40 (RKO, A-172, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.3 | 1e-11 | 23/39 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.62×** | +7.3 | 1e-11 | 24/39 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +7.0 | 1e-10 | 23/40 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +6.7 | 8e-10 | 24/38 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +6.6 | 2e-09 | 22/40 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +5.7 | 4e-07 | 19/39 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.28×** | +5.2 | 6e-06 | 18/40 (RKO, C32, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 369.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.216×** | -23.5 | 0e+00 | 40/40 (A549, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.221×** | -23.1 | 0e+00 | 40/40 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.257×** | -20.8 | 0e+00 | 40/40 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.474×** | -11.4 | 4e-28 | 31/40 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.548×** | -9.2 | 3e-18 | 29/39 (LoVo, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.564×** | -8.8 | 2e-16 | 30/39 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.624×** | -7.2 | 4e-11 | 24/40 (HEC-1-A, HS-578T, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.499×** | -5.6 | 2e-06 | 20/40 (HEC-1-A, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.777×** | -3.7 | 0.013 | 10/39 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | **0.813×** | -3.2 | 0.084 | 7/39 (J82, LS 180, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.750×** | -3.2 | 0.084 | 9/39 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.821× | -3.0 | 0.12 | 11/40 (A549, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 369. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.8 | 11 (3 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.06× (z +19.1) | [[Panobinostat (drug)]] 5 µM 0.123× (z -15.9) |
| [[HEC-1-A (line)]] | alt | 51.8 | 1 | 11 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -19.6) |
| [[A-172 (line)]] | wt | 52.6 | 7 | 3 | [[Harringtonine (drug)]] 0.5 µM 6.09× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.110× (z -14.8) |
| [[A498 (line)]] | wt | 81.8 | 8 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +21.7) | [[Panobinostat (drug)]] 5 µM 0.240× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 53.9 | 6 | 4 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +20.8) | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -18.3) |
| [[RKO (line)]] | wt | 37.8 | 7 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.0792× (z -16.6) |
| [[LoVo (line)]] | wt | 34.8 | 4 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.111× (z -16.3) |
| [[A549 (line)]] | wt | 36.4 | 4 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.0373× (z -21.6) |
| [[hTERT-HPNE (line)]] | wt | 48.5 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.0550× (z -15.3) |
| [[HS-578T (line)]] | alt | 35.5 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.0908× (z -14.9) |
| [[LS 180 (line)]] | wt | 65.3 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.0704× (z -19.4) |
| [[A-427 (line)]] | wt | 19.2 | 3 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 5.59× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.241× (z -8.7) |
| [[C32 (line)]] | wt | 34.2 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.86× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.110× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 52.8 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.0859× (z -20.7) |
| [[Panc 03.27 (line)]] | alt | 41.5 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.0778× (z -18.2) |
| [[PANC-1 (line)]] | alt | 11.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +18.1) | — |
| [[H4 (line)]] | wt | 42.9 | 1 | 3 | [[Harringtonine (drug)]] 0.5 µM 5.34× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.0409× (z -16.7) |
| [[LOX-IMVI (line)]] | wt | 28.9 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.0838× (z -16.4) |
| [[SW48 (line)]] | wt | 53.7 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 6.08× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.0649× (z -12.9) |
| [[HOP62 (line)]] | alt | 15.5 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -10.6) |
| [[Hs 766T (line)]] | wt | 34.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0857× (z -15.4) |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 24.7× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.237× (z -8.6) |
| [[SNU-423 (line)]] | alt | 23.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -9.1) |
| [[HCT15 (line)]] | alt | 39.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -11.7) |
| [[J82 (line)]] | alt | 10.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +13.2) | — |
| [[KATO III (line)]] | alt | 8.79 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -10.1) |
| [[SNU-1 (line)]] | wt | 19.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.02× (z +9.1) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0884× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.4× (z +14.2) | — |
| [[NCI-H1792 (line)]] | alt | 29.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 5.36× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 18.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -10.1) |
| [[AN3 CA (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.73 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.81 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 369), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTA2]] | +0.86 | +0.75 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SPATA18]] | +0.79 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[MDM2]] | +0.77 | +0.64 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 428 |
| [[ZMAT3]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[PLCL2]] | +0.72 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[TYMSOS]] | +0.71 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[DRAM1]] | +0.69 | +0.62 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[PTCHD4]] | +0.68 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[DDB2]] | +0.68 | +0.54 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[DCP1B]] | +0.67 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TP53I3]] | +0.65 | +0.54 / +0.56 | both halves | 1e-05 | pathway: TP53 Regulates Transcription of Cell Death Genes |
| [[EDA2R]] | +0.65 | +0.51 / +0.66 | both halves | 1e-05 | same gene group |
| [[ABCA12]] | +0.65 | +0.52 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST2]] | -0.60 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ST6GALNAC4]] | -0.59 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[RNF216]] | -0.57 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[SAMD4B]] | -0.57 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PWWP3A]] | -0.57 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[TMEM41B]] | -0.56 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[DGKD]] | -0.55 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[ANKRD27]] | -0.55 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[PHKA2]] | -0.55 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[GNAI2]] | -0.54 | -0.41 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[SH3PXD2B]] | -0.54 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[STUB1]] | -0.54 | -0.34 / -0.17 | ⚠ not reproduced | 0.001 | pathway: Death Receptor Signaling |
| [[PIP4K2A]] | -0.54 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[KCTD20]] | -0.54 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FAS's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.9% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[DRAM1]] | B | DRAM1 activity raises FAS's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 3.53× lower at baseline in the lines without DRAM1 | 0.018 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[PLCL2]] | B | PLCL2 activity strengthens FAS's drug response | lines that do not express PLCL2 (9) vs lines expressing it (31) | the lines without PLCL2 respond 0.65× as strongly (z diff +2.07); rises at some drug-doses, falls at others (28% from rises): Homoharringtonine 5 µM: 1.43x vs 2.31x (z diff +3.4); Belinostat 5 µM: 0.38x vs 0.21x (z diff +3.1); Panobinostat 0.05 µM: 0.69x vs 0.46x (z diff +2.7) | 0.026 | ⚠ within organs, on part of the lines; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[ANKRD33B]] | B | ANKRD33B activity raises FAS's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 1.83× lower at baseline in the lines without ANKRD33B | 0.029 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[ANKRD33B]] | B | ANKRD33B activity strengthens FAS's drug response | lines that do not express ANKRD33B (10) vs lines expressing it (30) | the lines without ANKRD33B respond 0.61× as strongly (z diff +2.36); strongest at Homoharringtonine 5 µM: 1.21x vs 2.52x (z diff +5.2) | 0.033 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22; target measured in part of the lines; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity strengthens FAS's drug response | lines that do not express PTCHD4 (27) vs lines expressing it (13) | the lines without PTCHD4 respond 0.72× as strongly (z diff +2.14); rises at some drug-doses, falls at others (62% from rises): Idarubicin (hydrochloride) 5 µM: 2.06x vs 4.37x (z diff +4.3); Homoharringtonine 0.5 µM: 1.55x vs 3.33x (z diff +3.7); Belinostat 5 µM: 0.28x vs 0.17x (z diff +2.5) | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens FAS's drug response | lines that do not express PINCR (23) vs lines expressing it (17) | the lines without PINCR respond 0.72× as strongly (z diff +1.87); rises at some drug-doses, falls at others (44% from rises): Idarubicin (hydrochloride) 5 µM: 1.92x vs 3.99x (z diff +3.8); Homoharringtonine 0.5 µM: 1.48x vs 2.97x (z diff +3.0); Belinostat 5 µM: 0.32x vs 0.17x (z diff +2.9) | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[ERAP2]] | B | ERAP2 activity raises FAS's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 3.01× lower at baseline in the lines without ERAP2 | 0.066 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[PLCL2]] | B | PLCL2 activity raises FAS's level | lines that do not express PLCL2 (12) vs lines expressing it (38) | 1.75× lower at baseline in the lines without PLCL2 | 0.089 | ⚠ within organs, on part of the lines |
| [[ACTA2]] | C | ACTA2 activity raises FAS's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 3.91× lower at baseline in the lines without ACTA2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent; co-absent with the target |
| [[MDM2]] | C | MDM2's natural level strengthens FAS's drug response | MDM2's natural level across 40 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.24; direction not clear | 0.016 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[ACTA2]] | C | ACTA2 activity strengthens FAS's drug response | lines that do not express ACTA2 (4) vs lines expressing it (36) | the lines without ACTA2 respond 0.37× as strongly (z diff +3.23); rises at some drug-doses, falls at others (57% from rises): Homoharringtonine 0.5 µM: 0.66x vs 2.28x (z diff +5.1); Homoharringtonine 5 µM: 1.15x vs 2.24x (z diff +4.7); Panobinostat 0.5 µM: 0.31x vs 0.17x (z diff +3.3) | 0.097 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DRAM1]] | B | FAS activity raises DRAM1's level | lines that do not express FAS (8) vs lines expressing it (42) | 2.70× lower at baseline in the lines without FAS | 0.005 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| [[BTG2]] | B | FAS activity strengthens BTG2's drug response | lines that do not express FAS (7) vs lines expressing it (34) | the lines without FAS respond 0.07× as strongly (z diff +2.51); strongest at Topotecan (hydrochloride) 5 µM: 0.30x vs 1.93x (z diff +7.8) | 0.028 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DCP1B]] | B | FAS activity raises DCP1B's level | lines that do not express FAS (8) vs lines expressing it (42) | 1.72× lower at baseline in the lines without FAS | 0.050 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| [[RRM2B]] | B | FAS activity raises RRM2B's level | lines that do not express FAS (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without FAS | 0.050 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| cells under [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM | B | FAS activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 0.5 µM (protects the cells) | lines that do not express FAS (8) vs lines expressing it (40) | the lines without FAS: 0.89× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| cells under [[Ixazomib (drug)]] 5 µM | B | FAS activity lowers the cells' numbers under Ixazomib 5 µM (makes them more sensitive) | lines that do not express FAS (8) vs lines expressing it (40) | the lines without FAS: 1.25× the cells of the other lines | 0.085 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| [[RPS27L]] | B | FAS activity raises RPS27L's level | lines that do not express FAS (8) vs lines expressing it (42) | 1.62× lower at baseline in the lines without FAS | 0.086 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM | B | FAS activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express FAS (8) vs lines expressing it (40) | the lines without FAS: 0.85× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| [[XPC]] | B | FAS activity raises XPC's level | lines that do not express FAS (8) vs lines expressing it (42) | 1.27× lower at baseline in the lines without FAS | 0.093 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | B | FAS activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express FAS (8) vs lines expressing it (40) | the lines without FAS: 0.85× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| [[OTUD4]] | B | FAS activity raises OTUD4's level | lines that do not express FAS (8) vs lines expressing it (42) | 1.30× lower at baseline in the lines without FAS | 0.099 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| [[ACTA2]] | C | FAS activity raises ACTA2's level | lines that do not express FAS (8) vs lines expressing it (42) | 3.04× lower at baseline in the lines without FAS | 0.006 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.5, 36.0); signed map (41.9, -23.4). **Vector** length 130, 39.0% of its response variance represented; |z| ≥ 3 in 1,281 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.0 | +18.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +8.4 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.3 | +7.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +4.8 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +4.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -8.0 | -23.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.2 | -23.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.0 | -20.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.4 | -9.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -8.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -7.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | Fas cell surface death receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:88,953,813-89,029,605 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD95, APO-1; previously FAS1, APT1, TNFRSF6 |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor receptor superfamily; Death inducing signaling complex |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, ALLOGRAFT_REJECTION, APOPTOSIS, XENOBIOTIC_METABOLISM, INTERFERON_GAMMA_RESPONSE, EPITHELIAL_MESENCHYMAL_TRANSITION, P53_PATHWAY |
| Reactome | 15 pathways, smallest: FasL/ CD95L signaling; CASP8 activity is inhibited; Dimerization of procaspase-8 |
| Matched by | ensembl_id |

**Function**, from UniProt [P25445](https://www.uniprot.org/uniprotkb/P25445) (Tumor necrosis factor receptor superfamily member 6):

> Receptor for TNFSF6/FASLG. The adapter molecule FADD recruits caspase CASP8 to the activated receptor. The resulting death-inducing signaling complex (DISC) performs CASP8 proteolytic activation which initiates the subsequent cascade of caspases (aspartate-specific cysteine proteases) mediating apoptosis. FAS-mediated apoptosis may have a role in the induction of peripheral tolerance, in the antigen-stimulated suicide of mature T-cells, or both. The secreted isoforms 2 to 6 block apoptosis (in …

**Summary**, from NCBI Gene [355](https://www.ncbi.nlm.nih.gov/gene/355):

> The protein encoded by this gene is a member of the TNF-receptor superfamily. This receptor contains a death domain. It has been shown to play a central role in the physiological regulation of programmed cell death, and has been implicated in the pathogenesis of various malignancies and diseases of the immune system. The interaction of this receptor with its ligand allows the formation of a death-inducing signaling complex that includes Fas-associated death domain protein (FADD), caspase 8, and …

**Accessions** — [HGNC:11920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11920) · Entrez [355](https://www.ncbi.nlm.nih.gov/gene/355) · UniProt [P25445](https://www.uniprot.org/uniprotkb/P25445) · Ensembl [ENSG00000026103](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000026103)

## Data

Gene col 369: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 369); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 369, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 369]; `tensor/DDL_lfc|DDL_z.npy` [369]; `embed/gene_vectors.npy` [369]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 369 or target_col == 369). Every well: [[FAS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
