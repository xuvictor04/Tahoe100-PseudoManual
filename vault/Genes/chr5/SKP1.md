---
symbol: "SKP1"
type: "gene"
col: 3472
ensembl_id: "ENSG00000113558"
name: "S-phase kinase associated protein 1"
location: "5q31.1"
module: 93
arm: "+"
pooled_cpm: 167.84
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# SKP1

*S-phase kinase associated protein 1* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.52× (z +14.0, q 1e-41, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +10.6, q 4e-24, up in 47 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUCB1]] (+0.57, fdr 4e-05), [[OAT]] (+0.54, fdr 4e-05), [[ANXA1]] (+0.53, fdr 2e-05); moves opposite to [[WDR75]] (-0.56, fdr 5e-05), [[ANGEL1]] (-0.51, fdr 3e-05), [[TIMM9]] (-0.51, fdr 1e-04).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CLU]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 19 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3472.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.52×** | +14.0 | 1e-41 | 49/49 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.74×** | +11.9 | 4e-30 | 40/48 (C32, NCI-H1792, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.6 | 4e-24 | 47/49 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.99×** | +10.0 | 2e-21 | 40/44 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.84×** | +9.2 | 3e-18 | 47/48 (COLO 205, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.90×** | +9.0 | 3e-17 | 45/45 (HOP62, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.79×** | +8.8 | 8e-17 | 46/48 (HEC-1-A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.76×** | +8.5 | 1e-15 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.85×** | +8.3 | 8e-15 | 46/48 (COLO 205, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.73×** | +8.3 | 8e-15 | 42/48 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.77×** | +7.7 | 9e-13 | 46/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.59×** | +7.0 | 1e-10 | 41/48 (HEC-1-A, COLO 205, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +6.8 | 3e-10 | 44/48 (LoVo, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.54×** | +6.3 | 2e-08 | 33/48 (NCI-H1792, NCI-H460, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +6.0 | 9e-08 | 47/48 (HEC-1-A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.002 | 39/49 (Hs 766T, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.030 | 26/48 (MIA PaCa-2, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3472.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | 0.810× | -3.2 | 0.41 | 28/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.859× | -3.2 | 0.41 | 17/48 (LoVo, SNU-1, …) | inconsistent across doses |  |
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.821× | -3.0 | 0.47 | 21/47 (hTERT-HPNE, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3472. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 153 | 12 (11 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +16.6) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 154 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +11.3) | — |
| [[KATO III (line)]] | alt | 146 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +13.1) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 137 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +16.7) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 190 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +18.0) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 145 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +8.6) | — |
| [[C32 (line)]] | wt | 170 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +19.3) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[COLO 205 (line)]] | alt | 156 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +16.4) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.44× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 198 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 171 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.3) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 114 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +19.0) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[SNU-423 (line)]] | alt | 157 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +10.0) | — |
| [[SW480 (line)]] | alt | 174 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A549 (line)]] | wt | 129 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[Hs 766T (line)]] | wt | 142 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.8) | — |
| [[LoVo (line)]] | wt | 242 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.7) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.12× (z +9.5) | — |
| [[A-172 (line)]] | wt | 175 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.9) | — |
| [[A498 (line)]] | wt | 148 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[AsPC-1 (line)]] | alt | 171 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.9) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +13.3) | — |
| [[BT-474 (line)]] | alt | 178 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +11.4) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[H4 (line)]] | wt | 189 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[HT-29 (line)]] | alt | 183 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.3) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.14× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 118 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +16.7) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[LS 180 (line)]] | wt | 184 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.7) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[Panc 03.27 (line)]] | alt | 183 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.9) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +11.7) | — |
| [[C-33 A (line)]] | alt | 147 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[CFPAC-1 (line)]] | alt | 221 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.6) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 127 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +16.4) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[J82 (line)]] | alt | 156 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 171 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.42× (z +9.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SHP-77 (line)]] | alt | 110 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 226 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SW 900 (line)]] | alt | 155 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SW1417 (line)]] | alt | 154 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.0) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[SW48 (line)]] | wt | 159 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +10.1) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[HCT15 (line)]] | alt | 203 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H23 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H2347 (line)]] | alt | 248 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.3) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[RPMI-7951 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.8) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[SNU-1 (line)]] | wt | 138 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SW 1271 (line)]] | alt | 203 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +8.7) | — |
| [[A-427 (line)]] | wt | 202 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 260 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 197 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 165 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 225 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3472), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUCB1]] | +0.57 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[OAT]] | +0.54 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[ANXA1]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[LGMN]] | +0.52 | +0.53 / +0.50 | both halves | 1e-05 | pathway: Toll-like Receptor Cascades |
| [[FAM222A]] | +0.52 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[APLP2]] | +0.52 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[HSP90AB1]] | +0.51 | +0.52 / +0.48 | both halves | 2e-05 | pathway: G2/M Transition; STRING 813 |
| [[DNAJA1]] | +0.51 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[SOD1]] | +0.51 | +0.52 / +0.52 | both halves | 1e-05 | pathway: Cellular response to chemical stress |
| [[GSTM3]] | +0.51 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[TPI1]] | +0.50 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[TENT5C]] | +0.50 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR75]] | -0.56 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[ANGEL1]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[TIMM9]] | -0.51 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[IKBKB]] | -0.51 | -0.40 / -0.50 | both halves | 5e-05 | pathway: Activation of NF-kappaB in B cells; STRING 672 |
| [[SCO1]] | -0.50 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[SPATA5L1]] | -0.49 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[NUP35]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[ILKAP]] | -0.49 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[MRPL15]] | -0.49 | -0.27 / -0.55 | both halves | 3e-04 |  |
| [[FAM86HP]] | -0.49 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[ZBTB24]] | -0.49 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[FARSA]] | -0.48 | -0.37 / -0.53 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLU]] | B | CLU activity lowers SKP1's level | lines that do not express CLU (11) vs lines expressing it (39) | 1.13× higher at baseline in the lines without CLU | 0.093 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.554). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-48.1, -9.1); signed map (1.5, 17.3). **Vector** length 78.8, 29.1% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.7 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +7.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.9 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.6 | +8.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +4.0 |
|  | [[Artemether (drug)]] 0.05 µM |  | +2.0 | +1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.9 | +2.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~92% of this change | -4.7 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -3.6 | +6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | +0.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -1.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | +0.4 |
|  | [[EX229 (drug)]] 0.5 µM |  | -2.3 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | S-phase kinase associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:134,148,935-134,176,964 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EMC19, OCP2, TCEB1L, MGC34403, OCP-II, p19A; previously SKP1A |
| Gene groups (HGNC) | SCF complex core subunits |
| Hallmark sets | NOTCH_SIGNALING |
| Reactome | 116 pathways, smallest: FBXW7 Mutants and NOTCH1 in Cancer; Loss of Function of FBXW7 in Cancer and NOTCH1 Signaling; Viral strategies to evade IFIT action |
| Matched by | ensembl_id |

**Function**, from UniProt [P63208](https://www.uniprot.org/uniprotkb/P63208) (S-phase kinase-associated protein 1):

> Essential component of the SCF (SKP1-CUL1-F-box protein) ubiquitin ligase complex, which mediates the ubiquitination of proteins involved in cell cycle progression, signal transduction and transcription. In the SCF complex, serves as an adapter that links the F-box protein to CUL1. The E3 ubiquitin-protein ligase activity is regulated by the COP9 signalosome (CSN), which restores the ligase to its inactive state and resets the ligase for substrate recognition by reversing the activating …

**Summary**, from NCBI Gene [6500](https://www.ncbi.nlm.nih.gov/gene/6500):

> This gene encodes a component of SCF complexes, which are composed of this protein, cullin 1, a ring-box protein, and one member of the F-box family of proteins. This protein binds directly to the F-box motif found in F-box proteins. SCF complexes are involved in the regulated ubiquitination of specific protein substrates, which targets them for degradation by the proteosome. Specific F-box proteins recognize different target protein(s), and many specific SCF substrates have been identified …

**Accessions** — [HGNC:10899](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10899) · Entrez [6500](https://www.ncbi.nlm.nih.gov/gene/6500) · UniProt [P63208](https://www.uniprot.org/uniprotkb/P63208) · Ensembl [ENSG00000113558](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113558)

## Data

Gene col 3472: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3472); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3472, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3472]; `tensor/DDL_lfc|DDL_z.npy` [3472]; `embed/gene_vectors.npy` [3472]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3472 or target_col == 3472). Every well: [[SKP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SKP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
