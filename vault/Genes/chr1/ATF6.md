---
symbol: "ATF6"
type: "gene"
col: 3972
ensembl_id: "ENSG00000118217"
name: "activating transcription factor 6"
location: "1q23.3"
module: 117
arm: "+"
pooled_cpm: 192.61
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# ATF6

*activating transcription factor 6* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +17.8, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.696× (z -11.0, q 1e-25, down in 35 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 13 lines (SW480 0.510×, KATO III 0.443×, RKO 0.515×, A549 0.475×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H23 0.327×, SNU-1 0.304×, KATO III 0.423×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.415×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.417×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRDC]] (+0.51, fdr 1e-05), [[NEBL]] (+0.50, fdr 1e-05), [[AIG1]] (+0.49, fdr 2e-04); moves opposite to [[TMEM51]] (-0.47, fdr 3e-05), [[ING2-DT]] (-0.46, fdr 0.001, ⚠ one half only (not replicated)), [[OTUD3]] (-0.45, fdr 3e-04), [[SLC15A4]] (-0.44, fdr 2e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NEBL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3972.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +17.8 | 0e+00 | 42/48 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.33×** | +12.8 | 6e-35 | 46/49 (NCI-H460, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +12.2 | 8e-32 | 42/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +10.4 | 3e-23 | 38/48 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +9.9 | 5e-21 | 41/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +8.0 | 2e-13 | 38/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +7.7 | 1e-12 | 34/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +7.6 | 2e-12 | 37/47 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +7.6 | 3e-12 | 36/48 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +7.2 | 3e-11 | 33/48 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +6.1 | 6e-08 | 35/48 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +5.8 | 3e-07 | 32/48 (C32, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +5.7 | 5e-07 | 31/48 (NCI-H460, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +5.7 | 5e-07 | 32/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.29×** | +5.5 | 2e-06 | 32/48 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +5.5 | 2e-06 | 30/48 (C32, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3972.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 13 lines (SW480 0.510×, KATO III 0.443×, RKO 0.515×, A549 0.475×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H23 0.327×, SNU-1 0.304×, KATO III 0.423×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.415×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.417×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -11.0 | 1e-25 | 35/49 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.753×** | -5.9 | 1e-06 | 30/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.853× | -4.9 | 2e-04 | 16/48 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.851× | -3.5 | 0.055 | 18/48 (A498, RKO, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~19% of this change | 0.852× | -3.5 | 0.055 | 22/48 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 422 | 10 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +22.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.558× (z -8.8) ⚠ toxic |
| [[HOP62 (line)]] | alt | 110 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +19.8) | — |
| [[NCI-H460 (line)]] | wt | 246 | 10 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +17.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -12.7) |
| [[SNU-1 (line)]] | wt | 163 | 9 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[A-172 (line)]] | wt | 167 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +19.1) | — |
| [[LOX-IMVI (line)]] | wt | 158 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +14.7) | — |
| [[Hs 766T (line)]] | wt | 161 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +16.7) | — |
| [[NCI-H1573 (line)]] | alt | 196 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -11.6) |
| [[RKO (line)]] | wt | 227 | 3 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.15× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -13.3) |
| [[A498 (line)]] | wt | 181 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -10.4) |
| [[A549 (line)]] | wt | 137 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +17.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -13.3) |
| [[BT-474 (line)]] | alt | 253 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 155 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 4.93× (z +13.2) | — |
| [[KATO III (line)]] | alt | 120 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.49× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -17.0) |
| [[MIA PaCa-2 (line)]] | alt | 200 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.7) | — |
| [[NCI-H1792 (line)]] | alt | 195 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 2.61× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 428 | 3 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.35× (z +12.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.74× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[SW480 (line)]] | alt | 145 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -17.5) |
| [[HS-578T (line)]] | alt | 113 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 178 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.7) | — |
| [[A-427 (line)]] | wt | 264 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.417× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 167 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +19.3) | — |
| [[hTERT-HPNE (line)]] | wt | 127 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 179 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 170 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +15.7) | — |
| [[Panc 03.27 (line)]] | alt | 161 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.7) | — |
| [[RPMI-7951 (line)]] | alt | 149 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.1) | — |
| [[SW 900 (line)]] | alt | 290 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.2) | — |
| [[SW1417 (line)]] | alt | 159 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 133 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +16.9) | — |
| [[CHP-212 (line)]] | wt | 237 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -8.9) |
| [[H4 (line)]] | wt | 150 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.5) | — |
| [[HepG2_C3A (line)]] | wt | 202 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 255 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -10.4) |
| [[J82 (line)]] | alt | 167 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.5) | — |
| [[LS 180 (line)]] | wt | 170 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -9.5) |
| [[SNU-423 (line)]] | alt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.5) | — |
| [[SW48 (line)]] | wt | 163 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -9.7) |
| [[AN3 CA (line)]] | alt | 195 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 159 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 206 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 158 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRDC]] | +0.51 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[NEBL]] | +0.50 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[AIG1]] | +0.49 | +0.29 / +0.57 | both halves | 2e-04 |  |
| [[SLC7A11]] | +0.49 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[HDAC8]] | +0.49 | +0.37 / +0.46 | both halves | 7e-05 |  |
| [[CLCN3]] | +0.47 | +0.29 / +0.59 | both halves | 2e-04 |  |
| [[YARS1]] | +0.47 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[MAP2]] | +0.47 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[CDC42BPA]] | +0.47 | +0.36 / +0.49 | both halves | 9e-05 |  |
| [[HNRNPC]] | +0.47 | +0.43 / +0.52 | both halves | 4e-05 |  |
| [[BOD1]] | +0.47 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[LARS1]] | +0.46 | +0.37 / +0.59 | both halves | 8e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM51]] | -0.47 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ING2-DT]] | -0.46 | -0.17 / -0.51 | ⚠ one half (not replicated) | 0.001 |  |
| [[OTUD3]] | -0.45 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[SLC15A4]] | -0.44 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[SLC12A9]] | -0.44 | -0.15 / -0.54 | ⚠ one half (not replicated) | 0.001 |  |
| [[SOCS5]] | -0.44 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ZNF710]] | -0.44 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ZNF250]] | -0.44 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[TMED8]] | -0.43 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[SPATA33]] | -0.43 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[MIR762HG]] | -0.43 | -0.24 / -0.51 | both halves | 5e-04 |  |
| [[UBTD1]] | -0.43 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[LSM11]] | -0.43 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[GRK5]] | -0.43 | -0.46 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEBL]] | B | NEBL activity raises ATF6's level | lines that do not express NEBL (17) vs lines expressing it (33) | 1.24× lower at baseline in the lines without NEBL | 0.083 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| [[ALCAM]] | B | ALCAM activity lowers ATF6's level | lines that do not express ALCAM (9) vs lines expressing it (41) | 1.25× higher at baseline in the lines without ALCAM | 0.083 | ⚠ within organs, on part of the lines; also absent: GEM, IL7, RND3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.369). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-9.8, 45.8); signed map (19.5, -39.6). **Vector** length 116, 39.0% of its response variance represented; |z| ≥ 3 in 1,463 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[5-Azacytidine (drug)]] 5 µM |  | +5.5 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | +5.5 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.4 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change | +4.3 | -2.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | +3.9 | +4.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.9 | +5.4 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +3.5 | +2.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.5 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -11.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.1 | -5.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.7 | -4.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.2 | -0.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -1.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | activating transcription factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,766,298-161,977,574 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATF6A, ATP6alpha |
| Gene groups (HGNC) | Activating transcription factor 6 family |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 10 pathways, smallest: ATF6 (ATF6-alpha) activates chaperone genes; ATF6 (ATF6-alpha) activates chaperones; Modulation of host responses by IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P18850](https://www.uniprot.org/uniprotkb/P18850) (Cyclic AMP-dependent transcription factor ATF-6 alpha):

> [Cyclic AMP-dependent transcription factor ATF-6 alpha]: Precursor of the transcription factor form (Processed cyclic AMP-dependent transcription factor ATF-6 alpha), which is embedded in the endoplasmic reticulum membrane. Endoplasmic reticulum stress promotes processing of this form, releasing the transcription factor form that translocates into the nucleus, where it activates transcription of genes involved in the unfolded protein response (UPR).; [Processed cyclic AMP-dependent …

**Summary**, from NCBI Gene [22926](https://www.ncbi.nlm.nih.gov/gene/22926):

> This gene encodes a transcription factor that activates target genes for the unfolded protein response (UPR) during endoplasmic reticulum (ER) stress. Although it is a transcription factor, this protein is unusual in that it is synthesized as a transmembrane protein that is embedded in the ER. It functions as an ER stress sensor/transducer, and following ER stress-induced proteolysis, it functions as a nuclear transcription factor via a cis-acting ER stress response element (ERSE) that is …

**Accessions** — [HGNC:791](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:791) · Entrez [22926](https://www.ncbi.nlm.nih.gov/gene/22926) · UniProt [P18850](https://www.uniprot.org/uniprotkb/P18850) · Ensembl [ENSG00000118217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118217)

## Data

Gene col 3972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3972); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3972]; `tensor/DDL_lfc|DDL_z.npy` [3972]; `embed/gene_vectors.npy` [3972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3972 or target_col == 3972). Every well: [[ATF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
