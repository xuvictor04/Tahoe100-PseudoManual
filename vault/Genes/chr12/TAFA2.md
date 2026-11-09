---
symbol: "TAFA2"
type: "gene"
col: 12638
ensembl_id: "ENSG00000198673"
name: "TAFA chemokine like family member 2"
location: "12q14.1"
module: 10
arm: "+"
pooled_cpm: 13.64
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 9
n_dd_up_clean: 35
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TAFA2

*TAFA chemokine like family member 2* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.93× (z +34.2, q 0e+00, up in 43 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.591× (z -6.1, q 5e-07, down in 22 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.618× (z -5.6, q 6e-06, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAP2C-AS1]] (+0.76, fdr 7e-06), [[CFAP418-AS1]] (+0.76, fdr 1e-05), [[PKN2-AS1]] (+0.76, fdr 3e-05); moves opposite to [[YIF1B]] (-0.68, fdr 6e-04), [[MAST3]] (-0.66, fdr 4e-04), [[CCDC134]] (-0.66, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12638.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.93×** | +34.2 | 0e+00 | 43/43 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.55×** | +15.5 | 0e+00 | 41/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.28×** | +13.4 | 2e-38 | 39/45 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.04×** | +12.5 | 1e-33 | 39/45 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +9.3 | 1e-18 | 29/39 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +8.4 | 5e-15 | 29/47 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.04×** | +8.3 | 6e-15 | 38/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +7.6 | 3e-12 | 14/21 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +6.5 | 7e-09 | 19/30 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +5.5 | 3e-06 | 21/48 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.62×** | +5.4 | 3e-06 | 21/46 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +5.2 | 8e-06 | 21/46 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.54×** | +4.8 | 8e-05 | 15/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.32×** | +4.6 | 2e-04 | 15/48 (NCI-H460, A-427, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +4.5 | 2e-04 | 16/47 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.48×** | +4.4 | 3e-04 | 18/45 (NCI-H23, LS 180, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.30×** | +4.3 | 6e-04 | 17/48 (A-172, NCI-H460, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +4.1 | 0.002 | 13/48 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.002 | 13/48 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12638.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.591×** | -6.1 | 5e-07 | 22/47 (NCI-H1573, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.618×** | -5.6 | 6e-06 | 24/46 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.667×** | -4.6 | 9e-04 | 20/46 (SW48, LoVo, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.694×** | -4.3 | 0.003 | 21/46 (LS 180, A-427, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.702×** | -4.1 | 0.004 | 18/47 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.747×** | -3.4 | 0.066 | 15/46 (NCI-H23, LS 180, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.754×** | -3.3 | 0.081 | 15/45 (hTERT-HPNE, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.750×** | -3.3 | 0.081 | 12/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.591×** | -3.2 | 0.085 | 9/45 (J82, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12638. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.96 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.0× (z +17.4) | — |
| [[NCI-H460 (line)]] | wt | 11.1 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +18.8) | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.79× (z +18.4) | — |
| [[A498 (line)]] | wt | 13.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +17.2) | — |
| [[HOP62 (line)]] | alt | 7.16 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.04× (z +14.0) | — |
| [[LoVo (line)]] | wt | 16.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +22.5) | — |
| [[LOX-IMVI (line)]] | wt | 97.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 33.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.61× (z +9.7) ⚠ position not correctable | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.141× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 10.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.9× (z +16.9) | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +11.1) | — |
| [[SW48 (line)]] | wt | 13.6 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.88× (z +10.0) | [[Digitoxin (drug)]] 0.05 µM 0.0575× (z -9.0) |
| [[SW480 (line)]] | alt | 8.68 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +14.1) | — |
| [[A-427 (line)]] | wt | 12.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0969× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.199× (z -9.2) |
| [[BT-474 (line)]] | alt | 11.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.76× (z +12.2) | [[Digitoxin (drug)]] 5 µM 0.0648× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[C-33 A (line)]] | alt | 17.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.0887× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 10.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 6.73 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.9× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 6.12 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +13.9) | — |
| [[LS 180 (line)]] | wt | 14.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +11.2) | [[Digitoxin (drug)]] 5 µM 0.0501× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[PANC-1 (line)]] | alt | 7.30 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.53× (z +16.1) | — |
| [[RPMI-7951 (line)]] | alt | 12.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.73× (z +11.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0960× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 6.71 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +13.1) | — |
| [[A549 (line)]] | wt | 8.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +14.5) | — |
| [[AsPC-1 (line)]] | alt | 6.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.41× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +15.0) | — |
| [[HepG2_C3A (line)]] | wt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +12.7) | — |
| [[HT-29 (line)]] | alt | 6.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +12.9) | — |
| [[hTERT-HPNE (line)]] | wt | 8.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.4× (z +13.5) | — |
| [[J82 (line)]] | alt | 6.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.75× (z +13.4) | — |
| [[KATO III (line)]] | alt | 5.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.30× (z +12.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.42 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 9.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.10× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 7.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.74× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 6.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.81× (z +12.2) | — |
| [[Panc 03.27 (line)]] | alt | 7.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 8.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +12.2) | — |
| [[SW1417 (line)]] | alt | 5.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +12.8) | — |
| [[AN3 CA (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12638), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAP2C-AS1]] | +0.76 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[CFAP418-AS1]] | +0.76 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[PKN2-AS1]] | +0.76 | +0.75 / +0.44 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.74 | +0.74 / +0.31 | both halves | 2e-04 |  |
| [[EYS]] | +0.73 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[STPG2]] | +0.73 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[ANXA2R-AS1]] | +0.73 | +0.73 / +0.39 | both halves | 5e-05 |  |
| [[PCNX4-DT]] | +0.73 | +0.75 / +0.32 | both halves | 1e-04 |  |
| [[FAM174B]] | +0.72 | +0.71 / +0.33 | both halves | 1e-04 |  |
| [[MAD2L1-DT]] | +0.72 | +0.74 / +0.28 | both halves | 3e-04 |  |
| [[WAC-AS1]] | +0.72 | +0.72 / +0.30 | both halves | 2e-04 |  |
| [[CCDC90B-AS1]] | +0.72 | +0.71 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIF1B]] | -0.68 | -0.63 / -0.22 | both halves | 6e-04 |  |
| [[MAST3]] | -0.66 | -0.57 / -0.25 | both halves | 4e-04 |  |
| [[CCDC134]] | -0.66 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[NBPF3]] | -0.65 | -0.60 / -0.28 | both halves | 3e-04 |  |
| [[CLTCL1]] | -0.63 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[PHKA2]] | -0.63 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[SH3PXD2B]] | -0.62 | -0.62 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TAFA2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.3% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[LINC00886]] | B | LINC00886 activity raises TAFA2's level | lines that do not express LINC00886 (16) vs lines expressing it (34) | 1.49× lower at baseline in the lines without LINC00886 | 0.068 | ⚠ within organs, on part of the lines; also absent: RASEF; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.798). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.1, 15.8); signed map (29.2, -10.1). **Vector** length 89.7, 19.9% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.5 | +34.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +13.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.3 | +15.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.8 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | +0.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | +3.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +2.0 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | TAFA chemokine like family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:61,708,273-62,279,150 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAFA-2; previously FAM19A2 |
| Gene groups (HGNC) | TAFA chemokine like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3H0](https://www.uniprot.org/uniprotkb/Q8N3H0) (Chemokine-like protein TAFA-2):

> Has a role as neurotrophic factor involved in neuronal survival and neurobiological functions.

**Summary**, from NCBI Gene [338811](https://www.ncbi.nlm.nih.gov/gene/338811):

> This gene is a member of the TAFA family which is composed of five highly homologous genes that encode small secreted proteins. These proteins contain conserved cysteine residues at fixed positions, and are distantly related to MIP-1alpha, a member of the CC-chemokine family. The TAFA proteins are predominantly expressed in specific regions of the brain, and are postulated to function as brain-specific chemokines or neurokines, that act as regulators of immune and nervous cells. [provided by …

**Accessions** — [HGNC:21589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21589) · Entrez [338811](https://www.ncbi.nlm.nih.gov/gene/338811) · UniProt [Q8N3H0](https://www.uniprot.org/uniprotkb/Q8N3H0) · Ensembl [ENSG00000198673](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198673)

## Data

Gene col 12638: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12638); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12638, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12638]; `tensor/DDL_lfc|DDL_z.npy` [12638]; `embed/gene_vectors.npy` [12638]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12638 or target_col == 12638). Every well: [[TAFA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAFA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
