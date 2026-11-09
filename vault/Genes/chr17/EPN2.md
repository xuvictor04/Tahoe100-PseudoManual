---
symbol: "EPN2"
type: "gene"
col: 1007
ensembl_id: "ENSG00000072134"
name: "epsin 2"
location: "17p11.2"
module: 154
arm: "+"
pooled_cpm: 158.68
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# EPN2

*epsin 2* — 17p11.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 6.12×, PANC-1 1.49×; ⚠ cell-cycle shift, explains ~58% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 1.42×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.417× (z -22.1, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.572× (z -19.9, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIB1]] (+0.69, fdr 1e-05), [[UBA6]] (+0.63, fdr 1e-05), [[B3GAT3]] (+0.63, fdr 3e-05); moves opposite to [[GAS2]] (-0.65, fdr 3e-04), [[ADI1]] (-0.64, fdr 3e-05), [[ZMYND11]] (-0.63, fdr 1e-05).
> It is in [[Module 154]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1007.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 6.12×, PANC-1 1.49×; ⚠ cell-cycle shift, explains ~58% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 1.42×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vortioxetine (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.36 | 8/48 (J82, HS-578T, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.36 | 4/48 (HEC-1-A, Panc 03.27, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.26× | +3.1 | 0.36 | 16/48 (SW480, COLO 205, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1007.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.417×** | -22.1 | 0e+00 | 46/49 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.413×** | -21.5 | 0e+00 | 40/44 (A549, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.572×** | -19.9 | 0e+00 | 46/49 (CFPAC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.434×** | -19.5 | 0e+00 | 39/45 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.300×** | -15.9 | 0e+00 | 46/49 (PANC-1, A549, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.528×** | -15.5 | 0e+00 | 42/47 (HOP62, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.594×** | -12.6 | 1e-34 | 33/48 (HS-578T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -12.4 | 2e-33 | 37/48 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.641×** | -11.2 | 3e-27 | 34/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.643×** | -11.1 | 5e-27 | 39/48 (A-172, LoVo, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -10.7 | 7e-25 | 38/50 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.511×** | -8.9 | 4e-17 | 36/48 (MIA PaCa-2, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.721×** | -8.2 | 8e-15 | 32/48 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.805×** | -7.7 | 5e-13 | 24/48 (J82, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.747×** | -7.1 | 6e-11 | 36/48 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.792×** | -5.9 | 1e-07 | 29/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.794×** | -5.8 | 2e-07 | 27/48 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.814×** | -4.9 | 3e-05 | 26/48 (HOP62, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.712×** | -4.5 | 2e-04 | 28/49 (NCI-H460, Hs 766T, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 333 | 0 | 17 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -15.4) |
| [[CFPAC-1 (line)]] | alt | 185 | 0 | 16 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -20.2) |
| [[KATO III (line)]] | alt | 221 | 0 | 14 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.380× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 264 | 0 | 13 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -20.0) |
| [[NCI-H460 (line)]] | wt | 148 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.223× (z -13.8) |
| [[A-172 (line)]] | wt | 159 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.343× (z -14.4) |
| [[HS-578T (line)]] | alt | 194 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -19.8) |
| [[MIA PaCa-2 (line)]] | alt | 188 | 0 | 11 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -16.5) |
| [[J82 (line)]] | alt | 144 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.481× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 189 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 148 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -15.2) |
| [[hTERT-HPNE (line)]] | wt | 146 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 191 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -13.0) |
| [[A549 (line)]] | wt | 232 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -34.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.196× (z -14.2) |
| [[C32 (line)]] | wt | 102 | 1 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +30.3) ⚠ cell-cycle shift, explains ~58% of this change | [[Harringtonine (drug)]] 0.5 µM 0.211× (z -18.4) |
| [[SW1417 (line)]] | alt | 106 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.392× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -10.8) |
| [[A498 (line)]] | wt | 105 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -14.8) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.370× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 152 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -13.4) |
| [[Hs 766T (line)]] | wt | 181 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.219× (z -9.7) |
| [[LoVo (line)]] | wt | 110 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.449× (z -12.2) |
| [[LS 180 (line)]] | wt | 96.5 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.451× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 158 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -17.6) |
| [[SW 900 (line)]] | alt | 247 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -14.0) |
| [[H4 (line)]] | wt | 166 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.6) |
| [[HCT15 (line)]] | alt | 326 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.362× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 91.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -14.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.338× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 126 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 197 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -11.6) |
| [[C-33 A (line)]] | alt | 284 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 119 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 249 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -30.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -11.0) |
| [[PANC-1 (line)]] | alt | 117 | 0 | 4 (3 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.217× (z -15.0) |
| [[RKO (line)]] | wt | 157 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -9.1) |
| [[SNU-1 (line)]] | wt | 119 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.494× (z -10.6) |
| [[COLO 205 (line)]] | alt | 150 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.320× (z -11.7) |
| [[SHP-77 (line)]] | alt | 194 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -11.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 115 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -10.1) |
| [[A-427 (line)]] | wt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.379× (z -12.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 134 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -10.2) |
| [[SW48 (line)]] | wt | 137 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0600× (z -28.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -11.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -11.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 85.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.499× (z -9.3) |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.110× (z -9.6) |
| [[SW 1271 (line)]] | alt | 284 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 73.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 167 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIB1]] | +0.69 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[UBA6]] | +0.63 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[B3GAT3]] | +0.63 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[GDPD5]] | +0.62 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[SH3GL1]] | +0.62 | +0.60 / +0.45 | both halves | 3e-05 | pathway: Cargo recognition for clathrin-mediated endocytosis; STRING 783 |
| [[TMEM184B]] | +0.62 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ZNRF1]] | +0.61 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[PIGH]] | +0.61 | +0.50 / +0.37 | both halves | 8e-05 |  |
| [[ABCB9]] | +0.61 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ZFYVE28]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[GIPR]] | +0.61 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[SH2B2]] | +0.61 | +0.53 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAS2]] | -0.65 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[ADI1]] | -0.64 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[ZMYND11]] | -0.63 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SUCLG2-DT]] | -0.60 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[DECR1]] | -0.59 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[DPY19L1P2]] | -0.59 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TOR1A]] | -0.58 | -0.52 / -0.27 | both halves | 3e-04 | pathway: Cargo recognition for clathrin-mediated endocytosis |
| [[RCN1]] | -0.58 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ZNF362]] | -0.58 | -0.55 / -0.23 | both halves | 5e-04 |  |
| [[ZFX]] | -0.58 | -0.57 / -0.40 | both halves | 4e-05 |  |
| [[AP5M1]] | -0.58 | -0.58 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[ACCS]] | -0.57 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[EWSR1]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.672). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.4, 2.7); signed map (-5.0, 47.1). **Vector** length 110, 36.0% of its response variance represented; |z| ≥ 3 in 1,492 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +6.8 | -3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +6.0 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | -2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.4 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +0.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.1 | +0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.5 | +1.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -9.6 | -15.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.9 | -8.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.1 | -15.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.9 | -7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.5 | -19.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | epsin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:19,215,615-19,336,715 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1065, EHB21 |
| Gene groups (HGNC) | Epsin family |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O95208](https://www.uniprot.org/uniprotkb/O95208) (Epsin-2):

> Plays a role in the formation of clathrin-coated invaginations and endocytosis.

**Summary**, from NCBI Gene [22905](https://www.ncbi.nlm.nih.gov/gene/22905):

> This gene encodes a protein which interacts with clathrin and adaptor-related protein complex 2, alpha 1 subunit. The protein is found in a brain-derived clathrin-coated vesicle fraction and localizes to the peri-Golgi region and the cell periphery. The protein is thought to be involved in clathrin-mediated endocytosis. Alternate splicing of this gene results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18639](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18639) · Entrez [22905](https://www.ncbi.nlm.nih.gov/gene/22905) · UniProt [O95208](https://www.uniprot.org/uniprotkb/O95208) · Ensembl [ENSG00000072134](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072134)

## Data

Gene col 1007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1007); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1007]; `tensor/DDL_lfc|DDL_z.npy` [1007]; `embed/gene_vectors.npy` [1007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1007 or target_col == 1007). Every well: [[EPN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
