---
symbol: "CLDN12"
type: "gene"
col: 8054
ensembl_id: "ENSG00000157224"
name: "claudin 12"
location: "7q21.13"
module: 24
arm: "+"
pooled_cpm: 88.26
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# CLDN12

*claudin 12* — 7q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.58× (z +9.6, q 3e-19, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.495× (z -14.3, q 1e-43, down in 33 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.597× (z -10.5, q 2e-23, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED10]] (+0.66, fdr 1e-05), [[CCDC127]] (+0.58, fdr 2e-05), [[NOP10]] (+0.57, fdr 1e-04, ⚠ NOP10 in the vector space only through flagged drug-doses), [[LDAF1]] (+0.57, fdr 4e-05); moves opposite to [[COPS3]] (-0.61, fdr 5e-05), [[HNRNPUL1]] (-0.55, fdr 5e-05), [[PRKDC]] (-0.55, fdr 8e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CLDN4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8054.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +9.6 | 3e-19 | 37/48 (C32, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +8.9 | 2e-16 | 32/48 (A-172, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +6.2 | 8e-08 | 29/49 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +5.5 | 5e-06 | 31/48 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.8 | 2e-04 | 24/48 (LS 180, HT-29, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 2e-04 | 24/47 (LS 180, HT-29, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +4.6 | 4e-04 | 23/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +4.5 | 4e-04 | 24/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +4.5 | 4e-04 | 22/47 (HT-29, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.24×** | +4.4 | 5e-04 | 23/49 (LoVo, KATO III, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.21×** | +4.0 | 0.004 | 24/48 (HEC-1-A, H4, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.9 | 0.005 | 0/50 | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.20× | +3.8 | 0.005 | 19/47 (HT-29, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.8 | 0.005 | 13/48 (KATO III, LoVo, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.20× | +3.8 | 0.005 | 20/48 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.009 | 21/48 (PANC-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.057 | 18/47 (LoVo, RKO, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8054.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.495×** | -14.3 | 1e-43 | 33/42 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.546×** | -12.8 | 5e-35 | 41/49 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -10.5 | 2e-23 | 39/48 (COLO 205, H4, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.724×** | -9.7 | 6e-20 | 27/48 (BT-474, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.461×** | -8.5 | 2e-15 | 40/49 (NCI-H2347, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -7.5 | 6e-12 | 33/50 (LS 180, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.508×** | -7.5 | 6e-12 | 36/48 (NCI-H2347, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.673×** | -6.9 | 5e-10 | 26/44 (BT-474, SW 900, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.823×** | -4.1 | 0.003 | 23/48 (HCT15, HepG2/C3A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | 0.844× | -3.6 | 0.018 | 21/48 (SW 900, NCI-H2347, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.844× | -3.6 | 0.018 | 16/48 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.900× | -3.2 | 0.074 | 13/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8054. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 119 | 0 | 15 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.265× (z -14.9) |
| [[SW 900 (line)]] | alt | 137 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -14.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.7) |
| [[LS 180 (line)]] | wt | 107 | 4 (1 ⚠) | 4 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.06× (z +8.7) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Selinexor (drug)]] 5 µM 1.62× (z +8.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -11.3) |
| [[COLO 205 (line)]] | alt | 144 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -12.4) |
| [[HT-29 (line)]] | alt | 122 | 4 | 2 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 2.68× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 95.1 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -9.2) |
| [[LoVo (line)]] | wt | 95.2 | 4 (1 ⚠) | 2 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.77× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 131 | 4 (4 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.18× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.0586× (z -29.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 167 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.467× (z -10.8) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.624× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 143 | 1 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.20× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -27.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -9.7) |
| [[SW480 (line)]] | alt | 80.2 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -17.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 147 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -11.1) |
| [[A-172 (line)]] | wt | 45.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.7) | — |
| [[C32 (line)]] | wt | 103 | 1 | 2 | [[Auranofin (drug)]] 5 µM 3.49× (z +14.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 115 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 93.6 | 1 | 2 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.75× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 52.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -13.5) |
| [[RKO (line)]] | wt | 86.6 | 2 | 1 | [[Auranofin (drug)]] 5 µM 3.43× (z +14.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 193 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -15.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 95.9 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 72.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -9.6) |
| [[HOP62 (line)]] | alt | 68.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.420× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 50.2 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.14× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -8.7) |
| [[SHP-77 (line)]] | alt | 72.9 | 1 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.03× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -19.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 91.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -12.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 59.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -9.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 65.7 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.289× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 65.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 81.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 68.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 65.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.34× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 75.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -14.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8054), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED10]] | +0.66 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[CCDC127]] | +0.58 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[NOP10]] ⚠ | +0.57 | +0.35 / +0.61 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[LDAF1]] | +0.57 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[ATP6V0D2]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[KCNK6]] | +0.55 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[PTAFR]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[ZNF836]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[KLC3]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[CYB561D1]] | +0.54 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[ACVR1]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[BEX2]] | +0.53 | +0.32 / +0.57 | both halves | 1e-04 |  |
| [[ZBTB43]] | +0.53 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS3]] | -0.61 | -0.40 / -0.71 | both halves | 5e-05 |  |
| [[HNRNPUL1]] | -0.55 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[PRKDC]] | -0.55 | -0.37 / -0.63 | both halves | 8e-05 |  |
| [[ZMYND11]] | -0.55 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[DUT]] | -0.54 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[FAM120A]] | -0.54 | -0.26 / -0.53 | both halves | 3e-04 |  |
| [[NCBP1]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ILF3]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 | pathway: Cell junction organization |
| [[SEPTIN11]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SYNCRIP]] | -0.51 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[MTHFD1]] | -0.51 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[HNRNPD]] | -0.50 | -0.31 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN4]] | B | CLDN4 activity raises CLDN12's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 1.48× lower at baseline in the lines without CLDN4 | 0.018 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[S100A14]] | B | S100A14 activity raises CLDN12's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 1.40× lower at baseline in the lines without S100A14 | 0.034 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[CLDN4]] | B | CLDN4 activity strengthens CLDN12's drug response | lines that do not express CLDN4 (26) vs lines expressing it (24) | the lines without CLDN4 respond 0.67× as strongly (z diff +1.68); strongest at Homoharringtonine 5 µM: 0.90x vs 0.64x (z diff +5.1) | 0.090 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6; artifact flags |
| [[FAM182B]] | C | FAM182B activity lowers CLDN12's level | lines that do not express FAM182B (4) vs lines expressing it (46) | 1.43× higher at baseline in the lines without FAM182B | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CATSPER2P1, FGF12, SLFNL1-AS1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.452). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.4, -32.5); signed map (-20.8, 14.3). **Vector** length 133, 39.7% of its response variance represented; |z| ≥ 3 in 1,312 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +12.4 | +8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +10.7 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +7.5 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.1 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.8 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.6 | +6.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.1 | +2.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.8 | -8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.4 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.6 | -0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.8 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -2.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | claudin 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.13 — chr7:90,383,721-90,513,402 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Claudins |
| Reactome | 4 pathways, smallest: Tight junction interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P56749](https://www.uniprot.org/uniprotkb/P56749) (Claudin-12):

> Plays a major role in tight junction-specific obliteration of the intercellular space, through calcium-independent cell-adhesion activity.

**Summary**, from NCBI Gene [9069](https://www.ncbi.nlm.nih.gov/gene/9069):

> This gene encodes a member of the claudin family. Claudins are integral membrane proteins and components of tight junction strands. Tight junction strands serve as a physical barrier to prevent solutes and water from passing freely through the paracellular space between epithelial or endothelial cell sheets, and also play critical roles in maintaining cell polarity and signal transductions. This gene is expressed in the inner ear and bladder epithelium, and it is over-expressed in colorectal …

**Accessions** — [HGNC:2034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2034) · Entrez [9069](https://www.ncbi.nlm.nih.gov/gene/9069) · UniProt [P56749](https://www.uniprot.org/uniprotkb/P56749) · Ensembl [ENSG00000157224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157224)

## Data

Gene col 8054: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8054); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8054, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8054]; `tensor/DDL_lfc|DDL_z.npy` [8054]; `embed/gene_vectors.npy` [8054]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8054 or target_col == 8054). Every well: [[CLDN12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLDN12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
