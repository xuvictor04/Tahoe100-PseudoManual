---
symbol: "HIPK3"
type: "gene"
col: 3136
ensembl_id: "ENSG00000110422"
name: "homeodomain interacting protein kinase 3"
location: "11p13"
module: 137
arm: "+"
pooled_cpm: 152.92
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# HIPK3

*homeodomain interacting protein kinase 3* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.95× (z +12.4, q 1e-32, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.234× (z -31.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (68 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 32 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYND11]] (+0.66, fdr 3e-05), [[UBTF]] (+0.64, fdr 6e-05), [[YAP1]] (+0.61, fdr 1e-05); moves opposite to [[AKR1A1]] (-0.56, fdr 0.001, ⚠ one half only (not replicated)), [[FBXO16]] (-0.56, fdr 1e-04), [[CDK18]] (-0.55, fdr 3e-04), [[ZNF511]] (-0.55, fdr 6e-04).
> It sits in the **+** arm of [[Module 137]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3136.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.95×** | +12.4 | 1e-32 | 47/49 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.42×** | +10.2 | 9e-22 | 46/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +7.5 | 1e-11 | 36/48 (SW480, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +7.0 | 5e-10 | 37/48 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +5.1 | 3e-05 | 30/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.033 | 20/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.042 | 19/48 (SW480, AsPC-1, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.085 | 21/48 (SW480, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.12 | 19/47 (COLO 205, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.0 | 0.14 | 17/48 (H4, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.0 | 0.14 | 14/47 (SW480, H4, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3136.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.234×** | -31.8 | 0e+00 | 48/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.248×** | -30.5 | 0e+00 | 48/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.307×** | -25.8 | 0e+00 | 48/48 (A549, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.566×** | -12.4 | 2e-33 | 45/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.703×** | -7.7 | 2e-12 | 38/48 (A549, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.790×** | -7.2 | 4e-11 | 35/48 (LOX-IMVI, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.722×** | -6.8 | 7e-10 | 31/47 (Panc 03.27, RKO, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.561×** | -6.6 | 3e-09 | 41/49 (A549, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -6.2 | 4e-08 | 29/48 (C32, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.801×** | -4.8 | 8e-05 | 24/49 (H4, SNU-423, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.831×** | -4.0 | 0.003 | 23/49 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.709×** | -3.9 | 0.004 | 30/48 (NCI-H2347, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.839× | -3.8 | 0.006 | 23/49 (SNU-423, NCI-H2347, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.725×** | -3.7 | 0.010 | 25/48 (NCI-H2347, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | 0.840× | -3.5 | 0.018 | 20/45 (C32, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.857× | -3.3 | 0.026 | 16/48 (SK-MEL-2, C32, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.746×** | -3.3 | 0.026 | 23/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.862× | -3.2 | 0.038 | 9/48 (RKO, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3136. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 203 | 2 | 6 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 7.97× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.243× (z -16.8) |
| [[LOX-IMVI (line)]] | wt | 189 | 3 | 5 | [[TAK-901 (drug)]] 0.05 µM 2.66× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.156× (z -25.3) |
| [[SW480 (line)]] | alt | 127 | 4 | 4 | [[TAK-901 (drug)]] 5 µM 6.53× (z +16.7) | [[Panobinostat (drug)]] 5 µM 0.225× (z -25.4) |
| [[SNU-423 (line)]] | alt | 178 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -22.1) |
| [[A-172 (line)]] | wt | 208 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -24.3) |
| [[A549 (line)]] | wt | 189 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.97× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.167× (z -25.0) |
| [[HOP62 (line)]] | alt | 180 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -24.1) |
| [[LS 180 (line)]] | wt | 133 | 3 | 3 | [[TAK-901 (drug)]] 5 µM 6.35× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -18.6) |
| [[SK-MEL-2 (line)]] | alt | 175 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.02× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -16.0) |
| [[SW1417 (line)]] | alt | 159 | 1 | 5 | [[TAK-901 (drug)]] 5 µM 3.18× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -21.2) |
| [[A-427 (line)]] | wt | 126 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 6.04× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.298× (z -16.0) |
| [[AsPC-1 (line)]] | alt | 211 | 1 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.149× (z -25.3) |
| [[HS-578T (line)]] | alt | 154 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -17.7) |
| [[HT-29 (line)]] | alt | 156 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 3.24× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.185× (z -24.3) |
| [[NCI-H1792 (line)]] | alt | 164 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.117× (z -26.6) |
| [[NCI-H2030 (line)]] | alt | 128 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 4.40× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.281× (z -16.5) |
| [[PANC-1 (line)]] | alt | 190 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 2.83× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.231× (z -24.9) |
| [[SW48 (line)]] | wt | 150 | 2 | 3 | [[TAK-901 (drug)]] 0.05 µM 3.56× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.212× (z -16.1) |
| [[A498 (line)]] | wt | 162 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -24.0) |
| [[BT-474 (line)]] | alt | 132 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -17.0) |
| [[C-33 A (line)]] | alt | 160 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -14.1) |
| [[CFPAC-1 (line)]] | alt | 93.8 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 1.90× (z +9.3) ⚠ cell-cycle shift, explains ~13% of this change | [[Panobinostat (drug)]] 5 µM 0.277× (z -18.7) |
| [[HepG2_C3A (line)]] | wt | 157 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -18.6) |
| [[hTERT-HPNE (line)]] | wt | 172 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -19.1) |
| [[J82 (line)]] | alt | 171 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -21.9) |
| [[KATO III (line)]] | alt | 77.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.20× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Belinostat (drug)]] 5 µM 0.254× (z -16.0) |
| [[LoVo (line)]] | wt | 117 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.76× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.343× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 137 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 4.72× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -16.0) |
| [[NCI-H23 (line)]] | alt | 174 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -20.2) |
| [[NCI-H2347 (line)]] | alt | 194 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -23.9) |
| [[NCI-H460 (line)]] | wt | 109 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 5.02× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.256× (z -19.4) |
| [[Panc 03.27 (line)]] | alt | 225 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -25.4) |
| [[RKO (line)]] | wt | 177 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.95× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -18.8) |
| [[H4 (line)]] | wt | 134 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -14.3) |
| [[HCT15 (line)]] | alt | 171 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.308× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 150 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.298× (z -20.5) |
| [[Hs 766T (line)]] | wt | 184 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -18.2) |
| [[MIA PaCa-2 (line)]] | alt | 139 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -21.4) |
| [[RPMI-7951 (line)]] | alt | 104 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -11.5) |
| [[SHP-77 (line)]] | alt | 107 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -15.8) |
| [[SW 900 (line)]] | alt | 77.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -16.2) |
| [[SNU-1 (line)]] | wt | 140 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.352× (z -10.7) |
| [[SW 1271 (line)]] | alt | 230 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -10.5) |
| [[AN3 CA (line)]] | alt | 143 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -9.8) |
| [[CHP-212 (line)]] | wt | 68.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -9.5) |
| [[COLO 205 (line)]] | alt | 83.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.78× (z +9.7) | — |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.157× (z -10.0) |
| [[SW 1088 (line)]] | alt | 101 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -8.5) |
| [[NCI-H2122 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 144 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3136), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 26 of them with an alert (⚠; 26 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | +0.66 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[UBTF]] | +0.64 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[YAP1]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[IRAK4]] | +0.58 | +0.25 / +0.50 | both halves | 4e-04 |  |
| [[C6orf120]] | +0.58 | +0.34 / +0.44 | both halves | 1e-04 |  |
| [[CFLAR]] | +0.57 | +0.21 / +0.59 | both halves | 7e-04 |  |
| [[IL13RA1]] | +0.56 | +0.26 / +0.62 | both halves | 4e-04 |  |
| [[ZMPSTE24]] | +0.56 | +0.36 / +0.43 | both halves | 9e-05 |  |
| [[ANGEL2]] | +0.55 | +0.37 / +0.37 | both halves | 8e-05 |  |
| [[EFCAB2]] | +0.55 | +0.15 / +0.49 | ⚠ not reproduced | 0.001 |  |
| [[TSTD2]] | +0.54 | +0.27 / +0.46 | both halves | 3e-04 |  |
| [[NCOA4]] | +0.54 | +0.21 / +0.44 | both halves | 7e-04 |  |
| [[SENP8]] | +0.54 | +0.25 / +0.28 | both halves | 4e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKR1A1]] | -0.56 | -0.16 / -0.59 | ⚠ one half (not replicated) | 0.001 |  |
| [[FBXO16]] | -0.56 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[CDK18]] | -0.55 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[ZNF511]] | -0.55 | -0.22 / -0.40 | both halves | 6e-04 |  |
| [[FCHO1]] | -0.54 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[RASAL1]] | -0.52 | -0.26 / -0.48 | both halves | 4e-04 |  |
| [[GALNT12]] | -0.51 | -0.23 / -0.42 | both halves | 5e-04 |  |
| [[CAMK2G]] | -0.51 | -0.22 / -0.44 | both halves | 6e-04 |  |
| [[TMEM144]] | -0.51 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[MCTP2]] | -0.50 | -0.26 / -0.36 | both halves | 3e-04 |  |
| [[HSPA12A]] | -0.50 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[CCDC134]] | -0.49 | -0.21 / -0.51 | both halves | 7e-04 |  |
| [[TVP23C]] | -0.49 | -0.33 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-4.8, 12.2); signed map (25.6, -25.1). **Vector** length 107, 34.7% of its response variance represented; |z| ≥ 3 in 1,349 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +10.1 | +0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +0.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | -0.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.6 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.5 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -7.2 |
|  | [[EX229 (drug)]] 5 µM |  | -3.8 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | homeodomain interacting protein kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:33,256,672-33,357,023 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PKY, DYRK6, YAK1, FIST3 |
| Gene groups (HGNC) | Homeodomain interacting protein kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H422](https://www.uniprot.org/uniprotkb/Q9H422) (Homeodomain-interacting protein kinase 3):

> Serine/threonine-protein kinase involved in transcription regulation, apoptosis and steroidogenic gene expression. Phosphorylates JUN and RUNX2. Seems to negatively regulate apoptosis by promoting FADD phosphorylation. Enhances androgen receptor-mediated transcription. May act as a transcriptional corepressor for NK homeodomain transcription factors. The phosphorylation of NR5A1 activates SF1 leading to increased steroidogenic gene expression upon cAMP signaling pathway stimulation. In …

**Summary**, from NCBI Gene [10114](https://www.ncbi.nlm.nih.gov/gene/10114):

> Enables protein serine/threonine kinase activity. Involved in mRNA transcription; negative regulation of apoptotic process; and protein phosphorylation. Located in cytosol and nuclear body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4915](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4915) · Entrez [10114](https://www.ncbi.nlm.nih.gov/gene/10114) · UniProt [Q9H422](https://www.uniprot.org/uniprotkb/Q9H422) · Ensembl [ENSG00000110422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110422)

## Data

Gene col 3136: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3136); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3136, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3136]; `tensor/DDL_lfc|DDL_z.npy` [3136]; `embed/gene_vectors.npy` [3136]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3136 or target_col == 3136). Every well: [[HIPK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIPK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
