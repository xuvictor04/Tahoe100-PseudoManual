---
symbol: "TGFBR2"
type: "gene"
col: 8705
ensembl_id: "ENSG00000163513"
name: "transforming growth factor beta receptor 2"
location: "3p24.1"
module: 97
arm: "+"
pooled_cpm: 97.36
n_lines_expressing: 43
n_dd_up: 26
n_dd_down: 29
n_dd_up_clean: 26
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 10
direction_downstream: 27
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# TGFBR2

*transforming growth factor beta receptor 2* — 3p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.59× (z +8.9, q 4e-16, up in 33 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.407× (z -17.3, q 0e+00, down in 39 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHOBTB2]] (+0.63, fdr 7e-06), [[ARHGAP18]] (+0.61, fdr 1e-05), [[SHROOM2]] (+0.59, fdr 1e-05); moves opposite to [[FAM219A]] (-0.58, fdr 1e-05), [[C9orf24]] (-0.51, fdr 2e-05), [[PTPN23-DT]] (-0.49, fdr 3e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CCL20]] → it (grade B ⚠); 27 go from it, the strongest it → [[TBC1D8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, none with an alert; shown: the 15 strongest. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8705.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +8.9 | 4e-16 | 33/41 (RKO, RPMI-7951, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.63×** | +6.7 | 7e-09 | 27/41 (NCI-H2347, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.58×** | +6.2 | 8e-08 | 26/41 (Hs 766T, NCI-H2347, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.57×** | +6.1 | 1e-07 | 25/41 (Panc 03.27, Hs 766T, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +5.8 | 7e-07 | 33/42 (LoVo, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.53×** | +5.8 | 7e-07 | 25/41 (SK-MEL-2, Hs 766T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.52×** | +5.7 | 1e-06 | 26/41 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.52×** | +5.3 | 9e-06 | 23/40 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.47×** | +5.3 | 9e-06 | 23/41 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.43×** | +4.8 | 8e-05 | 24/41 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.7 | 2e-04 | 22/41 (NCI-H1573, Panc 03.27, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.41×** | +4.6 | 2e-04 | 23/41 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 2e-04 | 28/42 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.25×** | +4.2 | 1e-03 | 21/41 (A498, NCI-H2347, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +4.2 | 0.001 | 25/41 (Panc 03.27, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8705.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.407×** | -17.3 | 0e+00 | 39/42 (SW1417, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.432×** | -11.0 | 1e-25 | 28/35 (LS 180, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.455×** | -10.7 | 1e-24 | 36/41 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.484×** | -9.4 | 1e-18 | 35/41 (HepG2/C3A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.492×** | -7.6 | 4e-12 | 26/41 (LS 180, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.570×** | -7.4 | 1e-11 | 31/43 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.584×** | -7.3 | 2e-11 | 32/41 (SW48, SW 900, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.593×** | -7.1 | 8e-11 | 35/41 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.582×** | -7.1 | 8e-11 | 29/40 (HepG2/C3A, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.614×** | -6.4 | 9e-09 | 29/41 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.650×** | -5.6 | 8e-07 | 26/41 (J82, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.601×** | -5.5 | 2e-06 | 24/42 (Hs 766T, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.675×** | -5.0 | 3e-05 | 23/37 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.686×** | -4.9 | 3e-05 | 23/40 (A-172, Hs 766T, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.698×** | -4.9 | 3e-05 | 22/41 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.756×** | -4.9 | 3e-05 | 25/43 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.793×** | -4.2 | 8e-04 | 21/42 (Hs 766T, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.796×** | -4.0 | 0.002 | 20/41 (Hs 766T, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.815×** | -4.0 | 0.002 | 19/42 (LS 180, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8705. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 237 | 0 | 12 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -14.0) |
| [[HepG2_C3A (line)]] | wt | 299 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -20.7) |
| [[SW480 (line)]] | alt | 210 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -18.4) |
| [[SW48 (line)]] | wt | 279 | 1 | 9 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 8.32× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -17.6) |
| [[SW1417 (line)]] | alt | 241 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -24.7) |
| [[Panc 03.27 (line)]] | alt | 143 | 3 (2 ⚠) | 5 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.48× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -14.7) |
| [[SW 900 (line)]] | alt | 148 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -18.1) |
| [[HOP62 (line)]] | alt | 177 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 175 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -16.9) |
| [[NCI-H2030 (line)]] | alt | 117 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 101 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.1) |
| [[KATO III (line)]] | alt | 183 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -12.1) |
| [[A-172 (line)]] | wt | 74.8 | 0 | 3 | — | [[Trametinib (drug)]] 5 µM 0.330× (z -9.6) |
| [[HT-29 (line)]] | alt | 103 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 132 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -14.7) |
| [[NCI-H2347 (line)]] | alt | 135 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 1.87× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -19.1) |
| [[A549 (line)]] | wt | 81.6 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 91.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -11.9) |
| [[C32 (line)]] | wt | 43.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0747× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 89.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -15.1) |
| [[HS-578T (line)]] | alt | 74.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -11.6) |
| [[PANC-1 (line)]] | alt | 61.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 89.6 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.23× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.4) |
| [[A498 (line)]] | wt | 61.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -16.9) |
| [[BT-474 (line)]] | alt | 31.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.87× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | — |
| [[COLO 205 (line)]] | alt | 101 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -9.7) |
| [[Hs 766T (line)]] | wt | 92.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -9.5) |
| [[J82 (line)]] | alt | 33.6 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.288× (z -10.7) |
| [[LoVo (line)]] | wt | 85.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.02× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 30.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.61× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 47.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 64.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -10.2) |
| [[SW 1271 (line)]] | alt | 255 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -8.5) |
| [[A-427 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 90.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.56 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.62 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 71.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8705), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOBTB2]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ARHGAP18]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[SHROOM2]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TBC1D8]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[MAML2]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[MAP3K1]] | +0.55 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[MMD]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[BCL2L1]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[CCND3]] | +0.52 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[CAVIN2]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CCN2]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 | STRING 748 |
| [[PKP2]] | +0.52 | +0.44 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM219A]] | -0.58 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[C9orf24]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[PTPN23-DT]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RBCK1]] | -0.48 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[DGKE]] | -0.47 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[LINC02680]] | -0.47 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[STX5-DT]] | -0.46 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[C17orf67]] | -0.46 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[L3MBTL1]] | -0.46 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[OTUD7B]] | -0.46 | -0.41 / -0.41 | both halves | 4e-05 | pathway: Deubiquitination |
| [[UNKL]] | -0.46 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[RAB6A]] | -0.45 | -0.36 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCL20]] | B | CCL20 activity raises TGFBR2's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.74× lower at baseline in the lines without CCL20 | 0.006 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[MAML2]] | B | MAML2 activity raises TGFBR2's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 3.78× lower at baseline in the lines without MAML2 | 0.008 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[TBC1D8]] | B | TBC1D8 activity raises TGFBR2's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 2.72× lower at baseline in the lines without TBC1D8 | 0.036 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[ADRA1B]] | B | ADRA1B activity raises TGFBR2's level | lines that do not express ADRA1B (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without ADRA1B | 0.038 | ⚠ within organs, on part of the lines; also absent: IL31RA, IGFBP3, STAC |
| [[NR3C1]] | B | NR3C1 activity raises TGFBR2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[FOXC2]] | B | FOXC2 activity raises TGFBR2's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 1.70× lower at baseline in the lines without FOXC2 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[EVA1C]] | B | EVA1C activity raises TGFBR2's level | lines that do not express EVA1C (15) vs lines expressing it (35) | 2.12× lower at baseline in the lines without EVA1C | 0.087 | ⚠ within organs, on part of the lines; also absent: PI3, ENSG00000260877, CYB5R2 |
| [[EREG]] | B | EREG activity raises TGFBR2's level | lines that do not express EREG (26) vs lines expressing it (24) | 2.16× lower at baseline in the lines without EREG | 0.091 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1 |
| [[PPARG]] | B | PPARG activity raises TGFBR2's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.01× lower at baseline in the lines without PPARG | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[TRIB1]] | C | TRIB1 activity raises TGFBR2's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 7.22× lower at baseline in the lines without TRIB1 | 0.009 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 26, C 1. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D8]] | B | TGFBR2 activity raises TBC1D8's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 2.90× lower at baseline in the lines without TGFBR2 | 0.008 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[CAV1]] | B | TGFBR2 activity raises CAV1's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 3.55× lower at baseline in the lines without TGFBR2 | 0.021 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[SERBP1]] | B | TGFBR2 activity lowers SERBP1's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 1.53× higher at baseline in the lines without TGFBR2 | 0.031 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[CCL20]] | B | TGFBR2 activity raises CCL20's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 2.77× lower at baseline in the lines without TGFBR2 | 0.031 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[EXTL2]] | B | TGFBR2 activity lowers EXTL2's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 1.89× higher at baseline in the lines without TGFBR2 | 0.035 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[MAP3K5]] | B | TGFBR2 activity raises MAP3K5's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 2.73× lower at baseline in the lines without TGFBR2 | 0.038 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[EVA1C]] | B | TGFBR2 activity raises EVA1C's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 3.81× lower at baseline in the lines without TGFBR2 | 0.038 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[ADRA1B]] | B | TGFBR2 activity raises ADRA1B's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 2.41× lower at baseline in the lines without TGFBR2 | 0.050 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[PPP3CA]] | B | TGFBR2 activity raises PPP3CA's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 2.13× lower at baseline in the lines without TGFBR2 | 0.053 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[PPARG]] | B | TGFBR2 activity raises PPARG's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 4.08× lower at baseline in the lines without TGFBR2 | 0.061 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[LRCH1]] | B | TGFBR2 activity raises LRCH1's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without TGFBR2 | 0.067 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[RBMS1]] | B | TGFBR2 activity raises RBMS1's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without TGFBR2 | 0.069 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.8, 11.5); signed map (15.2, 38.5). **Vector** length 143, 48.2% of its response variance represented; |z| ≥ 3 in 1,555 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +8.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.4 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.7 | +4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.6 | +5.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.5 | +6.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +5.0 | +6.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -7.0 | -10.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.0 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -17.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.0 | -9.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.9 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -7.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.5 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.3 | -4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | transforming growth factor beta receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.1 — chr3:30,606,478-30,694,249 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TBRII, TBR-ii; previously MFS2 |
| Gene groups (HGNC) | Type 2 receptor serine/threonine kinases |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 18 pathways, smallest: Loss of Function of TGFBR2 in Cancer; TGFBR2 Kinase Domain Mutants in Cancer; TGFBR1 LBD Mutants in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [P37173](https://www.uniprot.org/uniprotkb/P37173) (TGF-beta receptor type-2):

> Transmembrane serine/threonine kinase forming with the TGF-beta type I serine/threonine kinase receptor, TGFBR1, the non-promiscuous receptor for the TGF-beta cytokines TGFB1, TGFB2 and TGFB3. Transduces the TGFB1, TGFB2 and TGFB3 signal from the cell surface to the cytoplasm and thus regulates a plethora of physiological and pathological processes including cell cycle arrest in epithelial and hematopoietic cells, control of mesenchymal cell proliferation and differentiation, wound healing, …

**Summary**, from NCBI Gene [7048](https://www.ncbi.nlm.nih.gov/gene/7048):

> The protein encoded by this gene is a transmembrane protein that has a protein kinase domain, forms a heterodimeric complex with TGF-beta receptor type-1, and binds TGF-beta. This receptor/ligand complex phosphorylates proteins, which then enter the nucleus and regulate the transcription of genes related to cell proliferation, cell cycle arrest, wound healing, immunosuppression, and tumorigenesis. Mutations in this gene have been associated with Marfan Syndrome, Loeys-Deitz Aortic Aneurysm …

**Accessions** — [HGNC:11773](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11773) · Entrez [7048](https://www.ncbi.nlm.nih.gov/gene/7048) · UniProt [P37173](https://www.uniprot.org/uniprotkb/P37173) · Ensembl [ENSG00000163513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163513)

## Data

Gene col 8705: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8705); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8705, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8705]; `tensor/DDL_lfc|DDL_z.npy` [8705]; `embed/gene_vectors.npy` [8705]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8705 or target_col == 8705). Every well: [[TGFBR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGFBR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
