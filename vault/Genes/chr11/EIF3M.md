---
symbol: "EIF3M"
type: "gene"
col: 7341
ensembl_id: "ENSG00000149100"
name: "eukaryotic translation initiation factor 3 subunit M"
location: "11p13"
module: 33
arm: "+"
pooled_cpm: 113.53
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# EIF3M

*eukaryotic translation initiation factor 3 subunit M* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.95× (z +9.3, q 8e-18, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.54× (z +5.9, q 5e-07, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.729× (z -6.5, q 5e-08, down in 39 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.386×, A498 0.548×, RKO 0.587×, LoVo 0.582×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.305×, SNU-1 0.510×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.336×); [[Vortioxetine (drug)]] 0.05 µM in 1 line (SW 1088 0.0700×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNB1IP1]] (+0.69, fdr 1e-05), [[NLE1]] (+0.68, fdr 1e-05), [[RMND1]] (+0.65, fdr 1e-05); moves opposite to [[HMGN2]] (-0.66, fdr 1e-05), [[SNHG31]] (-0.59, fdr 6e-05), [[HMGN2P5]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TEKT4P2-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7341.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +9.3 | 8e-18 | 45/49 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +8.9 | 1e-16 | 36/44 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +6.6 | 6e-09 | 35/45 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +5.9 | 5e-07 | 40/48 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +5.2 | 3e-05 | 37/49 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +5.0 | 4e-05 | 37/48 (SHP-77, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +5.0 | 5e-05 | 40/48 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +5.0 | 5e-05 | 29/48 (HOP62, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +4.9 | 6e-05 | 39/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +4.3 | 8e-04 | 36/48 (HOP62, A-172, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.63×** | +3.7 | 0.010 | 35/48 (NCI-H460, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +3.6 | 0.013 | 27/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.30×** | +3.6 | 0.013 | 28/47 (KATO III, HCT15, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.019 | 19/49 (AN3 CA, H4, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.27×** | +3.4 | 0.021 | 29/48 (HOP62, LOX-IMVI, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.026 | 24/48 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.035 | 32/48 (SW 900, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.048 | 28/48 (SW1417, J82, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.051 | 27/49 (NCI-H2347, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.49×** | +3.0 | 0.067 | 24/48 (H4, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.067 | 24/48 (C-33 A, C32, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7341.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.386×, A498 0.548×, RKO 0.587×, LoVo 0.582×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.305×, SNU-1 0.510×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.336×); [[Vortioxetine (drug)]] 0.05 µM in 1 line (SW 1088 0.0700×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -6.5 | 5e-08 | 39/49 (MIA PaCa-2, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.796× | -3.2 | 0.39 | 24/48 (H4, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7341. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 89.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +14.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 90.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +12.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 231 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -16.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -13.0) |
| [[SNU-1 (line)]] | wt | 142 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 145 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +8.5) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -9.3) |
| [[HOP62 (line)]] | alt | 76.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +12.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 72.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +12.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 89.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 45.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 169 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.59× (z +11.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 172 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -10.2) |
| [[A549 (line)]] | wt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 64.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +8.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 51.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +8.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +10.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 71.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +9.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 138 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 86.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 78.3 | 0 | 1 | — | [[Vortioxetine (drug)]] 0.05 µM 0.0700× (z -9.2) |
| [[A-172 (line)]] | wt | 84.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 138 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 114 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 94.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 86.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 134 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7341), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNB1IP1]] | +0.69 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[NLE1]] | +0.68 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[RMND1]] | +0.65 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[POLR3A]] | +0.65 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[EARS2]] | +0.64 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[SLX9]] | +0.64 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[RPF2]] | +0.63 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[TAMM41]] | +0.62 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[DNAJA3]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[NOL10]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[CTU1]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[DCAF4]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN2]] | -0.66 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[SNHG31]] | -0.59 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[HMGN2P5]] | -0.56 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[DLEU2]] | -0.56 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[CDK2AP1]] | -0.55 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[STMN1]] | -0.54 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[WAC-AS1]] | -0.54 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[HMGB1]] | -0.54 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[MYL6]] | -0.53 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CFL1]] | -0.53 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[PKNOX1]] | -0.53 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[SRSF5]] | -0.52 | -0.45 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TEKT4P2-1]] | B | TEKT4P2-1 activity raises EIF3M's level | lines that do not express TEKT4P2-1 (20) vs lines expressing it (30) | 1.20× lower at baseline in the lines without TEKT4P2-1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000291032, ENSG00000291065, IL1RAPL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.1, -42.4); signed map (-8.8, -51.4). **Vector** length 98.0, 31.8% of its response variance represented; |z| ≥ 3 in 839 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.8 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +5.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -1.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 3 subunit M |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:32,583,798-32,606,264 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hfl-B5, FLJ29030, GA17, TANGO7; previously PCID1 |
| Gene groups (HGNC) | Eukaryotic translation initiation factor 3 complex subunits; Armadillo like helical domain containing |
| Reactome | 14 pathways, smallest: Formation of the ternary complex, and subsequently, the 43S complex; Ribosomal scanning and start codon recognition; Translation initiation complex formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L2H7](https://www.uniprot.org/uniprotkb/Q7L2H7) (Eukaryotic translation initiation factor 3 subunit M):

> Component of the eukaryotic translation initiation factor 3 (eIF-3) complex, which is required for several steps in the initiation of protein synthesis. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC). The eIF-3 complex stimulates mRNA recruitment to the 43S PIC and scanning of the mRNA for AUG recognition. The eIF-3 complex is also required for disassembly …

**Summary**, from NCBI Gene [10480](https://www.ncbi.nlm.nih.gov/gene/10480):

> This gene encodes a protein that is part of the eurkaryotic translation initiation factor 3 complete (eIF-3) required for protein synthesis. Elevated levels of the encoded protein are present in cancer cell lines. Inactivation of the encoded protein has been shown to interfere with translation of herpes virus mRNAs by preventing the association of mRNAs with the ribosomes. A pseudogene of this gene is located on the X chromosome. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:24460](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24460) · Entrez [10480](https://www.ncbi.nlm.nih.gov/gene/10480) · UniProt [Q7L2H7](https://www.uniprot.org/uniprotkb/Q7L2H7) · Ensembl [ENSG00000149100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149100)

## Data

Gene col 7341: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7341); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7341, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7341]; `tensor/DDL_lfc|DDL_z.npy` [7341]; `embed/gene_vectors.npy` [7341]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7341 or target_col == 7341). Every well: [[EIF3M — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3M.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
