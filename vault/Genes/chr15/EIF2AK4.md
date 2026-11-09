---
symbol: "EIF2AK4"
type: "gene"
col: 4923
ensembl_id: "ENSG00000128829"
name: "eukaryotic translation initiation factor 2 alpha kinase 4"
location: "15q15.1"
module: 213
arm: "+"
pooled_cpm: 63.82
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/213"]
generated_by: "tahoemap"
---

# EIF2AK4

*eukaryotic translation initiation factor 2 alpha kinase 4* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 1.41× (z +5.0, q 3e-04, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.650× (z -16.9, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNHIT6]] (+0.58, fdr 1e-05), [[GRHPR]] (+0.57, fdr 1e-05), [[XPO7]] (+0.56, fdr 1e-05); moves opposite to [[HNRNPD-DT]] (-0.47, fdr 1e-04), [[LINC01128]] (-0.47, fdr 4e-05), [[GABRE]] (-0.45, fdr 2e-04).
> It is in [[Module 213]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4923.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **1.41×** | +5.0 | 3e-04 | 19/47 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.13× | +4.9 | 3e-04 | 14/48 (A-427, HepG2/C3A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +4.5 | 0.002 | 17/48 (HT-29, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.16× | +4.0 | 0.008 | 10/48 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.030 | 13/48 (RPMI-7951, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.030 | 10/47 (KATO III, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.14× | +3.5 | 0.030 | 17/48 (Panc 03.27, MIA PaCa-2, …) | two highest doses | composition shift |
| [[Radotinib (drug)]] 5 µM |  | 1.09× | +3.5 | 0.030 | 4/48 (NCI-H1792, COLO 205, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.13× | +3.4 | 0.038 | 14/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.075 | 3/48 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | 1.23× | +3.0 | 0.12 | 3/48 (LOX-IMVI, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.11× | +3.0 | 0.12 | 10/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4923.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.650×** | -16.9 | 0e+00 | 39/48 (MIA PaCa-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.710×** | -9.5 | 5e-19 | 28/47 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.808×** | -8.4 | 1e-14 | 26/48 (NCI-H460, NCI-H1573, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.778×** | -7.0 | 5e-10 | 26/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -6.8 | 1e-09 | 0/49 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.795×** | -6.4 | 2e-08 | 24/48 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.807×** | -5.9 | 2e-07 | 24/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.822×** | -5.2 | 1e-05 | 23/48 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.829×** | -4.8 | 9e-05 | 22/45 (KATO III, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | 0.856× | -4.3 | 9e-04 | 18/48 (LoVo, A-427, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.744×** | -4.3 | 9e-04 | 22/48 (Hs 766T, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.880× | -3.4 | 0.029 | 20/49 (SW480, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.922× | -3.2 | 0.062 | 4/48 (HS-578T, MIA PaCa-2, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.888× | -3.2 | 0.062 | 15/47 (HepG2/C3A, SNU-423, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.894× | -3.1 | 0.073 | 12/47 (LOX-IMVI, COLO 205, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4923. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 70.7 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -22.3) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.375× (z -15.9) |
| [[HOP62 (line)]] | alt | 56.4 | 0 | 4 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.390× (z -16.1) |
| [[LoVo (line)]] | wt | 112 | 1 (1 ⚠) | 3 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.599× (z -11.6) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.569× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 47.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -15.0) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 33.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -13.3) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 126 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -11.2) |
| [[PANC-1 (line)]] | alt | 51.1 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +25.7) ⚠ cell-cycle shift, explains ~13% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -15.8) |
| [[A498 (line)]] | wt | 107 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 61.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +18.6) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[HS-578T (line)]] | alt | 51.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.358× (z -11.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.6) |
| [[J82 (line)]] | alt | 80.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -13.5) |
| [[KATO III (line)]] | alt | 38.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -12.1) |
| [[LS 180 (line)]] | wt | 50.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +12.9) | — |
| [[RKO (line)]] | wt | 108 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.392× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -10.3) |
| [[SNU-1 (line)]] | wt | 81.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.359× (z -8.7) |
| [[SW48 (line)]] | wt | 75.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.5) ⚠ cell-cycle shift, explains ~13% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 82.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -9.0) |
| [[COLO 205 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.5) ⚠ cell-cycle shift, explains ~13% of this change |
| [[H4 (line)]] | wt | 78.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 44.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.34× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 53.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -17.5) |
| [[MIA PaCa-2 (line)]] | alt | 67.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -18.6) |
| [[RPMI-7951 (line)]] | alt | 67.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -12.5) ⚠ cell-cycle shift, explains ~13% of this change |
| [[SHP-77 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.365× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 78.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -8.6) |
| [[SW1417 (line)]] | alt | 58.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -15.6) |
| [[SW480 (line)]] | alt | 53.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -10.1) |
| [[A-427 (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 103 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 85.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4923), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNHIT6]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[GRHPR]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[XPO7]] | +0.56 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[MRPL19]] | +0.54 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ACBD6]] | +0.54 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[VWA8]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ORC5]] | +0.53 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[BMS1]] | +0.52 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[ZNF30]] | +0.52 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[RIOX2]] | +0.52 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[SMARCAD1]] | +0.52 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[KBTBD6]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPD-DT]] | -0.47 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[LINC01128]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[GABRE]] | -0.45 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[KPNB1-DT]] | -0.45 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[UBE2R2-AS1]] | -0.44 | -0.24 / -0.46 | both halves | 4e-04 |  |
| [[SPATA1]] | -0.44 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[HCG20]] | -0.44 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[CCNYL1]] | -0.44 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[BTG1-DT]] | -0.43 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[USP34-DT]] | -0.43 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[HCG27]] | -0.43 | -0.25 / -0.47 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 213]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.548). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-18.1, -43.8); signed map (-13.3, -48.7). **Vector** length 105, 24.8% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +4.3 | +4.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +3.7 | +4.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.6 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.5 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.9 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -16.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 2 alpha kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:39,934,115-40,035,591 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GCN2, KIAA1338 |
| Gene groups (HGNC) | Eukaryotic translation initiation factor 2 alpha kinases; RWD domain containing |
| Reactome | 4 pathways, smallest: Response of EIF2AK4 (GCN2) to amino acid deficiency; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2K8](https://www.uniprot.org/uniprotkb/Q9P2K8) (eIF-2-alpha kinase GCN2):

> Metabolic-stress sensing protein kinase that phosphorylates the alpha subunit of eukaryotic translation initiation factor 2 (EIF2S1/eIF-2-alpha) in response to low amino acid availability. Plays a role as an activator of the integrated stress response (ISR) required for adaptation to amino acid starvation (By similarity). EIF2S1/eIF-2-alpha phosphorylation in response to stress converts EIF2S1/eIF-2-alpha into a global protein synthesis inhibitor, leading to a global attenuation of …

**Summary**, from NCBI Gene [440275](https://www.ncbi.nlm.nih.gov/gene/440275):

> This gene encodes a member of a family of kinases that phosphorylate the alpha subunit of eukaryotic translation initiation factor-2 (EIF2), resulting in the downregulaton of protein synthesis. The encoded protein responds to amino acid deprivation by binding uncharged transfer RNAs. It may also be activated by glucose deprivation and viral infection. Mutations in this gene have been found in individuals suffering from autosomal recessive pulmonary venoocclusive-disease-2. [provided by RefSeq, …

**Accessions** — [HGNC:19687](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19687) · Entrez [440275](https://www.ncbi.nlm.nih.gov/gene/440275) · UniProt [Q9P2K8](https://www.uniprot.org/uniprotkb/Q9P2K8) · Ensembl [ENSG00000128829](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128829)

## Data

Gene col 4923: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4923); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4923, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4923]; `tensor/DDL_lfc|DDL_z.npy` [4923]; `embed/gene_vectors.npy` [4923]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4923 or target_col == 4923). Every well: [[EIF2AK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF2AK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
