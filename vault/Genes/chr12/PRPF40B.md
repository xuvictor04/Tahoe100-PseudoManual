---
symbol: "PRPF40B"
type: "gene"
col: 3169
ensembl_id: "ENSG00000110844"
name: "pre-mRNA processing factor 40B"
location: "12q13.12"
module: 5
arm: "+"
pooled_cpm: 50.69
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PRPF40B

*pre-mRNA processing factor 40B* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.08× (z +4.8, q 8e-04, up in 1 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.22× (z +3.5, q 0.074, up in 17 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.531× (z -15.9, q 0e+00, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.643× (z -7.9, q 4e-13, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTRH2]] (+0.61, fdr 1e-05), [[ANKRD42-DT]] (+0.60, fdr 3e-05), [[TRNT1]] (+0.60, fdr 1e-05); moves opposite to [[CEP19]] (-0.49, fdr 9e-05), [[SKAP2]] (-0.48, fdr 5e-05), [[AFDN]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3169.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.8 | 8e-04 | 1/49 (NCI-H23) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.20× | +4.6 | 0.001 | 24/48 (C32, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +3.6 | 0.071 | 20/48 (Hs 766T, H4, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.074 | 17/48 (SK-MEL-2, SHP-77, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.21× | +3.3 | 0.10 | 13/48 (LOX-IMVI, COLO 205, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.10 | 16/48 (LS 180, C-33 A, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.10 | 13/48 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.1 | 0.10 | 12/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.10 | 13/48 (NCI-H23, SW 900, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.10 | 17/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[Methylthiouracil (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.10 | 4/48 (A-427, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3169.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.531×** | -15.9 | 0e+00 | 39/48 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.467×** | -12.1 | 3e-31 | 40/48 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.526×** | -11.4 | 6e-28 | 44/48 (PANC-1, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.536×** | -11.1 | 2e-26 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.576×** | -8.8 | 2e-16 | 40/47 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.643×** | -7.9 | 4e-13 | 32/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.662×** | -7.3 | 2e-11 | 30/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.682×** | -6.7 | 2e-09 | 34/48 (BT-474, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.495×** | -6.5 | 4e-09 | 32/49 (PANC-1, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.694×** | -6.4 | 9e-09 | 26/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.738×** | -5.3 | 6e-06 | 26/48 (AN3 CA, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -4.9 | 4e-05 | 26/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.760×** | -4.9 | 5e-05 | 24/48 (SW48, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.768×** | -4.7 | 1e-04 | 25/48 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.669×** | -3.7 | 0.007 | 20/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.670×** | -3.7 | 0.007 | 20/48 (CFPAC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.827×** | -3.4 | 0.024 | 12/48 (CHP-212, HOP62, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.698×** | -3.3 | 0.025 | 18/48 (SNU-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.819×** | -3.2 | 0.044 | 17/48 (HOP62, NCI-H460, …) | top dose only |  |
| [[Hesperidin (drug)]] 0.05 µM |  | **0.829×** | -3.1 | 0.053 | 13/48 (LoVo, H4, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.733×** | -2.9 | 0.092 | 15/48 (C32, SW 1271, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 46.2 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -16.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.289× (z -13.3) |
| [[PANC-1 (line)]] | alt | 74.5 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -18.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 52.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -16.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.400× (z -9.3) |
| [[A549 (line)]] | wt | 59.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -19.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.262× (z -13.5) |
| [[LoVo (line)]] | wt | 51.8 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.349× (z -11.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H23 (line)]] | alt | 132 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -12.2) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW480 (line)]] | alt | 59.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -16.4) ⚠ cell-cycle shift, explains ~45% of this change |
| [[AsPC-1 (line)]] | alt | 33.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -14.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW1417 (line)]] | alt | 42.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -12.3) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 113 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0921× (z -25.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 34.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.202× (z -12.3) ⚠ cell-cycle shift, explains ~45% of this change |
| [[C-33 A (line)]] | alt | 86.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 59.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -14.3) ⚠ cell-cycle shift, explains ~45% of this change |
| [[H4 (line)]] | wt | 70.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HEC-1-A (line)]] | alt | 50.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -11.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[HepG2_C3A (line)]] | wt | 41.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.256× (z -9.0) |
| [[HOP62 (line)]] | alt | 42.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.312× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 73.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -11.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SK-MEL-2 (line)]] | alt | 63.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 62.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.129× (z -10.1) |
| [[J82 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[KATO III (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.317× (z -9.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -8.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H661 (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0849× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 62.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -8.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[RKO (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.259× (z -8.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SNU-1 (line)]] | wt | 54.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.188× (z -10.9) |
| [[SNU-423 (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -14.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW 1271 (line)]] | alt | 54.4 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0649× (z -9.6) |
| [[SW48 (line)]] | wt | 36.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-172 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTRH2]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ANKRD42-DT]] | +0.60 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[TRNT1]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | +0.60 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[VPS51]] | +0.59 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[NAF1]] | +0.58 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[DHX34]] | +0.58 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[CTC-338M12.4]] | +0.58 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[EARS2]] | +0.58 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[TRMT1]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ZNF749]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MBTD1]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP19]] | -0.49 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[SKAP2]] | -0.48 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[AFDN]] | -0.47 | -0.36 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.481). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-25.9, -11.5); signed map (0.3, -2.0). **Vector** length 89.6, 22.6% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.7 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.6 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.9 | +4.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.1 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.0 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -2.9 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.7 | +3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -5.4 | -15.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.1 | -12.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -3.3 | -4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -1.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | pre-mRNA processing factor 40B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,568,218-49,644,666 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HYPC |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NWY9](https://www.uniprot.org/uniprotkb/Q6NWY9) (Pre-mRNA-processing factor 40 homolog B):

> May be involved in pre-mRNA splicing.

**Summary**, from NCBI Gene [25766](https://www.ncbi.nlm.nih.gov/gene/25766):

> This gene encodes a WW-domain containing protein similar to yeast splicing factor PRP40. This protein has been shown to interact with Huntingtin and methyl CpG binding protein 2 (MeCP2). Alternative splicing results in different transcript variants. [provided by RefSeq, Aug 2014]

**Accessions** — [HGNC:25031](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25031) · Entrez [25766](https://www.ncbi.nlm.nih.gov/gene/25766) · UniProt [Q6NWY9](https://www.uniprot.org/uniprotkb/Q6NWY9) · Ensembl [ENSG00000110844](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110844)

## Data

Gene col 3169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3169); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3169]; `tensor/DDL_lfc|DDL_z.npy` [3169]; `embed/gene_vectors.npy` [3169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3169 or target_col == 3169). Every well: [[PRPF40B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPF40B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
