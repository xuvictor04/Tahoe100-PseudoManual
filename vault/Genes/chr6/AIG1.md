---
symbol: "AIG1"
type: "gene"
col: 7093
ensembl_id: "ENSG00000146416"
name: "androgen induced 1"
location: "6q24.2"
module: 207
arm: "-"
pooled_cpm: 79.72
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 35
n_dd_up_clean: 10
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# AIG1

*androgen induced 1* — 6q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.48× (z +8.2, q 1e-13, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.278× (z -18.8, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGGY]] (+0.66, fdr 9e-06), [[WWOX]] (+0.58, fdr 1e-05), [[PCNX2]] (+0.57, fdr 4e-05); moves opposite to [[GLE1]] (-0.59, fdr 4e-05), [[MFSD8]] (-0.57, fdr 2e-05), [[GTF3C5]] (-0.56, fdr 3e-05).
> It sits in the **-** arm of [[Module 207]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CDCA7L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7093.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +8.2 | 1e-13 | 39/46 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +8.0 | 4e-13 | 38/46 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.5 | 0.001 | 21/41 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.015 | 23/45 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.032 | 25/46 (HOP62, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.047 | 14/47 (C-33 A, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.052 | 21/45 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.060 | 20/47 (HOP62, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.067 | 17/46 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.079 | 13/46 (COLO 205, HCT15, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.23×** | +3.1 | 0.092 | 21/47 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.1 | 0.092 | 15/46 (NCI-H1792, HEC-1-A, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.092 | 13/46 (SW1417, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7093.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.278×** | -18.8 | 0e+00 | 45/46 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.482×** | -15.1 | 0e+00 | 39/46 (CFPAC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.483×** | -15.1 | 0e+00 | 41/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.358×** | -15.1 | 0e+00 | 42/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.363×** | -14.9 | 0e+00 | 41/46 (HCT15, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.374×** | -14.4 | 4e-45 | 42/46 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.379×** | -14.2 | 4e-44 | 44/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.464×** | -10.8 | 2e-25 | 37/45 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.538×** | -9.1 | 7e-18 | 39/46 (SW480, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.521×** | -9.0 | 1e-17 | 37/46 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.558×** | -8.6 | 6e-16 | 33/46 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.604×** | -7.1 | 6e-11 | 30/46 (SW480, NCI-H1573, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.408×** | -6.9 | 3e-10 | 33/46 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.640×** | -6.3 | 1e-08 | 35/46 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.749×** | -6.0 | 9e-08 | 28/46 (CHP-212, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.461×** | -5.9 | 1e-07 | 33/46 (LS 180, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.604×** | -5.4 | 2e-06 | 31/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -4.7 | 7e-05 | 29/48 (SW480, A-427, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.541×** | -4.7 | 7e-05 | 30/46 (RKO, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7093. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 217 | 0 | 19 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -23.1) |
| [[A-427 (line)]] | wt | 146 | 0 | 12 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -20.6) |
| [[HCT15 (line)]] | alt | 128 | 0 | 11 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.121× (z -18.0) |
| [[HT-29 (line)]] | alt | 79.4 | 0 | 10 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.183× (z -17.2) |
| [[J82 (line)]] | alt | 78.8 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 65.3 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -16.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -12.8) |
| [[PANC-1 (line)]] | alt | 55.0 | 1 | 9 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.89× (z +8.6) | [[Ixazomib citrate (drug)]] 5 µM 0.209× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 213 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -16.6) |
| [[KATO III (line)]] | alt | 63.9 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.168× (z -16.7) |
| [[LS 180 (line)]] | wt | 149 | 0 | 9 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 80.5 | 0 | 9 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -16.9) |
| [[LoVo (line)]] | wt | 61.3 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.192× (z -17.7) |
| [[RKO (line)]] | wt | 56.6 | 1 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.96× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.135× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.1) |
| [[SHP-77 (line)]] | alt | 78.2 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -12.0) |
| [[H4 (line)]] | wt | 53.4 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 82.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -12.4) |
| [[A549 (line)]] | wt | 43.0 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.288× (z -10.2) |
| [[BT-474 (line)]] | alt | 74.7 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 41.6 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 5 µM 0.199× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 117 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 55.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -11.7) |
| [[SNU-1 (line)]] | wt | 64.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.237× (z -9.0) |
| [[SNU-423 (line)]] | alt | 103 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -13.7) |
| [[A-172 (line)]] | wt | 91.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -11.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.369× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 71.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -21.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.395× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 80.1 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -11.7) |
| [[SW 900 (line)]] | alt | 69.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -12.6) |
| [[SW1417 (line)]] | alt | 65.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -12.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.340× (z -9.4) |
| [[A498 (line)]] | wt | 68.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -12.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.368× (z -8.9) |
| [[CHP-212 (line)]] | wt | 87.6 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.210× (z -11.6) |
| [[COLO 205 (line)]] | alt | 40.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 41.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.298× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 36.0 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.328× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 100 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.279× (z -8.9) |
| [[HOP62 (line)]] | alt | 46.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.31× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 89.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 32.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.01× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 56.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -10.8) |
| [[SW 1271 (line)]] | alt | 84.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0984× (z -9.2) |
| [[AN3 CA (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.58 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7093), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGGY]] | +0.66 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[WWOX]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[PCNX2]] | +0.57 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[SERBP1]] | +0.55 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[USP9X]] | +0.55 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[PMFBP1]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[WWC3]] | +0.54 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[CLYBL]] | +0.54 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[TES]] | +0.51 | +0.37 / +0.54 | both halves | 9e-05 |  |
| [[DHX9]] | +0.51 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[C1QTNF3-AMACR]] | +0.50 | +0.41 / +0.40 | both halves | 4e-05 |  |
| [[GALNT10]] | +0.50 | +0.34 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLE1]] | -0.59 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[MFSD8]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[GTF3C5]] | -0.56 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[IL17RA]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ZFYVE21]] | -0.54 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[RABEP2]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ZNF500]] | -0.54 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[C8orf76]] | -0.52 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[TXNL4B]] | -0.51 | -0.29 / -0.31 | both halves | 3e-04 |  |
| [[COG7]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[FAHD2A]] | -0.50 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[RAB5B]] | -0.50 | -0.39 / -0.54 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCA7L]] | B | CDCA7L activity raises AIG1's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without CDCA7L | 0.042 | ⚠ within organs, on part of the lines |
| [[NBEA]] | B | NBEA activity raises AIG1's level | lines that do not express NBEA (7) vs lines expressing it (43) | 1.47× lower at baseline in the lines without NBEA | 0.046 | ⚠ within organs, on part of the lines; co-absent genes; also absent: HDGFL3, HLTF, FERMT2 |
| [[DNAH14]] | B | DNAH14 activity raises AIG1's level | lines that do not express DNAH14 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without DNAH14 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF790, ENSG00000289516; its own permutation p |
| [[PCNX2]] | B | PCNX2 activity raises AIG1's level | lines that do not express PCNX2 (8) vs lines expressing it (42) | 1.38× lower at baseline in the lines without PCNX2 | 0.097 | ⚠ within organs, on part of the lines; also absent: NAALADL2, PLEKHA5, KLHL29; maybe low, not absent |
| [[CYP2U1]] | C | CYP2U1 activity raises AIG1's level | lines that do not express CYP2U1 (4) vs lines expressing it (46) | 1.57× lower at baseline in the lines without CYP2U1 | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **-** arm (projection on the module's main direction -0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-15.4, 22.9); signed map (9.4, -11.1). **Vector** length 91.2, 28.7% of its response variance represented; |z| ≥ 3 in 1,450 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +8.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.4 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.0 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.8 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.8 | -15.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.9 | -10.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.7 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.1 | -14.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.1 | -9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -0.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -4.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.3 | -1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | androgen induced 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.2 — chr6:143,060,496-143,341,058 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ95L4.1, AIG-1, FLJ10485 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVV5](https://www.uniprot.org/uniprotkb/Q9NVV5) (Androgen-induced gene 1 protein):

> Hydrolyzes bioactive fatty-acid esters of hydroxy-fatty acids (FAHFAs), but not other major classes of lipids. Show a preference for FAHFAs with branching distal from the carboxylate head group of the lipids.

**Summary**, from NCBI Gene [51390](https://www.ncbi.nlm.nih.gov/gene/51390):

> Enables hydrolase activity. Involved in long-chain fatty acid catabolic process. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21607](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21607) · Entrez [51390](https://www.ncbi.nlm.nih.gov/gene/51390) · UniProt [Q9NVV5](https://www.uniprot.org/uniprotkb/Q9NVV5) · Ensembl [ENSG00000146416](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146416)

## Data

Gene col 7093: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7093); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7093, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7093]; `tensor/DDL_lfc|DDL_z.npy` [7093]; `embed/gene_vectors.npy` [7093]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7093 or target_col == 7093). Every well: [[AIG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AIG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
