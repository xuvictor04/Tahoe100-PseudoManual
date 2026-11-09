---
symbol: "UBASH3B"
type: "gene"
col: 7774
ensembl_id: "ENSG00000154127"
name: "ubiquitin associated and SH3 domain containing B"
location: "11q24.1"
module: 151
arm: "+"
pooled_cpm: 142.85
n_lines_expressing: 43
n_dd_up: 8
n_dd_down: 44
n_dd_up_clean: 3
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 21
direction_downstream: 22
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# UBASH3B

*ubiquitin associated and SH3 domain containing B* — 11q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.40× (z +7.1, q 8e-10, up in 30 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (6 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.530× (z -11.3, q 9e-27, down in 40 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRY4-AS1]] (+0.69, fdr 7e-06), [[SCHIP1]] (+0.65, fdr 7e-06), [[PNP]] (+0.65, fdr 7e-06); moves opposite to [[FPGT]] (-0.57, fdr 1e-05), [[HINT3]] (-0.53, fdr 3e-05), [[YY1AP1]] (-0.53, fdr 1e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[HMGA2]] → it (grade B ⚠); 22 go from it, the strongest it → [[AMOTL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7774.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +7.1 | 8e-10 | 30/41 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.8 | 5e-04 | 24/41 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.32×** | +4.0 | 0.012 | 21/41 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.26×** | +3.5 | 0.072 | 19/41 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.4 | 0.072 | 18/40 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.26×** | +3.3 | 0.085 | 19/43 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.095 | 16/41 (NCI-H460, RKO, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.24×** | +3.2 | 0.095 | 16/40 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.23× | +3.1 | 0.11 | 19/41 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.22× | +3.0 | 0.13 | 16/41 (RKO, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7774.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.530×** | -11.3 | 9e-27 | 40/41 (HEC-1-A, HCT15, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.489×** | -10.8 | 1e-24 | 38/43 (HEC-1-A, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.529×** | -9.4 | 7e-19 | 31/42 (SK-MEL-2, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **0.549×** | -9.3 | 2e-18 | 34/42 (HEC-1-A, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.551×** | -8.5 | 2e-15 | 36/41 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.571×** | -8.3 | 8e-15 | 34/41 (KATO III, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.559×** | -8.3 | 8e-15 | 26/38 (SK-MEL-2, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.622×** | -8.2 | 2e-14 | 32/41 (HEC-1-A, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.568×** | -7.8 | 5e-13 | 30/39 (NCI-H2030, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.594×** | -7.7 | 6e-13 | 32/42 (HEC-1-A, HCT15, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.605×** | -7.2 | 4e-11 | 34/40 (HEC-1-A, HCT15, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.655×** | -6.3 | 2e-08 | 28/40 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.649×** | -6.1 | 6e-08 | 33/41 (HEC-1-A, SW480, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.460×** | -6.0 | 7e-08 | 33/39 (HEC-1-A, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.747×** | -5.9 | 1e-07 | 27/42 (HEC-1-A, C32, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.491×** | -5.5 | 1e-06 | 29/41 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.692×** | -5.5 | 2e-06 | 26/41 (SK-MEL-2, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.773×** | -5.3 | 3e-06 | 29/41 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.785×** | -5.0 | 1e-05 | 22/41 (C32, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 191 | 0 | 19 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0267× (z -18.8) ⚠ toxic · without an alert: [[Trametinib (drug)]] 5 µM 0.178× (z -18.1) |
| [[NCI-H2030 (line)]] | alt | 823 | 0 | 18 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -23.2) |
| [[KATO III (line)]] | alt | 252 | 0 | 13 (3 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.216× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 237 | 0 | 13 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0626× (z -24.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -16.2) |
| [[C32 (line)]] | wt | 340 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0883× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.301× (z -11.8) |
| [[PANC-1 (line)]] | alt | 331 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -16.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -13.4) |
| [[HCT15 (line)]] | alt | 115 | 0 | 6 (1 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.328× (z -12.0) |
| [[A-427 (line)]] | wt | 85.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -14.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.361× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 268 | 0 | 5 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.114× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.183× (z -11.4) |
| [[HT-29 (line)]] | alt | 48.9 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +12.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.63× (z +8.7) | — |
| [[SW480 (line)]] | alt | 85.7 | 0 | 5 | — | [[Trametinib (drug)]] 5 µM 0.392× (z -10.8) |
| [[A549 (line)]] | wt | 234 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -12.9) |
| [[HS-578T (line)]] | alt | 194 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -10.9) |
| [[J82 (line)]] | alt | 81.0 | 0 | 4 (3 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.324× (z -10.1) |
| [[LS 180 (line)]] | wt | 82.7 | 3 (2 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +13.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 65.1 | 4 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +13.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +8.9) | — |
| [[H4 (line)]] | wt | 212 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.215× (z -10.0) |
| [[RKO (line)]] | wt | 126 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.362× (z -9.8) |
| [[A-172 (line)]] | wt | 47.1 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.337× (z -9.5) |
| [[LoVo (line)]] | wt | 93.7 | 2 (2 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +9.9) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[Panc 03.27 (line)]] | alt | 181 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -11.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 71.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 142 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 197 | 0 | 1 | — | [[Trametinib (drug)]] 0.5 µM 0.415× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -11.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 91.7 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.333× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.584× (z -15.5) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 44.3 | 0 | 1 | — | [[Trametinib (drug)]] 0.5 µM 0.381× (z -10.1) |
| [[A498 (line)]] | wt | 90.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 103 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 27.3 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRY4-AS1]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[SCHIP1]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[PNP]] | +0.65 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[ITGB5]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SLC4A7]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[OSBPL10]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[COL13A1]] | +0.62 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[SPRED2]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.61 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[KIAA1549L]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TNFRSF10A]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ACER3]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FPGT]] | -0.57 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[HINT3]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[YY1AP1]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[USP30]] | -0.52 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[ALDH3B1]] | -0.52 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[ERP29]] | -0.51 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[EMC2]] | -0.51 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 16, C 5. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGA2]] | B | HMGA2 activity raises UBASH3B's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 2.92× lower at baseline in the lines without HMGA2 | 0.008 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[AMOTL1]] | B | AMOTL1 activity raises UBASH3B's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 1.66× lower at baseline in the lines without AMOTL1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[ARHGAP22]] | B | ARHGAP22 activity raises UBASH3B's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without ARHGAP22 | 0.027 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[ANKH]] | B | ANKH activity raises UBASH3B's level | lines that do not express ANKH (6) vs lines expressing it (44) | 4.47× lower at baseline in the lines without ANKH | 0.027 | ⚠ within organs, on part of the lines; also absent: GCNT1, LCA5, CA13; maybe low, not absent |
| [[HTR7]] | B | HTR7 activity raises UBASH3B's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.85× lower at baseline in the lines without HTR7 | 0.038 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[TM4SF1]] | B | TM4SF1 activity raises UBASH3B's level | lines that do not express TM4SF1 (12) vs lines expressing it (38) | 2.49× lower at baseline in the lines without TM4SF1 | 0.038 | ⚠ within organs, on part of the lines; also absent: TM4SF1-AS1; maybe low, not absent |
| [[LINC02454]] | B | LINC02454 activity raises UBASH3B's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 2.08× lower at baseline in the lines without LINC02454 | 0.038 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers UBASH3B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FOSL1]] | B | FOSL1 activity raises UBASH3B's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 4.36× lower at baseline in the lines without FOSL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[ADORA2B]] | B | ADORA2B activity raises UBASH3B's level | lines that do not express ADORA2B (6) vs lines expressing it (44) | 2.52× lower at baseline in the lines without ADORA2B | 0.060 | ⚠ within organs, on part of the lines; also absent: SGK2, FOSL1, PAQR5; maybe low, not absent; its own permutation p |
| [[NPAS2]] | B | NPAS2 activity raises UBASH3B's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 2.17× lower at baseline in the lines without NPAS2 | 0.067 | ⚠ within organs, on part of the lines |
| [[WIPF1]] | B | WIPF1 activity raises UBASH3B's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 1.52× lower at baseline in the lines without WIPF1 | 0.082 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3 |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 20, C 2. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMOTL1]] | B | UBASH3B activity raises AMOTL1's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 1.71× lower at baseline in the lines without UBASH3B | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[FOSL1]] | B | UBASH3B activity raises FOSL1's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 2.21× lower at baseline in the lines without UBASH3B | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[FXYD5]] | B | UBASH3B activity raises FXYD5's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 2.52× lower at baseline in the lines without UBASH3B | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[MIR100HG]] | B | UBASH3B activity raises MIR100HG's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 4.76× lower at baseline in the lines without UBASH3B | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[COL13A1]] | B | UBASH3B activity raises COL13A1's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 2.21× lower at baseline in the lines without UBASH3B | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[ITGA2]] | B | UBASH3B activity raises ITGA2's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 2.58× lower at baseline in the lines without UBASH3B | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[LRRC8C]] | B | UBASH3B activity raises LRRC8C's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 3.13× lower at baseline in the lines without UBASH3B | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[CCND1]] | B | UBASH3B activity raises CCND1's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 1.93× lower at baseline in the lines without UBASH3B | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[ARHGAP22]] | B | UBASH3B activity raises ARHGAP22's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 3.71× lower at baseline in the lines without UBASH3B | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[ACTN1]] | B | UBASH3B activity raises ACTN1's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without UBASH3B | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[DCBLD2]] | B | UBASH3B activity raises DCBLD2's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 2.73× lower at baseline in the lines without UBASH3B | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[HMGA2]] | B | UBASH3B activity raises HMGA2's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 3.39× lower at baseline in the lines without UBASH3B | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.708). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.1, 6.0); signed map (6.1, 47.1). **Vector** length 145, 47.6% of its response variance represented; |z| ≥ 3 in 1,770 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.0 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +5.4 | +3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.2 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.1 | +4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.0 | +3.2 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +3.2 | +2.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.2 | +3.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -9.6 | -10.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -9.4 | -11.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -8.1 | -8.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -8.1 | -7.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -7.6 | -9.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -7.5 | -8.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin associated and SH3 domain containing B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.1 — chr11:122,655,722-122,814,473 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1959, STS-1, TULA2, TULA-2 |
| Gene groups (HGNC) | Protein phosphatases; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TF42](https://www.uniprot.org/uniprotkb/Q8TF42) (Ubiquitin-associated and SH3 domain-containing protein B):

> Interferes with CBL-mediated down-regulation and degradation of receptor-type tyrosine kinases. Promotes accumulation of activated target receptors, such as T-cell receptors and EGFR, on the cell surface. Exhibits tyrosine phosphatase activity toward several substrates including EGFR, FAK, SYK, and ZAP70. Down-regulates proteins that are dually modified by both protein tyrosine phosphorylation and ubiquitination.

**Summary**, from NCBI Gene [84959](https://www.ncbi.nlm.nih.gov/gene/84959):

> This gene encodes a protein that contains a ubiquitin associated domain at the N-terminus, an SH3 domain, and a C-terminal domain with similarities to the catalytic motif of phosphoglycerate mutase. The encoded protein was found to inhibit endocytosis of epidermal growth factor receptor (EGFR) and platelet-derived growth factor receptor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:29884](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29884) · Entrez [84959](https://www.ncbi.nlm.nih.gov/gene/84959) · UniProt [Q8TF42](https://www.uniprot.org/uniprotkb/Q8TF42) · Ensembl [ENSG00000154127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154127)

## Data

Gene col 7774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7774); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7774]; `tensor/DDL_lfc|DDL_z.npy` [7774]; `embed/gene_vectors.npy` [7774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7774 or target_col == 7774). Every well: [[UBASH3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBASH3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
