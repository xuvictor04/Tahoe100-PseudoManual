---
symbol: "RALGDS"
type: "gene"
col: 8330
ensembl_id: "ENSG00000160271"
name: "ral guanine nucleotide dissociation stimulator"
location: "9q34.13-q34.2"
module: 3
arm: "+"
pooled_cpm: 54.66
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# RALGDS

*ral guanine nucleotide dissociation stimulator* — 9q34.13-q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[XRK3F2 (drug)]] 0.5 µM: 1.64× (z +5.2, q 9e-05, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.380× (z -20.4, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM38]] (+0.72, fdr 5e-05), [[CARHSP1]] (+0.72, fdr 7e-06), [[ARID3A]] (+0.69, fdr 7e-06); moves opposite to [[HDHD2]] (-0.64, fdr 3e-05), [[ACADM]] (-0.64, fdr 1e-05), [[NDUFS1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[JAG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8330.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.64×** | +5.2 | 9e-05 | 32/47 (NCI-H2030, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +4.6 | 0.001 | 31/47 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.010 | 21/48 (KATO III, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.027 | 23/47 (RPMI-7951, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.56×** | +3.5 | 0.053 | 19/48 (HT-29, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Pimitespib (drug)]] 5 µM |  | 1.50× | +3.1 | 0.16 | 14/46 (LS 180, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.48× | +3.1 | 0.17 | 19/43 (SW480, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.18 | 16/49 (C32, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8330.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.380×** | -20.4 | 0e+00 | 40/48 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.398×** | -13.2 | 2e-37 | 33/39 (NCI-H2030, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.453×** | -11.6 | 6e-29 | 45/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.461×** | -11.5 | 1e-28 | 40/48 (RKO, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.495×** | -10.1 | 9e-22 | 40/48 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.619×** | -6.6 | 4e-09 | 33/44 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.744×** | -6.2 | 5e-08 | 27/48 (Panc 03.27, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -5.7 | 8e-07 | 24/49 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.685×** | -5.6 | 1e-06 | 27/48 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.724×** | -4.8 | 9e-05 | 27/48 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.797×** | -4.8 | 1e-04 | 22/48 (Hs 766T, SNU-423, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.737×** | -4.4 | 6e-04 | 23/47 (C32, Hs 766T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.758×** | -4.1 | 0.002 | 26/48 (KATO III, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.772×** | -3.8 | 0.005 | 22/48 (BT-474, SNU-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.775×** | -3.8 | 0.006 | 21/48 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.787×** | -3.6 | 0.013 | 22/48 (C32, Hs 766T, …) | top dose only |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.810×** | -3.1 | 0.066 | 15/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.803×** | -3.0 | 0.071 | 14/48 (AsPC-1, C32, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.803×** | -3.0 | 0.071 | 9/48 (RKO, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8330. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 188 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -27.7) |
| [[C32 (line)]] | wt | 87.7 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0846× (z -32.0) |
| [[AsPC-1 (line)]] | alt | 192 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -16.5) |
| [[MIA PaCa-2 (line)]] | alt | 95.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -23.5) |
| [[RKO (line)]] | wt | 116 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0837× (z -26.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.215× (z -23.2) |
| [[J82 (line)]] | alt | 63.5 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.461× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 39.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0891× (z -28.2) |
| [[SNU-423 (line)]] | alt | 51.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -19.5) |
| [[BT-474 (line)]] | alt | 69.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.281× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.5) |
| [[HT-29 (line)]] | alt | 80.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -15.8) |
| [[NCI-H2030 (line)]] | alt | 29.1 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0699× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.240× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 45.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -18.0) |
| [[A498 (line)]] | wt | 28.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 40.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -15.3) |
| [[HOP62 (line)]] | alt | 57.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.298× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 62.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 48.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -23.8) |
| [[NCI-H2347 (line)]] | alt | 42.3 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.445× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 50.0 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.332× (z -12.3) |
| [[C-33 A (line)]] | alt | 53.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.6) |
| [[HCT15 (line)]] | alt | 52.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -10.7) |
| [[LS 180 (line)]] | wt | 72.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 20.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 30.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 54.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -16.3) |
| [[SNU-1 (line)]] | wt | 65.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -13.6) |
| [[SW 900 (line)]] | alt | 33.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -12.8) |
| [[SW48 (line)]] | wt | 75.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.6) |
| [[A-172 (line)]] | wt | 61.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -11.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -10.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 64.1 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.128× (z -10.0) |
| [[CHP-212 (line)]] | wt | 72.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -10.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 50.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -8.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 34.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0859× (z -12.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 78.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.408× (z -9.6) |
| [[LoVo (line)]] | wt | 54.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -14.5) |
| [[PANC-1 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -9.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 37.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.1) |
| [[A549 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8330), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM38]] | +0.72 | +0.39 / +0.78 | both halves | 5e-05 |  |
| [[CARHSP1]] | +0.72 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ARID3A]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[TRIM62]] | +0.69 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[MPG]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[RAB11FIP5]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[RASSF7]] | +0.65 | +0.48 / +0.62 | both halves | 2e-05 | STRING 402 |
| [[SLC66A2]] | +0.65 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ANKRD9]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ENO2]] | +0.65 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[SIGIRR]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDHD2]] | -0.64 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[ACADM]] | -0.64 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[NDUFS1]] | -0.64 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[MTMR2]] | -0.62 | -0.27 / -0.65 | both halves | 3e-04 |  |
| [[PSME3IP1]] | -0.62 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.62 | -0.39 / -0.65 | both halves | 6e-05 |  |
| [[ZMPSTE24]] | -0.62 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[HNRNPK]] | -0.61 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[FGD5-AS1]] | -0.61 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.61 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[GMFB]] | -0.61 | -0.39 / -0.70 | both halves | 5e-05 |  |
| [[ERLIN2]] | -0.60 | -0.50 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAG2]] | B | JAG2 activity raises RALGDS's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.65× lower at baseline in the lines without JAG2 | 0.057 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[NOG]] | B | NOG activity raises RALGDS's level | lines that do not express NOG (26) vs lines expressing it (24) | 1.19× lower at baseline in the lines without NOG | 0.096 | ⚠ within organs, on part of the lines; also absent: LINC01776, ENSG00000279289, FLI1 |
| [[PPP2R5B]] | C | PPP2R5B's natural level strengthens RALGDS's drug response | PPP2R5B's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.21; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.5, -3.5); signed map (-30.8, 17.5). **Vector** length 125, 37.3% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | -1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.4 | +4.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +3.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.6 | +4.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.1 | +2.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +3.0 | +3.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.1 | -11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -10.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.0 | -6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.6 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -4.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.9 | -2.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.7 | -3.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -2.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ral guanine nucleotide dissociation stimulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13-q34.2 — chr9:133,097,720-133,149,334 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RGF, RalGEF, RGDS |
| Gene groups (HGNC) | Ral guanine nucleotide dissociation stimulator family |
| Hallmark sets | P53_PATHWAY |
| Reactome | 9 pathways, smallest: p38MAPK events; Signalling to RAS; Signalling to ERKs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12967](https://www.uniprot.org/uniprotkb/Q12967) (Ral guanine nucleotide dissociation stimulator):

> Functions as a guanine nucleotide exchange factor (GEF) activating either RalA or RalB GTPases and plays an important role in intracellular transport. Interacts and acts as an effector molecule for R-Ras, H-Ras, K-Ras, and Rap (By similarity). During bacterial clearance, recognizes 'Lys-33'-linked polyubiquitinated TRAF3 and subsequently mediates assembly of the exocyst complex.

**Summary**, from NCBI Gene [5900](https://www.ncbi.nlm.nih.gov/gene/5900):

> Guanine nucleotide dissociation stimulators (GDSs, or exchange factors), such as RALGDS, are effectors of Ras-related GTPases (see MIM 190020) that participate in signaling for a variety of cellular processes.[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:9842](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9842) · Entrez [5900](https://www.ncbi.nlm.nih.gov/gene/5900) · UniProt [Q12967](https://www.uniprot.org/uniprotkb/Q12967) · Ensembl [ENSG00000160271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160271)

## Data

Gene col 8330: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8330); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8330, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8330]; `tensor/DDL_lfc|DDL_z.npy` [8330]; `embed/gene_vectors.npy` [8330]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8330 or target_col == 8330). Every well: [[RALGDS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RALGDS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
