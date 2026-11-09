---
symbol: "RTF2"
type: "gene"
col: 333
ensembl_id: "ENSG00000022277"
name: "replication termination factor 2"
location: "20q13.31"
module: 210
arm: "+"
pooled_cpm: 96.73
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/210"]
generated_by: "tahoemap"
---

# RTF2

*replication termination factor 2* — 20q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.98× (z +18.4, q 0e+00, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.794× (z -10.5, q 7e-23, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE4A]] (+0.72, fdr 7e-06), [[TMCO1]] (+0.69, fdr 1e-05), [[SMU1]] (+0.68, fdr 7e-06); moves opposite to [[MEMO1]] (-0.60, fdr 4e-05), [[ORAI1]] (-0.59, fdr 1e-05), [[C2orf69]] (-0.53, fdr 1e-05).
> It is in [[Module 210]], a single-armed module (tRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 333.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.98×** | +18.4 | 0e+00 | 45/49 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +14.1 | 2e-42 | 41/48 (LoVo, SHP-77, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +12.3 | 1e-32 | 42/48 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +11.7 | 1e-29 | 44/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +11.2 | 4e-27 | 38/48 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +10.1 | 6e-22 | 37/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.28×** | +8.0 | 8e-14 | 28/48 (SK-MEL-2, BT-474, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +8.0 | 8e-14 | 30/45 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.28×** | +7.9 | 2e-13 | 28/49 (A-172, PANC-1, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.26×** | +7.5 | 3e-12 | 28/48 (SW480, PANC-1, …) | inconsistent across doses | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.57×** | +7.5 | 3e-12 | 37/45 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.17× | +7.3 | 1e-11 | 25/48 (RKO, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.26×** | +7.3 | 1e-11 | 29/48 (SW480, C-33 A, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.21×** | +6.0 | 9e-08 | 24/44 (NCI-H23, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +5.4 | 3e-06 | 24/49 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +5.2 | 7e-06 | 22/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.28×** | +4.2 | 1e-03 | 15/47 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.11× | +3.1 | 0.054 | 5/48 (C-33 A, A-427, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.065 | 3/48 (NCI-H2030, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | 1.19× | +3.0 | 0.071 | 9/49 (NCI-H1792, HS-578T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 333.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.794×** | -10.5 | 7e-23 | 32/48 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.806×** | -5.6 | 5e-06 | 22/49 (CHP-212, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -4.8 | 4e-04 | 18/48 (A498, HT-29, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.817×** | -4.6 | 5e-04 | 20/48 (COLO 205, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.961× | -4.4 | 0.001 | 0/50 | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.828×** | -4.3 | 0.001 | 13/49 (RPMI-7951, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.899× | -3.4 | 0.052 | 7/48 (AsPC-1, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.901× | -3.3 | 0.060 | 10/48 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.902× | -3.3 | 0.060 | 7/48 (NCI-H661, COLO 205, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.869× | -3.2 | 0.070 | 15/48 (RPMI-7951, Hs 766T, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.875× | -3.1 | 0.11 | 7/48 (NCI-H1573, SW 1088, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 333. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 76.6 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.56× (z +11.2) | — |
| [[RKO (line)]] | wt | 86.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.03× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.448× (z -9.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 123 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.24× (z +10.9) | — |
| [[SW480 (line)]] | alt | 116 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +10.7) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.88× (z +9.9) | — |
| [[A-427 (line)]] | wt | 84.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 1.98× (z +9.5) | — |
| [[A498 (line)]] | wt | 89.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.85× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 103 | 2 | 0 | [[Auranofin (drug)]] 5 µM 1.83× (z +9.1) | — |
| [[LoVo (line)]] | wt | 57.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.20× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 66.6 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.42× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 107 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.09× (z +9.4) | — |
| [[A-172 (line)]] | wt | 64.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[AsPC-1 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 238 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.24× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 74.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.40× (z +8.9) | — |
| [[C32 (line)]] | wt | 71.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.22× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 97.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.31× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 128 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.44× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 55.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.77× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 81.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.15× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 176 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.79× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 86.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.21× (z +10.1) | — |
| [[KATO III (line)]] | alt | 113 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.89× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 81.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.73× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 65.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.05× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 74.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.08× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 153 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.40× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 144 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.03× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.80× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A549 (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 83.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 99.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 96.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 333), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE4A]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[TMCO1]] | +0.69 | +0.72 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[SMU1]] | +0.68 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[GFM2]] | +0.68 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[DDX49]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[GPN1]] | +0.65 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[PEX19]] | +0.64 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[SUDS3]] | +0.64 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[VTI1B]] | +0.64 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[DYNC1LI2]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ASCC2]] | +0.63 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[MAGOH]] | +0.62 | +0.43 / +0.68 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEMO1]] | -0.60 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[ORAI1]] | -0.59 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[C2orf69]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[ZNF706]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ZIC2]] | -0.53 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[FOXA2]] | -0.52 | -0.32 / -0.61 | both halves | 2e-04 |  |
| [[SATB2]] | -0.51 | -0.49 / -0.49 | both halves | 2e-05 |  |
| [[PPP1R35]] ⚠ | -0.50 | -0.31 / -0.61 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PSPC1]] | -0.49 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[ZNRF2P1]] | -0.49 | -0.48 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 210]] — tRNA processing; 13 genes; every member is in the + arm (projection on the module's main direction 0.823). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.8, -12.8); signed map (-31.3, -28.5). **Vector** length 109, 29.1% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.6 | +14.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.0 | +18.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.9 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +6.5 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.0 | +11.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +10.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +11.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +5.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.6 | -10.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.0 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.9 | -5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.1 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -4.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.1 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | replication termination factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.31 — chr20:56,468,585-56,519,449 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC164, CDAO5; previously C20orf43, RTFDC1 |
| Gene groups (HGNC) | Degenerate RING E3 ubiquitin ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY42](https://www.uniprot.org/uniprotkb/Q9BY42) (Replication termination factor 2):

> Replication termination factor which is a component of the elongating replisome (Probable). Required for ATR pathway signaling upon DNA damage and has a positive activity during DNA replication. Might function to facilitate fork pausing at replication fork barriers like the rDNA. May be globally required to stimulate ATR signaling after the fork stalls or encounters a lesion (Probable). Interacts with nascent DNA.

**Summary**, from NCBI Gene [51507](https://www.ncbi.nlm.nih.gov/gene/51507):

> Enables DNA binding activity. Involved in cellular response to hydroxyurea and regulation of DNA stability. Located in nucleolus; nucleoplasm; and replication fork. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15890](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15890) · Entrez [51507](https://www.ncbi.nlm.nih.gov/gene/51507) · UniProt [Q9BY42](https://www.uniprot.org/uniprotkb/Q9BY42) · Ensembl [ENSG00000022277](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000022277)

## Data

Gene col 333: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 333); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 333, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 333]; `tensor/DDL_lfc|DDL_z.npy` [333]; `embed/gene_vectors.npy` [333]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 333 or target_col == 333). Every well: [[RTF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
