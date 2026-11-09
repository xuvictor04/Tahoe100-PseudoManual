---
symbol: "PXYLP1"
type: "gene"
col: 7928
ensembl_id: "ENSG00000155893"
name: "2-phosphoxylose phosphatase 1"
location: "3q23"
module: 97
arm: "+"
pooled_cpm: 24.51
n_lines_expressing: 47
n_dd_up: 22
n_dd_down: 18
n_dd_up_clean: 17
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# PXYLP1

*2-phosphoxylose phosphatase 1* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +18.7, q 0e+00, up in 32 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.437× (z -26.1, q 0e+00, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LDLRAD3]] (+0.64, fdr 7e-06), [[TMEM164]] (+0.60, fdr 1e-05), [[ADCY3]] (+0.60, fdr 1e-05); moves opposite to [[SYTL2]] (-0.54, fdr 3e-05), [[ZSCAN31]] (-0.50, fdr 3e-05), [[CHD2]] (-0.49, fdr 3e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NR3C1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ARHGEF19]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7928.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +18.7 | 0e+00 | 32/42 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +8.9 | 1e-16 | 24/44 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +8.1 | 7e-14 | 22/45 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.43×** | +8.0 | 2e-13 | 17/42 (NCI-H1792, A-172, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +7.9 | 3e-13 | 21/43 (NCI-H1792, HOP62, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +7.5 | 5e-12 | 20/43 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.38×** | +7.2 | 4e-11 | 19/43 (NCI-H1792, HOP62, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.37×** | +7.0 | 1e-10 | 21/44 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.37×** | +7.0 | 2e-10 | 18/44 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +6.6 | 2e-09 | 16/43 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.30×** | +5.9 | 2e-07 | 16/42 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.6 | 1e-06 | 14/40 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +5.4 | 4e-06 | 16/42 (PANC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.26×** | +5.1 | 1e-05 | 14/45 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.26×** | +5.1 | 1e-05 | 15/44 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.24×** | +4.8 | 6e-05 | 16/44 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +4.4 | 3e-04 | 10/45 (PANC-1, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.24×** | +4.4 | 3e-04 | 14/42 (NCI-H1792, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7928.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.437×** | -26.1 | 0e+00 | 32/45 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.486×** | -16.1 | 0e+00 | 33/43 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.574×** | -12.4 | 5e-33 | 28/43 (J82, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.576×** | -12.3 | 9e-33 | 26/39 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.576×** | -12.3 | 1e-32 | 30/44 (SNU-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.357×** | -12.0 | 3e-31 | 31/44 (NCI-H1792, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.575×** | -11.9 | 1e-30 | 31/44 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.618×** | -10.3 | 4e-23 | 21/30 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.670×** | -8.9 | 2e-17 | 27/43 (A549, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.678×** | -8.7 | 2e-16 | 28/44 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.681×** | -8.6 | 6e-16 | 25/43 (A549, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.673×** | -8.5 | 9e-16 | 27/41 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.714×** | -7.5 | 2e-12 | 24/43 (SK-MEL-2, Panc 03.27, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.562×** | -6.7 | 7e-10 | 24/42 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -6.6 | 1e-09 | 22/43 (HEC-1-A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.790×** | -5.2 | 5e-06 | 19/44 (HOP62, NCI-H23, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.853× | -5.0 | 2e-05 | 15/45 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.862× | -3.2 | 0.037 | 10/43 (SK-MEL-2, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7928. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 29.6 | 10 | 2 | [[Clobetasol propionate (drug)]] 0.5 µM 5.08× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0907× (z -23.9) |
| [[A549 (line)]] | wt | 65.6 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0861× (z -25.0) |
| [[HOP62 (line)]] | alt | 21.7 | 6 | 3 | [[Clobetasol propionate (drug)]] 0.05 µM 5.48× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -17.1) |
| [[HEC-1-A (line)]] | alt | 31.5 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -15.3) |
| [[HS-578T (line)]] | alt | 26.3 | 7 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 3.88× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 49.4 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -12.0) |
| [[RKO (line)]] | wt | 55.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -20.2) |
| [[J82 (line)]] | alt | 16.8 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0540× (z -18.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.204× (z -14.5) |
| [[A-172 (line)]] | wt | 16.8 | 3 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 5.10× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.166× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 30.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0846× (z -21.0) |
| [[A498 (line)]] | wt | 50.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0841× (z -17.5) |
| [[C-33 A (line)]] | alt | 46.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -13.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 39.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -10.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 30.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 9.66 | 2 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 4.39× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 8.97 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.1) |
| [[SNU-423 (line)]] | alt | 23.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -17.8) |
| [[SW 900 (line)]] | alt | 45.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -13.6) |
| [[SW1417 (line)]] | alt | 24.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -11.8) |
| [[A-427 (line)]] | wt | 30.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 44.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -10.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -15.0) |
| [[CFPAC-1 (line)]] | alt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -8.8) |
| [[HCT15 (line)]] | alt | 9.54 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0953× (z -8.5) |
| [[HT-29 (line)]] | alt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 6.47 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0981× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 20.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 24.4 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0923× (z -9.3) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 33.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -14.7) |
| [[SW480 (line)]] | alt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +14.2) | — |
| [[AsPC-1 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.45 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.08 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7928), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDLRAD3]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[TMEM164]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[SH3RF3]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[AFAP1L1]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TLR2]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[NT5M]] | +0.58 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[TYRO3]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ZHX3]] | +0.57 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[SEC14L2]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[GAB3]] | +0.55 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[TRABD2B]] | +0.55 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYTL2]] | -0.54 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ZSCAN31]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[CHD2]] | -0.49 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | -0.47 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[CLCN3]] | -0.47 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[MAF]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[GRIPAP1]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[ATRX]] | -0.45 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[KIAA1217]] | -0.45 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ARHGAP42]] | -0.45 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[SLAMF7]] | -0.45 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[OCIAD1]] | -0.45 | -0.36 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises PXYLP1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF19]] | C | PXYLP1 activity lowers ARHGEF19's level | lines that do not express PXYLP1 (3) vs lines expressing it (47) | 2.26× higher at baseline in the lines without PXYLP1 | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: PDE4C, ZFHX2, PDE5A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.0, 13.7); signed map (16.5, 35.0). **Vector** length 98.9, 23.0% of its response variance represented; |z| ≥ 3 in 1,343 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +18.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +8.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +4.0 | +7.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.0 | +4.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.9 | +6.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.9 | +7.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -16.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -26.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.7 | -12.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -7.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | 2-phosphoxylose phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:141,228,726-141,367,753 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23751; previously ACPL2 |
| Gene groups (HGNC) | Acid phosphatases |
| Reactome | 3 pathways, smallest: Glycosaminoglycan-protein linkage region biosynthesis; Glycosaminoglycan metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TE99](https://www.uniprot.org/uniprotkb/Q8TE99) (2-phosphoxylose phosphatase 1):

> Responsible for the 2-O-dephosphorylation of xylose in the glycosaminoglycan-protein linkage region of proteoglycans thereby regulating the amount of mature glycosaminoglycan (GAG) chains. Sulfated glycosaminoglycans (GAGs), including heparan sulfate and chondroitin sulfate, are synthesized on the so-called common GAG-protein linkage region (GlcUAbeta1-3Galbeta1-3Galbeta1-4Xylbeta1-O-Ser) of core proteins, which is formed by the stepwise addition of monosaccharide residues by the respective …

**Summary**, from NCBI Gene [92370](https://www.ncbi.nlm.nih.gov/gene/92370):

> Enables phosphatase activity. Involved in chondroitin sulfate proteoglycan biosynthetic process; glycosaminoglycan biosynthetic process; and positive regulation of heparan sulfate proteoglycan biosynthetic process. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26303) · Entrez [92370](https://www.ncbi.nlm.nih.gov/gene/92370) · UniProt [Q8TE99](https://www.uniprot.org/uniprotkb/Q8TE99) · Ensembl [ENSG00000155893](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155893)

## Data

Gene col 7928: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7928); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7928, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7928]; `tensor/DDL_lfc|DDL_z.npy` [7928]; `embed/gene_vectors.npy` [7928]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7928 or target_col == 7928). Every well: [[PXYLP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PXYLP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
