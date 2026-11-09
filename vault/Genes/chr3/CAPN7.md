---
symbol: "CAPN7"
type: "gene"
col: 5199
ensembl_id: "ENSG00000131375"
name: "calpain 7"
location: "3p25.1"
module: 54
arm: "+"
pooled_cpm: 95.75
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# CAPN7

*calpain 7* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.43× (z +10.1, q 3e-21, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.622× (z -18.7, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIN7B]] (+0.66, fdr 1e-05), [[SLC17A5]] (+0.64, fdr 1e-05), [[C15orf61]] (+0.63, fdr 3e-05, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[MIA3]] (+0.61, fdr 2e-05); moves opposite to [[KRT8P12]] (-0.62, fdr 2e-05), [[BHLHE40-AS1]] (-0.62, fdr 3e-05), [[ZEB1-AS1]] (-0.61, fdr 9e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +10.1 | 3e-21 | 39/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +6.9 | 2e-09 | 26/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +6.3 | 5e-08 | 27/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +6.1 | 2e-07 | 27/48 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.23×** | +6.0 | 3e-07 | 24/48 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +5.8 | 7e-07 | 24/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.22×** | +5.6 | 1e-06 | 23/48 (SK-MEL-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.40×** | +5.0 | 4e-05 | 25/47 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.5 | 4e-04 | 17/48 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.3 | 8e-04 | 14/48 (SK-MEL-2, HOP62, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.10× | +3.7 | 0.010 | 22/48 (HEC-1-A, NCI-H23, …) | rises with dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.012 | 9/49 (NCI-H23, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.012 | 15/49 (LOX-IMVI, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.6 | 0.012 | 16/48 (SK-MEL-2, NCI-H23, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.5 | 0.019 | 16/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.12× | +3.0 | 0.072 | 9/49 (C-33 A, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5199.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -18.7 | 0e+00 | 44/49 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -10.7 | 2e-24 | 40/50 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.675×** | -10.3 | 2e-22 | 30/45 (A-172, A549, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.688×** | -10.1 | 5e-22 | 26/44 (HT-29, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.818×** | -8.0 | 2e-13 | 28/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.772×** | -7.3 | 3e-11 | 29/49 (C32, NCI-H460, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.774×** | -7.2 | 4e-11 | 32/48 (A549, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.771×** | -7.0 | 1e-10 | 30/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.829×** | -5.3 | 8e-06 | 23/48 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.833×** | -5.0 | 4e-05 | 22/48 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.828×** | -4.9 | 4e-05 | 21/47 (SW 900, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | 0.835× | -4.9 | 5e-05 | 20/47 (RKO, SW 900, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.846× | -4.7 | 1e-04 | 21/48 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.957× | -4.2 | 0.001 | 0/50 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.875× | -3.7 | 0.007 | 14/48 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 5 µM |  | 0.921× | -3.2 | 0.040 | 3/48 (A498, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 138 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -22.3) |
| [[HOP62 (line)]] | alt | 135 | 1 | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -16.7) |
| [[SW480 (line)]] | alt | 103 | 2 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -11.8) |
| [[A-172 (line)]] | wt | 115 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 148 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +12.5) ⚠ cell-cycle shift, explains ~17% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -10.6) |
| [[LS 180 (line)]] | wt | 121 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -11.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 96.2 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -14.9) |
| [[C32 (line)]] | wt | 89.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -11.9) |
| [[HS-578T (line)]] | alt | 111 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 80.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.4) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[NCI-H460 (line)]] | wt | 80.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.67× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.59× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[RKO (line)]] | wt | 109 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -11.1) |
| [[SNU-423 (line)]] | alt | 111 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -13.4) |
| [[A-427 (line)]] | wt | 114 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.98× (z +10.8) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[AN3 CA (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -9.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 120 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -9.4) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -8.9) |
| [[SNU-1 (line)]] | wt | 170 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -10.3) |
| [[SW 900 (line)]] | alt | 96.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -14.7) |
| [[SW48 (line)]] | wt | 124 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -9.2) ⚠ cell-cycle shift, explains ~16% of this change |
| [[A498 (line)]] | wt | 57.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -12.7) |
| [[A549 (line)]] | wt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -13.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 67.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -16.0) |
| [[C-33 A (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +9.6) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[CHP-212 (line)]] | wt | 92.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[HCT15 (line)]] | alt | 137 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 94.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -8.5) |
| [[Hs 766T (line)]] | wt | 73.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -9.6) |
| [[HT-29 (line)]] | alt | 63.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -10.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 85.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -9.4) |
| [[KATO III (line)]] | alt | 84.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.7) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 94.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -10.3) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H1573 (line)]] | alt | 59.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 82.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -12.1) |
| [[PANC-1 (line)]] | alt | 64.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.655× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 95.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -9.1) |
| [[SW1417 (line)]] | alt | 141 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -11.0) |
| [[BT-474 (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 85.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 98.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 106 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 69.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 194 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7B]] | +0.66 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SLC17A5]] | +0.64 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[C15orf61]] ⚠ | +0.63 | +0.45 / +0.57 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MIA3]] | +0.61 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ZNF652]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PPP1R12B]] | +0.60 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[COX14]] | +0.59 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[TUT4]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[DHX29]] | +0.59 | +0.38 / +0.68 | both halves | 7e-05 |  |
| [[MAP2K7]] | +0.58 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[KRT10]] ⚠ | +0.58 | +0.51 / +0.46 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NME3]] | +0.58 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[UBE2B]] | +0.57 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[TTC38]] | +0.57 | +0.43 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT8P12]] | -0.62 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[BHLHE40-AS1]] | -0.62 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[ZEB1-AS1]] | -0.61 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[CCDC200]] | -0.60 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[PPIA]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[NOP14-AS1]] | -0.60 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[DDX39B]] | -0.59 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[HCG20]] | -0.58 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[MYOSLID]] | -0.58 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[PIGW]] | -0.58 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[RALY-AS1]] | -0.58 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[ITGA2-AS1]] | -0.57 | -0.41 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CAPN7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FMNL3]] | B | FMNL3 activity raises CAPN7's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 1.42× lower at baseline in the lines without FMNL3 | 0.016 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (14.0, -42.3); signed map (-46.5, 16.2). **Vector** length 120, 32.8% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.4 | +5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +6.0 |
|  | [[NG25 (drug)]] 5 µM |  | +4.6 | +5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +3.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.8 | -18.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -7.2 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.0 | -8.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -7.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | calpain 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:15,206,152-15,252,916 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PalBH |
| Gene groups (HGNC) | Calpains |
| Reactome | 2 pathways, smallest: Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6W3](https://www.uniprot.org/uniprotkb/Q9Y6W3) (Calpain-7):

> Calcium-regulated non-lysosomal thiol-protease.

**Summary**, from NCBI Gene [23473](https://www.ncbi.nlm.nih.gov/gene/23473):

> Calpains are ubiquitous, well-conserved family of calcium-dependent, cysteine proteases. The calpain proteins are heterodimers consisting of an invariant small subunit and variable large subunits. The large subunit possesses a cysteine protease domain, and both subunits possess calcium-binding domains. Calpains have been implicated in neurodegenerative processes, as their activation can be triggered by calcium influx and oxidative stress. The function of the protein encoded by this gene is not …

**Accessions** — [HGNC:1484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1484) · Entrez [23473](https://www.ncbi.nlm.nih.gov/gene/23473) · UniProt [Q9Y6W3](https://www.uniprot.org/uniprotkb/Q9Y6W3) · Ensembl [ENSG00000131375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131375)

## Data

Gene col 5199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5199); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5199]; `tensor/DDL_lfc|DDL_z.npy` [5199]; `embed/gene_vectors.npy` [5199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5199 or target_col == 5199). Every well: [[CAPN7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPN7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
