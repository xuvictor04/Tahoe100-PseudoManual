---
symbol: "RIPK1"
type: "gene"
col: 5996
ensembl_id: "ENSG00000137275"
name: "receptor interacting serine/threonine kinase 1"
location: "6p25.2"
module: 57
arm: "-"
pooled_cpm: 102.22
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# RIPK1

*receptor interacting serine/threonine kinase 1* — 6p25.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H460 4.13×, NCI-H1792 3.91×, CFPAC-1 2.19×, NCI-H2030 2.16×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 3.42×; ⚠ cell-cycle shift, explains ~37% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (NCI-H460 1.82×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.418× (z -13.7, q 5e-40, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLNRD1]] (+0.59, fdr 1e-05), [[CRK]] (+0.57, fdr 1e-05), [[MIR22HG]] (+0.56, fdr 1e-05); moves opposite to [[TNRC6A]] (-0.62, fdr 8e-06), [[RPP30]] (-0.60, fdr 1e-05), [[ATP5F1C]] (-0.58, fdr 2e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5996.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H460 4.13×, NCI-H1792 3.91×, CFPAC-1 2.19×, NCI-H2030 2.16×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 3.42×; ⚠ cell-cycle shift, explains ~37% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (NCI-H460 1.82×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.23× | +3.3 | 0.33 | 19/47 (hTERT-HPNE, HOP62, …) | two highest doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.3 | 0.33 | 16/48 (NCI-H460, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5996.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.418×** | -13.7 | 5e-40 | 41/48 (HT-29, BT-474, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.498×** | -10.9 | 2e-25 | 35/48 (KATO III, SNU-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.600×** | -8.0 | 2e-13 | 37/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.616×** | -7.6 | 4e-12 | 36/48 (HT-29, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.619×** | -7.5 | 6e-12 | 36/48 (H4, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.411×** | -7.3 | 3e-11 | 42/49 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.644×** | -6.9 | 4e-10 | 34/48 (RKO, SW480, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.564×** | -6.8 | 1e-09 | 36/47 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.747×** | -6.5 | 6e-09 | 32/48 (COLO 205, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.667×** | -6.4 | 1e-08 | 34/48 (A-172, J82, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.682×** | -6.0 | 9e-08 | 31/48 (LoVo, NCI-H1792, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.704×** | -5.5 | 2e-06 | 36/48 (A-172, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -5.4 | 4e-06 | 29/50 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.713×** | -5.3 | 5e-06 | 31/48 (SK-MEL-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **0.717×** | -5.2 | 7e-06 | 31/49 (A-172, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.732×** | -4.9 | 3e-05 | 30/48 (HepG2/C3A, A-172, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.830×** | -4.1 | 0.001 | 22/48 (RKO, AsPC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.622×** | -3.9 | 0.003 | 27/48 (SNU-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.626×** | -3.9 | 0.003 | 30/47 (AsPC-1, A-172, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.808×** | -3.3 | 0.021 | 23/48 (SNU-423, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.816×** | -3.2 | 0.035 | 19/48 (A-172, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5996. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 232 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -17.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.305× (z -11.3) |
| [[HT-29 (line)]] | alt | 134 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 132 | 0 | 7 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -12.1) |
| [[H4 (line)]] | wt | 79.2 | 0 | 5 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.110× (z -16.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.190× (z -12.2) |
| [[RKO (line)]] | wt | 117 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -12.6) |
| [[SNU-1 (line)]] | wt | 74.4 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -14.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.275× (z -9.6) |
| [[A-427 (line)]] | wt | 76.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.156× (z -9.8) |
| [[BT-474 (line)]] | alt | 68.3 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -15.6) |
| [[COLO 205 (line)]] | alt | 133 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -13.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.279× (z -11.9) |
| [[HOP62 (line)]] | alt | 115 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -14.8) |
| [[HS-578T (line)]] | alt | 102 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -11.5) |
| [[KATO III (line)]] | alt | 96.8 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.263× (z -14.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.320× (z -12.7) |
| [[LoVo (line)]] | wt | 143 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -14.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.446× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 89.7 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -13.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.309× (z -12.1) |
| [[SW480 (line)]] | alt | 74.6 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -14.8) |
| [[A549 (line)]] | wt | 84.4 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -11.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.269× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 116 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -9.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[LOX-IMVI (line)]] | wt | 77.8 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 104 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +18.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.296× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 72.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +23.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.82× (z +9.9) | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0801× (z -9.6) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[crizotinib (drug)]] 0.05 µM 0.0878× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 145 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.371× (z -11.8) |
| [[LS 180 (line)]] | wt | 92.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.423× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change |
| [[MIA PaCa-2 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.351× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change |
| [[PANC-1 (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[SW1417 (line)]] | alt | 89.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 128 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 66.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.486× (z -9.1) |
| [[Hs 766T (line)]] | wt | 86.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[NCI-H1573 (line)]] | alt | 88.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[NCI-H2030 (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 90.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.384× (z -9.5) |
| [[A498 (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 113 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5996), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLNRD1]] | +0.59 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[CRK]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[MIR22HG]] | +0.56 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[C21orf91-OT1]] | +0.55 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[MMP25]] | +0.55 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[THUMPD3-AS1]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ADAMTSL4-AS2]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[DUSP5-DT]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[EGR3]] | +0.53 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CYFIP1]] | +0.53 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[IQCJ-SCHIP1]] | +0.51 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PILRA]] | +0.51 | +0.48 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6A]] | -0.62 | -0.61 / -0.58 | both halves | 8e-06 |  |
| [[RPP30]] | -0.60 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[ATP5F1C]] | -0.58 | -0.61 / -0.49 | both halves | 2e-05 |  |
| [[HBS1L]] | -0.58 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[MINDY3]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 | STRING 555 |
| [[USP30]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 | pathway: Deubiquitination |
| [[NTPCR]] | -0.56 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[TMEM185A]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[SLC25A36]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[TMEM218]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[TRIT1]] | -0.54 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[STAM]] | -0.53 | -0.48 / -0.45 | both halves | 3e-05 | pathway: Deubiquitination |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.6, -7.7); signed map (8.7, 12.9). **Vector** length 108, 33.6% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.9 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.4 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +3.3 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.9 | -4.9 |
|  | [[NG25 (drug)]] 5 µM |  | -5.1 | -3.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.1 | -6.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.3 | -4.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.8 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.5 | -1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | receptor interacting serine/threonine kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:3,063,824-3,115,187 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RIP, RIP1, RIP-1 |
| Gene groups (HGNC) | Ripoptosome; Receptor interacting serine/threonine kinase family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, INTERFERON_GAMMA_RESPONSE |
| Reactome | 48 pathways, smallest: Microbial modulation of RIPK1-mediated regulated necrosis; TLR3-mediated TICAM1-dependent programmed cell death; Defective RIPK1-mediated regulated necrosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13546](https://www.uniprot.org/uniprotkb/Q13546) (Receptor-interacting serine/threonine-protein kinase 1):

> Serine-threonine kinase which is a key regulator of TNF-mediated apoptosis, necroptosis and inflammatory pathways. Exhibits kinase activity-dependent functions that regulate cell death (apoptosis and necroptosis) and kinase-independent scaffold functions regulating inflammatory signaling and cell survival. Upon binding of TNF to TNFR1 (TNFR1A or TNFR1B), RIPK1 is recruited by TNFR1 to the complex I (TNF-R1 signaling complex also known as TNF-RSC) as a scaffold protein. The activity of complex I …

**Summary**, from NCBI Gene [8737](https://www.ncbi.nlm.nih.gov/gene/8737):

> This gene encodes a member of the receptor-interacting protein (RIP) family of serine/threonine protein kinases. The encoded protein plays a role in inflammation and cell death in response to tissue damage, pathogen recognition, and as part of developmental regulation. RIPK1/RIPK3 kinase-mediated necrosis is referred to as necroptosis. Genetic disruption of this gene in mice results in death shortly after birth. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:10019](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10019) · Entrez [8737](https://www.ncbi.nlm.nih.gov/gene/8737) · UniProt [Q13546](https://www.uniprot.org/uniprotkb/Q13546) · Ensembl [ENSG00000137275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137275)

## Data

Gene col 5996: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5996); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5996, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5996]; `tensor/DDL_lfc|DDL_z.npy` [5996]; `embed/gene_vectors.npy` [5996]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5996 or target_col == 5996). Every well: [[RIPK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIPK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
