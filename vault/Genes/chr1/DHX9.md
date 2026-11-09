---
symbol: "DHX9"
type: "gene"
col: 5762
ensembl_id: "ENSG00000135829"
name: "DExH-box helicase 9"
location: "1q25.3"
module: 4
arm: "+"
pooled_cpm: 173.6
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# DHX9

*DExH-box helicase 9* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.95× (z +27.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.675× (z -10.0, q 1e-20, down in 42 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (RKO 0.455×, NCI-H23 0.558×, HEC-1-A 0.517×, HOP62 0.535×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.410×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX15]] (+0.77, fdr 7e-06), [[FAM98B]] (+0.77, fdr 7e-06), [[HNRNPD]] (+0.74, fdr 7e-06); moves opposite to [[ZNHIT1]] (-0.67, fdr 7e-06), [[GUK1]] (-0.66, fdr 7e-06), [[SELENOK]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ALDH5A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5762.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.95×** | +27.2 | 0e+00 | 47/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **7.68×** | +19.0 | 0e+00 | 49/49 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **5.97×** | +16.6 | 0e+00 | 47/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.51×** | +15.4 | 0e+00 | 48/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +14.3 | 3e-44 | 47/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.15×** | +13.6 | 3e-40 | 45/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +13.0 | 2e-36 | 45/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +11.6 | 4e-29 | 43/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.77×** | +10.1 | 3e-22 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +8.6 | 4e-16 | 37/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +8.1 | 2e-14 | 40/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.49×** | +7.0 | 9e-11 | 30/49 (SNU-423, NCI-H1792, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +6.2 | 2e-08 | 37/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.8 | 2e-07 | 28/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.5 | 2e-06 | 26/38 (NCI-H1573, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.011 | 23/48 (NCI-H460, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.017 | 23/48 (SNU-423, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.028 | 5/48 (BT-474, H4, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.034 | 21/47 (SW48, LOX-IMVI, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5762.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (RKO 0.455×, NCI-H23 0.558×, HEC-1-A 0.517×, HOP62 0.535×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.410×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -10.0 | 1e-20 | 42/49 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.843× | -3.1 | 0.51 | 21/48 (KATO III, A-172, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5762. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 244 | 15 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +23.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 99.0 | 13 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +20.1) | — |
| [[PANC-1 (line)]] | alt | 124 | 13 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +20.5) | — |
| [[HOP62 (line)]] | alt | 162 | 9 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +22.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 110 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +18.8) | — |
| [[LS 180 (line)]] | wt | 173 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.24× (z +19.9) | — |
| [[SW 900 (line)]] | alt | 233 | 8 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +19.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -9.8) |
| [[SW480 (line)]] | alt | 192 | 9 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.89× (z +16.5) | — |
| [[LoVo (line)]] | wt | 170 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +19.2) | — |
| [[SW48 (line)]] | wt | 232 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.54× (z +14.4) | — |
| [[A-172 (line)]] | wt | 152 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +23.0) | — |
| [[A549 (line)]] | wt | 166 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +28.8) | — |
| [[C32 (line)]] | wt | 128 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +18.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 123 | 7 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 8.39× (z +20.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.09× (z +20.2) | — |
| [[HT-29 (line)]] | alt | 130 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +20.6) | — |
| [[SNU-423 (line)]] | alt | 92.7 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +16.9) | — |
| [[HEC-1-A (line)]] | alt | 264 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +21.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -11.0) |
| [[KATO III (line)]] | alt | 130 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 208 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +16.0) | — |
| [[Panc 03.27 (line)]] | alt | 143 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +16.9) | — |
| [[SW1417 (line)]] | alt | 170 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +17.3) | — |
| [[BT-474 (line)]] | alt | 189 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +20.6) | — |
| [[H4 (line)]] | wt | 125 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +18.9) | — |
| [[Hs 766T (line)]] | wt | 109 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +14.8) | — |
| [[hTERT-HPNE (line)]] | wt | 102 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.5) | — |
| [[J82 (line)]] | alt | 169 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +19.4) | — |
| [[LOX-IMVI (line)]] | wt | 140 | 5 | 0 | [[PH-797804 (drug)]] 5 µM 11.0× (z +13.3) | — |
| [[RKO (line)]] | wt | 240 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -13.1) |
| [[A498 (line)]] | wt | 198 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +22.3) | — |
| [[AsPC-1 (line)]] | alt | 125 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +16.8) | — |
| [[HS-578T (line)]] | alt | 102 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +16.4) | — |
| [[NCI-H23 (line)]] | alt | 208 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 113 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +16.2) | — |
| [[SHP-77 (line)]] | alt | 222 | 4 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.01× (z +12.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.4) | — |
| [[SK-MEL-2 (line)]] | alt | 154 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.9) | — |
| [[A-427 (line)]] | wt | 217 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.21× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 162 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +17.0) | — |
| [[HCT15 (line)]] | alt | 196 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -8.8) |
| [[C-33 A (line)]] | alt | 267 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.61× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 123 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.0) | — |
| [[SNU-1 (line)]] | wt | 225 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.84× (z +11.3) | — |
| [[CHP-212 (line)]] | wt | 284 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 184 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 7.88× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 287 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.6) | — |
| [[AN3 CA (line)]] | alt | 260 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5762), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX15]] | +0.77 | +0.66 / +0.77 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 715 |
| [[FAM98B]] | +0.77 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[HNRNPD]] | +0.74 | +0.68 / +0.76 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 529 |
| [[HNRNPM]] | +0.73 | +0.78 / +0.75 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 974 |
| [[G3BP1]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 | STRING 472 |
| [[AGPS]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[CEP41]] | +0.72 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[EWSR1]] | +0.71 | +0.75 / +0.78 | both halves | 7e-06 | STRING 997 |
| [[SMG7]] | +0.70 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[NAA15]] | +0.68 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.67 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[CCT2]] | +0.67 | +0.70 / +0.65 | both halves | 7e-06 | STRING 429 |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNHIT1]] | -0.67 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[GUK1]] | -0.66 | -0.62 / -0.72 | both halves | 7e-06 |  |
| [[SELENOK]] | -0.66 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.65 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[RABGEF1]] | -0.65 | -0.54 / -0.67 | both halves | 1e-05 |  |
| [[NARF]] | -0.64 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[HIC2]] | -0.63 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[SEC61G]] | -0.63 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[TULP3]] | -0.63 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[RAB5A]] | -0.62 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[TPT1-AS1]] | -0.61 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[EIF1B]] | -0.61 | -0.57 / -0.65 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH5A1]] | B | ALDH5A1 activity raises DHX9's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without ALDH5A1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.1, -35.0); signed map (12.8, -39.3). **Vector** length 111, 45.5% of its response variance represented; |z| ≥ 3 in 1,266 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +9.8 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +9.2 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | +9.0 | +3.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.3 | +13.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.3 | +1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +3.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.3 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +16.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.0 | +0.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.5 | -10.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.7 | +13.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.5 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -0.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.2 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | +1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | DExH-box helicase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:182,839,347-182,887,982 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RHA; previously LKP, DDX9 |
| Gene groups (HGNC) | DEAH-box helicases |
| Reactome | 18 pathways, smallest: DEx/H-box helicases activate type I IFN and inflammatory cytokines production; RIP-mediated NFkB activation via ZBP1; ZBP1(DAI) mediated induction of type I IFNs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08211](https://www.uniprot.org/uniprotkb/Q08211) (ATP-dependent RNA helicase A):

> Multifunctional ATP-dependent nucleic acid helicase that unwinds DNA and RNA in a 3' to 5' direction and that plays important roles in many processes, such as DNA replication, transcriptional activation, post-transcriptional RNA regulation, mRNA translation and RNA-mediated gene silencing. Requires a 3'-single-stranded tail as entry site for acid nuclei unwinding activities as well as the binding and hydrolyzing of any of the four ribo- or deoxyribo-nucleotide triphosphates (NTPs). Unwinds …

**Summary**, from NCBI Gene [1660](https://www.ncbi.nlm.nih.gov/gene/1660):

> This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alternate splicing results in multiple transcript variants. Pseudogenes of this gene are found on …

**Accessions** — [HGNC:2750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2750) · Entrez [1660](https://www.ncbi.nlm.nih.gov/gene/1660) · UniProt [Q08211](https://www.uniprot.org/uniprotkb/Q08211) · Ensembl [ENSG00000135829](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135829)

## Data

Gene col 5762: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5762); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5762, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5762]; `tensor/DDL_lfc|DDL_z.npy` [5762]; `embed/gene_vectors.npy` [5762]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5762 or target_col == 5762). Every well: [[DHX9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
