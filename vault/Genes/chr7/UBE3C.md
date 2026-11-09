---
symbol: "UBE3C"
type: "gene"
col: 186
ensembl_id: "ENSG00000009335"
name: "ubiquitin protein ligase E3C"
location: "7q36.3"
module: 18
arm: "+"
pooled_cpm: 229.26
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# UBE3C

*ubiquitin protein ligase E3C* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.45× (z +8.9, q 4e-16, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.673× (z -8.3, q 5e-14, down in 32 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.802× (z -7.4, q 2e-11, down in 27 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (NCI-H2030 0.541×, A549 0.569×, SW480 0.666×, HEC-1-A 0.638×, …); [[Dinaciclib (drug)]] 5 µM in 6 lines (C-33 A 0.0353×, NCI-H23 0.339×, SNU-1 0.266×, SHP-77 0.389×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (C32 0.453×, HEC-1-A 0.550×, LoVo 0.579×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 0.517×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XPO5]] (+0.69, fdr 7e-06), [[PUS7]] (+0.68, fdr 7e-06), [[MDN1]] (+0.66, fdr 7e-06); moves opposite to [[ABCA5]] (-0.56, fdr 2e-05), [[TP53INP2]] (-0.54, fdr 1e-05), [[PIK3IP1]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CGNL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 186.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +8.9 | 4e-16 | 35/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.19×** | +8.3 | 3e-14 | 41/48 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +6.8 | 2e-09 | 36/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +6.5 | 1e-08 | 35/48 (SHP-77, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.79×** | +6.2 | 9e-08 | 40/49 (LoVo, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +5.9 | 3e-07 | 30/48 (CFPAC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.25×** | +5.2 | 2e-05 | 29/48 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.23×** | +4.9 | 6e-05 | 24/48 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.9 | 6e-05 | 32/48 (PANC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.21×** | +4.5 | 4e-04 | 22/48 (NCI-H1792, NCI-H2347, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.20×** | +4.1 | 0.002 | 24/47 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.002 | 22/48 (CFPAC-1, HCT15, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.003 | 21/47 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.19× | +4.0 | 0.003 | 22/48 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.6 | 0.011 | 27/45 (SNU-423, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.056 | 11/48 (SW480, HCT15, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 186.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (NCI-H2030 0.541×, A549 0.569×, SW480 0.666×, HEC-1-A 0.638×, …); [[Dinaciclib (drug)]] 5 µM in 6 lines (C-33 A 0.0353×, NCI-H23 0.339×, SNU-1 0.266×, SHP-77 0.389×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (C32 0.453×, HEC-1-A 0.550×, LoVo 0.579×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 0.517×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.673×** | -8.3 | 5e-14 | 32/45 (C-33 A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.718×** | -7.6 | 1e-11 | 31/44 (C-33 A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -7.4 | 2e-11 | 27/49 (NCI-H2030, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.733×** | -7.4 | 2e-11 | 31/49 (C-33 A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **0.781×** | -5.9 | 4e-07 | 32/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.872× | -3.1 | 0.16 | 16/47 (SW1417, RKO, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.880× | -3.1 | 0.18 | 10/48 (KATO III, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 186. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 465 | 2 (1 ⚠) | 4 (2 ⚠) | [[Decitabine (drug)]] 5 µM 1.79× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -21.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.453× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 253 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.508× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -11.5) |
| [[LoVo (line)]] | wt | 350 | 1 | 4 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.36× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.511× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -10.9) |
| [[SW480 (line)]] | alt | 324 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.57× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.666× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 239 | 3 (2 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.68× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.510× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 354 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.99× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -10.5) |
| [[A498 (line)]] | wt | 259 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -15.1) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 394 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0353× (z -47.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 347 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.79× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.650× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 123 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 1.96× (z +9.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[COLO 205 (line)]] | alt | 128 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -11.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 264 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.552× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 227 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 185 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.87× (z +9.3) ⚠ cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.632× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 198 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -13.6) |
| [[SHP-77 (line)]] | alt | 164 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -13.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 235 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -13.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 319 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.554× (z -9.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 395 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -8.9) |
| [[A-172 (line)]] | wt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -11.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 186 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.482× (z -11.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 199 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -13.4) |
| [[AN3 CA (line)]] | alt | 266 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.3) |
| [[Hs 766T (line)]] | wt | 174 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +8.5) | — |
| [[J82 (line)]] | alt | 210 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.529× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 102 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.49× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 310 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.98× (z +10.2) ⚠ unreliable plate only | — |
| [[SNU-1 (line)]] | wt | 201 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -15.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 221 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 138 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 196 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 169 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 215 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 176 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 186), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPO5]] | +0.69 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[PUS7]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[MDN1]] | +0.66 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[EXOC2]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ATR]] | +0.64 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[EHMT1]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[XPO4]] | +0.63 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[CLASP2]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[TYW1]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[ERI3]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[IPO11]] | +0.62 | +0.63 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCA5]] | -0.56 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[TP53INP2]] | -0.54 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[PIK3IP1]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[MTMR11]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[FAM117A]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[CCNG2]] | -0.52 | -0.45 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CGNL1]] | B | CGNL1 activity lowers UBE3C's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.26× higher at baseline in the lines without CGNL1 | 0.094 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[MTHFD1L]] | C | MTHFD1L activity raises UBE3C's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 1.71× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.7, -34.3); signed map (-14.6, -51.8). **Vector** length 118, 38.9% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +8.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.6 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | -7.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.3 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.8 | -0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -1.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -0.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin protein ligase E3C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.3 — chr7:157,138,926-157,269,370 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0010, KIAA10 |
| Gene groups (HGNC) | HECT domain E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15386](https://www.uniprot.org/uniprotkb/Q15386) (Ubiquitin-protein ligase E3C):

> E3 ubiquitin-protein ligase that specifically catalyzes 'Lys-29'- and 'Lys-48'-linked polyubiquitin chains. Accepts ubiquitin from the E2 ubiquitin-conjugating enzyme UBE2D1 in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Associates with the proteasome and promotes elongation of ubiquitin chains on substrates bound to the 26S proteasome. Also catalyzes 'Lys-29'- and 'Lys-48'-linked ubiquitination of 26S proteasome subunit ADRM1/RPN13 in response to …

**Summary**, from NCBI Gene [9690](https://www.ncbi.nlm.nih.gov/gene/9690):

> Enables ubiquitin protein ligase activity. Involved in protein K29-linked ubiquitination; protein K48-linked ubiquitination; and ubiquitin-dependent protein catabolic process. Predicted to be part of proteasome complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16803](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16803) · Entrez [9690](https://www.ncbi.nlm.nih.gov/gene/9690) · UniProt [Q15386](https://www.uniprot.org/uniprotkb/Q15386) · Ensembl [ENSG00000009335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000009335)

## Data

Gene col 186: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 186); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 186, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 186]; `tensor/DDL_lfc|DDL_z.npy` [186]; `embed/gene_vectors.npy` [186]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 186 or target_col == 186). Every well: [[UBE3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
