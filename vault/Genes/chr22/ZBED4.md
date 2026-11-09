---
symbol: "ZBED4"
type: "gene"
col: 1960
ensembl_id: "ENSG00000100426"
name: "zinc finger BED-type containing 4"
location: "22q13.33"
module: 36
arm: "+"
pooled_cpm: 32.53
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ZBED4

*zinc finger BED-type containing 4* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.50× (z +9.2, q 2e-17, up in 34 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.47× (z +8.8, q 6e-16, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.692× (z -11.8, q 2e-29, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYAR]] (+0.68, fdr 1e-05), [[VKORC1L1]] (+0.68, fdr 7e-06), [[CCM2]] (+0.67, fdr 7e-06); moves opposite to [[BDH2]] (-0.65, fdr 1e-05), [[BTN3A1]] (-0.64, fdr 1e-05), [[GIPC2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1960.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +9.2 | 2e-17 | 34/47 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +8.8 | 6e-16 | 32/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.41×** | +7.8 | 9e-13 | 28/48 (SW480, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.36×** | +6.9 | 8e-10 | 26/47 (SW 900, SW480, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.3 | 0.002 | 0/48 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.14× | +4.2 | 0.003 | 18/48 (A498, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.9 | 0.009 | 12/48 (SW 900, NCI-H1573, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.18× | +3.7 | 0.017 | 16/46 (A498, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | 1.18× | +3.6 | 0.020 | 19/46 (HT-29, NCI-H1792, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.022 | 9/47 (SNU-423, J82, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.17× | +3.5 | 0.025 | 12/47 (SW 900, C-33 A, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.17× | +3.5 | 0.026 | 9/47 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.035 | 8/47 (SW 900, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.063 | 8/47 (SW 900, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.063 | 9/47 (LoVo, LS 180, …) | rises with dose | low cells (technical?) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 1.16× | +3.1 | 0.063 | 5/47 (NCI-H23, J82, …) | top dose only | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.065 | 9/46 (SW 900, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.15× | +3.0 | 0.082 | 8/47 (NCI-H23, C32, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.0 | 0.082 | 5/48 (AsPC-1, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1960.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.692×** | -11.8 | 2e-29 | 32/48 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.646×** | -9.9 | 1e-20 | 26/45 (A-427, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.717×** | -7.0 | 6e-10 | 23/43 (SW48, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.631×** | -5.5 | 6e-06 | 22/45 (COLO 205, KATO III, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.862× | -4.8 | 2e-04 | 17/48 (A-427, BT-474, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.825×** | -4.4 | 0.001 | 18/48 (LoVo, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.835× | -3.9 | 0.007 | 19/39 (HEC-1-A, LS 180, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.847× | -3.8 | 0.010 | 17/47 (SW 900, CHP-212, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.872× | -3.8 | 0.010 | 16/48 (C32, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.869× | -3.7 | 0.013 | 11/48 (LoVo, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.849× | -3.6 | 0.018 | 23/48 (A-427, J82, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.897× | -3.5 | 0.020 | 14/48 (LoVo, AsPC-1, …) | all doses, flat | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 0.858× | -3.5 | 0.020 | 15/48 (KATO III, A-172, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.891× | -3.2 | 0.054 | 10/48 (Hs 766T, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.768×** | -3.1 | 0.063 | 14/48 (NCI-H1573, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.871× | -3.0 | 0.086 | 11/47 (SW480, COLO 205, …) | all doses, flat |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.878× | -3.0 | 0.093 | 7/48 (AN3 CA, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1960. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 28.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -14.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 42.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.3) |
| [[SW48 (line)]] | wt | 43.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -10.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 36.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0878× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.466× (z -11.0) |
| [[J82 (line)]] | alt | 29.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -15.0) |
| [[A-172 (line)]] | wt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -13.0) |
| [[A498 (line)]] | wt | 24.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -9.2) |
| [[AN3 CA (line)]] | alt | 53.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -9.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 32.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.2) |
| [[C32 (line)]] | wt | 40.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -10.2) |
| [[COLO 205 (line)]] | alt | 23.5 | 0 | 1 | — | [[NG25 (drug)]] 5 µM 0.0543× (z -8.8) |
| [[HOP62 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -9.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 32.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -9.8) |
| [[LS 180 (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 23.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 28.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 51.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.261× (z -8.9) ⚠ toxic |
| [[A549 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1960), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYAR]] | +0.68 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[VKORC1L1]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CCM2]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[DGCR8]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ABCC10]] | +0.64 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[PDCD11]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[AXIN1]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ZMYND19]] | +0.63 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[EEFSEC]] | +0.63 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[PINX1]] | +0.63 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ZNF496]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[MPP3]] | +0.61 | +0.57 / +0.61 | both halves | 9e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BDH2]] | -0.65 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[BTN3A1]] | -0.64 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[GIPC2]] | -0.60 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.60 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[PMPCB]] | -0.59 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[RBM39]] | -0.58 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[FAM111A-DT]] | -0.58 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[NR1D2]] | -0.57 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[CA11]] | -0.56 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[FMR1]] | -0.56 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[UFC1]] | -0.56 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[ECH1]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ZBED4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-6.6, -27.5); signed map (-45.0, -16.8). **Vector** length 100.0, 21.7% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.4 | +9.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +3.8 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +8.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.2 | +7.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -11.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.5 | -4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.5 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger BED-type containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:49,853,844-49,890,080 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0637 |
| Gene groups (HGNC) | Zinc fingers BED-type |
| Matched by | ensembl_id |

**Function**, from UniProt [O75132](https://www.uniprot.org/uniprotkb/O75132) (Zinc finger BED domain-containing protein 4):

> Transcriptional regulator that binds to poly-guanine tracts in gene promoters and activates transcription (By similarity). Able to bind single- and double-stranded DNA and RNA (By similarity).

**Summary**, from NCBI Gene [9889](https://www.ncbi.nlm.nih.gov/gene/9889):

> Enables identical protein binding activity. Predicted to be involved in positive regulation of transcription by RNA polymerase II. Located in cytoplasm and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20721](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20721) · Entrez [9889](https://www.ncbi.nlm.nih.gov/gene/9889) · UniProt [O75132](https://www.uniprot.org/uniprotkb/O75132) · Ensembl [ENSG00000100426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100426)

## Data

Gene col 1960: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1960); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1960, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1960]; `tensor/DDL_lfc|DDL_z.npy` [1960]; `embed/gene_vectors.npy` [1960]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1960 or target_col == 1960). Every well: [[ZBED4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBED4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
