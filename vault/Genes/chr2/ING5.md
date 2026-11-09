---
symbol: "ING5"
type: "gene"
col: 9642
ensembl_id: "ENSG00000168395"
name: "inhibitor of growth family member 5"
location: "2q37.3"
module: 38
arm: "+"
pooled_cpm: 37.64
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# ING5

*inhibitor of growth family member 5* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +12.3, q 6e-32, up in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 3.81×, NCI-H460 2.04×, A549 2.41×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 2.84×, NCI-H1573 2.59×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 3.45×; ⚠ cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.499× (z -12.8, q 8e-35, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS51]] (+0.68, fdr 1e-05), [[ACAD9]] (+0.65, fdr 7e-06), [[SFXN2]] (+0.64, fdr 1e-05); moves opposite to [[COMMD8]] (-0.59, fdr 4e-05), [[TMEM179B]] (-0.52, fdr 4e-05), [[MSRB2]] (-0.52, fdr 2e-04).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9642.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 3.81×, NCI-H460 2.04×, A549 2.41×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 2.84×, NCI-H1573 2.59×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 3.45×; ⚠ cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +12.3 | 6e-32 | 38/48 (AsPC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +6.2 | 2e-07 | 20/38 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.4 | 0.002 | 20/47 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.20× | +3.5 | 0.056 | 15/48 (A498, NCI-H460, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.056 | 11/48 (HT-29, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.13 | 10/48 (MIA PaCa-2, NCI-H460, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.14 | 17/48 (SNU-423, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9642.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.499×** | -12.8 | 8e-35 | 39/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.531×** | -12.1 | 2e-31 | 40/48 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.588×** | -10.2 | 4e-22 | 32/48 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.627×** | -8.9 | 6e-17 | 36/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.806×** | -5.8 | 7e-07 | 26/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.743×** | -5.7 | 1e-06 | 26/47 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.820×** | -5.4 | 6e-06 | 24/47 (RKO, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.763×** | -5.2 | 2e-05 | 28/48 (H4, hTERT-HPNE, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.780×** | -4.7 | 1e-04 | 25/48 (SNU-1, PANC-1, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.623×** | -4.7 | 1e-04 | 22/48 (BT-474, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -4.6 | 2e-04 | 19/48 (HCT15, KATO III, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.792×** | -4.4 | 4e-04 | 22/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.810×** | -4.0 | 0.002 | 22/48 (SW 900, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.814×** | -3.9 | 0.003 | 22/48 (SK-MEL-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.832×** | -3.5 | 0.018 | 17/48 (A549, HS-578T, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.886× | -3.2 | 0.037 | 14/48 (COLO 205, MIA PaCa-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.733×** | -3.1 | 0.051 | 13/48 (SW480, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cyclosporin A (drug)]] 5 µM |  | 0.850× | -3.1 | 0.051 | 10/48 (AsPC-1, LoVo, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.0 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.352× (z -12.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.437× (z -9.9) |
| [[A498 (line)]] | wt | 41.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.337× (z -10.9) |
| [[A-427 (line)]] | wt | 44.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.49× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.432× (z -9.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 56.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 68.5 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.265× (z -8.9) |
| [[HS-578T (line)]] | alt | 37.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 31.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.355× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 61.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.317× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 34.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 55.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.232× (z -14.3) |
| [[A549 (line)]] | wt | 31.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 31.6 | 0 | 1 | — | [[Indacaterol (maleate) (drug)]] 0.5 µM 0.0952× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 27.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +13.5) | — |
| [[BT-474 (line)]] | alt | 33.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 25.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.307× (z -9.2) |
| [[HOP62 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.390× (z -8.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[hTERT-HPNE (line)]] | wt | 44.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.259× (z -9.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 39.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 35.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -15.1) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 53.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.325× (z -8.7) |
| [[SW1417 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 49.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS51]] | +0.68 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[ACAD9]] | +0.65 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[SFXN2]] | +0.64 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[UBAP1L]] | +0.63 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[SYCE2]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[RBM14-RBM4]] | +0.62 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[ATAD3B]] | +0.62 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TRPV1]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[TRMT1]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[TFAP2E]] | +0.59 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[NPIPB11]] | +0.59 | +0.45 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD8]] | -0.59 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[TMEM179B]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[MSRB2]] | -0.52 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[TIGD2]] | -0.51 | -0.28 / -0.60 | both halves | 3e-04 |  |
| [[HPF1]] | -0.51 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[TRIM68]] | -0.50 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[AKR1B1]] | -0.50 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[GDE1]] | -0.50 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.3, -22.3); signed map (8.4, 0.7). **Vector** length 103, 25.2% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.1 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +6.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.4 | +2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.1 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.1 | -12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.6 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -12.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | -3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | inhibitor of growth family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,687,085-241,729,478 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23842, p28ING5 |
| Gene groups (HGNC) | PHD finger proteins; Inhibitor of growth family |
| Reactome | 6 pathways, smallest: Regulation of TP53 Activity through Acetylation; HATs acetylate histones; Regulation of TP53 Activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYH8](https://www.uniprot.org/uniprotkb/Q8WYH8) (Inhibitor of growth protein 5):

> Component of the HBO1 complex, which specifically mediates acetylation of histone H3 at 'Lys-14' (H3K14ac) and, to a lower extent, acetylation of histone H4. Component of the MOZ/MORF complex which has a histone H3 acetyltransferase activity. Through chromatin acetylation it may regulate DNA replication and may function as a transcriptional coactivator. Inhibits cell growth, induces a delay in S-phase progression and enhances Fas-induced apoptosis in an INCA1-dependent manner.

**Summary**, from NCBI Gene [84289](https://www.ncbi.nlm.nih.gov/gene/84289):

> This gene encodes a tumor suppressor protein that inhibits cell growth and induces apoptosis. This protein contains a PHD-type zinc finger. It interacts with tumor suppressor p53 and p300, a component of the histone acetyl transferase complex, suggesting a role in transcriptional regulation. Alternative splicing and the use of multiple promoters and 3' terminal exons results in multiple transcript variants. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:19421](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19421) · Entrez [84289](https://www.ncbi.nlm.nih.gov/gene/84289) · UniProt [Q8WYH8](https://www.uniprot.org/uniprotkb/Q8WYH8) · Ensembl [ENSG00000168395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168395)

## Data

Gene col 9642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9642); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9642]; `tensor/DDL_lfc|DDL_z.npy` [9642]; `embed/gene_vectors.npy` [9642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9642 or target_col == 9642). Every well: [[ING5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ING5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
