---
symbol: "CCDC149"
type: "gene"
col: 11229
ensembl_id: "ENSG00000181982"
name: "coiled-coil domain containing 149"
location: "4p15.2"
module: 49
arm: "+"
pooled_cpm: 20.94
n_lines_expressing: 40
n_dd_up: 0
n_dd_down: 33
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# CCDC149

*coiled-coil domain containing 149* — 4p15.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.297× (z -23.2, q 0e+00, down in 32 of 37 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.444× (z -15.5, q 0e+00, down in 31 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF70]] (+0.56, fdr 1e-05), [[VSTM4]] (+0.52, fdr 1e-05), [[MINAR1]] (+0.52, fdr 2e-05); moves opposite to [[TGFBR3]] (-0.47, fdr 4e-05), [[PHF21A]] (-0.45, fdr 4e-05), [[MUC1]] (-0.45, fdr 4e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC01705]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11229.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.26× | +3.2 | 0.46 | 10/37 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.55× | +3.1 | 0.46 | 6/37 (A498, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11229.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.297×** | -23.2 | 0e+00 | 32/37 (J82, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.181×** | -23.2 | 0e+00 | 36/38 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.195×** | -22.2 | 0e+00 | 36/38 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.235×** | -19.6 | 0e+00 | 37/38 (LoVo, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.286×** | -17.0 | 0e+00 | 33/38 (H4, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.306×** | -16.0 | 0e+00 | 31/35 (LoVo, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.444×** | -15.5 | 0e+00 | 31/37 (RPMI-7951, SW 900, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.300×** | -15.2 | 0e+00 | 29/37 (A549, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.394×** | -12.6 | 1e-34 | 33/35 (H4, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.426×** | -11.6 | 4e-29 | 32/38 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.464×** | -10.4 | 2e-23 | 27/37 (NCI-H1792, H4, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.480×** | -9.9 | 1e-21 | 27/38 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.273×** | -9.2 | 2e-18 | 30/38 (HOP62, SW 900, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.512×** | -9.0 | 6e-18 | 25/35 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.504×** | -8.6 | 3e-16 | 25/34 (A-172, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.580×** | -7.4 | 6e-12 | 29/36 (RPMI-7951, NCI-H1792, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.610×** | -6.7 | 8e-10 | 23/36 (SNU-1, RKO, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.719×** | -6.3 | 8e-09 | 21/37 (HS-578T, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.421×** | -6.1 | 3e-08 | 27/37 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.641×** | -6.0 | 5e-08 | 21/38 (HS-578T, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.457×** | -5.5 | 8e-07 | 21/35 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.760×** | -3.7 | 0.005 | 13/37 (hTERT-HPNE, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.767×** | -3.6 | 0.007 | 12/35 (C32, SW 900, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.788×** | -3.2 | 0.027 | 13/37 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.782×** | -3.1 | 0.039 | 14/37 (SW 900, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.70 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11229. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 59.4 | 0 | 15 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0217× (z -22.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.0506× (z -17.6) |
| [[HOP62 (line)]] | alt | 25.5 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -20.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -11.2) |
| [[A-172 (line)]] | wt | 29.3 | 0 | 13 (9 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0420× (z -21.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -14.4) |
| [[LoVo (line)]] | wt | 31.5 | 0 | 13 (11 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0828× (z -19.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -15.1) |
| [[HS-578T (line)]] | alt | 39.2 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -20.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 34.3 | 0 | 12 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0638× (z -18.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.253× (z -9.3) |
| [[RKO (line)]] | wt | 33.4 | 0 | 11 (10 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0492× (z -18.6) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -13.8) |
| [[J82 (line)]] | alt | 37.2 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -23.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.179× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 12.9 | 0 | 10 (9 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.132× (z -14.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 39.4 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -19.5) |
| [[SW 900 (line)]] | alt | 70.7 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -16.5) |
| [[A498 (line)]] | wt | 32.3 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -20.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 47.3 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -17.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.5) |
| [[LS 180 (line)]] | wt | 45.6 | 0 | 9 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0718× (z -20.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.200× (z -12.5) |
| [[A549 (line)]] | wt | 16.3 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -17.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.198× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 35.6 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -16.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -12.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.3) |
| [[SNU-423 (line)]] | alt | 18.8 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -8.9) |
| [[SNU-1 (line)]] | wt | 26.1 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0564× (z -14.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HCT15 (line)]] | alt | 29.6 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -11.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0668× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~74% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 27.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -17.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0477× (z -12.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 18.2 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.138× (z -12.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0793× (z -13.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 7.94 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -17.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -14.6) |
| [[NCI-H2347 (line)]] | alt | 23.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -12.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -9.1) |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.116× (z -8.7) |
| [[C32 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -10.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H23 (line)]] | alt | 8.33 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.107× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~72% of this change |
| [[A-427 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.09 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.84 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11229), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF70]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[VSTM4]] | +0.52 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[MINAR1]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ZNF417]] | +0.50 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[AK5]] | +0.50 | +0.46 / +0.36 | both halves | 9e-05 |  |
| [[LINC00632]] | +0.49 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[GSDME]] | +0.49 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[TMED3]] | +0.48 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[FAM98A]] | +0.48 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[STAC]] | +0.46 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[FAM124A]] | +0.46 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[CHFR]] | +0.46 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGFBR3]] | -0.47 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[PHF21A]] | -0.45 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[MUC1]] | -0.45 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[SSBP2]] | -0.45 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[BRWD3]] | -0.44 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[SRGN]] | -0.44 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[PTCH1]] | -0.43 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[ROBO1]] | -0.43 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[TMEM123]] | -0.43 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[USP28]] | -0.42 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[USP6NL]] | -0.41 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[SCNN1A]] | -0.41 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01705]] | B | LINC01705 activity raises CCDC149's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 2.32× lower at baseline in the lines without LINC01705 | 0.010 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[STAC]] | B | STAC activity raises CCDC149's level | lines that do not express STAC (25) vs lines expressing it (25) | 2.24× lower at baseline in the lines without STAC | 0.011 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[CPQ]] | B | CPQ activity raises CCDC149's level | lines that do not express CPQ (15) vs lines expressing it (35) | 2.63× lower at baseline in the lines without CPQ | 0.036 | ⚠ within organs, on part of the lines; also absent: NETO2, LINC01725, KMO; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises CCDC149's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ADAM12]] | B | ADAM12 activity raises CCDC149's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 2.05× lower at baseline in the lines without ADAM12 | 0.065 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity strengthens CCDC149's drug response | lines that do not express TMEM92-AS1 (12) vs lines expressing it (26) | the lines without TMEM92-AS1 respond 0.64× as strongly (z diff +2.01); strongest at Digitoxin 5 µM: 0.43x vs 0.24x (z diff +2.9) | 0.081 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.449). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (56.7, 13.1); signed map (24.0, 52.2). **Vector** length 80.5, 19.9% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | -2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~72% of this change | +3.3 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | -1.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.3 | +0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +1.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.7 | -12.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.8 | -9.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -11.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.0 | -17.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -6.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 149 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:24,803,514-24,980,204 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761B107 |
| Matched by | ensembl_id |

UniProt [Q6ZUS6](https://www.uniprot.org/uniprotkb/Q6ZUS6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25405) · Entrez [91050](https://www.ncbi.nlm.nih.gov/gene/91050) · UniProt [Q6ZUS6](https://www.uniprot.org/uniprotkb/Q6ZUS6) · Ensembl [ENSG00000181982](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181982)

## Data

Gene col 11229: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11229); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11229, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11229]; `tensor/DDL_lfc|DDL_z.npy` [11229]; `embed/gene_vectors.npy` [11229]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11229 or target_col == 11229). Every well: [[CCDC149 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC149.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
