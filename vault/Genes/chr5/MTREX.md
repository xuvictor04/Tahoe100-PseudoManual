---
symbol: "MTREX"
type: "gene"
col: 459
ensembl_id: "ENSG00000039123"
name: "Mtr4 exosome RNA helicase"
location: "5q11.2"
module: 1
arm: "+"
pooled_cpm: 155.32
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MTREX

*Mtr4 exosome RNA helicase* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.72× (z +14.8, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.779× (z -7.9, q 2e-12, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSUN3]] (+0.71, fdr 1e-05), [[RBM26]] (+0.69, fdr 7e-06), [[TAF2]] (+0.64, fdr 7e-06); moves opposite to [[PI4K2A]] (-0.59, fdr 1e-05), [[DNAAF3]] (-0.58, fdr 4e-05), [[RTN4R]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 459.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.72×** | +14.8 | 0e+00 | 47/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +13.6 | 2e-39 | 45/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +13.3 | 5e-38 | 33/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +10.1 | 5e-22 | 37/48 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +9.9 | 5e-21 | 34/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +9.8 | 1e-20 | 40/48 (LS 180, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +9.3 | 1e-18 | 36/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +8.9 | 5e-17 | 34/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +7.8 | 5e-13 | 33/48 (hTERT-HPNE, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +7.7 | 5e-13 | 33/48 (hTERT-HPNE, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +7.7 | 5e-13 | 31/48 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +7.2 | 2e-11 | 25/48 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.20× | +5.6 | 7e-07 | 22/48 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +4.8 | 6e-05 | 9/48 (NCI-H2347, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | 1.15× | +4.4 | 5e-04 | 19/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 6e-04 | 21/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.34×** | +4.3 | 6e-04 | 24/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.001 | 18/47 (MIA PaCa-2, COLO 205, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.14× | +3.9 | 0.003 | 9/48 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 459.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.779×** | -7.9 | 2e-12 | 32/48 (LOX-IMVI, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.788×** | -7.5 | 1e-11 | 31/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.795×** | -7.2 | 8e-11 | 27/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.805×** | -6.8 | 1e-09 | 25/48 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.808×** | -6.7 | 2e-09 | 28/49 (SNU-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.821×** | -6.2 | 4e-08 | 25/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.857× | -4.9 | 9e-05 | 21/48 (HS-578T, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.863× | -4.3 | 0.001 | 19/48 (RKO, CHP-212, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.888× | -3.8 | 0.011 | 14/48 (A-427, LOX-IMVI, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.891× | -3.7 | 0.013 | 6/48 (SK-MEL-2, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.888× | -3.6 | 0.015 | 17/44 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.924× | -3.6 | 0.017 | 3/48 (SNU-423, CHP-212, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.791×** | -3.5 | 0.021 | 15/48 (CHP-212, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.896× | -3.5 | 0.021 | 5/49 (MIA PaCa-2, C-33 A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.890× | -3.4 | 0.026 | 12/49 (RPMI-7951, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 459. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 194 | 7 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +16.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -12.2) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.523× (z -10.9) |
| [[SW480 (line)]] | alt | 209 | 3 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.21× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.610× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 100 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +15.8) | — |
| [[PANC-1 (line)]] | alt | 209 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +18.9) | — |
| [[LoVo (line)]] | wt | 153 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.592× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 147 | 4 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.512× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 199 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.84× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 174 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +12.9) | — |
| [[RKO (line)]] | wt | 200 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 148 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +16.8) | — |
| [[HEC-1-A (line)]] | alt | 131 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +12.5) | — |
| [[NCI-H2347 (line)]] | alt | 189 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +11.8) | — |
| [[SNU-1 (line)]] | wt | 178 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -9.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 148 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -10.7) ⚠ cell-cycle shift, explains ~3% of this change |
| [[COLO 205 (line)]] | alt | 185 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.42× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 120 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.46× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 151 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +15.0) | — |
| [[NCI-H2030 (line)]] | alt | 140 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +14.6) | — |
| [[Panc 03.27 (line)]] | alt | 165 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.23× (z +10.8) | [[Lonafarnib (drug)]] 5 µM 0.302× (z -9.0) ⚠ toxic |
| [[SW48 (line)]] | wt | 159 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.4) | — |
| [[A-427 (line)]] | wt | 252 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.99× (z +8.9) | — |
| [[C32 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.462× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 134 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.9) | — |
| [[NCI-H460 (line)]] | wt | 170 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.72× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 126 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 172 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +10.4) ⚠ cell-cycle shift, explains ~3% of this change | — |
| [[A-172 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 234 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 174 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 202 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 115 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 130 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 459), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN3]] | +0.71 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[RBM26]] | +0.69 | +0.59 / +0.70 | both halves | 7e-06 | pathway: Nuclear RNA decay; STRING 642 |
| [[TAF2]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ANKRD17]] | +0.64 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[WDR33]] | +0.62 | +0.54 / +0.49 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[CDK12]] | +0.62 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[AFG1L]] | +0.62 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[QRSL1]] | +0.62 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[LANCL2]] | +0.62 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[UBE3A]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[UTP20]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 900 |
| [[DNAJC11]] | +0.61 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PI4K2A]] | -0.59 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[DNAAF3]] | -0.58 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[RTN4R]] | -0.58 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[SNN]] | -0.58 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[PEDS1]] | -0.58 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[CARD19]] | -0.57 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[NATD1]] | -0.56 | -0.29 / -0.62 | both halves | 2e-04 |  |
| [[PIM1]] | -0.56 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[FAM89B]] | -0.56 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PGAP6]] | -0.56 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[TNK2]] | -0.55 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[RMC1]] | -0.55 | -0.40 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MTREX's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.496). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.2, 10.5); signed map (7.1, -39.3). **Vector** length 113, 33.4% of its response variance represented; |z| ≥ 3 in 1,203 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +8.9 |
|  | [[NG25 (drug)]] 5 µM |  | +4.9 | +4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +0.9 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.7 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +9.8 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.1 | -7.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.5 | -7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.0 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | -7.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.8 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | Mtr4 exosome RNA helicase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:55,307,989-55,425,579 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Mtr4, Dob1, fSAP118; previously KIAA0052, SKIV2L2 |
| Gene groups (HGNC) | Nuclear exosome targeting complex; Ski2 like RNA helicases |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 11 pathways, smallest: Regulation of endogenous retroelements by the Human Silencing Hub (HUSH) complex; Nuclear RNA decay; Regulation of endogenous retroelements |
| Matched by | ensembl_id |

**Function**, from UniProt [P42285](https://www.uniprot.org/uniprotkb/P42285) (Exosome RNA helicase MTR4):

> Catalyzes the ATP-dependent unwinding of RNA duplexes with a single-stranded 3' RNA extension. Central subunit of many protein complexes, namely TRAMP-like, nuclear exosome targeting (NEXT) and poly(A) tail exosome targeting (PAXT). NEXT functions as an RNA exosome cofactor that directs a subset of non-coding short-lived RNAs for exosomal degradation. NEXT is involved in surveillance and turnover of aberrant transcripts and non-coding RNAs. PAXT directs a subset of long and polyadenylated …

**Summary**, from NCBI Gene [23517](https://www.ncbi.nlm.nih.gov/gene/23517):

> Enables ATP binding activity and RNA helicase activity. Involved in DNA damage response; RNA catabolic process; and maturation of 5.8S rRNA. Located in nuclear exosome (RNase complex) and nucleoplasm. Part of TRAMP complex and catalytic step 2 spliceosome. Biomarker of amyotrophic lateral sclerosis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18734](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18734) · Entrez [23517](https://www.ncbi.nlm.nih.gov/gene/23517) · UniProt [P42285](https://www.uniprot.org/uniprotkb/P42285) · Ensembl [ENSG00000039123](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000039123)

## Data

Gene col 459: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 459); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 459, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 459]; `tensor/DDL_lfc|DDL_z.npy` [459]; `embed/gene_vectors.npy` [459]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 459 or target_col == 459). Every well: [[MTREX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTREX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
