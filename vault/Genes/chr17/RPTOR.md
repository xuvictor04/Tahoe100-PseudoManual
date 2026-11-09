---
symbol: "RPTOR"
type: "gene"
col: 6547
ensembl_id: "ENSG00000141564"
name: "regulatory associated protein of MTOR complex 1"
location: "17q25.3"
module: 5
arm: "+"
pooled_cpm: 162.7
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# RPTOR

*regulatory associated protein of MTOR complex 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.07× (z +12.5, q 7e-33, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.471× (z -11.8, q 2e-29, down in 36 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.573× (z -9.4, q 5e-19, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX10]] (+0.70, fdr 7e-06), [[DNAJC11]] (+0.69, fdr 7e-06), [[FARS2]] (+0.68, fdr 7e-06); moves opposite to [[TXNDC16]] (-0.62, fdr 1e-05), [[SVIP]] (-0.60, fdr 3e-05), [[ATP11B]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6547.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.07×** | +12.5 | 7e-33 | 47/49 (LoVo, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.30×** | +10.6 | 8e-24 | 47/48 (LS 180, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.86×** | +9.6 | 2e-19 | 44/48 (NCI-H1573, A549, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +8.8 | 2e-16 | 42/48 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +7.1 | 2e-10 | 39/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +6.3 | 3e-08 | 41/48 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.1 | 0.003 | 28/45 (A549, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.010 | 27/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.012 | 27/48 (SK-MEL-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6547.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.471×** | -11.8 | 2e-29 | 36/45 (SW48, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.499×** | -11.3 | 2e-27 | 41/44 (C-33 A, SW480, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.503×** | -10.4 | 5e-23 | 43/49 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.573×** | -9.4 | 5e-19 | 42/48 (J82, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.595×** | -8.5 | 3e-15 | 39/47 (NCI-H2030, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.724×** | -7.7 | 9e-13 | 43/48 (A-172, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.645×** | -7.4 | 8e-12 | 35/48 (SW1417, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.663×** | -7.0 | 2e-10 | 33/48 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.726×** | -5.4 | 4e-06 | 40/49 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.816×** | -4.9 | 6e-05 | 25/49 (A-172, CHP-212, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.749×** | -4.7 | 1e-04 | 28/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **0.769×** | -4.5 | 4e-04 | 31/48 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.790×** | -4.0 | 0.003 | 31/48 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.704×** | -3.1 | 0.076 | 24/49 (J82, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6547. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 158 | 5 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.97× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.401× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.508× (z -8.7) |
| [[PANC-1 (line)]] | alt | 186 | 3 | 6 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.63× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -16.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 166 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.465× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 135 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.71× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -19.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 181 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.95× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -15.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 208 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.08× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -10.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 524 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -13.2) |
| [[COLO 205 (line)]] | alt | 110 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.65× (z +13.7) | — |
| [[LoVo (line)]] | wt | 159 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.69× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.468× (z -9.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 180 | 4 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.51× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -12.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 165 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.35× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.0956× (z -22.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 172 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.05× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -23.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 192 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.347× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 136 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.56× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.387× (z -10.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 151 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.15× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -10.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 158 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.27× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -16.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 229 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 165 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.39× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 319 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -23.2) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 219 | 2 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.35× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -22.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 164 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -10.2) |
| [[A-172 (line)]] | wt | 160 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -15.9) |
| [[HCT15 (line)]] | alt | 173 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.50× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -15.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 117 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.01× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 122 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 8.42× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 206 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.51× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -13.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 166 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 7.10× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.200× (z -16.5) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 354 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -10.4) |
| [[SW48 (line)]] | wt | 173 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.24× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -18.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 172 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0770× (z -25.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 315 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -12.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 218 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -12.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 89.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.413× (z -9.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 141 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.51× (z +9.8) | [[Docetaxel (drug)]] 0.05 µM 0.410× (z -9.8) ⚠ transcription drop; cell-cycle shift, explains ~48% of this change |
| [[RPMI-7951 (line)]] | alt | 148 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.53× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -13.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 132 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 80.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.14× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 67.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.77× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 151 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +8.7) | — |
| [[SW 1088 (line)]] | alt | 152 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0926× (z -9.9) |
| [[SW 1271 (line)]] | alt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0811× (z -12.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 167 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.376× (z -9.5) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 126 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6547), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX10]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[FARS2]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[GATB]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[LARS2]] | +0.66 | +0.57 / +0.69 | both halves | 1e-05 | STRING 630 |
| [[EIPR1]] | +0.65 | +0.68 / +0.72 | both halves | 7e-06 | same gene group |
| [[EMG1]] | +0.65 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[LSG1]] | +0.64 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[GTPBP4]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ALG8]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[TSR1]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[L3HYPDH]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC16]] | -0.62 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[SVIP]] | -0.60 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[ATP11B]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[GRB7]] | -0.58 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[PLAG1]] | -0.58 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[HDAC5]] | -0.58 | -0.59 / -0.57 | both halves | 1e-05 | pathway: Intracellular signaling by second messengers |
| [[LNX2]] | -0.57 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[CDKN2D]] | -0.56 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.55 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[MINDY2]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers RPTOR's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ANAPC1P4]] | C | ANAPC1P4 activity raises RPTOR's level | lines that do not express ANAPC1P4 (4) vs lines expressing it (46) | 2.27× lower at baseline in the lines without ANAPC1P4 | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP19, MIR4435-2HG, MSX1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.0, -32.4); signed map (-5.4, -40.9). **Vector** length 127, 47.4% of its response variance represented; |z| ≥ 3 in 1,192 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +10.5 | +9.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.2 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.8 | +6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.6 | +12.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.5 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.9 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.0 | +10.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.0 | +3.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.3 | -5.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.8 | -7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | -3.2 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -3.1 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | regulatory associated protein of MTOR complex 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:80,544,819-80,966,371 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KOG1, Mip1, KIAA1303, raptor |
| Gene groups (HGNC) | WD repeat domain containing; MTOR complex 1; Armadillo like helical domain containing |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 21 pathways, smallest: Dengue virus modulates apoptosis; mTORC1-mediated signalling; Energy dependent regulation of mTOR by LKB1-AMPK |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N122](https://www.uniprot.org/uniprotkb/Q8N122) (Regulatory-associated protein of mTOR):

> Component of the mechanistic target of rapamycin complex 1 (mTORC1), an evolutionarily conserved central nutrient sensor that stimulates anabolic reactions and macromolecule biosynthesis to promote cellular biomass generation and growth. In response to nutrients, growth factors or amino acids, mTORC1 is recruited to the lysosome membrane and promotes protein, lipid and nucleotide synthesis by phosphorylating several substrates, such as ribosomal protein S6 kinase (RPS6KB1 and RPS6KB2) and …

**Summary**, from NCBI Gene [57521](https://www.ncbi.nlm.nih.gov/gene/57521):

> This gene encodes a component of a signaling pathway that regulates cell growth in response to nutrient and insulin levels. The encoded protein forms a stoichiometric complex with the mTOR kinase, and also associates with eukaryotic initiation factor 4E-binding protein-1 and ribosomal protein S6 kinase. The protein positively regulates the downstream effector ribosomal protein S6 kinase, and negatively regulates the mTOR kinase. Multiple transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:30287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30287) · Entrez [57521](https://www.ncbi.nlm.nih.gov/gene/57521) · UniProt [Q8N122](https://www.uniprot.org/uniprotkb/Q8N122) · Ensembl [ENSG00000141564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141564)

## Data

Gene col 6547: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6547); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6547, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6547]; `tensor/DDL_lfc|DDL_z.npy` [6547]; `embed/gene_vectors.npy` [6547]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6547 or target_col == 6547). Every well: [[RPTOR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPTOR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
