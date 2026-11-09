---
symbol: "NOP14-AS1"
type: "gene"
col: 14627
ensembl_id: "ENSG00000249673"
name: "NOP14 antisense RNA 1"
location: "4p16.3"
module: 101
arm: "+"
pooled_cpm: 11.62
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 19
n_dd_up_clean: 18
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# NOP14-AS1

*NOP14 antisense RNA 1* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.09× (z +19.4, q 0e+00, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 0.654× (z -5.0, q 3e-04, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINB8]] (+0.73, fdr 7e-06), [[LETM2]] (+0.72, fdr 7e-06), [[KRT8P12]] (+0.70, fdr 7e-06); moves opposite to [[LSM2]] (-0.60, fdr 2e-05), [[CAPN7]] (-0.60, fdr 1e-05), [[TADA1]] (-0.59, fdr 7e-06).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14627.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +19.4 | 0e+00 | 42/45 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +13.1 | 8e-37 | 32/44 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +9.7 | 7e-20 | 34/43 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +9.4 | 8e-19 | 31/43 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +8.1 | 9e-14 | 29/47 (HOP62, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +8.0 | 1e-13 | 20/30 (SW48, HOP62, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.04×** | +7.1 | 1e-10 | 25/45 (A498, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.76×** | +6.9 | 3e-10 | 32/47 (KATO III, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.74×** | +6.8 | 7e-10 | 30/46 (KATO III, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.63×** | +5.9 | 3e-07 | 17/35 (NCI-H460, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.4 | 3e-06 | 19/47 (SW480, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +5.0 | 3e-05 | 18/46 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.45×** | +4.5 | 3e-04 | 17/47 (KATO III, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +4.4 | 4e-04 | 19/46 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.43×** | +4.2 | 8e-04 | 17/44 (A498, NCI-H460, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +4.1 | 0.001 | 16/47 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.004 | 15/47 (SW480, LS 180, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.007 | 14/46 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.018 | 15/47 (A498, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.019 | 14/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +3.4 | 0.019 | 12/42 (A-172, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14627.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.654×** | -5.0 | 3e-04 | 20/47 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.655×** | -4.7 | 7e-04 | 18/47 (SW48, LoVo, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.684×** | -4.6 | 9e-04 | 19/44 (HS-578T, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.698×** | -4.3 | 0.002 | 19/46 (COLO 205, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.691×** | -4.3 | 0.002 | 19/45 (SW48, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.702×** | -4.1 | 0.004 | 20/44 (AsPC-1, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -4.0 | 0.006 | 10/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.733×** | -3.7 | 0.013 | 15/46 (LoVo, HT-29, …) | rises with dose | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.726×** | -3.7 | 0.013 | 18/43 (SNU-423, LS 180, …) | inconsistent across doses | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.738×** | -3.7 | 0.015 | 10/47 (SW48, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.744×** | -3.6 | 0.020 | 14/47 (RPMI-7951, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.026 | 13/46 (NCI-H1573, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.817×** | -3.4 | 0.026 | 18/47 (LoVo, RKO, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.822×** | -3.3 | 0.036 | 5/48 (SW 1088, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.601×** | -3.2 | 0.047 | 13/41 (HCT15, SW48, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.758×** | -3.1 | 0.067 | 13/43 (SW48, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.775×** | -3.1 | 0.069 | 15/45 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14627. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 13.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +21.0) | — |
| [[NCI-H460 (line)]] | wt | 11.6 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.91× (z +11.5) | — |
| [[A498 (line)]] | wt | 8.15 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +13.6) | — |
| [[A-172 (line)]] | wt | 17.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +18.4) | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +8.8) | [[Cobimetinib (drug)]] 5 µM 0.115× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +11.3) | [[Adagrasib (drug)]] 0.05 µM 0.604× (z -8.8) ⚠ position not correctable |
| [[NCI-H23 (line)]] | alt | 11.1 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.32× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.81× (z +18.7) | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0769× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 4.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.64× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 23.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.94× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 7.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 6.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +16.7) | — |
| [[SW 900 (line)]] | alt | 6.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 6.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +8.5) | — |
| [[SW48 (line)]] | wt | 29.3 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0883× (z -9.4) |
| [[SW480 (line)]] | alt | 8.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +10.6) | — |
| [[A-427 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14627), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB8]] | +0.73 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[LETM2]] | +0.72 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[KRT8P12]] | +0.70 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[ADAMTSL4-AS2]] | +0.70 | +0.71 / +0.64 | both halves | 7e-06 | same gene group |
| [[HCG20]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[ITGA2-AS1]] | +0.68 | +0.55 / +0.67 | both halves | 1e-05 | same gene group |
| [[LAT2]] | +0.67 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.66 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[KDM7A-DT]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[C11orf91]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[NABP1]] | +0.65 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[BTBD19]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM2]] | -0.60 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[CAPN7]] | -0.60 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[TADA1]] | -0.59 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[INTS10]] | -0.58 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[PRKRA]] | -0.58 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[MRPL34]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[RHOT1]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[PPP1R12B]] | -0.56 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[TNRC6A]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[HSF2]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[C15orf61]] ⚠ | -0.56 | -0.50 / -0.47 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MLLT10]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NOP14-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises NOP14-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[LUCAT1]] | B | LUCAT1 activity raises NOP14-AS1's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 1.49× lower at baseline in the lines without LUCAT1 | 0.077 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[EPHA2-AS1]] | B | EPHA2-AS1 activity raises NOP14-AS1's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 1.40× lower at baseline in the lines without EPHA2-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.851). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.7, -3.7); signed map (3.9, 31.6). **Vector** length 105, 24.8% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +19.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +6.0 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +5.9 | +3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +13.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +3.7 |
| fall | [[NG25 (drug)]] 5 µM |  | -4.2 | -3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.0 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.0 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.4 | -5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | NOP14 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4p16.3 — chr4:2,934,882-2,961,738 (+) |
| Ensembl biotype | lncRNA |
| Also known as | RES4-24; previously C4orf10 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:20205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20205) · Entrez [317648](https://www.ncbi.nlm.nih.gov/gene/317648) · Ensembl [ENSG00000249673](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249673)

## Data

Gene col 14627: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14627); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14627, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14627]; `tensor/DDL_lfc|DDL_z.npy` [14627]; `embed/gene_vectors.npy` [14627]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14627 or target_col == 14627). Every well: [[NOP14-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOP14-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
