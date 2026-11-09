---
symbol: "CARS2"
type: "gene"
col: 5625
ensembl_id: "ENSG00000134905"
name: "cysteinyl-tRNA synthetase 2, mitochondrial"
location: "13q34"
module: 59
arm: "-"
pooled_cpm: 63.58
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# CARS2

*cysteinyl-tRNA synthetase 2, mitochondrial* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.98× (z +22.1, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.704× (z -7.7, q 7e-12, down in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.826× (z -4.4, q 0.002, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 4 lines (HEC-1-A 0.383×, A549 0.328×, NCI-H23 0.324×, NCI-H460 0.392×; ⚠ cell-cycle shift, explains ~36% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.283×, SW480 0.474×; ⚠ cell-cycle shift, explains ~90% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HEC-1-A 0.441×, A549 0.534×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHLD2]] (+0.52, fdr 3e-05), [[CPNE7]] (+0.49, fdr 5e-05), [[TMEM181]] (+0.49, fdr 5e-05); moves opposite to [[SSBP3]] (-0.52, fdr 3e-05), [[CNOT4]] (-0.47, fdr 8e-05), [[RHOV]] (-0.47, fdr 1e-04).
> It sits in the **-** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5625.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +22.1 | 0e+00 | 41/48 (Panc 03.27, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +14.0 | 9e-42 | 39/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +11.2 | 6e-27 | 41/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +9.0 | 5e-17 | 32/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +7.9 | 3e-13 | 31/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +6.7 | 2e-09 | 24/48 (MIA PaCa-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.4 | 1e-08 | 25/48 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +5.8 | 5e-07 | 20/48 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +4.6 | 3e-04 | 21/48 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.19× | +4.0 | 0.003 | 16/48 (Hs 766T, LOX-IMVI, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.20× | +4.0 | 0.003 | 20/50 (LS 180, AsPC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.003 | 12/49 (KATO III, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.18× | +3.9 | 0.005 | 13/48 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.8 | 0.007 | 14/48 (RPMI-7951, NCI-H460, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.12× | +3.7 | 0.009 | 11/48 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.035 | 12/48 (Hs 766T, LOX-IMVI, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.035 | 15/48 (LOX-IMVI, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5625.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 4 lines (HEC-1-A 0.383×, A549 0.328×, NCI-H23 0.324×, NCI-H460 0.392×; ⚠ cell-cycle shift, explains ~36% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.283×, SW480 0.474×; ⚠ cell-cycle shift, explains ~90% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HEC-1-A 0.441×, A549 0.534×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.704×** | -7.7 | 7e-12 | 30/48 (HEC-1-A, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.721×** | -7.5 | 2e-11 | 25/47 (SW480, LoVo, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.755×** | -6.2 | 1e-07 | 25/47 (LoVo, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.826×** | -4.4 | 0.002 | 22/48 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -4.3 | 0.002 | 2/49 (NCI-H23, NCI-H661) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -4.1 | 0.004 | 19/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Pimitespib (drug)]] 0.05 µM |  | 0.845× | -3.6 | 0.022 | 13/48 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.805×** | -3.5 | 0.029 | 17/48 (RKO, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | 0.863× | -3.4 | 0.049 | 17/47 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.872× | -3.1 | 0.099 | 7/49 (LS 180, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5625. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 120 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.29× (z +13.1) | [[Digitoxin (drug)]] 5 µM 0.439× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[PANC-1 (line)]] | alt | 32.1 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -15.3) ⚠ cell-cycle shift, explains ~90% of this change |
| [[LoVo (line)]] | wt | 58.2 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +15.5) | [[Digitoxin (drug)]] 5 µM 0.476× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[NCI-H1573 (line)]] | alt | 79.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +13.8) | — |
| [[NCI-H460 (line)]] | wt | 58.0 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.6) | [[Digitoxin (drug)]] 0.5 µM 0.394× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 60.7 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.328× (z -10.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.534× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 129 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -14.3) |
| [[KATO III (line)]] | alt | 58.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 82.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 40.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +13.5) | [[Harringtonine (drug)]] 5 µM 0.324× (z -9.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 46.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 62.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 46.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 47.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +17.3) | — |
| [[LS 180 (line)]] | wt | 59.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 56.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 40.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 38.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.0) | — |
| [[C32 (line)]] | wt | 55.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +11.8) | — |
| [[CFPAC-1 (line)]] | alt | 28.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +10.5) | — |
| [[HepG2_C3A (line)]] | wt | 44.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +12.3) | — |
| [[HOP62 (line)]] | alt | 89.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 81.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +11.5) | — |
| [[J82 (line)]] | alt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 26.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 76.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +17.7) | — |
| [[SW 900 (line)]] | alt | 39.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +11.1) | — |
| [[SW48 (line)]] | wt | 91.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.1) | — |
| [[A-172 (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 109 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 63.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5625), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHLD2]] | +0.52 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[CPNE7]] | +0.49 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[TMEM181]] | +0.49 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[MROH1]] | +0.48 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[IL6R]] | +0.47 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[SPG7]] | +0.47 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[ING5]] | +0.46 | +0.33 / +0.52 | both halves | 1e-04 |  |
| [[TBC1D2]] | +0.45 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[SKI]] | +0.45 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[ITGB1BP1]] | +0.45 | +0.23 / +0.50 | both halves | 5e-04 |  |
| [[PRSS53]] | +0.45 | +0.24 / +0.52 | both halves | 4e-04 |  |
| [[FAM86DP-1]] | +0.45 | +0.43 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSBP3]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[CNOT4]] | -0.47 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[RHOV]] | -0.47 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[ELF3]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[CSTPP1]] | -0.47 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[ID3]] | -0.46 | -0.24 / -0.50 | both halves | 5e-04 |  |
| [[GPKOW]] | -0.44 | -0.25 / -0.59 | both halves | 4e-04 |  |
| [[AKR1C3]] | -0.44 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[RSPH1]] | -0.44 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[LINC02967]] | -0.44 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[TNFSF10]] | -0.44 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[IKZF2]] | -0.44 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CARS2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **-** arm (projection on the module's main direction -0.238). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.7, 32.7); signed map (-21.4, 0.5). **Vector** length 103, 25.9% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +1.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.8 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.0 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +3.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.8 | +2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.6 | +4.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -6.4 | -7.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | -3.8 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.8 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -4.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.5 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | cysteinyl-tRNA synthetase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:110,641,412-110,713,603 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12118 |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I |
| Reactome | 3 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HA77](https://www.uniprot.org/uniprotkb/Q9HA77) (Probable cysteine--tRNA ligase, mitochondrial):

> Mitochondrial cysteine-specific aminoacyl-tRNA synthetase that catalyzes the ATP-dependent ligation of cysteine to tRNA(Cys).; In addition to its role as an aminoacyl-tRNA synthetase, has also cysteine persulfide synthase activity. Produces reactive persulfide species such as cysteine persulfide (CysSSH) from substrate cysteine and mediate direct incorporation of CysSSH into proteins during translations, resulting in protein persulfides and polysulfides. CysSSHs behave as potent antioxidants …

**Summary**, from NCBI Gene [79587](https://www.ncbi.nlm.nih.gov/gene/79587):

> This gene encodes a putative member of the class I family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. This protein is encoded by the nuclear genome but is likely to be imported to the mitochondrion where it is thought to catalyze the ligation of cysteine to tRNA molecules. A splice-site mutation in this gene has been associated with a novel progressive myoclonic epilepsy disease with similar symptoms …

**Accessions** — [HGNC:25695](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25695) · Entrez [79587](https://www.ncbi.nlm.nih.gov/gene/79587) · UniProt [Q9HA77](https://www.uniprot.org/uniprotkb/Q9HA77) · Ensembl [ENSG00000134905](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134905)

## Data

Gene col 5625: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5625); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5625, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5625]; `tensor/DDL_lfc|DDL_z.npy` [5625]; `embed/gene_vectors.npy` [5625]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5625 or target_col == 5625). Every well: [[CARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
