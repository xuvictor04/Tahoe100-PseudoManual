---
symbol: "CCDC47"
type: "gene"
col: 2971
ensembl_id: "ENSG00000108588"
name: "coiled-coil domain containing 47"
location: "17q23.3"
module: 103
arm: "+"
pooled_cpm: 164.9
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# CCDC47

*coiled-coil domain containing 47* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (16 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.78× (z +11.4, q 2e-27, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +10.0, q 6e-21, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.786× (z -6.2, q 4e-07, down in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~64% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.765× (z -3.8, q 0.048, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.229×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.434×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.498×; ⚠ cell-cycle shift, explains ~97% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYH10]] (+0.60, fdr 3e-05), [[YEATS2]] (+0.59, fdr 1e-05), [[TBC1D9B]] (+0.58, fdr 1e-05); moves opposite to [[MTHFS]] (-0.52, fdr 6e-05), [[SPIN2B]] (-0.46, fdr 2e-04), [[ZNF691]] (-0.46, fdr 2e-04).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC2A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 19 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2971.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.78×** | +11.4 | 2e-27 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +10.0 | 6e-21 | 41/49 (Hs 766T, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.57×** | +8.9 | 1e-16 | 36/49 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.52×** | +8.3 | 2e-14 | 36/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.53×** | +8.1 | 6e-14 | 32/44 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.48×** | +7.7 | 1e-12 | 40/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.46×** | +7.5 | 7e-12 | 41/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.48×** | +6.9 | 3e-10 | 41/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.45×** | +6.6 | 3e-09 | 38/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.42×** | +6.2 | 3e-08 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.77×** | +5.9 | 2e-07 | 37/49 (HS-578T, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +5.8 | 3e-07 | 34/48 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +5.7 | 5e-07 | 39/48 (LoVo, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +5.4 | 3e-06 | 32/48 (Hs 766T, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.23×** | +5.3 | 4e-06 | 23/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 2e-05 | 29/48 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.52×** | +4.3 | 5e-04 | 34/48 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.1 | 0.001 | 22/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.001 | 26/48 (CFPAC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.003 | 32/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.018 | 20/49 (SW480, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.030 | 19/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.1 | 0.044 | 18/48 (C-33 A, SW480, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.052 | 16/49 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +2.9 | 0.063 | 22/48 (SW1417, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.32×** | +2.9 | 0.075 | 17/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2971.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.229×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.434×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.498×; ⚠ cell-cycle shift, explains ~97% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.786×** | -6.2 | 4e-07 | 29/48 (NCI-H1792, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.765×** | -3.8 | 0.048 | 30/48 (hTERT-HPNE, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.834× | -3.6 | 0.057 | 22/48 (CHP-212, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.832×** | -3.5 | 0.057 | 24/49 (A-427, HS-578T, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.837× | -3.5 | 0.057 | 22/48 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.884× | -3.2 | 0.12 | 5/48 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.855× | -3.1 | 0.17 | 13/48 (A-427, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2971. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 143 | 9 (8 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.38× (z +13.3) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 163 | 8 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +17.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Gefitinib (drug)]] 5 µM 1.95× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 134 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 138 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +10.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +10.0) | — |
| [[KATO III (line)]] | alt | 216 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +11.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +10.0) | — |
| [[LoVo (line)]] | wt | 126 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +12.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[LS 180 (line)]] | wt | 135 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +12.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 115 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.7) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[A498 (line)]] | wt | 155 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[NCI-H1792 (line)]] | alt | 157 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[PANC-1 (line)]] | alt | 122 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +13.0) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[AsPC-1 (line)]] | alt | 114 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +11.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 284 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[HEC-1-A (line)]] | alt | 149 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | — |
| [[Hs 766T (line)]] | wt | 106 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 203 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[SNU-1 (line)]] | wt | 152 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +10.1) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SW1417 (line)]] | alt | 118 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.4) | — |
| [[CHP-212 (line)]] | wt | 348 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -8.7) ⚠ cell-cycle shift, explains ~97% of this change |
| [[COLO 205 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +9.4) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[HepG2_C3A (line)]] | wt | 141 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.3) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[HOP62 (line)]] | alt | 189 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +10.2) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[J82 (line)]] | alt | 170 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 183 | 1 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.4) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H2347 (line)]] | alt | 198 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +9.5) | — |
| [[A-172 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 238 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 195 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 114 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 203 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 212 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 215 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 191 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 184 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 163 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2971), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYH10]] | +0.60 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[YEATS2]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TBC1D9B]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[P4HB]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[VDAC1]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 | pathway: Protein localization |
| [[PPFIA4]] | +0.57 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[FAM210A]] | +0.56 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[ARFGEF3]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[HSP90B1]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[LMAN1]] | +0.55 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[CRYBG3]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[AK2]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFS]] | -0.52 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[SPIN2B]] | -0.46 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[ZNF691]] | -0.46 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[KLHL42]] | -0.45 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[SHROOM1]] | -0.44 | -0.41 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A3]] | B | SLC2A3 activity raises CCDC47's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.30× lower at baseline in the lines without SLC2A3 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.2, -17.8); signed map (-38.7, 26.3). **Vector** length 105, 35.0% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +10.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.7 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -8.2 | -6.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -6.6 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.5 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.4 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -0.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 47 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:63,745,255-63,776,351 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GK001 |
| Gene groups (HGNC) | PAT complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A33](https://www.uniprot.org/uniprotkb/Q96A33) (PAT complex subunit CCDC47):

> Component of the multi-pass translocon (MPT) complex that mediates insertion of multi-pass membrane proteins into the lipid bilayer of membranes. The MPT complex takes over after the SEC61 complex: following membrane insertion of the first few transmembrane segments of proteins by the SEC61 complex, the MPT complex occludes the lateral gate of the SEC61 complex to promote insertion of subsequent transmembrane regions. Within the MPT complex, the PAT subcomplex sequesters any highly polar …

**Summary**, from NCBI Gene [57003](https://www.ncbi.nlm.nih.gov/gene/57003):

> Enables protein folding chaperone and ribosome binding activity. Involved in ERAD pathway; endoplasmic reticulum calcium ion homeostasis; and multi-pass transmembrane protein insertion into ER membrane. Located in endoplasmic reticulum membrane. Part of multi-pass translocon complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24856) · Entrez [57003](https://www.ncbi.nlm.nih.gov/gene/57003) · UniProt [Q96A33](https://www.uniprot.org/uniprotkb/Q96A33) · Ensembl [ENSG00000108588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108588)

## Data

Gene col 2971: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2971); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2971, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2971]; `tensor/DDL_lfc|DDL_z.npy` [2971]; `embed/gene_vectors.npy` [2971]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2971 or target_col == 2971). Every well: [[CCDC47 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC47.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
