---
symbol: "SNX3"
type: "gene"
col: 3359
ensembl_id: "ENSG00000112335"
name: "sorting nexin 3"
location: "6q21"
module: 60
arm: "+"
pooled_cpm: 116.05
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# SNX3

*sorting nexin 3* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.00× (z +11.1, q 5e-26, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.543× (z -13.9, q 7e-41, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NTAN1]] (+0.72, fdr 7e-06), [[ST13]] (+0.66, fdr 3e-05), [[ATP2C1]] (+0.65, fdr 7e-06); moves opposite to [[ZC3H7B]] (-0.63, fdr 1e-05), [[R3HDM2]] (-0.62, fdr 1e-05), [[CHAMP1]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3359.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +11.1 | 5e-26 | 47/48 (C32, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +10.9 | 2e-25 | 45/49 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +10.4 | 4e-23 | 40/44 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +7.7 | 2e-12 | 41/48 (KATO III, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +7.2 | 6e-11 | 41/48 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +6.6 | 3e-09 | 40/48 (KATO III, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +6.2 | 4e-08 | 33/45 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +5.6 | 1e-06 | 29/48 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.9 | 5e-05 | 36/45 (NCI-H2347, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.73×** | +4.6 | 2e-04 | 38/47 (C32, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.32×** | +4.5 | 4e-04 | 26/48 (KATO III, NCI-H460, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.31×** | +4.4 | 5e-04 | 35/48 (KATO III, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.011 | 26/49 (SW1417, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.022 | 28/48 (KATO III, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.2 | 0.044 | 20/47 (COLO 205, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Infigratinib (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.080 | 22/48 (AsPC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.080 | 21/48 (COLO 205, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3359.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.543×** | -13.9 | 7e-41 | 47/48 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.640×** | -7.2 | 2e-10 | 40/48 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.715×** | -5.4 | 1e-05 | 36/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.716×** | -5.4 | 1e-05 | 35/48 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.759×** | -3.9 | 0.010 | 27/48 (LoVo, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -3.5 | 0.045 | 20/48 (CFPAC-1, SNU-1, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -3.2 | 0.11 | 0/50 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3359. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 127 | 6 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.83× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.43× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.446× (z -9.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 132 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 131 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -16.9) |
| [[HOP62 (line)]] | alt | 93.9 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.53× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -14.3) |
| [[J82 (line)]] | alt | 100 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -13.4) |
| [[LoVo (line)]] | wt | 117 | 3 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.81× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -12.7) |
| [[PANC-1 (line)]] | alt | 168 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +13.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 90.1 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.16× (z +11.6) | [[Lonafarnib (drug)]] 5 µM 0.135× (z -10.5) ⚠ toxic |
| [[C-33 A (line)]] | alt | 236 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -13.1) |
| [[C32 (line)]] | wt | 91.1 | 2 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 4.36× (z +15.4) | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -9.0) |
| [[HS-578T (line)]] | alt | 148 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 113 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -17.3) |
| [[MIA PaCa-2 (line)]] | alt | 195 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.39× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 120 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 77.8 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.72× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 94.5 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.62× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -9.4) |
| [[A-427 (line)]] | wt | 119 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -14.3) |
| [[AN3 CA (line)]] | alt | 190 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -15.8) |
| [[CFPAC-1 (line)]] | alt | 110 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -13.0) |
| [[COLO 205 (line)]] | alt | 71.8 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 4.23× (z +10.5) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 131 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.92× (z +12.8) | — |
| [[Hs 766T (line)]] | wt | 115 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 93.9 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.58× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 113 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 89.2 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.89× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 123 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -15.0) |
| [[RKO (line)]] | wt | 101 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.34× (z +12.4) | — |
| [[RPMI-7951 (line)]] | alt | 168 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -17.7) |
| [[SHP-77 (line)]] | alt | 86.2 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.38× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.36× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 143 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.72× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -8.9) |
| [[SW480 (line)]] | alt | 90.9 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.91× (z +13.6) | — |
| [[A549 (line)]] | wt | 91.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 53.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 115 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 89.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -9.1) |
| [[SNU-423 (line)]] | alt | 256 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -14.2) |
| [[SW1417 (line)]] | alt | 36.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.80× (z +8.5) | — |
| [[A-172 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 92.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 95.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3359), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTAN1]] | +0.72 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[ST13]] | +0.66 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[ATP2C1]] | +0.65 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[CYB5R4]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SARAF]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[FTL]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[EEF1G]] | +0.62 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[CALCOCO2]] | +0.61 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[ALDH2]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[RTN3]] | +0.61 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[FXR1]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.60 | +0.74 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H7B]] | -0.63 | -0.76 / -0.53 | both halves | 1e-05 |  |
| [[R3HDM2]] | -0.62 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[CHAMP1]] | -0.62 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[FJX1]] | -0.61 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[AEN]] | -0.60 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[PPRC1]] | -0.59 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[ZBTB9]] | -0.57 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[PHF19]] | -0.57 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[REXO1]] | -0.57 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[CYREN]] | -0.57 | -0.73 / -0.46 | both halves | 3e-05 |  |
| [[RELB]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[NOP56]] | -0.56 | -0.67 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-16.8, -12.0); signed map (-34.4, -15.4). **Vector** length 114, 39.5% of its response variance represented; |z| ≥ 3 in 866 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.1 | +11.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.5 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.0 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +7.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.4 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.3 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.5 | -13.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.7 | -7.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.6 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:108,211,222-108,261,246 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Grd19 |
| Gene groups (HGNC) | Sorting nexins |
| Reactome | 4 pathways, smallest: WNT ligand biogenesis and trafficking; Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [O60493](https://www.uniprot.org/uniprotkb/O60493) (Sorting nexin-3):

> Phosphoinositide-binding protein required for multivesicular body formation. Specifically binds phosphatidylinositol 3-phosphate (PtdIns(P3)). Can also bind phosphatidylinositol 4-phosphate (PtdIns(P4)), phosphatidylinositol 5-phosphate (PtdIns(P5)) and phosphatidylinositol 3,5-biphosphate (PtdIns(3,5)P2) (By similarity). Plays a role in protein transport between cellular compartments. Together with RAB7A facilitates endosome membrane association of the retromer cargo-selective subcomplex …

**Summary**, from NCBI Gene [8724](https://www.ncbi.nlm.nih.gov/gene/8724):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This protein does not contain a coiled coil region, like most family members. This protein interacts with phosphatidylinositol-3-phosphate, and is involved in protein trafficking. A pseudogene of this gene is present on the sex chromosomes. Alternative splicing results in multiple transcript variants …

**Accessions** — [HGNC:11174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11174) · Entrez [8724](https://www.ncbi.nlm.nih.gov/gene/8724) · UniProt [O60493](https://www.uniprot.org/uniprotkb/O60493) · Ensembl [ENSG00000112335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112335)

## Data

Gene col 3359: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3359); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3359, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3359]; `tensor/DDL_lfc|DDL_z.npy` [3359]; `embed/gene_vectors.npy` [3359]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3359 or target_col == 3359). Every well: [[SNX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
