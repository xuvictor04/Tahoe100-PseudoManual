---
symbol: "EHD4"
type: "gene"
col: 2403
ensembl_id: "ENSG00000103966"
name: "EH domain containing 4"
location: "15q15.1"
module: 184
arm: "+"
pooled_cpm: 93.32
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 32
n_dd_up_clean: 4
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# EHD4

*EH domain containing 4* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.79× (z +12.3, q 3e-32, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.484× (z -21.7, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLNB]] (+0.68, fdr 1e-05), [[GPRIN1]] (+0.66, fdr 3e-05), [[SERPINB1]] (+0.66, fdr 1e-05); moves opposite to [[RPRD2]] (-0.68, fdr 1e-05), [[SLC35E2B]] (-0.66, fdr 1e-05), [[AHI1-DT]] (-0.65, fdr 4e-05).
> It sits in the **+** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MYO1E]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2403.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.79×** | +12.3 | 3e-32 | 41/48 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.79×** | +12.3 | 3e-32 | 41/48 (SW1417, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.77×** | +12.0 | 4e-31 | 43/48 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +7.2 | 6e-11 | 32/48 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.73×** | +6.1 | 1e-07 | 30/48 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +5.5 | 5e-06 | 26/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.7 | 2e-04 | 20/48 (PANC-1, BT-474, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.18× | +3.5 | 0.032 | 14/47 (LS 180, PANC-1, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +3.4 | 0.039 | 15/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2403.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.484×** | -21.7 | 0e+00 | 46/48 (A-172, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.547×** | -18.0 | 0e+00 | 38/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -12.5 | 1e-33 | 33/49 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.568×** | -11.5 | 3e-28 | 32/48 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.603×** | -10.2 | 1e-22 | 33/47 (CFPAC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.609×** | -9.6 | 5e-20 | 40/48 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.651×** | -9.0 | 1e-17 | 39/48 (KATO III, A-172, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -8.8 | 1e-16 | 33/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.713×** | -7.1 | 7e-11 | 34/48 (KATO III, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.731×** | -6.4 | 1e-08 | 25/40 (H4, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.752×** | -6.0 | 1e-07 | 33/48 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.775×** | -5.4 | 4e-06 | 26/48 (HS-578T, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -5.2 | 8e-06 | 24/50 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.623×** | -5.2 | 8e-06 | 23/47 (LoVo, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.788×** | -5.0 | 2e-05 | 24/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.802×** | -4.6 | 1e-04 | 23/49 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.868× | -4.2 | 8e-04 | 16/48 (A-172, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -4.1 | 0.001 | 22/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 117 | 0 | 9 (1 ⚠) | — | [[Binimetinib (drug)]] 0.05 µM 0.523× (z -10.9) |
| [[PANC-1 (line)]] | alt | 127 | 1 (1 ⚠) | 7 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.85× (z +8.6) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -32.0) |
| [[A498 (line)]] | wt | 161 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -19.5) |
| [[HS-578T (line)]] | alt | 55.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -18.8) |
| [[LoVo (line)]] | wt | 80.5 | 3 (1 ⚠) | 4 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.63× (z +12.5) | [[Selinexor (drug)]] 5 µM 0.594× (z -9.5) |
| [[A-172 (line)]] | wt | 106 | 0 | 6 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.282× (z -18.0) |
| [[A549 (line)]] | wt | 109 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -24.6) |
| [[KATO III (line)]] | alt | 80.2 | 3 (1 ⚠) | 3 | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +11.8) | [[Selinexor (drug)]] 5 µM 0.474× (z -10.9) |
| [[RKO (line)]] | wt | 75.0 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.394× (z -11.6) |
| [[J82 (line)]] | alt | 118 | 2 | 3 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.14× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 62.7 | 0 | 5 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 82.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -22.1) |
| [[NCI-H1792 (line)]] | alt | 127 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -17.3) |
| [[NCI-H2030 (line)]] | alt | 81.3 | 3 (1 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.41× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -19.7) |
| [[NCI-H460 (line)]] | wt | 44.0 | 3 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +10.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.94× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.494× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 179 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.358× (z -15.5) |
| [[Hs 766T (line)]] | wt | 147 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 58.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -17.3) |
| [[SW1417 (line)]] | alt | 81.2 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.20× (z +13.8) | — |
| [[BT-474 (line)]] | alt | 100 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.423× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 99.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 70.8 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.494× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 83.4 | 2 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.82× (z +9.9) | [[Selinexor (drug)]] 5 µM 0.511× (z -9.1) |
| [[SNU-423 (line)]] | alt | 57.0 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.323× (z -13.6) |
| [[HEC-1-A (line)]] | alt | 66.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.416× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.559× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 70.8 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.04× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 93.4 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.545× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 154 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -16.1) |
| [[A-427 (line)]] | wt | 30.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.449× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 201 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -10.4) |
| [[C32 (line)]] | wt | 88.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.341× (z -13.1) |
| [[COLO 205 (line)]] | alt | 115 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.401× (z -11.6) |
| [[H4 (line)]] | wt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0555× (z -17.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 98.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.443× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 42.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.31× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 73.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.432× (z -11.8) |
| [[SW 900 (line)]] | alt | 63.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.306× (z -14.9) |
| [[AN3 CA (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLNB]] | +0.68 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[GPRIN1]] | +0.66 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[SERPINB1]] | +0.66 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[SH3BGRL3]] | +0.65 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[IL1RAP]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ARID3B]] | +0.63 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[SIPA1]] | +0.63 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[CMIP]] | +0.63 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ABTB3]] | +0.62 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[UBA6]] | +0.62 | +0.62 / +0.35 | both halves | 1e-04 |  |
| [[GNAI2]] | +0.61 | +0.57 / +0.26 | both halves | 4e-04 |  |
| [[UCHL3]] | +0.61 | +0.55 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPRD2]] | -0.68 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[SLC35E2B]] | -0.66 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[AHI1-DT]] | -0.65 | -0.57 / -0.40 | both halves | 4e-05 |  |
| [[RRAGB]] | -0.64 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[TP53]] | -0.64 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[OXA1L-DT]] | -0.64 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[TTC32]] | -0.64 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[GIPC2]] | -0.64 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[MAIP1]] | -0.64 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[RNF146]] | -0.64 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[N4BP2L1]] | -0.63 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[RBM33]] | -0.62 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1E]] | B | MYO1E activity raises EHD4's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without MYO1E | 0.014 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[TGM2]] | B | TGM2 activity raises EHD4's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 1.51× lower at baseline in the lines without TGM2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[IL1RAP]] | B | IL1RAP activity raises EHD4's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.80× lower at baseline in the lines without IL1RAP | 0.034 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[HDAC6]] | B | HDAC6 activity lowers EHD4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SERPINB1]] | B | SERPINB1 activity raises EHD4's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 1.50× lower at baseline in the lines without SERPINB1 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[ABTB3]] | B | ABTB3 activity raises EHD4's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 1.46× lower at baseline in the lines without ABTB3 | 0.085 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[KRT15]] | B | KRT15 activity raises EHD4's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 1.47× lower at baseline in the lines without KRT15 | 0.087 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[FLNB]] | C | FLNB activity raises EHD4's level | lines that do not express FLNB (3) vs lines expressing it (47) | 2.04× lower at baseline in the lines without FLNB | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **+** arm (projection on the module's main direction 0.747). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-1.0, 15.8); signed map (-3.0, 46.2). **Vector** length 147, 47.7% of its response variance represented; |z| ≥ 3 in 1,641 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +10.9 | +12.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +10.7 | +12.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +9.6 | +12.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.6 | +7.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +5.5 | +5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.8 | +6.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +1.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -15.3 | -21.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.9 | -18.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -9.4 | -9.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -8.7 | -9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.7 | -6.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -5.7 | -6.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -5.1 | -7.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.8 | -3.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | EH domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:41,895,933-41,972,557 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PAST4 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H223](https://www.uniprot.org/uniprotkb/Q9H223) (EH domain-containing protein 4):

> ATP- and membrane-binding protein that probably controls membrane reorganization/tubulation upon ATP hydrolysis. Plays a role in early endosomal transport. During sprouting angiogenesis, in complex with PACSIN2 and MICALL1, forms recycling endosome-like tubular structure at asymmetric adherens junctions to control CDH5 trafficking (By similarity).

**Summary**, from NCBI Gene [30844](https://www.ncbi.nlm.nih.gov/gene/30844):

> Enables cadherin binding activity. Involved in endocytic recycling and protein homooligomerization. Located in endoplasmic reticulum and recycling endosome membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3245](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3245) · Entrez [30844](https://www.ncbi.nlm.nih.gov/gene/30844) · UniProt [Q9H223](https://www.uniprot.org/uniprotkb/Q9H223) · Ensembl [ENSG00000103966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103966)

## Data

Gene col 2403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2403); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2403]; `tensor/DDL_lfc|DDL_z.npy` [2403]; `embed/gene_vectors.npy` [2403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2403 or target_col == 2403). Every well: [[EHD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EHD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
