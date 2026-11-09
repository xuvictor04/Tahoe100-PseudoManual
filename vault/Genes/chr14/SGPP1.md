---
symbol: "SGPP1"
type: "gene"
col: 4771
ensembl_id: "ENSG00000126821"
name: "sphingosine-1-phosphate phosphatase 1"
location: "14q23.2"
module: 163
arm: "+"
pooled_cpm: 42.77
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# SGPP1

*sphingosine-1-phosphate phosphatase 1* — 14q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.02× (z +14.3, q 2e-43, up in 38 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.94× (z +13.5, q 5e-39, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.890× (z -8.1, q 3e-13, down in 3 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 0.802× (z -4.5, q 0.002, down in 19 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.163×, C-33 A 0.281×, AN3 CA 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 0.319×, NCI-H1792 0.416×, A549 0.579×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.148×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRLF3]] (+0.67, fdr 7e-06), [[SLC27A4]] (+0.67, fdr 7e-06), [[EPS15]] (+0.65, fdr 1e-05); moves opposite to [[DARS1]] (-0.60, fdr 1e-05), [[CHM]] (-0.58, fdr 1e-05), [[RBM23]] (-0.57, fdr 3e-05).
> It is in [[Module 163]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4771.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +14.3 | 2e-43 | 38/46 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.94×** | +13.5 | 5e-39 | 44/47 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +12.7 | 1e-34 | 44/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +11.6 | 5e-29 | 40/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +10.8 | 5e-25 | 31/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.66×** | +10.3 | 7e-23 | 40/46 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +9.8 | 6e-21 | 40/47 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +9.5 | 1e-19 | 38/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +9.4 | 2e-19 | 37/47 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +8.4 | 3e-15 | 30/47 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +8.1 | 2e-14 | 27/46 (LoVo, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +8.1 | 4e-14 | 30/46 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.98×** | +7.3 | 1e-11 | 35/47 (NCI-H23, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.36×** | +6.0 | 8e-08 | 30/46 (NCI-H460, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +5.4 | 2e-06 | 25/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +5.2 | 5e-06 | 23/47 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +5.1 | 1e-05 | 21/47 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +4.8 | 4e-05 | 19/46 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +4.2 | 7e-04 | 12/47 (NCI-H2030, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4771.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.163×, C-33 A 0.281×, AN3 CA 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 0.319×, NCI-H1792 0.416×, A549 0.579×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.148×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.890× | -8.1 | 3e-13 | 3/48 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.802×** | -4.5 | 0.002 | 19/47 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.720×** | -4.4 | 0.002 | 18/47 (AN3 CA, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.802×** | -4.3 | 0.002 | 20/40 (SNU-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.877× | -3.8 | 0.017 | 13/47 (NCI-H2347, LS 180, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.886× | -3.5 | 0.042 | 9/47 (CHP-212, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.5 | 0.045 | 11/47 (SNU-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.851× | -3.3 | 0.070 | 11/47 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.857× | -3.2 | 0.10 | 7/47 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4771. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 42.8 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.04× (z +12.5) | [[Selinexor (drug)]] 5 µM 0.417× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 49.5 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.95× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +10.7) | — |
| [[SW480 (line)]] | alt | 37.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +11.2) | — |
| [[BT-474 (line)]] | alt | 61.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 38.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 30.6 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.32× (z +8.9) | — |
| [[A-172 (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 59.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 70.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 67.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 31.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 37.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.28× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 46.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 56.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 56.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.69× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 57.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +9.2) | — |
| [[RKO (line)]] | wt | 56.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 87.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -15.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 74.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4771), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRLF3]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[SLC27A4]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[EPS15]] | +0.65 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.63 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[SERAC1]] | +0.62 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[RAP1A]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SRPK2]] | +0.62 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[RNF38]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[STIM1]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[CYTH3]] | +0.61 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[SVIL-AS1-1]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[UNC13B]] | +0.60 | +0.70 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DARS1]] | -0.60 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[CHM]] | -0.58 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[RBM23]] | -0.57 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[PAN2]] | -0.56 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[SF3B1]] | -0.55 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[CYB5D1]] | -0.54 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[INTS2]] | -0.54 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[FCF1]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ZNF646]] | -0.53 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[FBXO38]] | -0.53 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[RLIM]] | -0.52 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[PES1]] | -0.52 | -0.59 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.3, -0.5); signed map (-44.1, -6.3). **Vector** length 102, 26.4% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +3.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.3 | +8.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.2 | +4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.2 | +10.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +7.3 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.3 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.4 | -2.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | +1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -4.5 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | sphingosine-1-phosphate phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.2 — chr14:63,684,216-63,728,065 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sphingosine-1-phosphate phosphatases |
| Reactome | 3 pathways, smallest: Sphingolipid catabolism; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BX95](https://www.uniprot.org/uniprotkb/Q9BX95) (Sphingosine-1-phosphate phosphatase 1):

> Specifically dephosphorylates sphingosine 1-phosphate (S1P), dihydro-S1P, and phyto-S1P. Does not act on ceramide 1-phosphate, lysophosphatidic acid or phosphatidic acid. Sphingosine-1-phosphate phosphatase activity is needed for efficient recycling of sphingosine into the sphingolipid synthesis pathway. Regulates the intracellular levels of the bioactive sphingolipid metabolite S1P that regulates diverse biological processes acting both as an extracellular receptor ligand or as an …

**Summary**, from NCBI Gene [81537](https://www.ncbi.nlm.nih.gov/gene/81537):

> Sphingosine-1-phosphate (S1P) is a bioactive sphingolipid metabolite that regulates diverse biologic processes. SGPP1 catalyzes the degradation of S1P via salvage and recycling of sphingosine into long-chain ceramides (Mandala et al., 2000 [PubMed 10859351]; Le Stunff et al., 2007 [PubMed 17895250]).[supplied by OMIM, Jun 2009]

**Accessions** — [HGNC:17720](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17720) · Entrez [81537](https://www.ncbi.nlm.nih.gov/gene/81537) · UniProt [Q9BX95](https://www.uniprot.org/uniprotkb/Q9BX95) · Ensembl [ENSG00000126821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126821)

## Data

Gene col 4771: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4771); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4771, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4771]; `tensor/DDL_lfc|DDL_z.npy` [4771]; `embed/gene_vectors.npy` [4771]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4771 or target_col == 4771). Every well: [[SGPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
