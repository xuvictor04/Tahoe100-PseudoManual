---
symbol: "RIOK1"
type: "gene"
col: 4569
ensembl_id: "ENSG00000124784"
name: "RIO kinase 1"
location: "6p24.3"
module: 1
arm: "+"
pooled_cpm: 37.15
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RIOK1

*RIO kinase 1* — 6p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.22× (z +18.6, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.615× (z -11.4, q 3e-27, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAK1IP1]] (+0.78, fdr 7e-06), [[EIF2B3]] (+0.77, fdr 7e-06), [[ZNHIT6]] (+0.76, fdr 7e-06); moves opposite to [[YPEL5]] (-0.66, fdr 1e-05), [[SWT1]] (-0.64, fdr 7e-06), [[GNAS]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4569.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +18.6 | 0e+00 | 44/48 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.49×** | +15.1 | 0e+00 | 44/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.29×** | +13.1 | 3e-37 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.24×** | +10.2 | 4e-22 | 44/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.93×** | +9.3 | 2e-18 | 38/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.74×** | +9.2 | 4e-18 | 39/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.72×** | +8.9 | 3e-17 | 39/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.75×** | +8.9 | 3e-17 | 33/47 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.71×** | +8.8 | 6e-17 | 34/48 (HOP62, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.65×** | +8.2 | 1e-14 | 39/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.62×** | +8.0 | 7e-14 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +7.8 | 2e-13 | 34/47 (HepG2/C3A, C32, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +7.7 | 7e-13 | 34/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.53×** | +7.0 | 8e-11 | 33/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.41×** | +5.6 | 7e-07 | 25/48 (SW480, PANC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.82×** | +5.2 | 7e-06 | 33/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +5.1 | 1e-05 | 23/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.47×** | +4.5 | 2e-04 | 17/48 (PANC-1, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.64×** | +4.3 | 5e-04 | 21/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 6e-04 | 20/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.60×** | +4.1 | 0.001 | 18/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.002 | 19/48 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.005 | 19/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.005 | 16/48 (AN3 CA, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4569.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.615×** | -11.4 | 3e-27 | 38/48 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -5.4 | 2e-05 | 4/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.723×** | -5.2 | 4e-05 | 25/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.763×** | -4.5 | 1e-03 | 22/47 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.823×** | -4.5 | 1e-03 | 17/48 (LoVo, C-33 A, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.816× | -3.2 | 0.11 | 15/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | 0.827× | -3.1 | 0.14 | 13/47 (KATO III, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.823× | -3.1 | 0.14 | 14/47 (RKO, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4569. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 41.8 | 8 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.40× (z +9.9) | — |
| [[LoVo (line)]] | wt | 46.1 | 5 (2 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 3.36× (z +12.4) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -16.4) |
| [[PANC-1 (line)]] | alt | 64.3 | 5 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +10.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.8) | [[Adagrasib (drug)]] 0.05 µM 0.604× (z -12.0) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 16.6 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 31.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 20.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 28.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +10.0) | — |
| [[A498 (line)]] | wt | 22.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +13.1) | — |
| [[CFPAC-1 (line)]] | alt | 20.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +15.1) | — |
| [[HEC-1-A (line)]] | alt | 30.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +15.1) | — |
| [[Hs 766T (line)]] | wt | 18.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 18.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 59.2 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 28.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +13.7) | — |
| [[Panc 03.27 (line)]] | alt | 32.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.5) | — |
| [[A-172 (line)]] | wt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +13.0) | — |
| [[A-427 (line)]] | wt | 51.6 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.491× (z -8.9) |
| [[A549 (line)]] | wt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +11.6) | — |
| [[C-33 A (line)]] | alt | 56.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 27.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +9.8) | — |
| [[J82 (line)]] | alt | 43.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.8) | — |
| [[KATO III (line)]] | alt | 31.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 36.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 56.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.20× (z +10.2) | — |
| [[RKO (line)]] | wt | 60.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -18.0) |
| [[SHP-77 (line)]] | alt | 88.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 33.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +10.7) | — |
| [[SW48 (line)]] | wt | 67.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -12.0) |
| [[AN3 CA (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4569), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAK1IP1]] | +0.78 | +0.73 / +0.81 | both halves | 7e-06 | STRING 588 |
| [[EIF2B3]] | +0.77 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[ZNHIT6]] | +0.76 | +0.72 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[POLR1B]] | +0.75 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[NLE1]] | +0.74 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[PDCD11]] | +0.72 | +0.75 / +0.69 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 413 |
| [[CEP83]] | +0.72 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[BRIX1]] | +0.71 | +0.79 / +0.68 | both halves | 7e-06 | same gene group; STRING 447 |
| [[UTP14A]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 554 |
| [[SNHG17]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[RBM28]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 639 |
| [[NARS2]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL5]] | -0.66 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[SWT1]] | -0.64 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[GNAS]] | -0.62 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[MTCH1]] | -0.59 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[SLC25A53]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[RC3H1]] | -0.57 | -0.46 / -0.48 | both halves | 2e-05 | STRING 572 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises RIOK1's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds |
| [[PUDP]] | C | PUDP activity lowers RIOK1's level | lines that do not express PUDP (4) vs lines expressing it (46) | 1.76× higher at baseline in the lines without PUDP | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF264, ENSG00000287188 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.656). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.8, -42.3); signed map (-7.0, -49.0). **Vector** length 97.6, 28.3% of its response variance represented; |z| ≥ 3 in 1,190 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +7.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +15.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.9 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +5.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.3 | -11.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -3.7 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | RIO kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.3 — chr6:7,389,793-7,418,037 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AD034, FLJ30006, bA288G3.1, RRP10 |
| Gene groups (HGNC) | Ribosome biogenesis factors; RIO kinase family |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRS2](https://www.uniprot.org/uniprotkb/Q9BRS2) (Serine/threonine-protein kinase RIO1):

> Involved in the final steps of cytoplasmic maturation of the 40S ribosomal subunit. Involved in processing of 18S-E pre-rRNA to the mature 18S rRNA. Required for the recycling of NOB1 and PNO1 from the late 40S precursor. The association with the very late 40S subunit intermediate may involve a translation-like checkpoint point cycle preceeding the binding to the 60S ribosomal subunit (By similarity). Despite the protein kinase domain is proposed to act predominantly as an ATPase (By …

**Summary**, from NCBI Gene [83732](https://www.ncbi.nlm.nih.gov/gene/83732):

> The protein encoded by this gene competes with pICln for inclusion in the protein arginine methyltransferase 5 complex. This complex targets substrates for dimethylation. The encoded protein is essential for the last steps in the maturation of 40S subunits. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:18656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18656) · Entrez [83732](https://www.ncbi.nlm.nih.gov/gene/83732) · UniProt [Q9BRS2](https://www.uniprot.org/uniprotkb/Q9BRS2) · Ensembl [ENSG00000124784](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124784)

## Data

Gene col 4569: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4569); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4569, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4569]; `tensor/DDL_lfc|DDL_z.npy` [4569]; `embed/gene_vectors.npy` [4569]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4569 or target_col == 4569). Every well: [[RIOK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIOK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
