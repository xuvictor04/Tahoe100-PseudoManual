---
symbol: "PPME1"
type: "gene"
col: 13206
ensembl_id: "ENSG00000214517"
name: "protein phosphatase methylesterase 1"
location: "11q13.4"
module: 105
arm: "+"
pooled_cpm: 147.33
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 2
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# PPME1

*protein phosphatase methylesterase 1* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.05× (z +12.6, q 9e-34, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.706× (z -5.9, q 2e-06, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AN3 CA 0.193×, C32 0.266×, NCI-H1792 0.390×, SNU-423 0.506×; ⚠ cell-cycle shift, explains ~53% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (BT-474 0.324×, C-33 A 0.392×, CFPAC-1 0.379×, NCI-H2347 0.454×; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.661×, MIA PaCa-2 0.782×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 0.388×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LNPK]] (+0.61, fdr 2e-05), [[HELZ]] (+0.60, fdr 1e-05), [[BTAF1]] (+0.60, fdr 2e-05); moves opposite to [[TJP1]] (-0.51, fdr 5e-05), [[IKBKB]] (-0.50, fdr 3e-05), [[MYO1C]] (-0.48, fdr 5e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HLA-F-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13206.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.05×** | +12.6 | 9e-34 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +11.0 | 7e-26 | 40/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +10.5 | 2e-23 | 39/49 (NCI-H2030, AsPC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +8.6 | 7e-16 | 45/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +8.6 | 7e-16 | 42/48 (LoVo, SHP-77, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +8.1 | 4e-14 | 40/50 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +8.0 | 1e-13 | 40/49 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +7.7 | 1e-12 | 36/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.56×** | +7.5 | 4e-12 | 37/48 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +7.3 | 1e-11 | 39/48 (SW480, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.50×** | +7.2 | 4e-11 | 34/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +7.0 | 2e-10 | 36/48 (PANC-1, A498, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +6.8 | 5e-10 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +6.7 | 7e-10 | 37/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.46×** | +6.6 | 2e-09 | 38/49 (KATO III, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.39×** | +5.8 | 3e-07 | 34/48 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +5.2 | 8e-06 | 32/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.33×** | +5.0 | 1e-05 | 39/48 (LS 180, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13206.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AN3 CA 0.193×, C32 0.266×, NCI-H1792 0.390×, SNU-423 0.506×; ⚠ cell-cycle shift, explains ~53% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (BT-474 0.324×, C-33 A 0.392×, CFPAC-1 0.379×, NCI-H2347 0.454×; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.661×, MIA PaCa-2 0.782×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 0.388×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.706×** | -5.9 | 2e-06 | 31/44 (BT-474, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.789×** | -4.2 | 0.008 | 25/49 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.832× | -3.2 | 0.23 | 23/49 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 167 | 16 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +22.0) | — |
| [[PANC-1 (line)]] | alt | 118 | 14 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +17.7) | — |
| [[BT-474 (line)]] | alt | 236 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -11.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 109 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 106 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.43× (z +19.2) | — |
| [[LoVo (line)]] | wt | 109 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.12× (z +19.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 200 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +15.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +13.7) | — |
| [[NCI-H23 (line)]] | alt | 261 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +12.8) | [[Adagrasib (drug)]] 0.05 µM 0.661× (z -18.0) ⚠ position not correctable |
| [[C32 (line)]] | wt | 290 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -19.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.388× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 120 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -14.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A-427 (line)]] | wt | 114 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.30× (z +10.1) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[AsPC-1 (line)]] | alt | 114 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +14.3) | — |
| [[C-33 A (line)]] | alt | 140 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -9.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 123 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +11.2) | — |
| [[J82 (line)]] | alt | 313 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +13.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 135 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 118 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 96.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +15.6) | — |
| [[NCI-H2030 (line)]] | alt | 124 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +15.7) | — |
| [[SW1417 (line)]] | alt | 169 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.74× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +10.7) | — |
| [[A549 (line)]] | wt | 105 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.45× (z +10.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Selinexor (drug)]] 5 µM 1.86× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 62.8 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.64× (z +9.2) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 105 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 151 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 110 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.3) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 172 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -9.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 147 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.8) | — |
| [[RKO (line)]] | wt | 143 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 165 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +8.9) | — |
| [[A-172 (line)]] | wt | 158 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.31× (z +9.5) | — |
| [[A498 (line)]] | wt | 66.5 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.18× (z +11.9) | — |
| [[AN3 CA (line)]] | alt | 275 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -21.3) ⚠ cell-cycle shift, explains ~53% of this change |
| [[CFPAC-1 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -9.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 126 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 324 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.20× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.9) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SNU-423 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -11.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SW48 (line)]] | wt | 145 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +10.0) | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 187 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 124 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LNPK]] | +0.61 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[HELZ]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[BTAF1]] | +0.60 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[BMT2]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[PIAS2]] | +0.58 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PEX3]] | +0.58 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.57 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[AK2]] | +0.57 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[CRYBB2P1]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[FAM210A]] | +0.55 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[PDK1]] | +0.55 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[SNX3]] | +0.54 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TJP1]] | -0.51 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[IKBKB]] | -0.50 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[MYO1C]] | -0.48 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[PTPN21]] | -0.47 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[CHTOP]] | -0.47 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[PPRC1]] | -0.46 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[ACOT9]] | -0.45 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[NUP98]] | -0.45 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[WDR82]] | -0.44 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-F-AS1]] | B | HLA-F-AS1 activity lowers PPME1's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.48× higher at baseline in the lines without HLA-F-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.8, -18.9); signed map (-39.3, 24.2). **Vector** length 103, 34.3% of its response variance represented; |z| ≥ 3 in 1,384 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.9 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +10.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.8 | +5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.5 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +8.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.4 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -6.3 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.5 | +3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.4 | +0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase methylesterase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:74,171,267-74,254,703 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PME-1, ABDH19 |
| Gene groups (HGNC) | Abhydrolase domain containing; Protein phosphatase 2 modulatory subunits |
| Reactome | 5 pathways, smallest: Cyclin A/B1/B2 associated events during G2/M transition; G2/M Transition; Mitotic G2-G2/M phases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y570](https://www.uniprot.org/uniprotkb/Q9Y570) (Protein phosphatase methylesterase 1):

> Demethylates proteins that have been reversibly carboxymethylated. Demethylates PPP2CB (in vitro) and PPP2CA. Binding to PPP2CA displaces the manganese ion and inactivates the enzyme.

**Summary**, from NCBI Gene [51400](https://www.ncbi.nlm.nih.gov/gene/51400):

> This gene encodes a protein phosphatase methylesterase localized to the nucleus. The encoded protein acts on the protein phosphatase-2A catalytic subunit and supports the ERK pathway through dephosphorylation of regulatory proteins. It plays a role in malignant glioma progression. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:30178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30178) · Entrez [51400](https://www.ncbi.nlm.nih.gov/gene/51400) · UniProt [Q9Y570](https://www.uniprot.org/uniprotkb/Q9Y570) · Ensembl [ENSG00000214517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214517)

## Data

Gene col 13206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13206); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13206]; `tensor/DDL_lfc|DDL_z.npy` [13206]; `embed/gene_vectors.npy` [13206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13206 or target_col == 13206). Every well: [[PPME1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPME1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
