---
symbol: "ERRFI1"
type: "gene"
col: 3786
ensembl_id: "ENSG00000116285"
name: "ERBB receptor feedback inhibitor 1"
location: "1p36.23"
module: 113
arm: "+"
pooled_cpm: 605.8
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 43
n_dd_up_clean: 9
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 5
direction_downstream: 6
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# ERRFI1

*ERBB receptor feedback inhibitor 1* — 1p36.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.37× (z +5.6, q 1e-05, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.361× (z -18.0, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKAP12]] (+0.70, fdr 7e-06), [[ANGPTL4]] (+0.67, fdr 7e-06), [[SLC45A1]] (+0.67, fdr 1e-05); moves opposite to [[IQCK]] (-0.55, fdr 1e-05), [[TBC1D22B]] (-0.53, fdr 8e-05), [[EPB41]] (-0.52, fdr 1e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ERRFI1-DT]] → it (grade B ⚠); 6 go from it, the strongest it → [[PFKP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3786.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.6 | 1e-05 | 32/44 (SNU-423, SW480, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.43×** | +4.5 | 0.002 | 39/44 (KATO III, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.46×** | +4.4 | 0.002 | 31/43 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.38×** | +4.0 | 0.008 | 31/44 (LS 180, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.013 | 28/45 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.026 | 27/44 (LS 180, SNU-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.026 | 24/44 (SNU-423, HS-578T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.6 | 0.027 | 25/44 (MIA PaCa-2, SNU-1, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.040 | 24/44 (SNU-423, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.073 | 28/44 (LS 180, SHP-77, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.27× | +3.0 | 0.12 | 21/44 (SNU-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3786.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.361×** | -18.0 | 0e+00 | 42/45 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.392×** | -11.3 | 6e-27 | 41/43 (HepG2/C3A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.422×** | -10.4 | 5e-23 | 39/44 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.486×** | -8.7 | 5e-16 | 37/46 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.502×** | -8.6 | 8e-16 | 39/44 (A-172, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -8.0 | 1e-13 | 32/41 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.599×** | -7.8 | 4e-13 | 42/44 (SW480, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.646×** | -7.7 | 9e-13 | 29/44 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.541×** | -7.7 | 1e-12 | 40/44 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.564×** | -7.4 | 1e-11 | 39/46 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.560×** | -7.0 | 2e-10 | 39/43 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.574×** | -6.9 | 2e-10 | 34/45 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.580×** | -6.6 | 2e-09 | 38/44 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.608×** | -6.2 | 2e-08 | 41/44 (A-172, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.621×** | -6.0 | 9e-08 | 31/44 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.653×** | -6.0 | 9e-08 | 35/45 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.622×** | -5.9 | 1e-07 | 39/45 (A-172, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.713×** | -5.9 | 1e-07 | 40/44 (C32, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3786. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 376 | 18 | 3 | [[Budesonide (drug)]] 5 µM 3.68× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -15.1) |
| [[HOP62 (line)]] | alt | 1,435 | 1 (1 ⚠) | 14 (5 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.98× (z +10.0) ⚠ cell-cycle shift, explains ~15% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -20.5) |
| [[NCI-H23 (line)]] | alt | 1,147 | 0 | 15 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -22.9) |
| [[HepG2_C3A (line)]] | wt | 2,536 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -28.3) |
| [[LOX-IMVI (line)]] | wt | 882 | 0 | 14 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -20.7) |
| [[MIA PaCa-2 (line)]] | alt | 1,729 | 3 (1 ⚠) | 11 (4 ⚠) | [[Harringtonine (drug)]] 0.05 µM 2.77× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -28.0) |
| [[PANC-1 (line)]] | alt | 1,460 | 0 | 14 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -29.3) |
| [[A-172 (line)]] | wt | 483 | 0 | 13 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -17.5) |
| [[H4 (line)]] | wt | 551 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -15.1) |
| [[hTERT-HPNE (line)]] | wt | 518 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -17.1) |
| [[NCI-H2347 (line)]] | alt | 688 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -18.3) |
| [[NCI-H1573 (line)]] | alt | 860 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -17.1) |
| [[A-427 (line)]] | wt | 788 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.245× (z -15.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.562× (z -9.4) |
| [[HCT15 (line)]] | alt | 975 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -15.7) |
| [[HT-29 (line)]] | alt | 710 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -18.5) |
| [[Panc 03.27 (line)]] | alt | 520 | 1 (1 ⚠) | 6 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.47× (z +9.5) ⚠ cell-cycle shift, explains ~15% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -15.8) |
| [[C32 (line)]] | wt | 210 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +12.8) | [[Cobimetinib (drug)]] 5 µM 0.179× (z -11.7) |
| [[HS-578T (line)]] | alt | 638 | 1 | 5 (1 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 3.16× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -14.7) |
| [[NCI-H2030 (line)]] | alt | 670 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -20.4) |
| [[NCI-H460 (line)]] | wt | 439 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 617 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -10.8) |
| [[Hs 766T (line)]] | wt | 194 | 4 | 0 | [[Clobetasol propionate (drug)]] 5 µM 3.27× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 427 | 0 | 4 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.639× (z -11.0) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.251× (z -9.8) |
| [[SW 900 (line)]] | alt | 537 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -14.9) |
| [[AsPC-1 (line)]] | alt | 849 | 1 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +9.3) ⚠ cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -12.2) |
| [[CHP-212 (line)]] | wt | 338 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 428 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.342× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 169 | 0 | 3 | — | [[Trametinib (drug)]] 5 µM 0.341× (z -9.1) |
| [[SW 1088 (line)]] | alt | 1,428 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -12.6) |
| [[A498 (line)]] | wt | 294 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -14.8) |
| [[COLO 205 (line)]] | alt | 523 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.201× (z -13.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 379 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -8.9) |
| [[LoVo (line)]] | wt | 264 | 0 | 2 | — | [[Ponatinib (drug)]] 5 µM 0.439× (z -9.1) |
| [[SHP-77 (line)]] | alt | 300 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -13.1) |
| [[SNU-1 (line)]] | wt | 177 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.49× (z +10.2) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[SW480 (line)]] | alt | 295 | 0 | 2 | — | [[Trametinib (drug)]] 0.5 µM 0.429× (z -9.6) |
| [[A549 (line)]] | wt | 514 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -19.7) |
| [[LS 180 (line)]] | wt | 355 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.04× (z +9.0) | — |
| [[SW 1271 (line)]] | alt | 625 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -10.6) |
| [[AN3 CA (line)]] | alt | 121 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.8 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 330 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 766 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 555 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 116 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 126 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 240 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3786), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP12]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[ANGPTL4]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[SLC45A1]] | +0.67 | +0.60 / +0.56 | both halves | 1e-05 | STRING 499 |
| [[MCL1]] | +0.66 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[NIBAN2]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[PHC2]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[SERPINE1]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[PTPN12]] | +0.63 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ELL2]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[MT2A]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[TBC1D8]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCK]] | -0.55 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[TBC1D22B]] | -0.53 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[EPB41]] | -0.52 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[DENND2B]] | -0.51 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[GPRC5B]] | -0.51 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[P4HTM]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ZSCAN31]] | -0.49 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[FAM111A-DT]] | -0.48 | -0.55 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERRFI1-DT]] | B | ERRFI1-DT activity raises ERRFI1's level | lines that do not express ERRFI1-DT (13) vs lines expressing it (37) | 2.67× lower at baseline in the lines without ERRFI1-DT | 0.010 | ⚠ within organs, on part of the lines; also absent: GCAWKR; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ERRFI1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.6% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds |
| [[GPRC5B]] | B | GPRC5B activity weakens ERRFI1's drug response | lines that do not express GPRC5B (25) vs lines expressing it (21) | the lines without GPRC5B respond 1.43× as strongly (z diff -1.13); strongest at Dinaciclib 5 µM: 0.44x vs 0.68x (z diff -3.7) | 0.046 | ⚠ within organs, on part of the lines; also absent: PALMD, FYB1, AK5; target measured in part of the lines; both ways; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises ERRFI1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PFKP]] | C | PFKP activity raises ERRFI1's level | lines that do not express PFKP (3) vs lines expressing it (47) | 3.32× lower at baseline in the lines without PFKP | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent; its own permutation p |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PFKP]] | C | ERRFI1 activity raises PFKP's level | lines that do not express ERRFI1 (4) vs lines expressing it (46) | 3.18× lower at baseline in the lines without ERRFI1 | 0.010 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000256029; maybe low, not absent |
| [[DOCK5]] | C | ERRFI1 activity raises DOCK5's level | lines that do not express ERRFI1 (4) vs lines expressing it (46) | 2.90× lower at baseline in the lines without ERRFI1 | 0.072 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000256029; maybe low, not absent |
| [[PTPN12]] | C | ERRFI1 activity strengthens PTPN12's drug response | lines that do not express ERRFI1 (4) vs lines expressing it (45) | the lines without ERRFI1 respond 0.45× as strongly (z diff +2.98); strongest at Idarubicin (hydrochloride) 5 µM: 0.86x vs 0.51x (z diff +5.3) | 0.081 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000256029; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Trametinib (drug)]] 0.05 µM | C | ERRFI1 activity lowers the cells' numbers under Trametinib 0.05 µM (makes them more sensitive) | lines that do not express ERRFI1 (4) vs lines expressing it (44) | the lines without ERRFI1: 1.18× the cells of the other lines | 0.088 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000256029; maybe low, not absent |
| cells under [[Pimozide (drug)]] 0.5 µM | C | ERRFI1 activity raises the cells' numbers under Pimozide 0.5 µM (protects the cells) | lines that do not express ERRFI1 (4) vs lines expressing it (44) | the lines without ERRFI1: 0.75× the cells of the other lines | 0.093 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000256029; maybe low, not absent |
| cells under [[Mebendazole (drug)]] 5 µM | C | ERRFI1 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express ERRFI1 (4) vs lines expressing it (44) | the lines without ERRFI1: 0.63× the cells of the other lines | 0.099 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000256029; maybe low, not absent |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.1, 10.9); signed map (14.0, 36.2). **Vector** length 154, 60.7% of its response variance represented; |z| ≥ 3 in 2,194 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metallothioneins bind metals* (reactome, mean cos +0.52 to 5); *metallothionein* (control, mean cos +0.52 to 5); *Response to metal ions* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +10.0 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.7 | +5.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +8.5 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.9 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +3.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +5.5 | +3.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +5.4 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.4 | +4.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +5.3 | +1.9 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -9.7 | -7.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -8.7 | -7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -8.5 | -8.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -8.5 | -7.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -8.2 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.8 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | ERBB receptor feedback inhibitor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.23 — chr1:8,004,404-8,026,309 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MIG-6, GENE-33, RALT |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, HYPOXIA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJM3](https://www.uniprot.org/uniprotkb/Q9UJM3) (ERBB receptor feedback inhibitor 1):

> Negative regulator of EGFR signaling in skin morphogenesis. Acts as a negative regulator for several EGFR family members, including ERBB2, ERBB3 and ERBB4. Inhibits EGFR catalytic activity by interfering with its dimerization. Inhibits autophosphorylation of EGFR, ERBB2 and ERBB4. Important for normal keratinocyte proliferation and differentiation. Plays a role in modulating the response to steroid hormones in the uterus. Required for normal response to progesterone in the uterus and for …

**Summary**, from NCBI Gene [54206](https://www.ncbi.nlm.nih.gov/gene/54206):

> ERRFI1 is a cytoplasmic protein whose expression is upregulated with cell growth (Wick et al., 1995 [PubMed 7641805]). It shares significant homology with the protein product of rat gene-33, which is induced during cell stress and mediates cell signaling (Makkinje et al., 2000 [PubMed 10749885]; Fiorentino et al., 2000 [PubMed 11003669]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18185) · Entrez [54206](https://www.ncbi.nlm.nih.gov/gene/54206) · UniProt [Q9UJM3](https://www.uniprot.org/uniprotkb/Q9UJM3) · Ensembl [ENSG00000116285](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116285)

## Data

Gene col 3786: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3786); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3786, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3786]; `tensor/DDL_lfc|DDL_z.npy` [3786]; `embed/gene_vectors.npy` [3786]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3786 or target_col == 3786). Every well: [[ERRFI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERRFI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
