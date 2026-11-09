---
symbol: "GPAM"
type: "gene"
col: 4137
ensembl_id: "ENSG00000119927"
name: "glycerol-3-phosphate acyltransferase, mitochondrial"
location: "10q25.2"
module: 33
arm: "+"
pooled_cpm: 20.03
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 13
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# GPAM

*glycerol-3-phosphate acyltransferase, mitochondrial* — 10q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.03× (z +19.7, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.667× (z -7.2, q 4e-10, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSTF2]] (+0.63, fdr 3e-05), [[HEATR6]] (+0.62, fdr 1e-05), [[ORC5]] (+0.62, fdr 7e-06); moves opposite to [[TCF25]] (-0.56, fdr 5e-05), [[NFATC1]] (-0.55, fdr 4e-05), [[NPHS1]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4137.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.03×** | +19.7 | 0e+00 | 43/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.86×** | +18.7 | 0e+00 | 43/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.28×** | +14.7 | 0e+00 | 40/46 (SW480, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +12.0 | 7e-31 | 31/47 (NCI-H2347, HepG2/C3A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.54×** | +7.4 | 1e-11 | 15/28 (SW480, NCI-H1792, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.44×** | +6.4 | 1e-08 | 19/41 (LOX-IMVI, SK-MEL-2, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.95×** | +6.2 | 4e-08 | 18/47 (SK-MEL-2, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +6.0 | 1e-07 | 23/47 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +5.7 | 6e-07 | 19/47 (hTERT-HPNE, C32, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 1e-05 | 17/46 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.7 | 1e-04 | 12/47 (SW1417, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +4.7 | 1e-04 | 15/47 (SK-MEL-2, SHP-77, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.20× | +4.5 | 2e-04 | 13/47 (C32, RPMI-7951, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **1.30×** | +4.5 | 3e-04 | 16/43 (SW480, A-172, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +4.5 | 3e-04 | 14/43 (CFPAC-1, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 6e-04 | 10/47 (HepG2/C3A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 6e-04 | 12/47 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +4.0 | 0.002 | 12/46 (SHP-77, LOX-IMVI, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.004 | 15/46 (SHP-77, LOX-IMVI, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.032 | 7/47 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.13× | +3.0 | 0.052 | 4/47 (LoVo, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4137.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.667×** | -7.2 | 4e-10 | 25/47 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.721×** | -5.8 | 2e-06 | 21/45 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.797×** | -5.7 | 3e-06 | 20/46 (HepG2/C3A, NCI-H1792, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.748×** | -5.2 | 3e-05 | 16/46 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.740×** | -5.1 | 3e-05 | 21/44 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.767×** | -4.7 | 3e-04 | 17/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.779×** | -4.4 | 8e-04 | 14/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -4.2 | 0.002 | 3/47 (RKO, SW 1088, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.795×** | -3.9 | 0.006 | 14/46 (COLO 205, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.801×** | -3.8 | 0.009 | 19/47 (PANC-1, HepG2/C3A, …) | top dose only | composition shift |
| [[Thymol (drug)]] 0.5 µM |  | **0.800×** | -3.4 | 0.030 | 14/44 (SW48, SK-MEL-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.815×** | -3.4 | 0.030 | 14/47 (HepG2/C3A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **0.813×** | -3.4 | 0.030 | 13/44 (KATO III, HCT15, …) | inconsistent across doses |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **0.807×** | -3.3 | 0.038 | 12/46 (SW480, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4137. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 412 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0447× (z -26.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0586× (z -17.0) |
| [[PANC-1 (line)]] | alt | 19.6 | 2 (1 ⚠) | 5 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.24× (z +11.1) | [[Harringtonine (drug)]] 5 µM 0.229× (z -13.4) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 17.6 | 2 (1 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +9.5) | [[Digitoxin (drug)]] 0.5 µM 0.249× (z -11.8) |
| [[LoVo (line)]] | wt | 14.0 | 3 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.59× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[SW480 (line)]] | alt | 17.1 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.80× (z +12.1) | — |
| [[A-427 (line)]] | wt | 25.3 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -14.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 7.27 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.22× (z +9.0) | — |
| [[KATO III (line)]] | alt | 15.3 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.19× (z +8.6) ⚠ cell-cycle shift, explains ~25% of this change | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.118× (z -11.8) |
| [[A549 (line)]] | wt | 13.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.86× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0950× (z -8.8) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -9.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0757× (z -15.6) ⚠ toxic; cell-cycle shift, explains ~63% of this change |
| [[NCI-H2347 (line)]] | alt | 14.2 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.29× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 29.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.121× (z -10.0) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.26× (z +8.6) | — |
| [[SW48 (line)]] | wt | 20.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0809× (z -9.4) |
| [[A-172 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4137), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSTF2]] | +0.63 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[HEATR6]] | +0.62 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[ORC5]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[TRAPPC11]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SDHAF3]] | +0.60 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[MTERF3]] | +0.57 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[ELMOD2]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ANAPC4]] | +0.57 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[CNEP1R1]] | +0.56 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[KAT14]] | +0.56 | +0.48 / +0.59 | both halves | 2e-05 | pathway: Epigenetic regulation by WDR5-containing histone modifying complexes |
| [[GEMIN5]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[DLAT]] | +0.55 | +0.42 / +0.54 | both halves | 4e-05 | pathway: HALLMARK_ADIPOGENESIS |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF25]] | -0.56 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[NFATC1]] | -0.55 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[NPHS1]] | -0.54 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[CATSPERG]] | -0.53 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[MC1R]] | -0.52 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[NLGN3]] | -0.52 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[TTC36-AS1]] | -0.52 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[PPP1R15B-AS1]] | -0.52 | -0.25 / -0.59 | both halves | 4e-04 |  |
| [[MDGA1]] | -0.51 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[ERF]] | -0.51 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[CDK3]] | -0.50 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[SLC9C1]] | -0.50 | -0.34 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-4.1, -9.5); signed map (-28.3, -14.4). **Vector** length 75.4, 13.8% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.0 | +12.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +19.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.9 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.9 | +18.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +4.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.3 | +2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +5.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.2 | -5.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -3.4 | -3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.1 | +2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.3 | -5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -2.2 | +3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -1.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.8 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | glycerol-3-phosphate acyltransferase, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.2 — chr10:112,149,865-112,215,377 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1560, MGC26846, GPAT1 |
| Gene groups (HGNC) | Glycerol-3-phosphate acyltransferases |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 19 pathways, smallest: RUNX1 regulates estrogen receptor mediated transcription; Triglyceride biosynthesis; Triglyceride metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCL2](https://www.uniprot.org/uniprotkb/Q9HCL2) (Glycerol-3-phosphate acyltransferase 1, mitochondrial):

> Mitochondrial membrane protein that catalyzes the essential first step of biosynthesis of glycerolipids such as triglycerides, phosphatidic acids and lysophosphatidic acids. Esterifies acyl-group from acyl-coenzyme A (acyl-CoA) to the sn-1 position of glycerol-3-phosphate, to produce lysophosphatidic acid. Has a narrow hydrophobic binding cleft that selects for a linear acyl chain. Catalytic activity is higher for substrates with a 16-carbon acyl chain.

**Summary**, from NCBI Gene [57678](https://www.ncbi.nlm.nih.gov/gene/57678):

> This gene encodes a mitochondrial enzyme which prefers saturated fatty acids as its substrate for the synthesis of glycerolipids. This metabolic pathway's first step is catalyzed by the encoded enzyme. Two forms for this enzyme exist, one in the mitochondria and one in the endoplasmic reticulum. Two alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:24865](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24865) · Entrez [57678](https://www.ncbi.nlm.nih.gov/gene/57678) · UniProt [Q9HCL2](https://www.uniprot.org/uniprotkb/Q9HCL2) · Ensembl [ENSG00000119927](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119927)

## Data

Gene col 4137: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4137); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4137, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4137]; `tensor/DDL_lfc|DDL_z.npy` [4137]; `embed/gene_vectors.npy` [4137]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4137 or target_col == 4137). Every well: [[GPAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
