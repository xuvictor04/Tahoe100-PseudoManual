---
symbol: "GALM"
type: "gene"
col: 6821
ensembl_id: "ENSG00000143891"
name: "galactose mutarotase"
location: "2p22.1"
module: 44
arm: "+"
pooled_cpm: 14.92
n_lines_expressing: 39
n_dd_up: 31
n_dd_down: 21
n_dd_up_clean: 28
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 20
direction_downstream: 7
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# GALM

*galactose mutarotase* — 2p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.90× (z +12.8, q 5e-35, up in 33 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.344× (z -12.9, q 3e-35, down in 35 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TJP3]] (+0.70, fdr 7e-06), [[YPEL2]] (+0.66, fdr 1e-05), [[ATP8B1]] (+0.65, fdr 1e-05); moves opposite to [[MSANTD2]] (-0.64, fdr 1e-05), [[AVEN]] (-0.61, fdr 3e-05), [[CSTF3]] (-0.59, fdr 6e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[ELF3]] → it (grade B ⚠); 7 go from it, the strongest it → [[ATP8B1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6821.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.90×** | +12.8 | 5e-35 | 33/36 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.53×** | +11.2 | 1e-26 | 33/36 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.47×** | +10.9 | 2e-25 | 32/36 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.07×** | +8.8 | 3e-16 | 30/37 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +7.1 | 1e-10 | 26/37 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.70×** | +6.1 | 7e-08 | 25/36 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.66×** | +6.1 | 8e-08 | 23/36 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +6.0 | 1e-07 | 24/36 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.41×** | +5.8 | 4e-07 | 25/37 (AsPC-1, RPMI-7951, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.38×** | +5.5 | 3e-06 | 25/37 (NCI-H23, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +5.1 | 2e-05 | 15/33 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +4.4 | 4e-04 | 19/37 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +4.4 | 4e-04 | 9/21 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 5e-04 | 15/37 (LoVo, AsPC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.2 | 9e-04 | 15/37 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +4.2 | 9e-04 | 19/37 (AsPC-1, SW480, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **1.94×** | +4.2 | 9e-04 | 15/35 (A549, A498, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6821.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.344×** | -12.9 | 3e-35 | 35/36 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.361×** | -12.3 | 2e-32 | 29/36 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.409×** | -10.8 | 5e-25 | 29/36 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.473×** | -9.1 | 2e-17 | 24/36 (A498, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -8.8 | 1e-16 | 29/36 (COLO 205, HT-29, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.610×** | -6.0 | 2e-07 | 23/36 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.613×** | -5.9 | 3e-07 | 22/36 (A498, SW1417, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.628×** | -5.6 | 1e-06 | 24/36 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.642×** | -5.4 | 5e-06 | 19/36 (HT-29, LS 180, …) | two highest doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.670×** | -4.8 | 7e-05 | 20/36 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.765×** | -4.6 | 2e-04 | 19/37 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.718×** | -4.0 | 0.003 | 17/36 (LS 180, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.727×** | -3.9 | 0.005 | 17/36 (LS 180, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.741×** | -3.5 | 0.020 | 19/36 (NCI-H23, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.818×** | -3.4 | 0.023 | 17/36 (NCI-H2347, HT-29, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.763×** | -3.3 | 0.036 | 15/36 (Panc 03.27, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.763×** | -3.3 | 0.036 | 12/37 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.767×** | -3.2 | 0.041 | 17/36 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.615×** | -3.1 | 0.061 | 10/36 (LS 180, Hs 766T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.765×** | -3.1 | 0.061 | 9/37 (NCI-H2030, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6821. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 29.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0615× (z -15.6) |
| [[HT-29 (line)]] | alt | 29.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -12.2) |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -9.8) |
| [[SW 900 (line)]] | alt | 23.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.160× (z -10.1) |
| [[A498 (line)]] | wt | 13.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 29.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -10.0) |
| [[HOP62 (line)]] | alt | 8.60 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.07× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 18.0 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 48.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -12.8) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.346× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 30.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -9.0) |
| [[A-172 (line)]] | wt | 6.38 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.129× (z -8.7) |
| [[A549 (line)]] | wt | 15.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0570× (z -8.5) |
| [[HCT15 (line)]] | alt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0701× (z -11.8) |
| [[KATO III (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -9.3) |
| [[LoVo (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 9.69 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.60× (z +9.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 14.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.217× (z -10.1) |
| [[SW480 (line)]] | alt | 22.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.234× (z -10.9) |
| [[A-427 (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6821), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TJP3]] | +0.70 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[YPEL2]] | +0.66 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ATP8B1]] | +0.65 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[DBP]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[KBTBD3]] | +0.64 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[THRA]] | +0.63 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[SLC25A23]] | +0.63 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[SNX2]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[RHPN2]] | +0.62 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[CFD]] | +0.62 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[TCEA3]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SUFU]] | +0.62 | +0.45 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSANTD2]] | -0.64 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[AVEN]] | -0.61 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[CSTF3]] | -0.59 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[WDR27]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[AGO2]] | -0.58 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ELK4]] | -0.57 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[PIGW]] | -0.57 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[SPOPL-DT]] | -0.57 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ENOX2]] | -0.57 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TECPR2]] | -0.56 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[MSRA]] | -0.56 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[LTO1]] | -0.56 | -0.35 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3]] | B | ELF3 activity raises GALM's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.55× lower at baseline in the lines without ELF3 | 0.006 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[SLC40A1]] | B | SLC40A1 activity raises GALM's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.01× lower at baseline in the lines without SLC40A1 | 0.011 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[SLC44A4]] | B | SLC44A4 activity raises GALM's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.34× lower at baseline in the lines without SLC44A4 | 0.015 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[VWA1]] | B | VWA1 activity raises GALM's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 2.43× lower at baseline in the lines without VWA1 | 0.030 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[WFDC2]] | B | WFDC2 activity raises GALM's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.29× lower at baseline in the lines without WFDC2 | 0.035 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[SEC16B]] | B | SEC16B activity raises GALM's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 2.25× lower at baseline in the lines without SEC16B | 0.038 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[CXADR]] | B | CXADR activity raises GALM's level | lines that do not express CXADR (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without CXADR | 0.040 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[FAAH2]] | B | FAAH2 activity raises GALM's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without FAAH2 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[TJP3]] | B | TJP3 activity raises GALM's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.10× lower at baseline in the lines without TJP3 | 0.046 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[ATAD3C]] | B | ATAD3C activity raises GALM's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 2.10× lower at baseline in the lines without ATAD3C | 0.057 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[RNF183]] | B | RNF183 activity raises GALM's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 1.90× lower at baseline in the lines without RNF183 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1 |
| [[FAM221A]] | B | FAM221A activity weakens GALM's drug response | lines that do not express FAM221A (9) vs lines expressing it (28) | the lines without FAM221A respond 0.91× as strongly (z diff +0.48); strongest at Panobinostat 5 µM: 3.88x vs 2.59x (z diff -1.7) | 0.058 | ⚠ within organs, on part of the lines; also absent: TRIM2, MICE; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP8B1]] | B | GALM activity raises ATP8B1's level | lines that do not express GALM (11) vs lines expressing it (39) | 2.08× lower at baseline in the lines without GALM | 0.044 | ⚠ within organs, on part of the lines; also absent: ACOT11, GRIN2D, STAP2; maybe low, not absent |
| [[NSUN7]] | B | GALM activity raises NSUN7's level | lines that do not express GALM (11) vs lines expressing it (39) | 2.03× lower at baseline in the lines without GALM | 0.050 | ⚠ within organs, on part of the lines; also absent: ACOT11, GRIN2D, STAP2; maybe low, not absent |
| [[TMEM135]] | B | GALM activity lowers TMEM135's level | lines that do not express GALM (11) vs lines expressing it (39) | 1.51× higher at baseline in the lines without GALM | 0.050 | ⚠ within organs, on part of the lines; also absent: ACOT11, GRIN2D, STAP2; maybe low, not absent |
| [[SEC16B]] | B | GALM activity raises SEC16B's level | lines that do not express GALM (11) vs lines expressing it (39) | 1.87× lower at baseline in the lines without GALM | 0.063 | ⚠ within organs, on part of the lines; also absent: ACOT11, GRIN2D, STAP2; maybe low, not absent |
| [[BMAL2]] | B | GALM activity raises BMAL2's level | lines that do not express GALM (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without GALM | 0.063 | ⚠ within organs, on part of the lines; also absent: ACOT11, GRIN2D, STAP2; maybe low, not absent |
| [[ELF3]] | B | GALM activity raises ELF3's level | lines that do not express GALM (11) vs lines expressing it (39) | 3.74× lower at baseline in the lines without GALM | 0.067 | ⚠ within organs, on part of the lines; also absent: ACOT11, GRIN2D, STAP2; maybe low, not absent |
| [[TUFT1]] | B | GALM activity raises TUFT1's level | lines that do not express GALM (11) vs lines expressing it (39) | 2.20× lower at baseline in the lines without GALM | 0.072 | ⚠ within organs, on part of the lines; also absent: ACOT11, GRIN2D, STAP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.7, -0.5); signed map (-6.1, 16.4). **Vector** length 92.0, 24.4% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[NG25 (drug)]] 5 µM |  | +3.9 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +7.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +5.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +12.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +8.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +4.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | +4.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -8.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -12.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | galactose mutarotase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.1 — chr2:38,666,081-38,741,237 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 5 pathways, smallest: Galactose catabolism; Diseases associated with glycosylation precursor biosynthesis; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C23](https://www.uniprot.org/uniprotkb/Q96C23) (Galactose mutarotase):

> Mutarotase that catalyzes the interconversion of beta-D-galactose and alpha-D-galactose during galactose metabolism. Beta-D-galactose is metabolized in the liver into glucose 1-phosphate, the primary metabolic fuel, by the action of four enzymes that constitute the Leloir pathway: GALM, GALK1 (galactokinase), GALT (galactose-1-phosphate uridylyltransferase) and GALE (UDP-galactose-4'-epimerase). Involved in the maintenance of the equilibrium between the beta- and alpha-anomers of galactose, …

**Summary**, from NCBI Gene [130589](https://www.ncbi.nlm.nih.gov/gene/130589):

> This gene encodes an enzyme that catalyzes the epimerization of hexose sugars such as glucose and galactose. The encoded protein is expressed in the cytoplasm and has a preference for galactose. The encoded protein may be required for normal galactose metabolism by maintaining the equilibrium of alpha and beta anomers of galactose.[provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:24063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24063) · Entrez [130589](https://www.ncbi.nlm.nih.gov/gene/130589) · UniProt [Q96C23](https://www.uniprot.org/uniprotkb/Q96C23) · Ensembl [ENSG00000143891](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143891)

## Data

Gene col 6821: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6821); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6821, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6821]; `tensor/DDL_lfc|DDL_z.npy` [6821]; `embed/gene_vectors.npy` [6821]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6821 or target_col == 6821). Every well: [[GALM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
