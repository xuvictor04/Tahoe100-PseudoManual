---
symbol: "TOX2"
type: "gene"
col: 4494
ensembl_id: "ENSG00000124191"
name: "TOX high mobility group box family member 2"
location: "20q13.12"
module: 97
arm: "+"
pooled_cpm: 29.63
n_lines_expressing: 32
n_dd_up: 25
n_dd_down: 48
n_dd_up_clean: 23
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# TOX2

*TOX high mobility group box family member 2* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.25× (z +19.9, q 0e+00, up in 28 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.339× (z -26.6, q 0e+00, down in 27 of 30 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETV5]] (+0.67, fdr 1e-05), [[PTPRS]] (+0.66, fdr 1e-05), [[AKAP13]] (+0.64, fdr 1e-05); moves opposite to [[C5orf15]] (-0.62, fdr 5e-05), [[AHI1-DT]] (-0.59, fdr 1e-04), [[DECR1]] (-0.58, fdr 1e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 3 go from it, the strongest it → [[PBLD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 3 with an alert ⚠; shown: the 15 strongest. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4494.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.25×** | +19.9 | 0e+00 | 28/30 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.00×** | +12.0 | 6e-31 | 25/30 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +10.3 | 1e-22 | 25/30 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +9.6 | 8e-20 | 21/30 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +9.4 | 5e-19 | 27/30 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +8.9 | 4e-17 | 23/30 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.17×** | +7.1 | 1e-10 | 19/30 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +5.5 | 3e-06 | 16/30 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 8e-06 | 14/30 (PANC-1, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 1e-05 | 13/30 (PANC-1, NCI-H1792, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 5e-04 | 15/30 (PANC-1, SW 900, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.28×** | +4.4 | 6e-04 | 11/30 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.002 | 13/30 (PANC-1, NCI-H1792, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.005 | 11/30 (PANC-1, SW 900, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.006 | 13/30 (PANC-1, HS-578T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 20 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4494.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.339×** | -26.6 | 0e+00 | 27/30 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.324×** | -18.8 | 0e+00 | 27/30 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.389×** | -15.8 | 0e+00 | 25/29 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.556×** | -14.4 | 4e-45 | 26/30 (SNU-423, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.451×** | -13.8 | 2e-41 | 22/30 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.460×** | -13.5 | 2e-39 | 23/30 (RKO, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.485×** | -12.6 | 2e-34 | 23/30 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.281×** | -11.6 | 5e-29 | 22/30 (RKO, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.337×** | -9.9 | 3e-21 | 22/30 (HOP62, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; position correction uncertain | **0.576×** | -9.6 | 5e-20 | 22/29 (HCT15, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.570×** | -9.4 | 3e-19 | 21/29 (A-172, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.592×** | -9.1 | 4e-18 | 25/30 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.616×** | -8.4 | 2e-15 | 20/30 (SW48, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.642×** | -7.7 | 6e-13 | 18/30 (SW48, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.681×** | -7.3 | 1e-11 | 19/30 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.649×** | -7.2 | 2e-11 | 17/29 (Panc 03.27, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.695×** | -6.3 | 7e-09 | 17/30 (NCI-H1792, A-172, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.741×** | -6.2 | 1e-08 | 18/30 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4494. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 37.3 | 12 | 3 | [[Panobinostat (drug)]] 0.05 µM 3.40× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 37.3 | 2 | 9 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.79× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -14.1) |
| [[RKO (line)]] | wt | 51.0 | 1 | 10 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.72× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -17.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -14.0) |
| [[SNU-423 (line)]] | alt | 211 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -30.4) |
| [[HOP62 (line)]] | alt | 43.4 | 3 | 6 | [[Tucidinostat (drug)]] 5 µM 2.32× (z +10.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 63.3 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -21.0) |
| [[NCI-H1792 (line)]] | alt | 154 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -26.1) |
| [[RPMI-7951 (line)]] | alt | 205 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -20.1) |
| [[CFPAC-1 (line)]] | alt | 32.2 | 1 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.47× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -16.4) |
| [[NCI-H2030 (line)]] | alt | 47.0 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -15.9) |
| [[HCT15 (line)]] | alt | 67.3 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -17.5) |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -12.9) |
| [[LoVo (line)]] | wt | 22.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -12.9) |
| [[SW 900 (line)]] | alt | 88.8 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -15.7) |
| [[SW48 (line)]] | wt | 22.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0450× (z -15.2) |
| [[A-172 (line)]] | wt | 22.4 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 3.07× (z +10.8) | [[Cobimetinib (drug)]] 5 µM 0.210× (z -10.2) |
| [[A-427 (line)]] | wt | 37.5 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -13.3) |
| [[SW480 (line)]] | alt | 18.5 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 3.21× (z +12.6) | [[Harringtonine (drug)]] 0.5 µM 0.327× (z -8.5) |
| [[BT-474 (line)]] | alt | 8.47 | 0 | 2 | — | [[Neratinib (drug)]] 0.05 µM 0.0740× (z -9.6) |
| [[SW 1271 (line)]] | alt | 73.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -10.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 15.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.02× (z +8.5) | — |
| [[A498 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.05 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.67 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4494), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETV5]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PTPRS]] | +0.66 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[AKAP13]] | +0.64 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[LPAR3]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SH3RF3]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[SLC45A1]] | +0.63 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[MT1X]] | +0.63 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ERGIC1]] | +0.62 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[HPCAL1]] | +0.61 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[PPP1R14C]] | +0.61 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[RGS17]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[ABLIM3]] | +0.60 | +0.58 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C5orf15]] | -0.62 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[AHI1-DT]] | -0.59 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[DECR1]] | -0.58 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[PBLD]] | -0.58 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[LINC02068]] | -0.57 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[LINC02100]] | -0.56 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[DNAI4]] | -0.55 | -0.49 / -0.25 | both halves | 4e-04 |  |
| [[GAS2]] | -0.54 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[LINC01134]] | -0.54 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[KMO]] | -0.53 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[PNISR-AS1]] | -0.53 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[CTSO]] | -0.53 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises TOX2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[FHL1]] | B | FHL1 activity raises TOX2's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 2.68× lower at baseline in the lines without FHL1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[MFGE8]] | B | MFGE8 activity raises TOX2's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 2.46× lower at baseline in the lines without MFGE8 | 0.049 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B |
| [[LPAR3]] | B | LPAR3 activity raises TOX2's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 3.01× lower at baseline in the lines without LPAR3 | 0.058 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |
| [[PRKAR2B]] | B | PRKAR2B activity raises TOX2's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 2.95× lower at baseline in the lines without PRKAR2B | 0.071 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |
| [[OSBPL6]] | B | OSBPL6 activity raises TOX2's level | lines that do not express OSBPL6 (12) vs lines expressing it (38) | 2.87× lower at baseline in the lines without OSBPL6 | 0.071 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises TOX2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PBLD]] | B | TOX2 activity raises PBLD's level | lines that do not express TOX2 (18) vs lines expressing it (32) | 1.24× lower at baseline in the lines without TOX2 | 0.077 | ⚠ within organs, on part of the lines; also absent: TWIST2, OLFM1, PLEKHG4B |
| [[TANC2]] | B | TOX2 activity raises TANC2's level | lines that do not express TOX2 (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without TOX2 | 0.077 | ⚠ within organs, on part of the lines; also absent: TWIST2, OLFM1, PLEKHG4B |
| [[JCAD]] | B | TOX2 activity raises JCAD's level | lines that do not express TOX2 (18) vs lines expressing it (32) | 2.41× lower at baseline in the lines without TOX2 | 0.098 | ⚠ within organs, on part of the lines; also absent: TWIST2, OLFM1, PLEKHG4B |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.724). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.7, 13.4); signed map (13.0, 35.7). **Vector** length 111, 28.6% of its response variance represented; |z| ≥ 3 in 1,266 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.3 | +19.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +12.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.5 | +9.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.3 | +10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +9.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | -0.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +3.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -26.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.7 | -9.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.6 | -7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -15.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.1 | -6.2 |
|  | [[Binimetinib (drug)]] 5 µM | ⚠ position correction uncertain | -5.0 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.7 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.6 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | TOX high mobility group box family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:43,914,852-44,069,616 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1108D11.2, GCX-1; previously C20orf100 |
| Gene groups (HGNC) | thymocyte selection associated high mobility group box family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NM4](https://www.uniprot.org/uniprotkb/Q96NM4) (TOX high mobility group box family member 2):

> Putative transcriptional activator involved in the hypothalamo-pituitary-gonadal system.

**Summary**, from NCBI Gene [84969](https://www.ncbi.nlm.nih.gov/gene/84969):

> Enables transcription coactivator activity. Involved in positive regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16095](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16095) · Entrez [84969](https://www.ncbi.nlm.nih.gov/gene/84969) · UniProt [Q96NM4](https://www.uniprot.org/uniprotkb/Q96NM4) · Ensembl [ENSG00000124191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124191)

## Data

Gene col 4494: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4494); `tables/drug_effects.parquet` (84 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4494, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4494]; `tensor/DDL_lfc|DDL_z.npy` [4494]; `embed/gene_vectors.npy` [4494]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4494 or target_col == 4494). Every well: [[TOX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
