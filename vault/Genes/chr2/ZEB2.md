---
symbol: "ZEB2"
type: "gene"
col: 9815
ensembl_id: "ENSG00000169554"
name: "zinc finger E-box binding homeobox 2"
location: "2q22.3"
module: 121
arm: "+"
pooled_cpm: 123.74
n_lines_expressing: 23
n_dd_up: 21
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 22
direction_downstream: 31
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# ZEB2

*zinc finger E-box binding homeobox 2* — 2q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.54× (z +10.7, q 7e-24, up in 15 of 21 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.79× (z +10.2, q 5e-22, up in 17 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.414× (z -15.5, q 0e+00, down in 20 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBMS3]] (+0.72, fdr 7e-06), [[ABI3BP]] (+0.70, fdr 7e-06), [[NLGN4Y]] (+0.68, fdr 7e-06); moves opposite to [[CTNNBIP1]] (-0.46, fdr 5e-05), [[ANXA11]] (-0.45, fdr 8e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[PRRX1]] → it (grade C ⚠); 31 go from it, the strongest it → [[PLD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9815.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.54×** | +10.7 | 7e-24 | 15/21 (A498, HOP62, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +10.2 | 5e-22 | 17/21 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +8.6 | 2e-15 | 16/21 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +6.0 | 2e-07 | 0/22 | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +5.7 | 1e-06 | 13/21 (C32, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +5.5 | 3e-06 | 10/21 (hTERT-HPNE, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.37×** | +5.5 | 3e-06 | 0/21 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.9 | 8e-05 | 0/19 | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.3 | 0.001 | 3/21 (SK-MEL-2, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +4.2 | 0.001 | 16/23 (C32, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +4.1 | 0.002 | 11/22 (NCI-H460, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.002 | 9/22 (C32, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.25×** | +4.0 | 0.003 | 1/21 (H4) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.25×** | +3.9 | 0.003 | 16/21 (A498, C32, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.004 | 0/21 | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.20× | +3.8 | 0.005 | 10/21 (C32, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.006 | 7/21 (A498, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.009 | 12/21 (C32, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.040 | 0/23 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Alpelisib (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.041 | 3/20 (HOP62, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +2.9 | 0.085 | 0/22 | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9815.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.414×** | -15.5 | 0e+00 | 20/21 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.457×** | -13.7 | 2e-40 | 21/21 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.470×** | -13.2 | 2e-37 | 21/21 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.648×** | -7.6 | 5e-12 | 15/21 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Larotrectinib (drug)]] 5 µM |  | **0.806×** | -5.3 | 1e-05 | 17/21 (A498, A-172, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.634×** | -4.2 | 0.003 | 11/22 (A-172, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.782×** | -4.1 | 0.003 | 16/21 (A-172, NCI-H460, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.793×** | -4.0 | 0.004 | 2/21 (A498, A549) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.805×** | -3.8 | 0.010 | 17/21 (NCI-H460, J82, …) | top dose only |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.809×** | -3.6 | 0.021 | 1/20 (SW 1271) | top dose only |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.834× | -3.2 | 0.080 | 0/21 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.836× | -3.1 | 0.080 | 9/21 (A-172, J82, …) | rises with dose |  |
| [[Ivermectin (drug)]] 5 µM |  | 0.836× | -3.1 | 0.080 | 0/21 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9815. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 230 | 12 (2 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.25× (z +12.4) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.34× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.217× (z -13.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 335 | 2 (1 ⚠) | 11 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.0512× (z -33.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0928× (z -27.0) |
| [[hTERT-HPNE (line)]] | wt | 349 | 3 (1 ⚠) | 9 (7 ⚠) | [[Harringtonine (drug)]] 5 µM 4.17× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -17.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.249× (z -11.9) |
| [[J82 (line)]] | alt | 442 | 2 (1 ⚠) | 9 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.39× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.117× (z -22.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.216× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 641 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -24.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.166× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 591 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0650× (z -23.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.132× (z -17.1) |
| [[A498 (line)]] | wt | 229 | 5 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 7.42× (z +19.2) | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -15.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 265 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.104× (z -20.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.121× (z -18.6) |
| [[RPMI-7951 (line)]] | alt | 377 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -21.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.202× (z -15.4) |
| [[SNU-423 (line)]] | alt | 151 | 2 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +15.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.49× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.170× (z -15.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.374× (z -8.5) |
| [[SW 900 (line)]] | alt | 210 | 2 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.239× (z -12.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.300× (z -10.4) |
| [[HOP62 (line)]] | alt | 170 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +15.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.35× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.165× (z -15.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.309× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 190 | 1 (1 ⚠) | 4 (4 ⚠) | [[Trametinib (drug)]] 5 µM 2.63× (z +9.3) ⚠ cell-cycle shift, explains ~18% of this change | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 200 | 2 (1 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.30× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -13.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.286× (z -10.3) |
| [[NCI-H661 (line)]] | alt | 762 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -11.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[H4 (line)]] | wt | 147 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.4) ⚠ cell-cycle shift, explains ~32% of this change | [[Panobinostat (drug)]] 5 µM 0.223× (z -10.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[CHP-212 (line)]] | wt | 143 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -9.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 1088 (line)]] | alt | 232 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0438× (z -13.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 69.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +8.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.08 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.80 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.99 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.45 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.15 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.33 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.60 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.0 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.88 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.16 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.66 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.32 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9815), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBMS3]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ABI3BP]] | +0.70 | +0.63 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[NLGN4Y]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[TRPC4]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[MSC]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[UTY]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[TEX41]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ARHGAP24]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[JAM2]] | +0.63 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[LINC02335]] | +0.62 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[NR3C1]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[MIR137HG]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNBIP1]] | -0.46 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[ANXA11]] | -0.45 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 0, C 22. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRRX1]] | C | PRRX1 activity raises ZEB2's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 5.81× lower at baseline in the lines without PRRX1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[TEX41]] | C | TEX41 activity raises ZEB2's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 8.30× lower at baseline in the lines without TEX41 | 0.013 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12; co-absent with the target |
| [[FGF2]] | C | FGF2 activity raises ZEB2's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 6.29× lower at baseline in the lines without FGF2 | 0.014 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2; co-absent with the target |
| [[PLAGL1]] | C | PLAGL1 activity raises ZEB2's level | lines that do not express PLAGL1 (22) vs lines expressing it (28) | 3.58× lower at baseline in the lines without PLAGL1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, GJA1, SOX5; co-absent with the target |
| [[JAM2]] | C | JAM2 activity raises ZEB2's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 7.03× lower at baseline in the lines without JAM2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R; co-absent with the target |
| [[FBXL7]] | C | FBXL7 activity raises ZEB2's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 5.47× lower at baseline in the lines without FBXL7 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[ADAMTS2]] | C | ADAMTS2 activity raises ZEB2's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 7.32× lower at baseline in the lines without ADAMTS2 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |
| [[IL7R]] | C | IL7R activity raises ZEB2's level | lines that do not express IL7R (30) vs lines expressing it (20) | 7.80× lower at baseline in the lines without IL7R | 0.031 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1; co-absent with the target |
| [[SHISAL1]] | C | SHISAL1 activity raises ZEB2's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 6.27× lower at baseline in the lines without SHISAL1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |
| [[ABI3BP]] | C | ABI3BP activity raises ZEB2's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 5.47× lower at baseline in the lines without ABI3BP | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |
| [[UTY]] | C | UTY activity raises ZEB2's level | lines that do not express UTY (31) vs lines expressing it (19) | 4.41× lower at baseline in the lines without UTY | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[COL8A1]] | C | COL8A1 activity raises ZEB2's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 6.29× lower at baseline in the lines without COL8A1 | 0.044 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 3, C 28. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLD1]] | B | ZEB2 activity raises PLD1's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 2.58× lower at baseline in the lines without ZEB2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16 |
| [[CTNNBIP1]] | B | ZEB2 activity lowers CTNNBIP1's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 1.41× higher at baseline in the lines without ZEB2 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16 |
| [[DSE]] | B | ZEB2 activity raises DSE's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 2.79× lower at baseline in the lines without ZEB2 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16 |
| [[FBXL7]] | C | ZEB2 activity raises FBXL7's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 7.14× lower at baseline in the lines without ZEB2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[FGF2]] | C | ZEB2 activity raises FGF2's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 3.66× lower at baseline in the lines without ZEB2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[RBMS3]] | C | ZEB2 activity raises RBMS3's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 7.61× lower at baseline in the lines without ZEB2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[TNFAIP6]] | C | ZEB2 activity raises TNFAIP6's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 3.86× lower at baseline in the lines without ZEB2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[ADAMTS2]] | C | ZEB2 activity raises ADAMTS2's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 4.12× lower at baseline in the lines without ZEB2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[AKT3]] | C | ZEB2 activity raises AKT3's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 6.94× lower at baseline in the lines without ZEB2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[UTY]] | C | ZEB2 activity raises UTY's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 5.46× lower at baseline in the lines without ZEB2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[IL7R]] | C | ZEB2 activity raises IL7R's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 4.91× lower at baseline in the lines without ZEB2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[JAM2]] | C | ZEB2 activity raises JAM2's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 3.70× lower at baseline in the lines without ZEB2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.1, 24.4); signed map (42.0, 25.7). **Vector** length 113, 42.7% of its response variance represented; |z| ≥ 3 in 785 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +7.0 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.2 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | -0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +1.3 |
| fall | [[Ipatasertib (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -2.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger E-box binding homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q22.3 — chr2:144,364,364-144,521,057 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0569, SIP-1, SIP1; previously ZFHX1B |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZF class homeoboxes and pseudogenes |
| Reactome | 16 pathways, smallest: Formation of the posterior neural plate; Formation of the anterior neural plate; Regulation of CDH11 gene transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [O60315](https://www.uniprot.org/uniprotkb/O60315) (Zinc finger E-box-binding homeobox 2):

> Transcriptional inhibitor that binds to DNA sequence 5'-CACCT-3' in different promoters. Represses transcription of E-cadherin. Represses expression of MEOX2.

**Summary**, from NCBI Gene [9839](https://www.ncbi.nlm.nih.gov/gene/9839):

> The protein encoded by this gene is a member of the Zfh1 family of 2-handed zinc finger/homeodomain proteins. It is located in the nucleus and functions as a DNA-binding transcriptional repressor that interacts with activated SMADs. Mutations in this gene are associated with Hirschsprung disease/Mowat-Wilson syndrome. Alternatively spliced transcript variants have been found for this gene.[provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:14881](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14881) · Entrez [9839](https://www.ncbi.nlm.nih.gov/gene/9839) · UniProt [O60315](https://www.uniprot.org/uniprotkb/O60315) · Ensembl [ENSG00000169554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169554)

## Data

Gene col 9815: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9815); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9815, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9815]; `tensor/DDL_lfc|DDL_z.npy` [9815]; `embed/gene_vectors.npy` [9815]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9815 or target_col == 9815). Every well: [[ZEB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZEB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
