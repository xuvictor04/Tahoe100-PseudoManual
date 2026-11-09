---
symbol: "SCOC"
type: "gene"
col: 7692
ensembl_id: "ENSG00000153130"
name: "short coiled-coil protein"
location: "4q31.1"
module: 17
arm: "+"
pooled_cpm: 38.63
n_lines_expressing: 46
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# SCOC

*short coiled-coil protein* — 4q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.14× (z +14.2, q 7e-43, up in 41 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +6.3, q 5e-08, up in 31 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (HEC-1-A 3.18×, HOP62 4.07×, NCI-H460 3.80×, A498 3.68×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (HEC-1-A 3.79×, NCI-H460 3.91×, A549 5.22×, PANC-1 3.34×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HOP62 2.48×, A-172 2.44×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.553× (z -7.3, q 1e-10, down in 34 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.598× (z -6.4, q 6e-08, down in 34 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDH1]] (+0.62, fdr 7e-06), [[COMMD8]] (+0.57, fdr 2e-05), [[PGM2]] (+0.56, fdr 3e-05); moves opposite to [[TRIR]] (-0.57, fdr 3e-05, ⚠ TRIR in the vector space only through flagged drug-doses), [[SMPD4BP]] (-0.56, fdr 1e-05), [[HIRA]] (-0.53, fdr 1e-05), [[GUSBP11]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[TWF1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7692.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (HEC-1-A 3.18×, HOP62 4.07×, NCI-H460 3.80×, A498 3.68×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (HEC-1-A 3.79×, NCI-H460 3.91×, A549 5.22×, PANC-1 3.34×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HOP62 2.48×, A-172 2.44×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.14×** | +14.2 | 7e-43 | 41/42 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.67×** | +11.7 | 3e-29 | 35/37 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.08×** | +7.8 | 1e-12 | 33/38 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.3 | 5e-08 | 31/44 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.59×** | +5.7 | 1e-06 | 30/44 (LS 180, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.54×** | +5.3 | 9e-06 | 33/44 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.52×** | +5.2 | 2e-05 | 27/44 (A498, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.44×** | +4.5 | 5e-04 | 29/43 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.45×** | +4.4 | 5e-04 | 28/43 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.007 | 24/44 (KATO III, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.34×** | +3.6 | 0.015 | 19/44 (HOP62, A549, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.5 | 0.018 | 20/42 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.33×** | +3.4 | 0.032 | 21/43 (A498, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.28× | +3.0 | 0.10 | 23/44 (HOP62, NCI-H460, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7692.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.553×** | -7.3 | 1e-10 | 34/43 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.598×** | -6.4 | 6e-08 | 34/43 (LS 180, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.607×** | -6.2 | 1e-07 | 34/44 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -6.1 | 1e-07 | 35/44 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.880× | -5.4 | 8e-06 | 8/44 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.494×** | -4.6 | 5e-04 | 32/43 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.500×** | -4.5 | 6e-04 | 26/43 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 123 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -23.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -10.5) |
| [[HOP62 (line)]] | alt | 52.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 36.9 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.34× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Digitoxin (drug)]] 5 µM 0.295× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.386× (z -8.7) |
| [[LS 180 (line)]] | wt | 57.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.387× (z -8.5) |
| [[A-172 (line)]] | wt | 54.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 39.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A549 (line)]] | wt | 30.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[C32 (line)]] | wt | 40.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[CFPAC-1 (line)]] | alt | 80.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HEC-1-A (line)]] | alt | 55.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HepG2_C3A (line)]] | wt | 43.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.99× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HT-29 (line)]] | alt | 52.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Digitoxin (drug)]] 5 µM 0.383× (z -8.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 44.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 20.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2030 (line)]] | alt | 44.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2347 (line)]] | alt | 48.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H460 (line)]] | wt | 36.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SNU-423 (line)]] | alt | 32.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW480 (line)]] | alt | 21.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HCT15 (line)]] | alt | 47.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[Hs 766T (line)]] | wt | 37.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HS-578T (line)]] | alt | 39.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[LOX-IMVI (line)]] | wt | 47.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1792 (line)]] | alt | 37.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SHP-77 (line)]] | alt | 29.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 45.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-427 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDH1]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[COMMD8]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[PGM2]] | +0.56 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[ENPP4]] | +0.55 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[AKAP11]] | +0.52 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[TSPAN31]] | +0.52 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[EIF2AK1]] | +0.51 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[CLCN3]] | +0.51 | +0.64 / +0.37 | both halves | 9e-05 |  |
| [[BROX]] | +0.51 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[ALDH9A1]] | +0.51 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ZBTB41]] | +0.51 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[MOCS2]] | +0.50 | +0.56 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIR]] ⚠ | -0.57 | -0.51 / -0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SMPD4BP]] | -0.56 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[HIRA]] | -0.53 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[GUSBP11]] | -0.53 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[LSM7]] | -0.53 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[LRFN4]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[VKORC1L1]] | -0.51 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[KMT2B]] | -0.50 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ADAT3]] | -0.50 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[ZMYND19]] | -0.49 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[GATD1-DT]] | -0.49 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[DDX51]] | -0.49 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[SETD1A]] | -0.49 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SCOC's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TWF1]] | C | SCOC activity lowers TWF1's level | lines that do not express SCOC (4) vs lines expressing it (46) | 1.67× higher at baseline in the lines without SCOC | 0.023 | ⚠ few lines (4 vs 46); within organs, on part of the lines |
| [[CDR2]] | C | SCOC activity lowers CDR2's level | lines that do not express SCOC (4) vs lines expressing it (46) | 1.43× higher at baseline in the lines without SCOC | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines |
| [[LRRC69]] | C | SCOC activity lowers LRRC69's level | lines that do not express SCOC (4) vs lines expressing it (46) | 1.65× higher at baseline in the lines without SCOC | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.257). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-27.9, -12.7); signed map (6.2, -36.2). **Vector** length 76.7, 18.0% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.6 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +3.3 | +14.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +2.8 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.0 | +1.4 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.9 | -6.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -6.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -1.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -5.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.4 | -0.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.3 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | short coiled-coil protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.1 — chr4:140,257,286-140,385,728 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HRIHFB2072, SCOCO, UNC-69 |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIL1](https://www.uniprot.org/uniprotkb/Q9UIL1) (Short coiled-coil protein):

> Positive regulator of amino acid starvation-induced autophagy.

**Summary**, from NCBI Gene [60592](https://www.ncbi.nlm.nih.gov/gene/60592):

> This gene encodes a short coiled-coiled domain-containing protein that localizes to the Golgi apparatus. The encoded protein interacts with ADP-ribosylation factor-like proteins. Pseudogenes of this gene are found on chromosomes 1 and 14. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:20335](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20335) · Entrez [60592](https://www.ncbi.nlm.nih.gov/gene/60592) · UniProt [Q9UIL1](https://www.uniprot.org/uniprotkb/Q9UIL1) · Ensembl [ENSG00000153130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153130)

## Data

Gene col 7692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7692); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7692]; `tensor/DDL_lfc|DDL_z.npy` [7692]; `embed/gene_vectors.npy` [7692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7692 or target_col == 7692). Every well: [[SCOC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCOC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
