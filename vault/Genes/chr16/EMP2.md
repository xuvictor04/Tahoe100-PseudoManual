---
symbol: "EMP2"
type: "gene"
col: 13140
ensembl_id: "ENSG00000213853"
name: "epithelial membrane protein 2"
location: "16p13.13"
module: 6
arm: "+"
pooled_cpm: 32.1
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 21
n_dd_up_clean: 10
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# EMP2

*epithelial membrane protein 2* — 16p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.72× (z +9.9, q 2e-20, up in 25 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.48× (z +9.8, q 2e-20, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.575× (z -10.1, q 5e-21, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01290]] (+0.65, fdr 7e-06, ⚠ read-through risk), [[ATAD2]] (+0.63, fdr 7e-06), [[GMNN]] (+0.58, fdr 2e-05), [[CENPU]] (+0.58, fdr 3e-05); moves opposite to [[ATP6V1G1]] (-0.50, fdr 4e-05), [[APTX]] (-0.48, fdr 7e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SORT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13140.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.72×** | +9.9 | 2e-20 | 25/41 (A-427, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +9.8 | 2e-20 | 36/47 (HepG2/C3A, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +8.0 | 2e-13 | 30/47 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.53×** | +7.5 | 1e-11 | 19/36 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +7.0 | 4e-10 | 23/47 (SW1417, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.42×** | +5.9 | 3e-07 | 20/38 (NCI-H2347, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +5.6 | 2e-06 | 22/47 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.006 | 16/47 (HS-578T, NCI-H2347, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.006 | 14/47 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.007 | 20/47 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.016 | 14/45 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.022 | 17/47 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.21×** | +3.3 | 0.042 | 18/47 (PANC-1, A549, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.052 | 10/47 (C32, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.053 | 12/47 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.053 | 13/47 (HS-578T, A498, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.055 | 2/45 (NCI-H1792, NCI-H2347) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.061 | 14/45 (A498, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.065 | 12/47 (HS-578T, NCI-H2347, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.065 | 8/47 (PANC-1, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13140.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.575×** | -10.1 | 5e-21 | 27/46 (KATO III, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.761×** | -6.7 | 5e-09 | 25/47 (A-172, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.723×** | -5.9 | 8e-07 | 20/47 (Hs 766T, A-427, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.718×** | -5.1 | 5e-05 | 24/47 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -4.8 | 2e-04 | 21/45 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.611×** | -4.6 | 4e-04 | 18/46 (SW480, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.777×** | -4.6 | 4e-04 | 21/47 (A-427, LS 180, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.784×** | -4.4 | 7e-04 | 16/47 (KATO III, LS 180, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.789×** | -4.3 | 0.001 | 21/47 (KATO III, SW480, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.642×** | -4.1 | 0.002 | 14/46 (SW480, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.848× | -4.0 | 0.003 | 18/47 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.801×** | -4.0 | 0.003 | 24/47 (NCI-H1573, HT-29, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.802×** | -4.0 | 0.003 | 19/47 (HOP62, KATO III, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.805×** | -3.9 | 0.003 | 14/46 (KATO III, LS 180, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.657×** | -3.9 | 0.003 | 18/43 (A498, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.858× | -3.8 | 0.006 | 15/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.763×** | -3.5 | 0.015 | 10/47 (Hs 766T, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.825×** | -3.5 | 0.016 | 18/47 (NCI-H1573, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.696×** | -3.4 | 0.021 | 14/47 (KATO III, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.702×** | -3.3 | 0.027 | 12/47 (KATO III, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13140. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 113 | 1 (1 ⚠) | 12 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.14× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.217× (z -11.2) |
| [[KATO III (line)]] | alt | 101 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -16.8) |
| [[Hs 766T (line)]] | wt | 43.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -13.8) |
| [[A-427 (line)]] | wt | 35.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | [[PH-797804 (drug)]] 5 µM 0.0533× (z -12.7) |
| [[COLO 205 (line)]] | alt | 46.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -18.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -8.7) |
| [[HOP62 (line)]] | alt | 34.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -9.4) |
| [[HT-29 (line)]] | alt | 44.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.219× (z -11.1) |
| [[LS 180 (line)]] | wt | 58.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0956× (z -15.1) |
| [[A-172 (line)]] | wt | 26.1 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.319× (z -10.9) ⚠ cell-cycle shift, explains ~41% of this change |
| [[PANC-1 (line)]] | alt | 15.0 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.25× (z +10.0) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[A549 (line)]] | wt | 19.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 67.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.617× (z -10.9) ⚠ position not correctable |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 40.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -9.2) |
| [[A498 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 41.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13140), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01290]] | +0.65 | +0.60 / +0.74 | both halves | 7e-06 | ⚠ **readthrough risk**: LINC01290 lies 0.2 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[ATAD2]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[GMNN]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[CENPU]] | +0.58 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[WDR76]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[NCAPG2]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[RHOBTB2]] | +0.56 | +0.28 / +0.61 | both halves | 3e-04 |  |
| [[TGFBR3]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SYTL4]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[BLM]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CENPM]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[E2F2]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[E2F8]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1G1]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[APTX]] | -0.48 | -0.44 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORT1]] | B | SORT1 activity raises EMP2's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.90× lower at baseline in the lines without SORT1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[PLEKHG6]] | B | PLEKHG6 activity raises EMP2's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 1.70× lower at baseline in the lines without PLEKHG6 | 0.036 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity raises EMP2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[LINC01290]] | C | LINC01290 activity raises EMP2's level | lines that do not express LINC01290 (3) vs lines expressing it (47) | 2.77× lower at baseline in the lines without LINC01290 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: UGDH, IQSEC2, APOBEC3F; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.6, -47.4); signed map (-39.7, -44.7). **Vector** length 114, 29.0% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.0 | +8.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.1 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +4.0 | +3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | +2.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.9 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.9 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.9 | -6.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.4 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -4.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -4.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | epithelial membrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.13 — chr16:10,528,422-10,580,632 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XMP |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Matched by | ensembl_id |

**Function**, from UniProt [P54851](https://www.uniprot.org/uniprotkb/P54851) (Epithelial membrane protein 2):

> Functions as a key regulator of cell membrane composition by regulating protein surface expression. Also, plays a role in regulation of processes including cell migration, cell proliferation, cell contraction and cell adhesion. Regulates transepithelial migration of neutrophils into the alveolar lumen, potentially via mediation of cell surface expression of adhesion markers and lipid raft formation (By similarity). Negatively regulates caveolae formation by reducing CAV1 expression and CAV1 …

**Summary**, from NCBI Gene [2013](https://www.ncbi.nlm.nih.gov/gene/2013):

> This gene encodes a tetraspan protein of the PMP22/EMP family. The encoded protein regulates cell membrane composition. It has been associated with various functions including endocytosis, cell signaling, cell proliferation, cell migration, cell adhesion, cell death, cholesterol homeostasis, urinary albumin excretion, and embryo implantation. It is known to negatively regulate caveolin-1, a scaffolding protein which is the main component of the caveolae plasma membrane invaginations found in …

**Accessions** — [HGNC:3334](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3334) · Entrez [2013](https://www.ncbi.nlm.nih.gov/gene/2013) · UniProt [P54851](https://www.uniprot.org/uniprotkb/P54851) · Ensembl [ENSG00000213853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213853)

## Data

Gene col 13140: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13140); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13140, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13140]; `tensor/DDL_lfc|DDL_z.npy` [13140]; `embed/gene_vectors.npy` [13140]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13140 or target_col == 13140). Every well: [[EMP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
