---
symbol: "TKT"
type: "gene"
col: 8812
ensembl_id: "ENSG00000163931"
name: "transketolase"
location: "3p21.1"
module: 86
arm: "+"
pooled_cpm: 156.76
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# TKT

*transketolase* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.76× (z +13.1, q 3e-36, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.61× (z +6.1, q 1e-07, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.724× (z -5.9, q 3e-06, down in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.746× (z -5.3, q 3e-05, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (SHP-77 0.360×, A-427 0.349×, HT-29 0.461×, SNU-1 0.393×, …); [[Selinexor (drug)]] 5 µM in 2 lines (KATO III 0.544×, LS 180 0.544×; ⚠ cell-cycle shift, explains ~48% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDH1]] (+0.62, fdr 1e-05), [[SCD]] (+0.62, fdr 1e-05), [[SLC25A6]] (+0.60, fdr 2e-05); moves opposite to [[MED18]] (-0.62, fdr 1e-05), [[ZNF101]] (-0.57, fdr 3e-05), [[ZNF274]] (-0.56, fdr 1e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8812.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +13.1 | 3e-36 | 49/49 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +10.3 | 3e-22 | 44/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +7.9 | 4e-13 | 41/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +7.7 | 2e-12 | 42/45 (NCI-H2030, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +6.1 | 1e-07 | 37/48 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +6.0 | 1e-07 | 43/48 (HEC-1-A, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +5.9 | 3e-07 | 40/48 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +4.6 | 3e-04 | 29/48 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.42×** | +4.5 | 4e-04 | 38/47 (H4, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.36×** | +3.9 | 0.004 | 34/48 (RKO, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +3.9 | 0.004 | 29/48 (NCI-H1792, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.6 | 0.014 | 30/45 (HEC-1-A, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +3.5 | 0.021 | 28/48 (RKO, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 1.19× | +3.3 | 0.046 | 20/48 (NCI-H23, C32, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | 1.19× | +3.1 | 0.065 | 20/49 (NCI-H23, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8812.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (SHP-77 0.360×, A-427 0.349×, HT-29 0.461×, SNU-1 0.393×, …); [[Selinexor (drug)]] 5 µM in 2 lines (KATO III 0.544×, LS 180 0.544×; ⚠ cell-cycle shift, explains ~48% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.724×** | -5.9 | 3e-06 | 37/48 (KATO III, LS 180, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.746×** | -5.3 | 3e-05 | 28/48 (SHP-77, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.668×** | -5.2 | 4e-05 | 41/48 (A498, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.767×** | -3.4 | 0.095 | 26/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.778× | -3.1 | 0.23 | 29/49 (CFPAC-1, NCI-H1573, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8812. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 97.8 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.86× (z +9.9) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 3.10× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 196 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -12.6) |
| [[KATO III (line)]] | alt | 154 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -10.2) |
| [[LoVo (line)]] | wt | 152 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.42× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 140 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.32× (z +8.7) | [[Selinexor (drug)]] 5 µM 0.544× (z -8.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H1792 (line)]] | alt | 124 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.62× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 215 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +14.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 341 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.44× (z +12.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 204 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 90.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 127 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +11.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 215 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 79.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +12.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 157 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 73.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.38× (z +13.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 124 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.56× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 94.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 180 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -15.5) |
| [[SK-MEL-2 (line)]] | alt | 212 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -9.8) |
| [[SW480 (line)]] | alt | 97.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +12.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 89.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -15.1) |
| [[A498 (line)]] | wt | 347 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 79.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.55× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 71.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.68× (z +12.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 219 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.34× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 218 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 174 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 162 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 106 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +13.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 155 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 137 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.4) |
| [[SNU-423 (line)]] | alt | 259 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 154 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 72.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 97.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 144 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8812), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDH1]] | +0.62 | +0.67 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS; STRING 689 |
| [[SCD]] | +0.62 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SLC25A6]] | +0.60 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[PGD]] | +0.59 | +0.53 / +0.65 | both halves | 1e-05 | pathway: Cellular response to chemical stress; STRING 975 |
| [[PIR]] | +0.58 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[NXPE3]] | +0.58 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[FXR1]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[FDFT1]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 | STRING 499 |
| [[HNRNPA1]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[TALDO1]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS; STRING 999 |
| [[CCNG1]] | +0.56 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[LAMP2]] | +0.55 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED18]] | -0.62 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[ZNF101]] | -0.57 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[ZNF274]] | -0.56 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[DGUOK]] | -0.54 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[ZCCHC3]] | -0.54 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[ZNF75A]] | -0.54 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CHAMP1]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ZNF518A]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ZNF200]] | -0.54 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[TJAP1]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[HELQ]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[LINC00467]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.510). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.0, -51.6); signed map (-51.3, 30.3). **Vector** length 120, 43.7% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.4 | +7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.9 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.9 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.3 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.1 | +0.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.8 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +6.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -9.5 | -1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -7.7 | -5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.4 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.8 | -2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.7 | -0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | transketolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:53,224,712-53,256,052 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 9 pathways, smallest: NFE2L2 regulates pentose phosphate pathway genes; Pentose phosphate pathway; Integration of energy metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P29401](https://www.uniprot.org/uniprotkb/P29401) (Transketolase):

> Catalyzes the transfer of a two-carbon ketol group from a ketose donor to an aldose acceptor, via a covalent intermediate with the cofactor thiamine pyrophosphate. Thus, catalyzes the reversible transfer of a two-carbon ketol group from sedoheptulose-7-phosphate to glyceraldehyde-3-phosphate, producing xylulose-5-phosphate and ribose-5-phosphate. The phosphate group of the substrate plays a role in stabilizing the substrate-thiamine intermediate while preventing the formation of the reactive …

**Summary**, from NCBI Gene [7086](https://www.ncbi.nlm.nih.gov/gene/7086):

> This gene encodes a thiamine-dependent enzyme which plays a role in the channeling of excess sugar phosphates to glycolysis in the pentose phosphate pathway. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:11834](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11834) · Entrez [7086](https://www.ncbi.nlm.nih.gov/gene/7086) · UniProt [P29401](https://www.uniprot.org/uniprotkb/P29401) · Ensembl [ENSG00000163931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163931)

## Data

Gene col 8812: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8812); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8812, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8812]; `tensor/DDL_lfc|DDL_z.npy` [8812]; `embed/gene_vectors.npy` [8812]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8812 or target_col == 8812). Every well: [[TKT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TKT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
