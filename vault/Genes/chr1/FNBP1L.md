---
symbol: "FNBP1L"
type: "gene"
col: 6095
ensembl_id: "ENSG00000137942"
name: "formin binding protein 1 like"
location: "1p22.1"
module: 204
arm: "+"
pooled_cpm: 205.3
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/204"]
generated_by: "tahoemap"
---

# FNBP1L

*formin binding protein 1 like* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.48× (z +8.5, q 7e-15, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.604× (z -10.5, q 6e-23, down in 39 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.770× (z -8.0, q 2e-13, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 11 lines (Hs 766T 0.358×, HOP62 0.430×, MIA PaCa-2 0.440×, NCI-H1573 0.482×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (C-33 A 0.120×, LS 180 0.202×, A-427 0.239×, Panc 03.27 0.336×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.388×, MIA PaCa-2 0.395×, NCI-H460 0.478×, NCI-H2347 0.491×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX7]] (+0.64, fdr 1e-05), [[PPP2R5A]] (+0.62, fdr 1e-05), [[MBOAT2]] (+0.62, fdr 1e-05); moves opposite to [[TAF2]] (-0.62, fdr 2e-05), [[REXO1]] (-0.61, fdr 1e-05), [[MLH1]] (-0.59, fdr 3e-05).
> It is in [[Module 204]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GRB7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6095.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +8.5 | 7e-15 | 30/47 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +4.4 | 0.002 | 26/47 (LoVo, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.24×** | +4.4 | 0.002 | 27/48 (SNU-423, C-33 A, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.4 | 0.002 | 17/48 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +4.2 | 0.004 | 15/47 (C32, NCI-H460, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.011 | 20/48 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.7 | 0.015 | 10/47 (Panc 03.27, SW48, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.017 | 12/47 (NCI-H2030, BT-474, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.025 | 18/47 (NCI-H2030, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.025 | 20/47 (J82, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.036 | 21/47 (SW480, PANC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.070 | 21/46 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.086 | 19/48 (HepG2/C3A, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.095 | 16/48 (NCI-H460, C32, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6095.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 11 lines (Hs 766T 0.358×, HOP62 0.430×, MIA PaCa-2 0.440×, NCI-H1573 0.482×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (C-33 A 0.120×, LS 180 0.202×, A-427 0.239×, Panc 03.27 0.336×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.388×, MIA PaCa-2 0.395×, NCI-H460 0.478×, NCI-H2347 0.491×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.604×** | -10.5 | 6e-23 | 39/46 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.619×** | -10.4 | 1e-22 | 36/48 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.619×** | -9.9 | 5e-21 | 33/43 (C-33 A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.770×** | -8.0 | 2e-13 | 24/47 (Hs 766T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.779×** | -7.6 | 3e-12 | 22/48 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.718×** | -7.2 | 7e-11 | 29/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.703×** | -7.0 | 1e-10 | 25/44 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.879× | -3.9 | 0.006 | 13/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.954× | -3.6 | 0.022 | 1/49 (HOP62) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.890× | -3.6 | 0.022 | 14/47 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.850× | -3.5 | 0.023 | 21/47 (LS 180, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.852× | -3.5 | 0.025 | 20/47 (BT-474, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.859× | -3.3 | 0.047 | 19/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.862× | -3.2 | 0.053 | 18/47 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.868× | -3.0 | 0.089 | 12/47 (CFPAC-1, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6095. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 340 | 0 | 9 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.221× (z -18.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.560× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 359 | 2 | 6 (5 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.02× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.470× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 253 | 2 | 6 (5 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.61× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.637× (z -8.5) |
| [[SW480 (line)]] | alt | 238 | 4 (3 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -12.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HepG2_C3A (line)]] | wt | 262 | 3 (2 ⚠) | 4 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.75× (z +12.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +11.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.381× (z -11.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.568× (z -10.2) |
| [[LoVo (line)]] | wt | 197 | 2 (1 ⚠) | 5 (4 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.46× (z +13.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.05× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.623× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 250 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 243 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -13.7) |
| [[SW1417 (line)]] | alt | 307 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +13.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.459× (z -10.0) ⚠ toxic |
| [[KATO III (line)]] | alt | 208 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -12.0) ⚠ cell-cycle shift, explains ~18% of this change |
| [[LS 180 (line)]] | wt | 408 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -20.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 268 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.549× (z -9.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 119 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +16.2) | — |
| [[BT-474 (line)]] | alt | 425 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.416× (z -10.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HEC-1-A (line)]] | alt | 388 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.461× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 356 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -12.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 191 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.3) |
| [[A-427 (line)]] | wt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -16.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 284 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -24.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 89.5 | 2 | 0 | [[Ponatinib (drug)]] 5 µM 2.76× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -14.3) |
| [[Hs 766T (line)]] | wt | 167 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -16.1) |
| [[NCI-H460 (line)]] | wt | 149 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.478× (z -10.9) |
| [[A549 (line)]] | wt | 171 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -10.8) ⚠ cell-cycle shift, explains ~18% of this change |
| [[AsPC-1 (line)]] | alt | 171 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 248 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -11.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 201 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -11.0) |
| [[J82 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.52× (z +9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 206 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.423× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 143 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.611× (z -9.6) |
| [[A498 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 137 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 98.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 84.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 123 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.9 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 183 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6095), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX7]] | +0.64 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[PPP2R5A]] | +0.62 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[MBOAT2]] | +0.62 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[PPP1R2]] | +0.62 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[KRAS]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[TBC1D12]] | +0.60 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[LTA4H]] | +0.59 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[SNX30]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[RAP1A]] | +0.59 | +0.70 / +0.39 | both halves | 6e-05 |  |
| [[TMEM131L]] | +0.59 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[STRN]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[LRRC1]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF2]] | -0.62 | -0.68 / -0.47 | both halves | 2e-05 |  |
| [[REXO1]] | -0.61 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[MLH1]] | -0.59 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[ACAD9]] | -0.59 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[AGAP6]] | -0.58 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[SNAPC5]] | -0.58 | -0.64 / -0.38 | both halves | 6e-05 |  |
| [[SP2]] | -0.57 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[FIZ1]] | -0.56 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[MIRLET7IHG]] | -0.55 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[CSTF3]] | -0.55 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[MIS12]] | -0.54 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[EMG1]] | -0.54 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRB7]] | B | GRB7 activity raises FNBP1L's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 1.81× lower at baseline in the lines without GRB7 | 0.012 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[GRB7]] | B | GRB7 activity strengthens FNBP1L's drug response | lines that do not express GRB7 (24) vs lines expressing it (24) | the lines without GRB7 respond 0.55× as strongly (z diff +1.96); strongest at Dinaciclib 0.5 µM: 0.78x vs 0.53x (z diff +4.6) | 0.039 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP; target measured in part of the lines; artifact flags |
| [[ZNF655]] | B | ZNF655 activity lowers FNBP1L's level | lines that do not express ZNF655 (7) vs lines expressing it (43) | 1.75× higher at baseline in the lines without ZNF655 | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 204]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.771). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.9, -12.2); signed map (-21.8, 16.9). **Vector** length 125, 39.4% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.5 | +1.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.2 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.0 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.6 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.2 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.1 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.1 | -10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.4 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -1.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.8 | -1.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | formin binding protein 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:93,448,118-93,554,661 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TOCA1, FLJ20275; previously C1orf39 |
| Gene groups (HGNC) | F-BAR domain containing; SH3 domain containing |
| Reactome | 8 pathways, smallest: RHOJ GTPase cycle; Clathrin-mediated endocytosis; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T0N5](https://www.uniprot.org/uniprotkb/Q5T0N5) (Formin-binding protein 1-like):

> Required to coordinate membrane tubulation with reorganization of the actin cytoskeleton during endocytosis. May bind to lipids such as phosphatidylinositol 4,5-bisphosphate and phosphatidylserine and promote membrane invagination and the formation of tubules. Also promotes CDC42-induced actin polymerization by activating the WASL/N-WASP-WASPIP/WIP complex, the predominant form of WASL/N-WASP in cells. Actin polymerization may promote the fission of membrane tubules to form endocytic vesicles. …

**Summary**, from NCBI Gene [54874](https://www.ncbi.nlm.nih.gov/gene/54874):

> The protein encoded by this gene binds to both CDC42 and N-WASP. This protein promotes CDC42-induced actin polymerization by activating the N-WASP-WIP complex and, therefore, is involved in a pathway that links cell surface signals to the actin cytoskeleton. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20851) · Entrez [54874](https://www.ncbi.nlm.nih.gov/gene/54874) · UniProt [Q5T0N5](https://www.uniprot.org/uniprotkb/Q5T0N5) · Ensembl [ENSG00000137942](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137942)

## Data

Gene col 6095: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6095); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6095, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6095]; `tensor/DDL_lfc|DDL_z.npy` [6095]; `embed/gene_vectors.npy` [6095]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6095 or target_col == 6095). Every well: [[FNBP1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FNBP1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
