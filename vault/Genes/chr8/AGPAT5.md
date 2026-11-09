---
symbol: "AGPAT5"
type: "gene"
col: 7876
ensembl_id: "ENSG00000155189"
name: "1-acylglycerol-3-phosphate O-acyltransferase 5"
location: "8p23.1"
module: 28
arm: "+"
pooled_cpm: 93.12
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# AGPAT5

*1-acylglycerol-3-phosphate O-acyltransferase 5* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.87× (z +29.6, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.810× (z -4.2, q 0.016, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.413×, C-33 A 0.453×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.386×); [[Harringtonine (drug)]] 5 µM in 1 line (C32 0.312×); [[Harringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.278×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCPH1-AS1]] (+0.62, fdr 1e-05, ⚠ same locus), [[PFKP]] (+0.61, fdr 1e-05), [[MTR]] (+0.60, fdr 1e-05), [[PCID2]] (+0.54, fdr 1e-05); moves opposite to [[LRRFIP2]] (-0.54, fdr 2e-05), [[MARCHF5]] (-0.50, fdr 5e-05), [[STX18]] (-0.49, fdr 8e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[INAVA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7876.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.87×** | +29.6 | 0e+00 | 37/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.19×** | +15.5 | 0e+00 | 38/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.12×** | +14.9 | 0e+00 | 36/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +13.8 | 4e-41 | 39/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.95×** | +13.2 | 5e-38 | 37/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +11.0 | 5e-26 | 39/48 (SHP-77, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.73×** | +10.9 | 1e-25 | 34/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +10.1 | 4e-22 | 32/48 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +9.2 | 2e-18 | 32/47 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +8.6 | 3e-16 | 28/45 (NCI-H2347, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +8.6 | 3e-16 | 35/48 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +7.7 | 5e-13 | 26/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.03×** | +7.3 | 9e-12 | 33/36 (HEC-1-A, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.87×** | +6.5 | 3e-09 | 37/48 (HEC-1-A, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +6.3 | 2e-08 | 25/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[EX229 (drug)]] 5 µM |  | **1.65×** | +5.2 | 7e-06 | 25/48 (NCI-H460, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.43×** | +5.0 | 2e-05 | 26/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +4.8 | 6e-05 | 27/49 (NCI-H2347, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 4e-04 | 23/48 (LoVo, LS 180, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.49×** | +4.2 | 8e-04 | 24/48 (HEC-1-A, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7876.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.413×, C-33 A 0.453×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.386×); [[Harringtonine (drug)]] 5 µM in 1 line (C32 0.312×); [[Harringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.278×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.810×** | -4.2 | 0.016 | 23/48 (MIA PaCa-2, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.848× | -3.6 | 0.085 | 16/48 (SW480, CHP-212, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.818×** | -3.5 | 0.095 | 17/50 (SW480, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.886× | -3.2 | 0.15 | 9/49 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.845× | -3.2 | 0.15 | 14/48 (SW480, A549, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.744× | -3.1 | 0.20 | 15/50 (CHP-212, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7876. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 152 | 15 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +24.2) | — |
| [[NCI-H2347 (line)]] | alt | 45.7 | 14 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.3× (z +43.7) | — |
| [[AsPC-1 (line)]] | alt | 77.1 | 13 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.6× (z +31.6) | — |
| [[HEC-1-A (line)]] | alt | 116 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.39× (z +16.2) | — |
| [[NCI-H1573 (line)]] | alt | 72.7 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +29.7) | — |
| [[NCI-H460 (line)]] | wt | 90.4 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.34× (z +19.3) | — |
| [[BT-474 (line)]] | alt | 46.1 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +22.0) | — |
| [[COLO 205 (line)]] | alt | 36.4 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 75.5× (z +32.4) | — |
| [[HepG2_C3A (line)]] | wt | 91.6 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +16.9) | — |
| [[SW48 (line)]] | wt | 96.7 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +33.1) | — |
| [[H4 (line)]] | wt | 196 | 7 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.68× (z +11.1) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 5.11× (z +10.8) | — |
| [[KATO III (line)]] | alt | 111 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.57× (z +32.4) | — |
| [[LoVo (line)]] | wt | 56.6 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.7× (z +44.6) | — |
| [[HOP62 (line)]] | alt | 91.7 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.29× (z +15.1) | — |
| [[LS 180 (line)]] | wt | 91.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.92× (z +30.9) | — |
| [[SNU-423 (line)]] | alt | 80.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +21.7) | — |
| [[HT-29 (line)]] | alt | 30.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +18.8) | — |
| [[NCI-H2030 (line)]] | alt | 50.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.91× (z +33.2) | — |
| [[Panc 03.27 (line)]] | alt | 31.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +19.3) | — |
| [[A498 (line)]] | wt | 39.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.47× (z +31.8) | — |
| [[A549 (line)]] | wt | 83.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +22.7) | — |
| [[Hs 766T (line)]] | wt | 77.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +21.1) | — |
| [[LOX-IMVI (line)]] | wt | 137 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +10.2) | — |
| [[SW1417 (line)]] | alt | 36.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +18.1) | — |
| [[HS-578T (line)]] | alt | 148 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.16× (z +14.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 161 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.09× (z +11.2) | — |
| [[A-427 (line)]] | wt | 71.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +20.0) | — |
| [[C32 (line)]] | wt | 126 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 35.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +14.4) | — |
| [[HCT15 (line)]] | alt | 193 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.45× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 53.4 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.25× (z +10.2) | — |
| [[A-172 (line)]] | wt | 233 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +15.4) | — |
| [[AN3 CA (line)]] | alt | 100 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +13.1) | — |
| [[C-33 A (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.453× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[MIA PaCa-2 (line)]] | alt | 166 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +17.3) | — |
| [[NCI-H1792 (line)]] | alt | 151 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 88.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.413× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[PANC-1 (line)]] | alt | 54.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.1) | — |
| [[RKO (line)]] | wt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.5) | — |
| [[SHP-77 (line)]] | alt | 174 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.62× (z +16.3) | — |
| [[SNU-1 (line)]] | wt | 95.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.278× (z -10.9) |
| [[SW 1271 (line)]] | alt | 79.3 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0725× (z -10.2) ⚠ toxic |
| [[SW 900 (line)]] | alt | 79.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.7) | — |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7876), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCPH1-AS1]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 | ⚠ same locus (0.4 kb: neighbours can correlate without regulation) |
| [[PFKP]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[MTR]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PCID2]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[MTCH2]] | +0.54 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ZNG1B]] | +0.53 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ZBTB25]] | +0.51 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[MLH3]] | +0.50 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[ZNF638]] | +0.48 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[ZNG1A]] | +0.48 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[SBF2-AS1]] | +0.48 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[LRRC58]] | +0.48 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[ALG13]] | +0.47 | +0.36 / +0.44 | both halves | 1e-04 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRFIP2]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MARCHF5]] | -0.50 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[STX18]] | -0.49 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[IL22RA1]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ORMDL3]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[EIF4E2]] | -0.48 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[PLEKHM3]] | -0.48 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[PDCL]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[JUP]] | -0.47 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[AMBRA1]] | -0.46 | -0.42 / -0.45 | both halves | 4e-05 | same gene group |
| [[INAVA]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[YPEL2]] | -0.45 | -0.31 / -0.46 | both halves | 2e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INAVA]] | B | INAVA activity strengthens AGPAT5's drug response | lines that do not express INAVA (29) vs lines expressing it (19) | the lines without INAVA respond 0.50× as strongly (z diff +3.40); strongest at Harringtonine 5 µM: 1.34x vs 4.43x (z diff +5.2) | 0.063 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3; target measured in part of the lines; artifact flags |
| [[FAM216A]] | B | FAM216A activity raises AGPAT5's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without FAM216A | 0.069 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[TC2N]] | B | TC2N activity strengthens AGPAT5's drug response | lines that do not express TC2N (28) vs lines expressing it (20) | the lines without TC2N respond 0.46× as strongly (z diff +3.49); strongest at Homoharringtonine 0.5 µM: 1.47x vs 4.99x (z diff +5.6) | 0.071 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14; target measured in part of the lines; artifact flags |
| [[ST14]] | B | ST14 activity strengthens AGPAT5's drug response | lines that do not express ST14 (32) vs lines expressing it (16) | the lines without ST14 respond 0.50× as strongly (z diff +3.43); strongest at Homoharringtonine 0.5 µM: 1.64x vs 5.41x (z diff +4.9) | 0.081 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; target measured in part of the lines; artifact flags |
| [[ELF3]] | B | ELF3 activity strengthens AGPAT5's drug response | lines that do not express ELF3 (23) vs lines expressing it (25) | the lines without ELF3 respond 0.50× as strongly (z diff +3.23); strongest at Harringtonine 5 µM: 1.16x vs 3.78x (z diff +6.1) | 0.083 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3; target measured in part of the lines; artifact flags |
| [[TMEM92]] | B | TMEM92 activity strengthens AGPAT5's drug response | lines that do not express TMEM92 (22) vs lines expressing it (26) | the lines without TMEM92 respond 0.44× as strongly (z diff +3.40); strongest at Harringtonine 5 µM: 1.20x vs 3.51x (z diff +5.7) | 0.088 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.207). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.2, 18.6); signed map (9.0, -14.9). **Vector** length 114, 32.7% of its response variance represented; |z| ≥ 3 in 1,326 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.9 | +11.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.0 | +8.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.2 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +14.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.1 | +13.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.5 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.1 | +5.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.6 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | 1-acylglycerol-3-phosphate O-acyltransferase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:6,708,642-6,761,503 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11210, LPAAT-e, LPAAT-epsilon, LPLAT5 |
| Gene groups (HGNC) | 1-acylglycerol-3-phosphate O-acyltransferases; MicroRNA protein coding host genes; Lysophospholipid acyltransferases |
| Reactome | 4 pathways, smallest: Synthesis of PA; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUQ2](https://www.uniprot.org/uniprotkb/Q9NUQ2) (1-acyl-sn-glycerol-3-phosphate acyltransferase epsilon):

> Converts 1-acyl-sn-glycerol-3-phosphate (lysophosphatidic acid or LPA) into 1,2-diacyl-sn-glycerol-3-phosphate (phosphatidic acid or PA) by incorporating an acyl moiety at the sn-2 position of the glycerol backbone. Acts on LPA containing saturated or unsaturated fatty acids C15:0-C20:4 at the sn-1 position using C18:1-CoA as the acyl donor. Also acts on lysophosphatidylethanolamine using oleoyl-CoA, but not arachidonoyl-CoA, and lysophosphatidylinositol using arachidonoyl-CoA, but not …

**Summary**, from NCBI Gene [55326](https://www.ncbi.nlm.nih.gov/gene/55326):

> This gene encodes a member of the 1-acylglycerol-3-phosphate O-acyltransferase family. This integral membrane protein converts lysophosphatidic acid to phosphatidic acid, the second step in de novo phospholipid biosynthesis. A pseudogene of this gene is present on the Y chromosome. [provided by RefSeq, Aug 2014]

**Accessions** — [HGNC:20886](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20886) · Entrez [55326](https://www.ncbi.nlm.nih.gov/gene/55326) · UniProt [Q9NUQ2](https://www.uniprot.org/uniprotkb/Q9NUQ2) · Ensembl [ENSG00000155189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155189)

## Data

Gene col 7876: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7876); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7876, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7876]; `tensor/DDL_lfc|DDL_z.npy` [7876]; `embed/gene_vectors.npy` [7876]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7876 or target_col == 7876). Every well: [[AGPAT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGPAT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
