---
symbol: "TTC5"
type: "gene"
col: 5854
ensembl_id: "ENSG00000136319"
name: "tetratricopeptide repeat domain 5"
location: "14q11.2"
module: 17
arm: "+"
pooled_cpm: 16.37
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 12
n_dd_up_clean: 25
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TTC5

*tetratricopeptide repeat domain 5* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.68× (z +16.6, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.444× (z -13.7, q 6e-40, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAAL1]] (+0.71, fdr 7e-06), [[MRPS31P4]] (+0.71, fdr 9e-06), [[ALKBH8]] (+0.70, fdr 1e-05); moves opposite to [[PDE6D]] (-0.63, fdr 3e-05), [[C2]] (-0.60, fdr 2e-04), [[TPTEP2-CSNK1E]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF420]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5854.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.68×** | +16.6 | 0e+00 | 45/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.50×** | +15.4 | 0e+00 | 46/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.30×** | +14.0 | 5e-42 | 45/47 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +10.4 | 3e-23 | 39/48 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +10.3 | 1e-22 | 37/48 (NCI-H2347, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +9.5 | 2e-19 | 15/25 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +8.4 | 3e-15 | 26/42 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +7.3 | 1e-11 | 24/44 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +7.0 | 2e-10 | 31/48 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +6.3 | 2e-08 | 23/48 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +5.6 | 9e-07 | 24/48 (NCI-H1792, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.40×** | +5.6 | 9e-07 | 17/48 (HCT15, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.5 | 2e-06 | 18/47 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.38×** | +5.3 | 4e-06 | 14/48 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +5.0 | 2e-05 | 16/47 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +4.8 | 5e-05 | 15/47 (AsPC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 2e-04 | 15/47 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 2e-04 | 18/47 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5854.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.444×** | -13.7 | 6e-40 | 39/47 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.465×** | -12.9 | 8e-36 | 37/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.492×** | -12.0 | 1e-30 | 41/48 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.510×** | -11.4 | 1e-27 | 38/47 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.567×** | -9.2 | 4e-18 | 31/47 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.620×** | -7.8 | 8e-13 | 24/46 (A549, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.653×** | -7.2 | 4e-11 | 27/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -6.9 | 3e-10 | 25/48 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.715×** | -5.7 | 8e-07 | 25/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.730×** | -5.3 | 6e-06 | 18/48 (J82, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.819×** | -3.4 | 0.036 | 12/47 (CFPAC-1, COLO 205, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.831×** | -3.2 | 0.076 | 8/47 (SNU-423, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5854. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.0 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.08× (z +9.2) | — |
| [[SW480 (line)]] | alt | 21.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.301× (z -10.0) |
| [[BT-474 (line)]] | alt | 22.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.71× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.165× (z -10.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 16.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Thymol (drug)]] 0.5 µM 0.128× (z -9.6) |
| [[LoVo (line)]] | wt | 8.16 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.03× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.199× (z -9.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 16.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.79× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 23.7 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.98× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.329× (z -8.7) |
| [[A-427 (line)]] | wt | 24.3 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.327× (z -12.7) |
| [[A498 (line)]] | wt | 8.34 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.180× (z -11.8) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 4.28 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0687× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 22.4 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0597× (z -14.8) |
| [[CHP-212 (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -8.6) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 37.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.269× (z -8.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 10.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.288× (z -9.9) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 39.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +10.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0791× (z -12.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -11.3) |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -9.7) |
| [[A-172 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5854), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAAL1]] | +0.71 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[MRPS31P4]] | +0.71 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[ALKBH8]] | +0.70 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[QDPR]] | +0.70 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[RBM18]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[COG2]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[EHMT2]] | +0.68 | +0.52 / +0.69 | both halves | 1e-05 | pathway: Regulation of TP53 Activity |
| [[IRAK1BP1]] | +0.68 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[BBS5]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[DLAT]] | +0.66 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[DLD]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[VTA1]] | +0.65 | +0.47 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE6D]] | -0.63 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[C2]] | -0.60 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[TPTEP2-CSNK1E]] | -0.60 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[PSMD6-AS2]] | -0.57 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[NFATC2IP]] | -0.56 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[NR2C2]] | -0.56 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[PRDM10]] | -0.55 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[TMEM11-DT]] | -0.54 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[LINC00862]] | -0.54 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[TRPV1]] | -0.54 | -0.21 / -0.57 | both halves | 7e-04 |  |
| [[ING2-DT]] | -0.54 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[DLEU2]] | -0.53 | -0.33 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF420]] | B | ZNF420 activity raises TTC5's level | lines that do not express ZNF420 (7) vs lines expressing it (43) | 1.72× lower at baseline in the lines without ZNF420 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF850, ZNF540 |
| [[TOP2A]] | B | TOP2A activity raises TTC5's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.738). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.2, -1.5); signed map (-22.0, -16.8). **Vector** length 85.3, 18.0% of its response variance represented; |z| ≥ 3 in 1,222 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.3 | +10.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +4.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +9.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +7.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +3.4 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.1 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.8 | -11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -4.7 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:20,256,558-20,305,960 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Strap |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Reactome | 3 pathways, smallest: Regulation of TP53 Activity through Methylation; Regulation of TP53 Activity; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N0Z6](https://www.uniprot.org/uniprotkb/Q8N0Z6) (Tetratricopeptide repeat protein 5):

> Cofactor involved in the regulation of various cellular mechanisms such as actin regulation, autophagy, chromatin regulation and DNA repair. In non-stress conditions, interacts with cofactor JMY in the cytoplasm which prevents JMY's actin nucleation activity and ability to activate the Arp2/3 complex. Acts as a negative regulator of nutrient stress-induced autophagy by preventing JMY's interaction with MAP1LC3B, thereby preventing autophagosome formation (By similarity). Involves in tubulin …

**Summary**, from NCBI Gene [91875](https://www.ncbi.nlm.nih.gov/gene/91875):

> Enables ribosome binding activity. Involved in positive regulation of mRNA catabolic process. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19274](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19274) · Entrez [91875](https://www.ncbi.nlm.nih.gov/gene/91875) · UniProt [Q8N0Z6](https://www.uniprot.org/uniprotkb/Q8N0Z6) · Ensembl [ENSG00000136319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136319)

## Data

Gene col 5854: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5854); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5854, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5854]; `tensor/DDL_lfc|DDL_z.npy` [5854]; `embed/gene_vectors.npy` [5854]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5854 or target_col == 5854). Every well: [[TTC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
