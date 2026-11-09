---
symbol: "IL1R1"
type: "gene"
col: 3699
ensembl_id: "ENSG00000115594"
name: "interleukin 1 receptor type 1"
location: "2q11.2-q12.1"
module: 104
arm: "+"
pooled_cpm: 26.63
n_lines_expressing: 33
n_dd_up: 29
n_dd_down: 22
n_dd_up_clean: 23
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 13
direction_downstream: 10
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# IL1R1

*interleukin 1 receptor type 1* — 2q11.2-q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.27× (z +13.3, q 2e-37, up in 19 of 30 measured lines) ⚠ position correction uncertain. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.45× (z +6.0, q 2e-07, up in 15 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.605× (z -8.1, q 3e-13, down in 23 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PID1]] (+0.69, fdr 1e-05), [[NNMT]] (+0.68, fdr 7e-06), [[HECW2]] (+0.65, fdr 8e-06); moves opposite to [[C7orf57]] (-0.58, fdr 1e-05), [[SNX25]] (-0.54, fdr 1e-05), [[ZNF710-AS1]] (-0.52, fdr 2e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[MGST1]] → it (grade B ⚠); 10 go from it, the strongest it → [[SOD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3699.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **2.27×** | +13.3 | 2e-37 | 19/30 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.91×** | +7.4 | 5e-11 | 15/30 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | **1.85×** | +6.7 | 4e-09 | 22/30 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.74×** | +6.3 | 4e-08 | 20/30 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +6.0 | 2e-07 | 15/31 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.62×** | +5.1 | 3e-05 | 20/29 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.56×** | +5.1 | 3e-05 | 17/31 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.59×** | +4.8 | 1e-04 | 20/31 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM | ⚠ position correction uncertain | **1.50×** | +4.6 | 3e-04 | 18/31 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 7e-04 | 12/30 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.002 | 17/31 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.004 | 16/31 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.016 | 14/30 (RPMI-7951, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.019 | 15/31 (HS-578T, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.024 | 13/30 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.024 | 12/31 (MIA PaCa-2, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.034 | 13/28 (A549, HepG2/C3A, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +3.1 | 0.061 | 14/31 (RPMI-7951, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Econazole (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.078 | 12/31 (HS-578T, HOP62, …) | top dose only |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.078 | 13/31 (HS-578T, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3699.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.605×** | -8.1 | 3e-13 | 23/30 (NCI-H1792, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.545×** | -6.9 | 1e-09 | 20/31 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.575×** | -6.3 | 5e-08 | 20/30 (NCI-H460, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.601×** | -5.8 | 9e-07 | 19/31 (NCI-H460, HepG2/C3A, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -5.2 | 3e-05 | 19/29 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.655×** | -4.6 | 3e-04 | 22/30 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.678×** | -4.4 | 7e-04 | 17/30 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.685×** | -4.3 | 0.001 | 18/31 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.722×** | -3.7 | 0.013 | 17/30 (AN3 CA, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.732×** | -3.6 | 0.021 | 15/31 (HS-578T, A498, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.803×** | -3.5 | 0.021 | 9/31 (Panc 03.27, PANC-1, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.571×** | -3.3 | 0.039 | 15/29 (H4, LOX-IMVI, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.748×** | -3.3 | 0.040 | 11/30 (MIA PaCa-2, A498, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.757×** | -3.2 | 0.061 | 13/31 (NCI-H460, H4, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **0.747×** | -3.1 | 0.062 | 6/31 (NCI-H23, CFPAC-1, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.827×** | -3.1 | 0.074 | 10/31 (CHP-212, NCI-H1792, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.766×** | -3.0 | 0.074 | 9/30 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.769×** | -3.0 | 0.079 | 7/31 (HS-578T, NCI-H23, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.763×** | -3.0 | 0.081 | 8/29 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.754×** | -2.9 | 0.093 | 6/31 (HepG2/C3A, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3699. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 64.9 | 20 (4 ⚠) | 1 | [[Budesonide (drug)]] 0.5 µM 8.01× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -9.2) |
| [[HOP62 (line)]] | alt | 25.8 | 10 (4 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 7.16× (z +11.0) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 5 µM 5.19× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 69.6 | 2 (2 ⚠) | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +15.8) ⚠ position correction uncertain | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -11.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -11.2) |
| [[H4 (line)]] | wt | 45.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +9.5) ⚠ position correction uncertain | [[Docetaxel (drug)]] 0.05 µM 0.0880× (z -11.7) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 31.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +13.0) ⚠ position correction uncertain | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 7.36 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.7× (z +23.3) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 5.45× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 48.2 | 1 (1 ⚠) | 2 | [[Adagrasib (drug)]] 0.05 µM 1.68× (z +11.5) ⚠ position not correctable | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 62.9 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 5.27× (z +10.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 30.1 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0780× (z -16.0) |
| [[A-172 (line)]] | wt | 18.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +9.5) ⚠ position correction uncertain | — |
| [[HepG2_C3A (line)]] | wt | 57.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[J82 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.139× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~54% of this change |
| [[NCI-H1792 (line)]] | alt | 177 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -12.5) |
| [[SNU-423 (line)]] | alt | 96.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -8.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW 900 (line)]] | alt | 93.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -9.6) |
| [[A-427 (line)]] | wt | 5.71 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.37 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.60 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.87 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.15 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3699), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PID1]] | +0.69 | +0.57 / +0.76 | both halves | 1e-05 |  |
| [[NNMT]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[HECW2]] | +0.65 | +0.57 / +0.65 | both halves | 8e-06 |  |
| [[HIPK2]] | +0.64 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[HIF1A]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 434 |
| [[SOD2]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ROS1]] | +0.61 | +0.70 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[LINC02015]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[IRAK3]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 | pathway: Interleukin-1 family signaling; STRING 877 |
| [[ZC3H12C]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SLC7A2]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[TMTC1]] | +0.61 | +0.47 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C7orf57]] | -0.58 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SNX25]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZNF710-AS1]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[TMEM158]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[UBA6]] | -0.50 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TMEM51]] | -0.50 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[LHX1-DT]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ANKRD37]] | -0.49 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 6, C 7. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGST1]] | B | MGST1 activity raises IL1R1's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 2.45× lower at baseline in the lines without MGST1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[KYNU]] | B | KYNU activity raises IL1R1's level | lines that do not express KYNU (29) vs lines expressing it (21) | 3.77× lower at baseline in the lines without KYNU | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[CD38]] | B | CD38 activity raises IL1R1's level | lines that do not express CD38 (35) vs lines expressing it (15) | 2.85× lower at baseline in the lines without CD38 | 0.055 | ⚠ within organs, on part of the lines; also absent: MAGEA10, RNF17, GRIA2; maybe low, not absent |
| [[PID1]] | B | PID1 activity raises IL1R1's level | lines that do not express PID1 (22) vs lines expressing it (28) | 2.90× lower at baseline in the lines without PID1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TRPA1, DOCK10, ENSG00000289600 |
| [[NR3C1]] | B | NR3C1 activity raises IL1R1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds |
| [[TLR2]] | B | TLR2 activity raises IL1R1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 2.26× lower at baseline in the lines without TLR2 | 0.093 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[PAPPA]] | C | PAPPA activity raises IL1R1's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 4.01× lower at baseline in the lines without PAPPA | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[RHCG]] | C | RHCG activity raises IL1R1's level | lines that do not express RHCG (33) vs lines expressing it (17) | 3.18× lower at baseline in the lines without RHCG | 0.019 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10; co-absent with the target |
| [[SRGN]] | C | SRGN activity raises IL1R1's level | lines that do not express SRGN (30) vs lines expressing it (20) | 4.24× lower at baseline in the lines without SRGN | 0.038 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3; co-absent with the target |
| [[LINC02015]] | C | LINC02015 activity raises IL1R1's level | lines that do not express LINC02015 (27) vs lines expressing it (23) | 3.39× lower at baseline in the lines without LINC02015 | 0.043 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, CRLF2, PXDN; co-absent with the target |
| [[TMEM158]] | C | TMEM158 activity raises IL1R1's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 3.42× lower at baseline in the lines without TMEM158 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B; co-absent with the target |
| [[LINC02057]] | C | LINC02057 activity raises IL1R1's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 3.34× lower at baseline in the lines without LINC02057 | 0.073 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOD2]] | B | IL1R1 activity raises SOD2's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 2.69× lower at baseline in the lines without IL1R1 | 0.040 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1 |
| [[MGST1]] | B | IL1R1 activity raises MGST1's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 1.93× lower at baseline in the lines without IL1R1 | 0.058 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1 |
| [[SLCO2A1]] | B | IL1R1 activity raises SLCO2A1's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 1.88× lower at baseline in the lines without IL1R1 | 0.061 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1 |
| [[SQOR]] | B | IL1R1 activity raises SQOR's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 2.24× lower at baseline in the lines without IL1R1 | 0.062 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1 |
| [[ZC3H12A]] | B | IL1R1 activity raises ZC3H12A's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 1.96× lower at baseline in the lines without IL1R1 | 0.081 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1 |
| [[TNFAIP3]] | B | IL1R1 activity raises TNFAIP3's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 2.70× lower at baseline in the lines without IL1R1 | 0.084 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1 |
| [[KYNU]] | B | IL1R1 activity raises KYNU's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 4.82× lower at baseline in the lines without IL1R1 | 0.084 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1 |
| [[BASP1]] | C | IL1R1 activity raises BASP1's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 6.38× lower at baseline in the lines without IL1R1 | 0.007 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1; co-absent with the target |
| [[RHCG]] | C | IL1R1 activity raises RHCG's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 2.71× lower at baseline in the lines without IL1R1 | 0.023 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1; co-absent with the target |
| [[SRGN]] | C | IL1R1 activity raises SRGN's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 5.82× lower at baseline in the lines without IL1R1 | 0.084 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.8, 17.2); signed map (18.9, 31.9). **Vector** length 107, 31.2% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | +6.3 | +13.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | +4.9 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | +4.9 | +7.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.9 | +4.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM | ⚠ position correction uncertain | +3.8 | +6.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.7 | +5.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +3.7 | +5.1 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -5.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.2 | -6.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 1 receptor type 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2-q12.1 — chr2:102,064,544-102,179,874 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D2S1473, CD121A; previously IL1R, IL1RA |
| Gene groups (HGNC) | CD molecules; I-set domain containing; Interleukin receptors; TIR domain containing |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INFLAMMATORY_RESPONSE, XENOBIOTIC_METABOLISM |
| Reactome | 8 pathways, smallest: Interleukin-10 signaling; Potential therapeutics for SARS; Interleukin-1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P14778](https://www.uniprot.org/uniprotkb/P14778) (Interleukin-1 receptor type 1):

> Receptor for IL1A, IL1B and IL1RN. After binding to interleukin-1 associates with the coreceptor IL1RAP to form the high affinity interleukin-1 receptor complex which mediates interleukin-1-dependent activation of NF-kappa-B, MAPK and other pathways. Signaling involves the recruitment of adapter molecules such as TOLLIP, MYD88, and IRAK1 or IRAK2 via the respective TIR domains of the receptor/coreceptor subunits. Binds ligands with comparable affinity and binding of antagonist IL1RN prevents …

**Summary**, from NCBI Gene [3554](https://www.ncbi.nlm.nih.gov/gene/3554):

> This gene encodes a cytokine receptor that belongs to the interleukin-1 receptor family. The encoded protein is a receptor for interleukin-1 alpha, interleukin-1 beta, and interleukin-1 receptor antagonist. It is an important mediator involved in many cytokine-induced immune and inflammatory responses. This gene is located in a cluster of related cytokine receptor genes on chromosome 2q12. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:5993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5993) · Entrez [3554](https://www.ncbi.nlm.nih.gov/gene/3554) · UniProt [P14778](https://www.uniprot.org/uniprotkb/P14778) · Ensembl [ENSG00000115594](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115594)

## Data

Gene col 3699: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3699); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3699, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3699]; `tensor/DDL_lfc|DDL_z.npy` [3699]; `embed/gene_vectors.npy` [3699]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3699 or target_col == 3699). Every well: [[IL1R1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL1R1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
