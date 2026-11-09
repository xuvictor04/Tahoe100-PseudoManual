---
symbol: "UBE2Z"
type: "gene"
col: 8228
ensembl_id: "ENSG00000159202"
name: "ubiquitin conjugating enzyme E2 Z"
location: "17q21.32"
module: 70
arm: "+"
pooled_cpm: 140.23
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# UBE2Z

*ubiquitin conjugating enzyme E2 Z* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.96× (z +17.9, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.537× (z -16.4, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-E]] (+0.63, fdr 1e-05), [[APBA3]] (+0.59, fdr 2e-05), [[PRRG4]] (+0.57, fdr 4e-05); moves opposite to [[NCBP1]] (-0.62, fdr 7e-06), [[GNB1L]] (-0.53, fdr 5e-05), [[TNIK]] (-0.50, fdr 4e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GSDMD]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8228.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +17.9 | 0e+00 | 45/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +15.2 | 0e+00 | 42/48 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +11.3 | 3e-27 | 37/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +7.4 | 2e-11 | 35/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +6.4 | 2e-08 | 29/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +5.8 | 6e-07 | 26/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.31×** | +5.1 | 3e-05 | 27/47 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +4.7 | 2e-04 | 20/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.4 | 6e-04 | 19/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.17× | +4.1 | 0.002 | 21/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.5 | 0.023 | 8/49 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.068 | 15/48 (CHP-212, LS 180, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.095 | 9/48 (SK-MEL-2, RPMI-7951, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8228.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.537×** | -16.4 | 0e+00 | 45/48 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.543×** | -16.1 | 0e+00 | 42/48 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.561×** | -15.3 | 0e+00 | 41/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.633×** | -12.1 | 2e-31 | 44/48 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -11.8 | 4e-30 | 36/49 (SK-MEL-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.694×** | -9.6 | 6e-20 | 38/48 (SW 900, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.599×** | -7.1 | 1e-10 | 42/49 (LOX-IMVI, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.773×** | -6.3 | 3e-08 | 26/45 (CHP-212, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.799×** | -5.7 | 9e-07 | 22/44 (Panc 03.27, NCI-H1573, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.799×** | -4.9 | 7e-05 | 24/49 (RKO, AsPC-1, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.846× | -4.4 | 6e-04 | 17/48 (SK-MEL-2, Panc 03.27, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.890× | -4.3 | 7e-04 | 6/48 (LOX-IMVI, CFPAC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.869× | -3.5 | 0.024 | 11/47 (BT-474, SW48, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | 0.879× | -3.4 | 0.030 | 6/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8228. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 501 | 8 (5 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.76× (z +27.0) | [[Panobinostat (drug)]] 0.5 µM 0.501× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 160 | 4 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.413× (z -13.3) |
| [[PANC-1 (line)]] | alt | 220 | 7 (3 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +22.3) | [[Belinostat (drug)]] 5 µM 0.541× (z -10.5) |
| [[A-172 (line)]] | wt | 176 | 2 (2 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Belinostat (drug)]] 5 µM 0.423× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 143 | 3 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.379× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 100 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +18.8) | — |
| [[HOP62 (line)]] | alt | 154 | 2 (1 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.414× (z -15.5) |
| [[SK-MEL-2 (line)]] | alt | 164 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.446× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 225 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 153 | 1 | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.466× (z -13.1) |
| [[SNU-423 (line)]] | alt | 192 | 2 (1 ⚠) | 4 | [[Harringtonine (drug)]] 5 µM 2.24× (z +10.3) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -10.5) |
| [[A498 (line)]] | wt | 182 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.376× (z -13.7) |
| [[H4 (line)]] | wt | 164 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 117 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 103 | 2 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.458× (z -11.0) |
| [[SW480 (line)]] | alt | 99.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +19.5) | [[Homoharringtonine (drug)]] 5 µM 0.598× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 177 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.425× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.529× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 129 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[hTERT-HPNE (line)]] | wt | 198 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.387× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 135 | 2 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.562× (z -9.0) |
| [[SW 900 (line)]] | alt | 137 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.457× (z -9.8) |
| [[A-427 (line)]] | wt | 117 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.434× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 136 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -17.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.399× (z -10.2) |
| [[HS-578T (line)]] | alt | 153 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.491× (z -9.4) |
| [[KATO III (line)]] | alt | 129 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.511× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[MIA PaCa-2 (line)]] | alt | 154 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.440× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 101 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.72× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.8) | — |
| [[RKO (line)]] | wt | 94.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -8.9) |
| [[SHP-77 (line)]] | alt | 63.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 99.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +11.7) | — |
| [[C-33 A (line)]] | alt | 86.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.403× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 86.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 190 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 139 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.664× (z -9.0) |
| [[Hs 766T (line)]] | wt | 119 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.416× (z -9.9) |
| [[HT-29 (line)]] | alt | 81.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.57× (z +11.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 70.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 177 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SNU-1 (line)]] | wt | 83.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW 1271 (line)]] | alt | 174 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.228× (z -8.6) |
| [[AN3 CA (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 86.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8228), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-E]] | +0.63 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[APBA3]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[PRRG4]] | +0.57 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[APOL2]] | +0.55 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[LRCH3]] | +0.55 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[HLA-B]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 | pathway: Protein ubiquitination |
| [[KANSL1L]] | +0.54 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[EGLN2]] | +0.54 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[EIF1]] | +0.54 | +0.43 / +0.50 | both halves | 4e-05 |  |
| [[OGFR]] | +0.53 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ZFYVE1]] | +0.53 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[FLCN]] | +0.53 | +0.34 / +0.48 | both halves | 1e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCBP1]] | -0.62 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[GNB1L]] | -0.53 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TNIK]] | -0.50 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[SYNCRIP]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PRKDC]] | -0.48 | -0.32 / -0.50 | both halves | 2e-04 | pathway: Protein ubiquitination |
| [[NF2]] | -0.48 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[LAS1L]] | -0.47 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[ATG16L1]] | -0.47 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[ALDH18A1]] | -0.47 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[ASPH]] | -0.47 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[ELAVL1]] | -0.47 | -0.24 / -0.55 | both halves | 5e-04 |  |
| [[MPRIP]] | -0.46 | -0.27 / -0.44 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSDMD]] | B | GSDMD activity raises UBE2Z's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without GSDMD | 0.017 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP |
| [[HDAC6]] | B | HDAC6 activity raises UBE2Z's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.497). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.2, -41.6); signed map (-10.7, 0.1). **Vector** length 102, 30.2% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DAP12 interactions* (reactome, mean cos +0.50 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.5 | +17.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +15.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +0.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.4 | +1.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.4 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.4 | +1.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.0 | +0.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.5 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.1 | -0.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.1 | -9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -4.3 | -6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.2 | -12.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -7.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 Z |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,908,407-48,929,056 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13855, USE1 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 5 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Protein ubiquitination; Antigen processing: Ubiquitination & Proteasome degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H832](https://www.uniprot.org/uniprotkb/Q9H832) (Ubiquitin-conjugating enzyme E2 Z):

> Catalyzes the covalent attachment of ubiquitin to other proteins (By similarity). Specific substrate for UBA6, not charged with ubiquitin by UBE1. May be involved in apoptosis regulation.

**Summary**, from NCBI Gene [65264](https://www.ncbi.nlm.nih.gov/gene/65264):

> This gene encodes an enzyme which ubiquitinates proteins which participate in signaling pathways and apoptosis. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:25847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25847) · Entrez [65264](https://www.ncbi.nlm.nih.gov/gene/65264) · UniProt [Q9H832](https://www.uniprot.org/uniprotkb/Q9H832) · Ensembl [ENSG00000159202](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159202)

## Data

Gene col 8228: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8228); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8228, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8228]; `tensor/DDL_lfc|DDL_z.npy` [8228]; `embed/gene_vectors.npy` [8228]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8228 or target_col == 8228). Every well: [[UBE2Z — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2Z.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
