---
symbol: "TSPAN3"
type: "gene"
col: 6400
ensembl_id: "ENSG00000140391"
name: "tetraspanin 3"
location: "15q24.3"
module: 12
arm: "-"
pooled_cpm: 83.73
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 13
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# TSPAN3

*tetraspanin 3* — 15q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.43× (z +17.6, q 0e+00, up in 43 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.40× (z +6.4, q 2e-08, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.606× (z -14.1, q 3e-42, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTN4]] (+0.53, fdr 2e-05), [[TP53I11]] (+0.52, fdr 6e-05), [[TSPAN1]] (+0.51, fdr 4e-05); moves opposite to [[C2orf74]] (-0.55, fdr 2e-05), [[C1orf131]] (-0.51, fdr 4e-05), [[CCDC174]] (-0.51, fdr 3e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[TMC5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +17.6 | 0e+00 | 43/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +14.7 | 0e+00 | 37/41 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +8.3 | 1e-14 | 35/43 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +7.1 | 1e-10 | 1/50 (CFPAC-1) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.4 | 2e-08 | 27/48 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.25×** | +6.1 | 8e-08 | 24/49 (NCI-H23, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +5.9 | 3e-07 | 26/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.32×** | +5.5 | 3e-06 | 24/48 (PANC-1, SW480, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.53×** | +5.2 | 1e-05 | 34/48 (COLO 205, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +4.8 | 1e-04 | 29/48 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +4.6 | 2e-04 | 23/50 (HOP62, SW480, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.46×** | +4.6 | 2e-04 | 26/47 (NCI-H460, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.1 | 0.002 | 17/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~12% of this change | **1.23×** | +4.1 | 0.002 | 19/48 (HS-578T, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.015 | 16/48 (A-172, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.084 | 9/48 (A-172, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.084 | 14/46 (NCI-H1573, SW 900, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6400.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.606×** | -14.1 | 3e-42 | 34/48 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.502×** | -13.2 | 4e-37 | 39/48 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.643×** | -6.0 | 3e-07 | 29/48 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.587×** | -5.0 | 8e-05 | 26/49 (LS 180, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.777×** | -4.8 | 2e-04 | 26/49 (C-33 A, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.826×** | -3.8 | 0.013 | 23/48 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.699×** | -3.4 | 0.060 | 20/48 (RKO, BT-474, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 78.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -15.8) |
| [[A549 (line)]] | wt | 136 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -20.0) |
| [[AsPC-1 (line)]] | alt | 147 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -18.4) |
| [[PANC-1 (line)]] | alt | 38.3 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -14.3) |
| [[Hs 766T (line)]] | wt | 211 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -25.8) |
| [[LS 180 (line)]] | wt | 123 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -19.8) |
| [[NCI-H2347 (line)]] | alt | 97.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -18.7) |
| [[NCI-H460 (line)]] | wt | 48.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -12.8) |
| [[A498 (line)]] | wt | 59.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -13.1) |
| [[C32 (line)]] | wt | 127 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.370× (z -9.6) |
| [[COLO 205 (line)]] | alt | 217 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -33.0) |
| [[HT-29 (line)]] | alt | 282 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -28.3) |
| [[KATO III (line)]] | alt | 201 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -22.2) |
| [[A-172 (line)]] | wt | 86.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 142 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -25.3) |
| [[HEC-1-A (line)]] | alt | 72.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +12.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 58.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +14.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 64.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -10.8) |
| [[LoVo (line)]] | wt | 180 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -13.7) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.382× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 30.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.90× (z +14.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 76.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +13.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 93.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -8.6) |
| [[SW 900 (line)]] | alt | 60.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -10.2) |
| [[SW1417 (line)]] | alt | 60.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -9.4) |
| [[SW480 (line)]] | alt | 52.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 32.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +9.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 57.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 40.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +8.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 24.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +8.7) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[RPMI-7951 (line)]] | alt | 57.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 41.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 58.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 72.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 99.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTN4]] | +0.53 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[TP53I11]] | +0.52 | +0.57 / +0.39 | both halves | 6e-05 |  |
| [[TSPAN1]] | +0.51 | +0.55 / +0.40 | both halves | 4e-05 | same gene group |
| [[PIGR]] | +0.50 | +0.48 / +0.38 | both halves | 7e-05 |  |
| [[CEACAM6]] | +0.50 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[CLSTN1]] | +0.48 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[SELENON]] | +0.48 | +0.49 / +0.38 | both halves | 7e-05 |  |
| [[DIAPH1]] | +0.48 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[TMC5]] | +0.48 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[GOLM1]] | +0.48 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[CALM3]] | +0.47 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[LAPTM4B]] | +0.47 | +0.38 / +0.45 | both halves | 7e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2orf74]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[C1orf131]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[CCDC174]] | -0.51 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[TCEAL8]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ZNF830]] | -0.48 | -0.43 / -0.49 | both halves | 4e-05 |  |
| [[GSPT2]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[USP27X]] | -0.48 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[PEX12]] | -0.47 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SURF6]] | -0.47 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[CCDC43]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[C18orf21]] | -0.46 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[ARMCX2]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMC5]] | B | TMC5 activity raises TSPAN3's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 2.04× lower at baseline in the lines without TMC5 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[ALOX5]] | B | ALOX5 activity raises TSPAN3's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 1.59× lower at baseline in the lines without ALOX5 | 0.008 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[ATP10B]] | B | ATP10B activity raises TSPAN3's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 2.12× lower at baseline in the lines without ATP10B | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[MUC13]] | B | MUC13 activity raises TSPAN3's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 2.17× lower at baseline in the lines without MUC13 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[TMC5]] | B | TMC5 activity weakens TSPAN3's drug response | lines that do not express TMC5 (29) vs lines expressing it (21) | the lines without TMC5 respond 1.24× as strongly (z diff -0.53); strongest at Idarubicin (hydrochloride) 5 µM: 1.33x vs 0.86x (z diff -5.5) | 0.039 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4; both ways; artifact flags |
| [[CEACAM6]] | B | CEACAM6 activity raises TSPAN3's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 1.83× lower at baseline in the lines without CEACAM6 | 0.044 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[WNT5A]] | B | WNT5A activity strengthens TSPAN3's drug response | lines that do not express WNT5A (30) vs lines expressing it (20) | the lines without WNT5A respond 0.81× as strongly (z diff +0.76); strongest at Idarubicin (hydrochloride) 5 µM: 1.00x vs 1.34x (z diff +3.7) | 0.052 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; both ways; artifact flags |
| [[DAPK1]] | B | DAPK1 activity raises TSPAN3's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 1.41× lower at baseline in the lines without DAPK1 | 0.064 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[CEACAM5]] | B | CEACAM5 activity raises TSPAN3's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 1.79× lower at baseline in the lines without CEACAM5 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[CEACAM5]] | B | CEACAM5 activity weakens TSPAN3's drug response | lines that do not express CEACAM5 (39) vs lines expressing it (11) | the lines without CEACAM5 respond 1.61× as strongly (z diff -0.86); strongest at Idarubicin (hydrochloride) 5 µM: 1.22x vs 0.78x (z diff -6.4) | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; both ways; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers TSPAN3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CEACAM6]] | B | CEACAM6 activity weakens TSPAN3's drug response | lines that do not express CEACAM6 (37) vs lines expressing it (13) | the lines without CEACAM6 respond 1.32× as strongly (z diff -0.62); strongest at Idarubicin (hydrochloride) 5 µM: 1.25x vs 0.79x (z diff -5.8) | 0.095 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-18.9, 26.4); signed map (69.5, 3.3). **Vector** length 117, 32.5% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +17.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -14.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -6.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -4.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.3 — chr15:77,041,404-77,083,984 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TM4-A, TSPAN-3; previously TM4SF8 |
| Gene groups (HGNC) | Tetraspanin family |
| Matched by | ensembl_id |

**Function**, from UniProt [O60637](https://www.uniprot.org/uniprotkb/O60637) (Tetraspanin-3):

> Regulates the proliferation and migration of oligodendrocytes, a process essential for normal myelination and repair.

**Summary**, from NCBI Gene [10099](https://www.ncbi.nlm.nih.gov/gene/10099):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. The use of alternate polyadenylation sites has been found for this gene. Multiple alternative transcripts encoding different …

**Accessions** — [HGNC:17752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17752) · Entrez [10099](https://www.ncbi.nlm.nih.gov/gene/10099) · UniProt [O60637](https://www.uniprot.org/uniprotkb/O60637) · Ensembl [ENSG00000140391](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140391)

## Data

Gene col 6400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6400); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6400]; `tensor/DDL_lfc|DDL_z.npy` [6400]; `embed/gene_vectors.npy` [6400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6400 or target_col == 6400). Every well: [[TSPAN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
