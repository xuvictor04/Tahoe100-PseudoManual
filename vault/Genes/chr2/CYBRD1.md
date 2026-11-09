---
symbol: "CYBRD1"
type: "gene"
col: 997
ensembl_id: "ENSG00000071967"
name: "cytochrome b reductase 1"
location: "2q31.1"
module: 29
arm: "+"
pooled_cpm: 25.51
n_lines_expressing: 33
n_dd_up: 12
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CYBRD1

*cytochrome b reductase 1* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.90× (z +10.2, q 1e-21, up in 20 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +7.7, q 2e-12, up in 19 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.257× (z -22.4, q 0e+00, down in 27 of 31 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NNT]] (+0.60, fdr 4e-05), [[CIAO2A]] (+0.58, fdr 3e-05), [[LDB1]] (+0.58, fdr 4e-05); moves opposite to [[MTRES1]] (-0.58, fdr 3e-05), [[TXNDC17]] (-0.56, fdr 3e-05), [[MRPL17]] (-0.55, fdr 3e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[CSDE1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 997.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +10.2 | 1e-21 | 20/26 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.43×** | +8.3 | 2e-14 | 20/31 (J82, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.7 | 2e-12 | 19/31 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +7.6 | 6e-12 | 20/28 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +7.5 | 1e-11 | 4/31 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +6.0 | 2e-07 | 20/31 (J82, HS-578T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.2 | 2e-05 | 14/29 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.71×** | +4.4 | 6e-04 | 15/31 (Hs 766T, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.32×** | +4.2 | 0.001 | 12/26 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.28×** | +3.4 | 0.033 | 10/31 (A-427, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +3.4 | 0.033 | 9/31 (HCT15, Hs 766T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.045 | 9/29 (Hs 766T, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.23×** | +3.2 | 0.053 | 6/30 (HS-578T, J82, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.053 | 6/31 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.21×** | +3.1 | 0.072 | 8/30 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 997.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.257×** | -22.4 | 0e+00 | 27/31 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.280×** | -21.0 | 0e+00 | 30/31 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.359×** | -16.9 | 0e+00 | 27/31 (SNU-423, SW480, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.506×** | -15.9 | 0e+00 | 26/31 (LoVo, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.401×** | -14.5 | 1e-45 | 26/31 (LoVo, AsPC-1, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.499×** | -11.4 | 2e-28 | 27/31 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.529×** | -10.5 | 8e-24 | 23/30 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -7.8 | 3e-13 | 22/31 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.598×** | -6.0 | 1e-07 | 22/30 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.503×** | -5.7 | 9e-07 | 15/30 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.507×** | -5.6 | 1e-06 | 20/30 (LoVo, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.514×** | -5.5 | 2e-06 | 19/30 (NCI-H1792, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.723×** | -5.3 | 4e-06 | 22/31 (SNU-423, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.742×** | -4.9 | 4e-05 | 13/31 (A-172, LoVo, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.670×** | -4.7 | 1e-04 | 11/31 (NCI-H1792, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.566×** | -4.7 | 1e-04 | 15/30 (NCI-H1792, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.589×** | -4.3 | 5e-04 | 15/30 (HS-578T, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.696×** | -4.3 | 7e-04 | 15/31 (RPMI-7951, H4, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.626×** | -3.9 | 0.003 | 14/29 (LoVo, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 997. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 25.8 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0928× (z -18.7) |
| [[A-172 (line)]] | wt | 119 | 2 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -10.2) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.418× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 81.2 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.223× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 29.6 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -13.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -11.8) |
| [[SW480 (line)]] | alt | 33.7 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.117× (z -21.3) |
| [[SNU-423 (line)]] | alt | 62.2 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -21.5) |
| [[HCT15 (line)]] | alt | 39.7 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -13.3) |
| [[Hs 766T (line)]] | wt | 46.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -12.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.266× (z -10.5) |
| [[J82 (line)]] | alt | 49.6 | 2 (2 ⚠) | 3 | [[Selinexor (drug)]] 5 µM 1.96× (z +8.9) ⚠ cell-cycle shift, explains ~62% of this change | [[Panobinostat (drug)]] 0.5 µM 0.336× (z -10.3) |
| [[LS 180 (line)]] | wt | 19.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0418× (z -19.5) |
| [[MIA PaCa-2 (line)]] | alt | 77.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0372× (z -32.8) |
| [[A-427 (line)]] | wt | 41.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -12.3) |
| [[H4 (line)]] | wt | 24.1 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -11.1) |
| [[HS-578T (line)]] | alt | 24.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 41.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -16.8) |
| [[A549 (line)]] | wt | 23.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -13.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.297× (z -8.5) |
| [[HOP62 (line)]] | alt | 38.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 11.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 83.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -13.4) |
| [[AN3 CA (line)]] | alt | 47.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0763× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 40.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.258× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 30.8 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.215× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 81.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.325× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 9.75 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 32.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -8.6) |
| [[A498 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 997), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NNT]] | +0.60 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[CIAO2A]] | +0.58 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[LDB1]] | +0.58 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[YPEL5]] | +0.58 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[DVL3]] | +0.57 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[PGRMC1]] | +0.56 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[PCMTD1]] | +0.56 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[SETD7]] | +0.56 | +0.41 / +0.36 | both halves | 9e-05 |  |
| [[STRADB]] | +0.56 | +0.38 / +0.44 | both halves | 7e-05 |  |
| [[MSL3]] | +0.56 | +0.33 / +0.45 | both halves | 1e-04 |  |
| [[SNHG22]] | +0.55 | +0.35 / +0.39 | both halves | 1e-04 |  |
| [[MTURN]] | +0.55 | +0.46 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTRES1]] | -0.58 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[TXNDC17]] | -0.56 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[MRPL17]] | -0.55 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[VPS37C]] | -0.54 | -0.26 / -0.48 | both halves | 4e-04 |  |
| [[MRPL14]] | -0.53 | -0.18 / -0.53 | ⚠ one half (not replicated) | 1e-03 |  |
| [[MTLN]] ⚠ | -0.53 | -0.38 / -0.46 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DHRS2]] | -0.52 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[ARF6]] | -0.52 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[EXOC6]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[SLFN11]] | -0.51 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[DDX50]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[H3-3B]] | -0.50 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[NTMT1]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[INTS13]] | -0.48 | -0.37 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSDE1]] | B | CYBRD1 activity raises CSDE1's level | lines that do not express CYBRD1 (17) vs lines expressing it (33) | 1.19× lower at baseline in the lines without CYBRD1 | 0.035 | ⚠ within organs, on part of the lines; also absent: MME, BDNF, APOBEC3G |
| [[EEF1A1P5]] | B | CYBRD1 activity raises EEF1A1P5's level | lines that do not express CYBRD1 (17) vs lines expressing it (33) | 1.13× lower at baseline in the lines without CYBRD1 | 0.055 | ⚠ within organs, on part of the lines; also absent: MME, BDNF, APOBEC3G |
| [[EEF1A1]] | B | CYBRD1 activity raises EEF1A1's level | lines that do not express CYBRD1 (17) vs lines expressing it (33) | 1.15× lower at baseline in the lines without CYBRD1 | 0.061 | ⚠ within organs, on part of the lines; also absent: MME, BDNF, APOBEC3G |
| [[HIPK1]] | B | CYBRD1 activity raises HIPK1's level | lines that do not express CYBRD1 (17) vs lines expressing it (33) | 1.17× lower at baseline in the lines without CYBRD1 | 0.065 | ⚠ within organs, on part of the lines; also absent: MME, BDNF, APOBEC3G |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.494). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-13.5, 15.9); signed map (-17.3, -31.4). **Vector** length 85.3, 20.9% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +5.1 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +1.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.8 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.4 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -22.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -21.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -16.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -11.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -4.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -5.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome b reductase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:171,522,247-171,558,129 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DCYTB, FLJ23462, FRRS3, CYB561A2 |
| Gene groups (HGNC) | Cytochrome b561 |
| Reactome | 2 pathways, smallest: Iron uptake and transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53TN4](https://www.uniprot.org/uniprotkb/Q53TN4) (Plasma membrane ascorbate-dependent reductase CYBRD1):

> Plasma membrane reductase that uses cytoplasmic ascorbate as an electron donor to reduce extracellular Fe(3+) into Fe(2+). Probably functions in dietary iron absorption at the brush border of duodenal enterocytes by producing Fe(2+), the divalent form of iron that can be transported into enterocytes. It is also able to reduce extracellular monodehydro-L-ascorbate and may be involved in extracellular ascorbate regeneration by erythrocytes in blood. May also act as a ferrireductase in airway …

**Summary**, from NCBI Gene [79901](https://www.ncbi.nlm.nih.gov/gene/79901):

> This gene is a member of the cytochrome b(561) family that encodes an iron-regulated protein. It highly expressed in the duodenal brush border membrane. It has ferric reductase activity and is believed to play a physiological role in dietary iron absorption. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20797) · Entrez [79901](https://www.ncbi.nlm.nih.gov/gene/79901) · UniProt [Q53TN4](https://www.uniprot.org/uniprotkb/Q53TN4) · Ensembl [ENSG00000071967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071967)

## Data

Gene col 997: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 997); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 997, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 997]; `tensor/DDL_lfc|DDL_z.npy` [997]; `embed/gene_vectors.npy` [997]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 997 or target_col == 997). Every well: [[CYBRD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYBRD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
