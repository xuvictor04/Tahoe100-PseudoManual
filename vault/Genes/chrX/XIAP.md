---
symbol: "XIAP"
type: "gene"
col: 2195
ensembl_id: "ENSG00000101966"
name: "X-linked inhibitor of apoptosis"
location: "Xq25"
module: 57
arm: "-"
pooled_cpm: 145.99
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# XIAP

*X-linked inhibitor of apoptosis* — Xq25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.33× (z +8.4, q 2e-14, up in 35 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.32× (z +8.3, q 4e-14, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.326× (z -33.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRCH3]] (+0.72, fdr 9e-06), [[CYP20A1]] (+0.65, fdr 1e-05), [[NFKBIB]] (+0.65, fdr 1e-05); moves opposite to [[SKP2]] (-0.74, fdr 7e-06), [[POMGNT2]] (-0.65, fdr 1e-05), [[PAPSS1]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2195.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +8.4 | 2e-14 | 35/48 (CFPAC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +8.3 | 4e-14 | 33/48 (SNU-423, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +7.7 | 2e-12 | 31/48 (SNU-423, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +7.3 | 3e-11 | 30/48 (PANC-1, SNU-423, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +5.6 | 2e-06 | 23/48 (PANC-1, SNU-423, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.7 | 2e-04 | 17/48 (SNU-423, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.17× | +4.6 | 3e-04 | 20/48 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +4.3 | 0.002 | 19/48 (RKO, A-172, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.13× | +3.7 | 0.012 | 14/48 (HT-29, KATO III, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.050 | 7/48 (LOX-IMVI, SW 1088, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.08× | +3.2 | 0.071 | 4/48 (J82, Hs 766T, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.11× | +3.2 | 0.074 | 5/48 (CFPAC-1, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2195.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.326×** | -33.2 | 0e+00 | 48/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.339×** | -32.0 | 0e+00 | 47/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.374×** | -29.1 | 0e+00 | 48/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.599×** | -15.2 | 0e+00 | 46/48 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.645×** | -13.0 | 2e-36 | 43/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.742×** | -12.5 | 7e-34 | 36/49 (A498, A549, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.496×** | -10.9 | 1e-25 | 43/49 (AsPC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.600×** | -7.9 | 2e-13 | 37/49 (PANC-1, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.643×** | -6.8 | 5e-10 | 30/48 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -6.5 | 4e-09 | 19/48 (HT-29, SW 900, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.659×** | -6.5 | 6e-09 | 29/45 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.806×** | -6.1 | 4e-08 | 27/48 (HS-578T, H4, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.700×** | -5.5 | 1e-06 | 37/47 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.804×** | -5.4 | 3e-06 | 27/48 (PANC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.745×** | -4.5 | 2e-04 | 24/38 (H4, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.888× | -3.4 | 0.021 | 8/48 (NCI-H2030, HT-29, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.895× | -3.3 | 0.029 | 10/47 (SW 900, NCI-H2347, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.899× | -3.1 | 0.043 | 11/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | 0.863× | -3.1 | 0.046 | 4/48 (AsPC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 215 | 2 (1 ⚠) | 10 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.57× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.301× (z -25.5) |
| [[HT-29 (line)]] | alt | 198 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -26.9) |
| [[SNU-423 (line)]] | alt | 329 | 4 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.323× (z -19.1) |
| [[A-172 (line)]] | wt | 89.4 | 2 (2 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | [[Belinostat (drug)]] 5 µM 0.321× (z -14.9) |
| [[COLO 205 (line)]] | alt | 170 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.156× (z -25.4) |
| [[KATO III (line)]] | alt | 197 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -26.8) |
| [[AsPC-1 (line)]] | alt | 235 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -26.9) |
| [[J82 (line)]] | alt | 152 | 3 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.418× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 171 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -29.3) |
| [[A549 (line)]] | wt | 182 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -26.3) |
| [[HEC-1-A (line)]] | alt | 119 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.286× (z -20.1) |
| [[Hs 766T (line)]] | wt | 144 | 1 (1 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 1.84× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.365× (z -15.2) |
| [[HS-578T (line)]] | alt | 112 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.283× (z -17.3) |
| [[NCI-H2030 (line)]] | alt | 135 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -18.4) |
| [[NCI-H460 (line)]] | wt | 172 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.315× (z -19.6) |
| [[Panc 03.27 (line)]] | alt | 137 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -19.0) |
| [[SW 900 (line)]] | alt | 115 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -21.3) |
| [[SW480 (line)]] | alt | 161 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -26.0) |
| [[A-427 (line)]] | wt | 131 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -16.7) |
| [[A498 (line)]] | wt | 143 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -21.2) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.455× (z -13.5) |
| [[BT-474 (line)]] | alt | 78.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 126 | 1 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 1.76× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.314× (z -19.1) |
| [[H4 (line)]] | wt | 133 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -13.4) |
| [[HCT15 (line)]] | alt | 129 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.388× (z -10.2) |
| [[HOP62 (line)]] | alt | 162 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.301× (z -20.2) |
| [[LOX-IMVI (line)]] | wt | 97.4 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.315× (z -16.6) |
| [[LS 180 (line)]] | wt | 128 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.269× (z -18.2) |
| [[MIA PaCa-2 (line)]] | alt | 143 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.323× (z -16.7) |
| [[NCI-H1792 (line)]] | alt | 109 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.241× (z -17.5) |
| [[NCI-H2347 (line)]] | alt | 136 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -16.8) |
| [[SW1417 (line)]] | alt | 149 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.364× (z -15.2) |
| [[C32 (line)]] | wt | 68.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.334× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 108 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 105 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -13.6) |
| [[LoVo (line)]] | wt | 113 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -21.3) |
| [[NCI-H23 (line)]] | alt | 169 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -15.4) |
| [[RKO (line)]] | wt | 120 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.435× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.366× (z -11.0) |
| [[C-33 A (line)]] | alt | 81.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -11.1) |
| [[SHP-77 (line)]] | alt | 68.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.363× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 161 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -14.7) |
| [[AN3 CA (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 84.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 97.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRCH3]] | +0.72 | +0.76 / +0.57 | both halves | 9e-06 |  |
| [[CYP20A1]] | +0.65 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[NFKBIB]] | +0.65 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CHMP4A]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 | pathway: Programmed Cell Death |
| [[N4BP2L2]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PLA2G4C]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[KRBOX5]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[GATAD1]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[OFD1]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[TRIM56]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 | same gene group |
| [[SLC9A8]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[EIF1B]] | +0.58 | +0.65 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKP2]] | -0.74 | -0.68 / -0.71 | both halves | 7e-06 |  |
| [[POMGNT2]] | -0.65 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[PAPSS1]] | -0.62 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[KDM1A]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[ARHGEF7]] | -0.60 | -0.53 / -0.51 | both halves | 1e-05 | pathway: Death Receptor Signaling |
| [[GRB2]] | -0.60 | -0.53 / -0.49 | both halves | 1e-05 | pathway: Cell-Cell communication; STRING 482 |
| [[PIK3R2]] | -0.59 | -0.47 / -0.55 | both halves | 2e-05 | pathway: Cell-Cell communication |
| [[WASF3]] | -0.59 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[COLGALT1]] | -0.59 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[FAM234B]] | -0.59 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[FTO]] | -0.58 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[WRNIP1]] | -0.58 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.1, -14.5); signed map (3.9, -12.9). **Vector** length 111, 32.6% of its response variance represented; |z| ≥ 3 in 1,262 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +8.6 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +8.0 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.4 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.3 | +1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.0 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.9 | +1.5 |
|  | [[Resveratrol (drug)]] 5 µM |  | +2.4 | +2.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.3 | -7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.1 | -6.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.8 | -13.0 |
|  | [[NG25 (drug)]] 5 µM |  | -4.2 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.2 | -15.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -10.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | X-linked inhibitor of apoptosis |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq25 — chrX:123,859,712-123,913,972 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hILP, ILP-1; previously API3, BIRC4 |
| Gene groups (HGNC) | Ring finger proteins; Baculoviral IAP repeat containing; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | TGF_BETA_SIGNALING, APOPTOSIS |
| Reactome | 32 pathways, smallest: Activation of caspases through apoptosome-mediated cleavage; SMAC (DIABLO) binds to IAPs; SMAC(DIABLO)-mediated dissociation of IAP:caspase complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [P98170](https://www.uniprot.org/uniprotkb/P98170) (E3 ubiquitin-protein ligase XIAP):

> Multi-functional protein which regulates not only caspases and apoptosis, but also modulates inflammatory signaling and immunity, copper homeostasis, mitogenic kinase signaling, cell proliferation, as well as cell invasion and metastasis. Acts as a direct caspase inhibitor. Directly bind to the active site pocket of CASP3 and CASP7 and obstructs substrate entry. Inactivates CASP9 by keeping it in a monomeric, inactive state. Acts as an E3 ubiquitin-protein ligase regulating NF-kappa-B signaling …

**Summary**, from NCBI Gene [331](https://www.ncbi.nlm.nih.gov/gene/331):

> This gene encodes a protein that belongs to a family of apoptotic suppressor proteins. Members of this family share a conserved motif termed, baculovirus IAP repeat, which is necessary for their anti-apoptotic function. This protein functions through binding to tumor necrosis factor receptor-associated factors TRAF1 and TRAF2 and inhibits apoptosis induced by menadione, a potent inducer of free radicals, and interleukin 1-beta converting enzyme. This protein also inhibits at least two members …

**Accessions** — [HGNC:592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:592) · Entrez [331](https://www.ncbi.nlm.nih.gov/gene/331) · UniProt [P98170](https://www.uniprot.org/uniprotkb/P98170) · Ensembl [ENSG00000101966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101966)

## Data

Gene col 2195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2195); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2195]; `tensor/DDL_lfc|DDL_z.npy` [2195]; `embed/gene_vectors.npy` [2195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2195 or target_col == 2195). Every well: [[XIAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XIAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
