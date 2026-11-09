---
symbol: "TRMT11"
type: "gene"
col: 834
ensembl_id: "ENSG00000066651"
name: "tRNA methyltransferase 11"
location: "6q22.32"
module: 4
arm: "+"
pooled_cpm: 113.83
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TRMT11

*tRNA methyltransferase 11* — 6q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.50× (z +9.7, q 2e-19, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 1.86× (z +5.5, q 1e-05, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.596× (z -12.4, q 1e-32, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METAP1D]] (+0.66, fdr 1e-05), [[PHF14]] (+0.64, fdr 7e-06), [[SHLD1]] (+0.64, fdr 1e-05); moves opposite to [[DRAP1]] (-0.61, fdr 1e-05), [[UACA]] (-0.53, fdr 3e-05), [[MAPK8IP3]] (-0.53, fdr 6e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 834.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.50×** | +9.7 | 2e-19 | 44/48 (J82, HT-29, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.86×** | +5.5 | 1e-05 | 39/49 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +4.5 | 0.001 | 31/48 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.3 | 0.002 | 28/48 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.0 | 0.005 | 1/50 (NCI-H1792) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.27×** | +4.0 | 0.005 | 27/48 (hTERT-HPNE, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +3.8 | 0.012 | 26/47 (SW1417, A498, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.15× | +3.4 | 0.048 | 6/48 (NCI-H2030, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +3.3 | 0.057 | 20/48 (HT-29, SW1417, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.058 | 21/50 (NCI-H1792, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.087 | 14/48 (NCI-H1792, HepG2/C3A, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.14× | +3.0 | 0.11 | 5/48 (RKO, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠; shown: the 15 strongest. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 834.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -12.4 | 1e-32 | 43/49 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.642×** | -10.6 | 6e-24 | 36/48 (A498, PANC-1, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.593×** | -8.9 | 2e-16 | 43/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.605×** | -8.5 | 2e-15 | 42/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.613×** | -8.3 | 1e-14 | 43/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.623×** | -8.0 | 9e-14 | 42/48 (KATO III, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.655×** | -7.2 | 6e-11 | 39/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.677×** | -6.4 | 1e-08 | 30/44 (RPMI-7951, C-33 A, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.695×** | -6.2 | 4e-08 | 44/48 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **0.713×** | -5.8 | 5e-07 | 27/49 (PANC-1, HCT15, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.761×** | -4.6 | 2e-04 | 29/48 (BT-474, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.764×** | -4.6 | 2e-04 | 24/48 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.760×** | -4.5 | 3e-04 | 27/48 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~91% of this change | **0.778×** | -4.3 | 8e-04 | 28/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.877× | -3.2 | 0.059 | 12/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 834. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 176 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -14.5) |
| [[PANC-1 (line)]] | alt | 146 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -16.6) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.536× (z -9.4) |
| [[KATO III (line)]] | alt | 142 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -13.7) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.368× (z -10.8) |
| [[SW480 (line)]] | alt | 242 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.321× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.362× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 141 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.320× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -9.8) |
| [[A498 (line)]] | wt | 76.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -17.5) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -13.8) |
| [[COLO 205 (line)]] | alt | 114 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -14.5) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 283 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.438× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 80.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -8.9) |
| [[SW 900 (line)]] | alt | 89.3 | 0 | 3 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.402× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~91% of this change |
| [[A549 (line)]] | wt | 71.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 57.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -9.0) |
| [[H4 (line)]] | wt | 84.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.331× (z -9.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HCT15 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.421× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 79.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -11.0) ⚠ cell-cycle shift, explains ~77% of this change |
| [[NCI-H23 (line)]] | alt | 163 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -10.6) |
| [[SW1417 (line)]] | alt | 109 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -11.7) |
| [[C-33 A (line)]] | alt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[CFPAC-1 (line)]] | alt | 55.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -9.8) ⚠ cell-cycle shift, explains ~77% of this change |
| [[CHP-212 (line)]] | wt | 178 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[HS-578T (line)]] | alt | 73.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -8.8) ⚠ cell-cycle shift, explains ~77% of this change |
| [[HT-29 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.70× (z +8.8) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 82.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -11.7) ⚠ cell-cycle shift, explains ~77% of this change |
| [[J82 (line)]] | alt | 70.6 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.88× (z +9.4) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[LOX-IMVI (line)]] | wt | 78.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[NCI-H1792 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -11.2) ⚠ cell-cycle shift, explains ~77% of this change |
| [[NCI-H2030 (line)]] | alt | 154 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -9.6) ⚠ cell-cycle shift, explains ~77% of this change |
| [[RPMI-7951 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[SK-MEL-2 (line)]] | alt | 90.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[SNU-423 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -16.2) ⚠ cell-cycle shift, explains ~77% of this change |
| [[SW48 (line)]] | wt | 99.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[A-172 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 175 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 88.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 151 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 177 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 834), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1D]] | +0.66 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[PHF14]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[SHLD1]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ANKAR]] | +0.63 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[COX10]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[RMDN2]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PGGT1B]] | +0.61 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[HDDC2]] | +0.61 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[RABGGTB]] | +0.60 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[ZZZ3]] | +0.60 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[SPIN3]] | +0.59 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[FUBP1]] | +0.59 | +0.46 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRAP1]] | -0.61 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[UACA]] | -0.53 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[MAPK8IP3]] | -0.53 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[ACTR1B]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[PPP1R13L]] | -0.52 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[DNAAF3]] | -0.52 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[NARF]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[FOXO6]] | -0.51 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[RNF24]] | -0.51 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[GCAT]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ESYT2]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[NDRG1]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.509). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-17.2, 3.9); signed map (7.8, -41.0). **Vector** length 119, 37.9% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +12.1 | +9.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.6 | +4.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.0 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +0.7 |
|  | [[EX229 (drug)]] 5 µM |  | +5.0 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.8 | +3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.5 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -12.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.4 | -6.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.4 | -8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -4.2 | -10.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.0 | -8.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.3 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.5 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.32 — chr6:125,986,479-126,203,817 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDS024, dJ187J11.2, TRM11, TRMT11-1; previously C6orf75 |
| Gene groups (HGNC) | 7BS N2-guanosine RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4G4](https://www.uniprot.org/uniprotkb/Q7Z4G4) (tRNA):

> Catalytic subunit of the TRMT11-TRM112 methyltransferase complex, that specifically mediates the S-adenosyl-L-methionine-dependent N(2)-methylation of guanosine nucleotide at position 10 (m2G10) in tRNAs. This is one of the major tRNA (guanine-N(2))-methyltransferases.

**Summary**, from NCBI Gene [60487](https://www.ncbi.nlm.nih.gov/gene/60487):

> Enables tRNA (guanine(10)-N2)-methyltransferase activity. Predicted to be involved in RNA methylation. Located in mitochondrion. Part of tRNA (m2G10) methyltransferase complex. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21080](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21080) · Entrez [60487](https://www.ncbi.nlm.nih.gov/gene/60487) · UniProt [Q7Z4G4](https://www.uniprot.org/uniprotkb/Q7Z4G4) · Ensembl [ENSG00000066651](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066651)

## Data

Gene col 834: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 834); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 834, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 834]; `tensor/DDL_lfc|DDL_z.npy` [834]; `embed/gene_vectors.npy` [834]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 834 or target_col == 834). Every well: [[TRMT11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
