---
symbol: "PKP2"
type: "gene"
col: 646
ensembl_id: "ENSG00000057294"
name: "plakophilin 2"
location: "12p11.21"
module: 97
arm: "+"
pooled_cpm: 62.67
n_lines_expressing: 34
n_dd_up: 20
n_dd_down: 22
n_dd_up_clean: 18
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 36
direction_downstream: 25
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# PKP2

*plakophilin 2* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.66× (z +9.8, q 6e-20, up in 19 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.543× (z -16.8, q 0e+00, down in 29 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNS4]] (+0.72, fdr 7e-06), [[KIF13B]] (+0.64, fdr 1e-05), [[PDE9A]] (+0.64, fdr 1e-05); moves opposite to [[ZSCAN31]] (-0.57, fdr 1e-05), [[LINC02100]] (-0.54, fdr 5e-05), [[HTATIP2]] (-0.52, fdr 1e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 36 arrows point to it, the strongest [[B3GNT3]] → it (grade B ⚠); 25 go from it, the strongest it → [[BCL2L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 646.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +9.8 | 6e-20 | 19/32 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +9.1 | 2e-17 | 26/32 (SW1417, A-427, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +8.1 | 1e-13 | 17/32 (HOP62, A-172, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.44×** | +7.1 | 2e-10 | 14/32 (SNU-423, SW 900, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.40×** | +6.3 | 3e-08 | 15/33 (SW 900, SNU-423, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.84×** | +6.2 | 5e-08 | 15/33 (A-427, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.36×** | +6.0 | 2e-07 | 17/32 (SNU-423, Hs 766T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.38×** | +5.9 | 2e-07 | 17/32 (SW 900, SNU-423, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.35×** | +5.8 | 3e-07 | 18/32 (A-427, NCI-H23, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.35×** | +5.4 | 4e-06 | 15/32 (SW 900, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.30×** | +5.1 | 2e-05 | 15/32 (SNU-423, SW 900, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.29×** | +5.0 | 3e-05 | 15/32 (A-427, NCI-H23, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +5.0 | 3e-05 | 17/32 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 1e-04 | 15/33 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +4.6 | 2e-04 | 17/32 (SNU-423, Hs 766T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.25×** | +4.4 | 5e-04 | 13/32 (SW 900, Hs 766T, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.3 | 5e-04 | 13/32 (Hs 766T, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 646.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -16.8 | 0e+00 | 29/33 (HCT15, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.610×** | -13.6 | 2e-39 | 23/32 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.532×** | -12.3 | 3e-32 | 28/32 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.534×** | -12.2 | 7e-32 | 28/32 (LS 180, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.701×** | -9.8 | 2e-20 | 24/32 (CFPAC-1, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.635×** | -8.8 | 1e-16 | 25/32 (LoVo, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.628×** | -8.5 | 1e-15 | 24/32 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -8.2 | 2e-14 | 20/32 (RKO, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.660×** | -7.7 | 6e-13 | 21/32 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -7.1 | 6e-11 | 22/32 (SW 900, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -6.4 | 7e-09 | 23/34 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.720×** | -6.4 | 9e-09 | 21/32 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.727×** | -6.2 | 3e-08 | 17/32 (LoVo, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -6.0 | 8e-08 | 3/33 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.589×** | -5.4 | 3e-06 | 17/30 (HCT15, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.791×** | -4.5 | 2e-04 | 15/32 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.658×** | -4.2 | 7e-04 | 16/33 (LoVo, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.858× | -4.2 | 8e-04 | 14/32 (SNU-423, BT-474, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.675×** | -4.0 | 0.002 | 12/32 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 646. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 406 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0985× (z -23.2) |
| [[LS 180 (line)]] | wt | 323 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -15.7) |
| [[NCI-H1573 (line)]] | alt | 128 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0984× (z -32.2) |
| [[SW 900 (line)]] | alt | 73.0 | 5 | 3 | [[Dexamethasone (drug)]] 5 µM 3.16× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -15.0) |
| [[RKO (line)]] | wt | 40.3 | 1 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.161× (z -14.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.174× (z -13.9) |
| [[SNU-423 (line)]] | alt | 35.8 | 6 | 1 | [[Clobetasol propionate (drug)]] 5 µM 3.71× (z +9.3) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.414× (z -8.8) |
| [[A-427 (line)]] | wt | 45.7 | 3 (2 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.94× (z +10.5) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.89× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -11.5) |
| [[HCT15 (line)]] | alt | 204 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 28.9 | 3 (2 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 3.61× (z +9.8) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Belinostat (drug)]] 5 µM 3.39× (z +9.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -11.4) |
| [[SW480 (line)]] | alt | 111 | 0 | 5 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.472× (z -11.8) |
| [[BT-474 (line)]] | alt | 76.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -18.3) |
| [[CFPAC-1 (line)]] | alt | 82.9 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -13.8) |
| [[COLO 205 (line)]] | alt | 34.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -10.9) |
| [[HT-29 (line)]] | alt | 62.8 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.321× (z -10.5) |
| [[KATO III (line)]] | alt | 142 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 40.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -13.0) |
| [[SW48 (line)]] | wt | 41.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 48.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 55.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -13.5) |
| [[A549 (line)]] | wt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 50.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -12.9) |
| [[HOP62 (line)]] | alt | 18.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.93× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 59.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 83.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.202× (z -8.6) ⚠ toxic |
| [[SW1417 (line)]] | alt | 56.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -11.2) |
| [[A-172 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.95 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.97 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.94 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.52 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.54 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.65 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.85 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 66.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 646), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNS4]] | +0.72 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[KIF13B]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PDE9A]] | +0.64 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[TBC1D8]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[ITGB4]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ABLIM2]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[P2RY2]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[SH2D3A]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[MT1X]] | +0.59 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[PPARG]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[FRY]] | +0.58 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[B3GNT3]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN31]] | -0.57 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[LINC02100]] | -0.54 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[HTATIP2]] | -0.52 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[BBOX1-AS1]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[NEK11]] | -0.51 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[ATE1OSP]] | -0.51 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[PRRT2]] | -0.51 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[APOBEC3F]] | -0.50 | -0.43 / -0.37 | both halves | 9e-05 |  |
| [[TTC6]] | -0.50 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[BTN3A3]] | -0.50 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[ZFHX2-AS1]] | -0.50 | -0.45 / -0.20 | both halves | 7e-04 |  |
| [[SUPT7L]] | -0.49 | -0.47 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 27, C 9. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GNT3]] | B | B3GNT3 activity raises PKP2's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.81× lower at baseline in the lines without B3GNT3 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[HS3ST1]] | B | HS3ST1 activity raises PKP2's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 4.05× lower at baseline in the lines without HS3ST1 | 0.003 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[KIAA0040]] | B | KIAA0040 activity raises PKP2's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 3.01× lower at baseline in the lines without KIAA0040 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises PKP2's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.43× lower at baseline in the lines without TMPRSS4 | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[SH2D3A]] | B | SH2D3A activity raises PKP2's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.51× lower at baseline in the lines without SH2D3A | 0.021 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[SCEL]] | B | SCEL activity raises PKP2's level | lines that do not express SCEL (35) vs lines expressing it (15) | 3.46× lower at baseline in the lines without SCEL | 0.022 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[GSDMC]] | B | GSDMC activity raises PKP2's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 2.65× lower at baseline in the lines without GSDMC | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[MCF2L]] | B | MCF2L activity raises PKP2's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.79× lower at baseline in the lines without MCF2L | 0.023 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[ATP2C2]] | B | ATP2C2 activity raises PKP2's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 4.14× lower at baseline in the lines without ATP2C2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[NR3C1]] | B | NR3C1 activity raises PKP2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[SLC6A14]] | B | SLC6A14 activity raises PKP2's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 3.53× lower at baseline in the lines without SLC6A14 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[RAPGEF5]] | B | RAPGEF5 activity raises PKP2's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.79× lower at baseline in the lines without RAPGEF5 | 0.036 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 16, C 9. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2L1]] | B | PKP2 activity raises BCL2L1's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.98× lower at baseline in the lines without PKP2 | 0.005 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[CORO2A]] | B | PKP2 activity strengthens CORO2A's drug response | lines that do not express PKP2 (14) vs lines expressing it (31) | the lines without PKP2 respond 0.58× as strongly (z diff +1.92); strongest at Ouabain (Octahydrate) 0.5 µM: 0.68x vs 0.37x (z diff +3.8) | 0.012 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN; target measured in part of the lines; artifact flags |
| [[TMC6]] | B | PKP2 activity raises TMC6's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 3.12× lower at baseline in the lines without PKP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[PDE9A]] | B | PKP2 activity raises PDE9A's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.88× lower at baseline in the lines without PKP2 | 0.017 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[BAIAP2L1]] | B | PKP2 activity raises BAIAP2L1's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.48× lower at baseline in the lines without PKP2 | 0.021 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[PRKACB]] | B | PKP2 activity lowers PRKACB's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.27× higher at baseline in the lines without PKP2 | 0.023 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[ACOT11]] | B | PKP2 activity raises ACOT11's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.52× lower at baseline in the lines without PKP2 | 0.026 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[ITGA6]] | B | PKP2 activity raises ITGA6's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.38× lower at baseline in the lines without PKP2 | 0.034 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[CORO2A]] | B | PKP2 activity raises CORO2A's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.00× lower at baseline in the lines without PKP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[ARHGEF6]] | B | PKP2 activity lowers ARHGEF6's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.70× higher at baseline in the lines without PKP2 | 0.055 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[B3GNT3]] | B | PKP2 activity raises B3GNT3's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 3.41× lower at baseline in the lines without PKP2 | 0.055 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[PTK2B]] | B | PKP2 activity raises PTK2B's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.25× lower at baseline in the lines without PKP2 | 0.063 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.8, 49.1); signed map (11.1, 33.7). **Vector** length 125, 35.3% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.4 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.3 | +5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.0 | +5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.6 | +9.1 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.6 | +7.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.6 | +3.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.5 | +2.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +3.5 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.8 | -9.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.6 | -12.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -16.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -12.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.3 | -2.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.2 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | plakophilin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.21 — chr12:32,790,745-32,896,798 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Armadillo repeat containing; Plakophilins |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99959](https://www.uniprot.org/uniprotkb/Q99959) (Plakophilin-2):

> A component of desmosome cell-cell junctions which are required for positive regulation of cellular adhesion. Regulates focal adhesion turnover resulting in changes in focal adhesion size, cell adhesion and cell spreading, potentially via transcriptional modulation of beta-integrins. Required to maintain gingival epithelial barrier function. Important component of the desmosome that is also required for localization of desmosome component proteins such as DSC2, DSG2 and JUP to the desmosome …

**Summary**, from NCBI Gene [5318](https://www.ncbi.nlm.nih.gov/gene/5318):

> This gene encodes a member of the arm-repeat (armadillo) and plakophilin gene families. Plakophilin proteins contain numerous armadillo repeats, localize to cell desmosomes and nuclei, and participate in linking cadherins to intermediate filaments in the cytoskeleton. This gene may regulate the signaling activity of beta-catenin and is required to maintain transcription of genes that control intracellular calcium cycling including ryanodine receptor 2, ankyrin-B, triadin, and calcium channel, …

**Accessions** — [HGNC:9024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9024) · Entrez [5318](https://www.ncbi.nlm.nih.gov/gene/5318) · UniProt [Q99959](https://www.uniprot.org/uniprotkb/Q99959) · Ensembl [ENSG00000057294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000057294)

## Data

Gene col 646: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 646); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 646, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 646]; `tensor/DDL_lfc|DDL_z.npy` [646]; `embed/gene_vectors.npy` [646]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 646 or target_col == 646). Every well: [[PKP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
