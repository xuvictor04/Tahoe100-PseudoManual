---
symbol: "MALT1"
type: "gene"
col: 10221
ensembl_id: "ENSG00000172175"
name: "MALT1 paracaspase"
location: "18q21.32"
module: 16
arm: "-"
pooled_cpm: 116.47
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# MALT1

*MALT1 paracaspase* — 18q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.39× (z +6.5, q 6e-08, up in 29 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +5.9, q 8e-07, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.558× (z -10.5, q 3e-23, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX14]] (+0.54, fdr 1e-05), [[VDAC1]] (+0.52, fdr 1e-05), [[PTDSS1]] (+0.51, fdr 2e-05); moves opposite to [[ZNF554]] (-0.56, fdr 8e-06), [[ZNF776]] (-0.55, fdr 1e-05), [[JHY]] (-0.55, fdr 1e-05).
> It sits in the **-** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10221.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +6.5 | 6e-08 | 29/48 (Panc 03.27, A549, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.9 | 8e-07 | 32/48 (RKO, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.4 | 0.002 | 24/50 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 0.002 | 28/48 (PANC-1, SNU-423, …) | two highest doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.16× | +4.1 | 0.005 | 24/49 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.029 | 18/48 (SNU-423, HOP62, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.039 | 20/48 (Panc 03.27, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.20× | +3.2 | 0.086 | 20/49 (NCI-H1573, NCI-H1792, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10221.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.558×** | -10.5 | 3e-23 | 42/48 (HepG2/C3A, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.558×** | -10.5 | 3e-23 | 33/45 (RKO, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.609×** | -9.6 | 1e-19 | 38/49 (HepG2/C3A, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.595×** | -9.4 | 9e-19 | 35/44 (HepG2/C3A, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.712×** | -9.4 | 9e-19 | 27/48 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.692×** | -7.2 | 7e-11 | 37/48 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.713×** | -6.6 | 4e-09 | 37/48 (HepG2/C3A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.719×** | -6.4 | 1e-08 | 32/48 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -6.0 | 1e-07 | 28/47 (HepG2/C3A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.726×** | -5.8 | 5e-07 | 33/48 (SHP-77, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.752×** | -5.5 | 2e-06 | 25/48 (HepG2/C3A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -4.4 | 4e-04 | 19/48 (NCI-H2347, RKO, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.798×** | -4.4 | 5e-04 | 26/48 (HepG2/C3A, C32, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.807×** | -4.2 | 0.001 | 24/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.807×** | -4.2 | 0.001 | 28/48 (PANC-1, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.844× | -4.0 | 0.002 | 16/48 (SW480, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.835× | -3.5 | 0.013 | 19/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.883× | -3.3 | 0.022 | 14/49 (NCI-H2347, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.875× | -3.3 | 0.029 | 14/48 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.812×** | -2.9 | 0.088 | 15/48 (SW480, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 416 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -28.0) |
| [[SW480 (line)]] | alt | 174 | 0 | 10 (4 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.435× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 283 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.288× (z -14.7) |
| [[KATO III (line)]] | alt | 139 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 220 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -15.8) |
| [[CFPAC-1 (line)]] | alt | 162 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -15.1) |
| [[HCT15 (line)]] | alt | 152 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -14.6) |
| [[NCI-H2347 (line)]] | alt | 105 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -15.1) |
| [[RKO (line)]] | wt | 131 | 1 | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.0809× (z -25.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.440× (z -9.1) |
| [[A549 (line)]] | wt | 93.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.19× (z +9.3) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.382× (z -10.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 151 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 101 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -9.7) |
| [[J82 (line)]] | alt | 127 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 91.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.8) ⚠ cell-cycle shift, explains ~8% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.435× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 119 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.346× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 66.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.376× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 90.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.78× (z +10.9) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.373× (z -9.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 58.5 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.56× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 158 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -11.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 49.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -10.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 75.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -10.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -11.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 118 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.351× (z -8.6) |
| [[H4 (line)]] | wt | 133 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.385× (z -8.8) |
| [[Hs 766T (line)]] | wt | 95.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -11.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 89.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.525× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 90.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 70.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.66× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.329× (z -9.0) ⚠ toxic |
| [[SW48 (line)]] | wt | 89.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -9.2) |
| [[A-172 (line)]] | wt | 93.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 112 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 130 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 238 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX14]] | +0.54 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[VDAC1]] | +0.52 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[PTDSS1]] | +0.51 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[POC1B]] | +0.51 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[MGAT5]] | +0.51 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[SNHG30]] | +0.51 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[PLEKHA8]] | +0.51 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[SNX25]] | +0.50 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[CHSY1]] | +0.49 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[TPI1]] | +0.49 | +0.40 / +0.49 | both halves | 4e-05 |  |
| [[PIK3C2A]] | +0.49 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[TENT4A]] | +0.49 | +0.48 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF554]] | -0.56 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[ZNF776]] | -0.55 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[JHY]] | -0.55 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[TCEANC]] | -0.54 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[KAT5]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CHTOP]] | -0.53 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[KLF11]] | -0.53 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ZNF839]] | -0.51 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[CPLANE1]] | -0.51 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[RTL6]] | -0.50 | -0.53 / -0.49 | both halves | 2e-05 |  |
| [[PABIR1]] | -0.49 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[CUTALP]] | -0.49 | -0.55 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.523). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.3, 15.3); signed map (-39.7, 28.1). **Vector** length 114, 32.3% of its response variance represented; |z| ≥ 3 in 1,215 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +12.7 | +4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +10.0 | +4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | -1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.4 | +4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.9 | -10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -1.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | MALT1 paracaspase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.32 — chr18:58,671,465-58,754,477 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PCASP1; previously MLT |
| Gene groups (HGNC) | Immunoglobulin like domain containing; CBM complex; Cysteine endopeptidases |
| Reactome | 12 pathways, smallest: CLEC7A/inflammasome pathway; Activation of NF-kappaB in B cells; FCERI mediated NF-kB activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UDY8](https://www.uniprot.org/uniprotkb/Q9UDY8) (Mucosa-associated lymphoid tissue lymphoma translocation protein 1):

> Protease that enhances BCL10-induced activation: acts via formation of CBM complexes that channel adaptive and innate immune signaling downstream of CARD domain-containing proteins (CARD9, CARD11 and CARD14) to activate NF-kappa-B and MAP kinase p38 pathways which stimulate expression of genes encoding pro-inflammatory cytokines and chemokines. Mediates BCL10 cleavage: MALT1-dependent BCL10 cleavage plays an important role in T-cell antigen receptor-induced integrin adhesion. Involved in the …

**Summary**, from NCBI Gene [10892](https://www.ncbi.nlm.nih.gov/gene/10892):

> This gene encodes a caspase-like protease that plays a role in BCL10-induced activation of NF-kappaB. The protein is a component of the CARMA1-BCL10-MALT1 (CBM) signalosome that triggers NF-kappaB signaling and lymphoctye activation following antigen-receptor stimulation. Mutations in this gene result in immunodeficiency 12 (IMD12). This gene has been found to be recurrently rearranged in chromosomal translocations with other genes in mucosa-associated lymphoid tissue lymphomas, including a …

**Accessions** — [HGNC:6819](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6819) · Entrez [10892](https://www.ncbi.nlm.nih.gov/gene/10892) · UniProt [Q9UDY8](https://www.uniprot.org/uniprotkb/Q9UDY8) · Ensembl [ENSG00000172175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172175)

## Data

Gene col 10221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10221); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10221]; `tensor/DDL_lfc|DDL_z.npy` [10221]; `embed/gene_vectors.npy` [10221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10221 or target_col == 10221). Every well: [[MALT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MALT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
