---
symbol: "SUPT16H"
type: "gene"
col: 1694
ensembl_id: "ENSG00000092201"
name: "SPT16 homolog, facilitates chromatin remodeling subunit"
location: "14q11.2"
module: 4
arm: "+"
pooled_cpm: 132.26
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SUPT16H

*SPT16 homolog, facilitates chromatin remodeling subunit* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.06× (z +17.1, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.53× (z +6.5, q 7e-09, up in 41 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.278×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW1417 0.481×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.420×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP155]] (+0.78, fdr 7e-06), [[XRCC5]] (+0.74, fdr 7e-06), [[ILF3]] (+0.74, fdr 7e-06); moves opposite to [[MIEN1]] (-0.63, fdr 1e-05), [[SAT2]] (-0.61, fdr 1e-05), [[DCTN6-DT]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 17 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1694.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.06×** | +17.1 | 0e+00 | 49/49 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.91×** | +15.7 | 0e+00 | 43/44 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.40×** | +12.3 | 1e-32 | 45/45 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +8.1 | 1e-13 | 43/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +6.5 | 7e-09 | 41/48 (SW480, AN3 CA, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.49×** | +6.1 | 1e-07 | 35/48 (NCI-H1573, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.47×** | +5.9 | 3e-07 | 35/48 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.44×** | +5.5 | 2e-06 | 34/48 (NCI-H1792, A549, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.4 | 3e-06 | 35/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.38×** | +4.7 | 2e-04 | 34/50 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.24×** | +4.7 | 2e-04 | 34/48 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.77×** | +4.6 | 2e-04 | 31/49 (NCI-H1792, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~70% of this change | **1.36×** | +4.5 | 3e-04 | 30/47 (C32, NCI-H1792, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.23×** | +4.4 | 3e-04 | 25/49 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **1.22×** | +4.3 | 6e-04 | 30/48 (NCI-H460, HCT15, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.44×** | +2.9 | 0.089 | 19/47 (SK-MEL-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1694.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.278×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW1417 0.481×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.420×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.870× | -3.0 | 0.84 | 7/48 (NCI-H1792, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1694. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 114 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HS-578T (line)]] | alt | 57.2 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[CFPAC-1 (line)]] | alt | 110 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H2347 (line)]] | alt | 120 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +12.8) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.78× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 97.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 186 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1573 (line)]] | alt | 94.7 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 85.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SW1417 (line)]] | alt | 121 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.481× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 179 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.18× (z +9.3) | — |
| [[A498 (line)]] | wt | 93.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A549 (line)]] | wt | 100 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[AsPC-1 (line)]] | alt | 60.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HOP62 (line)]] | alt | 108 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[Hs 766T (line)]] | wt | 77.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 102 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H2030 (line)]] | alt | 182 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[PANC-1 (line)]] | alt | 137 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A-172 (line)]] | wt | 81.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[AN3 CA (line)]] | alt | 178 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.44× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.278× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[H4 (line)]] | wt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HCT15 (line)]] | alt | 193 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HT-29 (line)]] | alt | 73.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[J82 (line)]] | alt | 189 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[KATO III (line)]] | alt | 121 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LoVo (line)]] | wt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LS 180 (line)]] | wt | 80.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H460 (line)]] | wt | 125 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[Panc 03.27 (line)]] | alt | 126 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[RPMI-7951 (line)]] | alt | 122 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SW 900 (line)]] | alt | 86.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A-427 (line)]] | wt | 202 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[BT-474 (line)]] | alt | 178 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.420× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 171 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HepG2_C3A (line)]] | wt | 75.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H23 (line)]] | alt | 249 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[RKO (line)]] | wt | 211 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SHP-77 (line)]] | alt | 306 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.29× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[C-33 A (line)]] | alt | 273 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 96.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 223 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1694), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP155]] | +0.78 | +0.69 / +0.75 | both halves | 7e-06 | pathway: HIV Infection |
| [[XRCC5]] | +0.74 | +0.67 / +0.69 | both halves | 7e-06 | pathway: HIV Infection; STRING 665 |
| [[ILF3]] | +0.74 | +0.76 / +0.67 | both halves | 7e-06 | STRING 438 |
| [[PRKDC]] | +0.67 | +0.62 / +0.71 | both halves | 7e-06 | same gene group; STRING 407 |
| [[EIF4G1]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[NCBP1]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 | pathway: Formation of HIV elongation complex in the absence of HIV Tat; STRING 735 |
| [[CCT2]] | +0.64 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[LAS1L]] | +0.64 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[SMC1A]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 | STRING 437 |
| [[TOPBP1]] | +0.63 | +0.42 / +0.68 | both halves | 4e-05 | pathway: Regulation of TP53 Activity |
| [[ABCE1]] | +0.62 | +0.63 / +0.62 | both halves | 7e-06 | STRING 447 |
| [[EIF2S1]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 | STRING 507 |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIEN1]] | -0.63 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[SAT2]] | -0.61 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | -0.60 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[FKBP2]] ⚠ | -0.57 | -0.50 / -0.47 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GABARAPL2]] | -0.57 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[ZFAND2B]] | -0.56 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[CCDC126]] | -0.56 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[CIAO2B]] | -0.56 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[VPS37D]] | -0.56 | -0.55 / -0.48 | both halves | 2e-05 | pathway: HIV Infection |
| [[GUK1]] | -0.55 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[HOTAIRM1]] | -0.55 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[RNF114]] | -0.55 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[SNHG25]] | -0.55 | -0.61 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SUPT16H's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.616). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.9, -32.6); signed map (-13.9, -44.8). **Vector** length 104, 37.7% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +6.2 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +0.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.8 | +3.2 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +2.8 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +6.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.4 | +1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.9 | -1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.3 | -0.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.8 | -1.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.5 | +0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.4 | +0.4 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | SPT16 homolog, facilitates chromatin remodeling subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:21,351,476-21,384,019 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FACT, FACTP140, SPT16/CDC68, FLJ14010, FLJ10857, CDC68 |
| Gene groups (HGNC) | M24 metallopeptidase family; Armadillo like helical domain containing |
| Reactome | 28 pathways, smallest: Pausing and recovery of Tat-mediated HIV elongation; Tat-mediated HIV elongation arrest and recovery; HIV elongation arrest and recovery |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5B9](https://www.uniprot.org/uniprotkb/Q9Y5B9) (FACT complex subunit SPT16):

> Component of the FACT complex, a general chromatin factor that acts to reorganize nucleosomes. The FACT complex is involved in multiple processes that require DNA as a template such as mRNA elongation, DNA replication and DNA repair. During transcription elongation the FACT complex acts as a histone chaperone that both destabilizes and restores nucleosomal structure. It facilitates the passage of RNA polymerase II and transcription by promoting the dissociation of one histone H2A-H2B dimer from …

**Summary**, from NCBI Gene [11198](https://www.ncbi.nlm.nih.gov/gene/11198):

> Transcription of protein-coding genes can be reconstituted on naked DNA with only the general transcription factors and RNA polymerase II. However, this minimal system cannot transcribe DNA packaged into chromatin, indicating that accessory factors may facilitate access to DNA. One such factor, FACT (facilitates chromatin transcription), interacts specifically with histones H2A/H2B to effect nucleosome disassembly and transcription elongation. FACT is composed of an 80 kDa subunit and a 140 kDa …

**Accessions** — [HGNC:11465](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11465) · Entrez [11198](https://www.ncbi.nlm.nih.gov/gene/11198) · UniProt [Q9Y5B9](https://www.uniprot.org/uniprotkb/Q9Y5B9) · Ensembl [ENSG00000092201](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092201)

## Data

Gene col 1694: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1694); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1694, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1694]; `tensor/DDL_lfc|DDL_z.npy` [1694]; `embed/gene_vectors.npy` [1694]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1694 or target_col == 1694). Every well: [[SUPT16H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUPT16H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
