---
symbol: "HMGCL"
type: "gene"
col: 3893
ensembl_id: "ENSG00000117305"
name: "3-hydroxy-3-methylglutaryl-CoA lyase"
location: "1p36.11"
module: 4
arm: "-"
pooled_cpm: 29.32
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 21
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# HMGCL

*3-hydroxy-3-methylglutaryl-CoA lyase* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +8.5, q 1e-14, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.382× (z -15.0, q 0e+00, down in 40 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.236× (z -12.2, q 7e-32, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF160]] (+0.71, fdr 7e-06), [[ZKSCAN1]] (+0.71, fdr 7e-06), [[ZC3H6]] (+0.70, fdr 7e-06); moves opposite to [[AGPS]] (-0.68, fdr 7e-06), [[TFDP1]] (-0.67, fdr 7e-06), [[USP14]] (-0.67, fdr 7e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3893.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +8.5 | 1e-14 | 34/47 (AsPC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 0.002 | 24/47 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.008 | 19/48 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.23×** | +3.4 | 0.089 | 13/48 (CFPAC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.22× | +3.3 | 0.10 | 12/48 (KATO III, HOP62, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.23× | +3.3 | 0.11 | 22/48 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.31× | +3.2 | 0.12 | 14/46 (A-427, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.21× | +3.1 | 0.13 | 16/48 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | 1.42× | +3.0 | 0.16 | 10/45 (LS 180, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3893.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.382×** | -15.0 | 0e+00 | 40/47 (SNU-423, NCI-H23, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.236×** | -12.2 | 7e-32 | 41/46 (C32, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.237×** | -12.2 | 9e-32 | 42/48 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.612×** | -7.9 | 4e-13 | 27/44 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.624×** | -7.6 | 4e-12 | 35/48 (SNU-423, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.626×** | -7.5 | 4e-12 | 30/48 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.637×** | -7.3 | 3e-11 | 32/48 (HCT15, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -6.5 | 7e-09 | 20/33 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.715×** | -5.1 | 2e-05 | 27/48 (HT-29, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.739×** | -4.9 | 7e-05 | 24/48 (SW480, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.739×** | -4.6 | 3e-04 | 23/47 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.745×** | -4.5 | 3e-04 | 24/48 (PANC-1, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.737×** | -4.5 | 3e-04 | 21/39 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.590×** | -4.4 | 4e-04 | 19/41 (J82, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.771×** | -4.2 | 0.001 | 17/48 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.805×** | -3.5 | 0.016 | 17/48 (LS 180, SW480, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.805×** | -3.5 | 0.016 | 14/48 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.684×** | -3.2 | 0.039 | 13/46 (SK-MEL-2, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3893. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 38.9 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.159× (z -14.5) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.122× (z -9.0) |
| [[SNU-423 (line)]] | alt | 43.5 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0287× (z -30.6) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.131× (z -9.5) |
| [[Hs 766T (line)]] | wt | 58.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0526× (z -24.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 31.9 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.133× (z -17.5) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.153× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 22.7 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.212× (z -13.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.365× (z -9.3) |
| [[PANC-1 (line)]] | alt | 43.1 | 0 | 4 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0813× (z -16.2) |
| [[CFPAC-1 (line)]] | alt | 40.9 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.315× (z -9.7) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.122× (z -9.6) |
| [[HCT15 (line)]] | alt | 57.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.304× (z -8.5) |
| [[HS-578T (line)]] | alt | 37.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0340× (z -27.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.359× (z -8.5) |
| [[A-427 (line)]] | wt | 26.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0583× (z -11.3) |
| [[C-33 A (line)]] | alt | 48.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0977× (z -15.4) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 27.1 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0743× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 29.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0873× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 31.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0618× (z -20.7) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 41.2 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +9.6) | — |
| [[C32 (line)]] | wt | 31.3 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0281× (z -13.2) |
| [[COLO 205 (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -9.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 27.8 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.115× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 42.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -13.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.297× (z -11.0) ⚠ toxic |
| [[HT-29 (line)]] | alt | 27.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.121× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.184× (z -10.1) ⚠ toxic |
| [[KATO III (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -10.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.267× (z -10.4) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +10.8) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 27.4 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0613× (z -10.1) |
| [[A-172 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3893), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF160]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[ZKSCAN1]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[ZC3H6]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[TRNAU1AP]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[NDUFC1]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[MITD1]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[CCS]] | +0.65 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[ZBTB25]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[EXOC1]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[POLR1H]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[TERF2IP]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[BET1]] | +0.64 | +0.68 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGPS]] | -0.68 | -0.66 / -0.66 | both halves | 7e-06 | pathway: Peroxisomal protein import |
| [[TFDP1]] | -0.67 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[USP14]] | -0.67 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[HERC2]] | -0.64 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.63 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[YWHAQ]] | -0.62 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[TMX3]] | -0.62 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[RPRD1A]] | -0.62 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[NCK2]] | -0.62 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[CHCHD6]] | -0.62 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[SPATA5]] | -0.61 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[CCT2]] | -0.61 | -0.51 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.679). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.7, -33.0); signed map (-4.3, 3.1). **Vector** length 108, 28.0% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +5.2 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +2.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.4 | -15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | -6.3 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.1 | -7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.7 | -12.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.3 | -4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | 3-hydroxy-3-methylglutaryl-CoA lyase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:23,801,885-23,838,620 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HL, HMGCL1 |
| Gene groups (HGNC) | 3-hydroxy-3-methylglutarate-CoA lyase family |
| Hallmark sets | PEROXISOME, FATTY_ACID_METABOLISM |
| Reactome | 5 pathways, smallest: Synthesis of Ketone Bodies; Ketone body metabolism; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [P35914](https://www.uniprot.org/uniprotkb/P35914) (Hydroxymethylglutaryl-CoA lyase, mitochondrial):

> Mitochondrial 3-hydroxy-3-methylglutaryl-CoA lyase that catalyzes a cation-dependent cleavage of (S)-3-hydroxy-3-methylglutaryl-CoA into acetyl-CoA and acetoacetate, a key step in ketogenesis. Terminal step in leucine catabolism. Ketone bodies (beta-hydroxybutyrate, acetoacetate and acetone) are essential as an alternative source of energy to glucose, as lipid precursors and as regulators of metabolism.

**Summary**, from NCBI Gene [3155](https://www.ncbi.nlm.nih.gov/gene/3155):

> The protein encoded by this gene belongs to the HMG-CoA lyase family. It is a mitochondrial enzyme that catalyzes the final step of leucine degradation and plays a key role in ketone body formation. Mutations in this gene are associated with HMG-CoA lyase deficiency. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:5005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5005) · Entrez [3155](https://www.ncbi.nlm.nih.gov/gene/3155) · UniProt [P35914](https://www.uniprot.org/uniprotkb/P35914) · Ensembl [ENSG00000117305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117305)

## Data

Gene col 3893: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3893); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3893, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3893]; `tensor/DDL_lfc|DDL_z.npy` [3893]; `embed/gene_vectors.npy` [3893]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3893 or target_col == 3893). Every well: [[HMGCL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGCL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
