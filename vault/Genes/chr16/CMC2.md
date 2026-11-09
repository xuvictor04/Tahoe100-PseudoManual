---
symbol: "CMC2"
type: "gene"
col: 2321
ensembl_id: "ENSG00000103121"
name: "C-X9-C motif containing 2"
location: "16q23.2"
module: 67
arm: "+"
pooled_cpm: 57.5
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CMC2

*C-X9-C motif containing 2* — 16q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (18 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.20× (z +15.3, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.52× (z +8.2, q 2e-14, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.693× (z -10.1, q 2e-21, down in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.773× (z -5.0, q 9e-05, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STIL]] (+0.74, fdr 7e-06), [[POC1A]] (+0.72, fdr 7e-06), [[SRGAP2D]] (+0.72, fdr 7e-06); moves opposite to [[ZBED9]] (-0.63, fdr 1e-05), [[KICS2]] (-0.61, fdr 2e-05), [[ZNF772]] (-0.60, fdr 1e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 19 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2321.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.20×** | +15.3 | 0e+00 | 46/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.17×** | +15.1 | 0e+00 | 46/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.04×** | +13.9 | 2e-41 | 44/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.81×** | +11.6 | 6e-29 | 42/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.80×** | +11.4 | 3e-28 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.51×** | +11.3 | 2e-27 | 39/47 (CFPAC-1, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.68×** | +10.1 | 5e-22 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.60×** | +9.2 | 3e-18 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +8.2 | 2e-14 | 38/48 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.49×** | +7.5 | 5e-12 | 29/47 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.43×** | +6.9 | 2e-10 | 34/48 (SW1417, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.93×** | +6.7 | 1e-09 | 29/48 (SW480, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.26×** | +6.4 | 6e-09 | 26/48 (NCI-H460, RKO, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.39×** | +6.4 | 8e-09 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +6.2 | 2e-08 | 28/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 6e-06 | 25/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +4.6 | 1e-04 | 21/48 (A549, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.007 | 13/48 (SNU-423, A549, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2321.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.693×** | -10.1 | 2e-21 | 35/48 (AsPC-1, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.677×** | -7.6 | 7e-12 | 37/48 (CHP-212, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.773×** | -5.0 | 9e-05 | 26/48 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.794×** | -4.5 | 9e-04 | 24/48 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.801×** | -4.3 | 0.002 | 24/48 (HOP62, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.842× | -3.2 | 0.097 | 16/48 (A498, J82, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.729×** | -3.2 | 0.097 | 13/47 (MIA PaCa-2, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.849× | -3.2 | 0.097 | 14/48 (A-172, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2321. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.9 | 10 (10 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +11.3) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[SW480 (line)]] | alt | 114 | 7 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +12.7) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[LS 180 (line)]] | wt | 41.8 | 4 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +9.6) ⚠ cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.373× (z -12.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[PANC-1 (line)]] | alt | 38.3 | 5 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.36× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[LoVo (line)]] | wt | 38.5 | 2 (2 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.32× (z +8.9) ⚠ cell-cycle shift, explains ~40% of this change | [[Dinaciclib (drug)]] 5 µM 0.264× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 68.2 | 4 (4 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.35× (z +10.0) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H23 (line)]] | alt | 52.5 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.63× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SHP-77 (line)]] | alt | 92.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.13× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Dinaciclib (drug)]] 5 µM 0.0898× (z -26.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.441× (z -9.3) |
| [[A-427 (line)]] | wt | 78.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.329× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.558× (z -8.6) |
| [[H4 (line)]] | wt | 48.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.311× (z -10.8) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Temsirolimus (drug)]] 0.5 µM 0.256× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 43.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +8.6) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H1792 (line)]] | alt | 38.1 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.47× (z +9.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[RKO (line)]] | wt | 52.8 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.30× (z +10.4) ⚠ toxic; cell-cycle shift, explains ~37% of this change | — |
| [[A-172 (line)]] | wt | 67.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.518× (z -9.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A498 (line)]] | wt | 92.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.494× (z -10.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A549 (line)]] | wt | 48.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[AsPC-1 (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.384× (z -12.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[CFPAC-1 (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.2) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HEC-1-A (line)]] | alt | 56.6 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.07× (z +9.1) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HOP62 (line)]] | alt | 64.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.510× (z -9.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[KATO III (line)]] | alt | 49.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.62× (z +8.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H2347 (line)]] | alt | 32.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +8.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[RPMI-7951 (line)]] | alt | 48.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +8.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SNU-423 (line)]] | alt | 40.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.2) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[AN3 CA (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2321), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STIL]] | +0.74 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[POC1A]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[SRGAP2D]] | +0.72 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[RAD51]] | +0.70 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[NUDT1]] | +0.70 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[BARD1]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[RAD54L]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[ABHD12]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SAP130]] | +0.68 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[HAT1]] | +0.68 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[CENPJ]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[SIVA1]] | +0.66 | +0.68 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED9]] | -0.63 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[KICS2]] | -0.61 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[ZNF772]] | -0.60 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.59 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[AIMP1]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[GPRASP1]] | -0.59 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ZSCAN29]] | -0.59 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[USP40]] | -0.58 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.58 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ZNF606]] | -0.58 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[RPL7L1]] | -0.58 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[RNF6]] | -0.57 | -0.52 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-30.3, -50.3); signed map (-42.2, -40.1). **Vector** length 103, 29.7% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.59 to 12); *G2/M checkpoint* (hallmark, mean cos +0.62 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.57 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.6 | +11.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.1 | +15.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.2 | +6.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +2.6 | +11.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +4.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.6 | +3.6 |
|  | [[8-Hydroxyquinoline (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.3 | +1.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -10.7 | -10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.0 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.9 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.8 | -0.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -7.4 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.2 | -5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | C-X9-C motif containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.2 — chr16:80,966,448-81,020,270 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DC13, MGC45036; previously C16orf61 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRP2](https://www.uniprot.org/uniprotkb/Q9NRP2) (COX assembly mitochondrial protein 2 homolog):

> May be involved in cytochrome c oxidase biogenesis.

**Summary**, from NCBI Gene [56942](https://www.ncbi.nlm.nih.gov/gene/56942):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24447](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24447) · Entrez [56942](https://www.ncbi.nlm.nih.gov/gene/56942) · UniProt [Q9NRP2](https://www.uniprot.org/uniprotkb/Q9NRP2) · Ensembl [ENSG00000103121](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103121)

## Data

Gene col 2321: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2321); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2321, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2321]; `tensor/DDL_lfc|DDL_z.npy` [2321]; `embed/gene_vectors.npy` [2321]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2321 or target_col == 2321). Every well: [[CMC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
