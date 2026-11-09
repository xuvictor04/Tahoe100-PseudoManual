---
symbol: "CYP27A1"
type: "gene"
col: 5781
ensembl_id: "ENSG00000135929"
name: "cytochrome P450 family 27 subfamily A member 1"
location: "2q35"
module: 37
arm: "+"
pooled_cpm: 10.56
n_lines_expressing: 40
n_dd_up: 23
n_dd_down: 17
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 8
direction_downstream: 5
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# CYP27A1

*cytochrome P450 family 27 subfamily A member 1* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +13.6, q 2e-39, up in 19 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.396× (z -13.5, q 7e-39, down in 27 of 36 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.620× (z -7.3, q 4e-11, down in 19 of 36 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAXDC2]] (+0.62, fdr 1e-05), [[LINC02609]] (+0.50, fdr 6e-05), [[MAP7D2]] (+0.50, fdr 3e-05); moves opposite to [[UNC13A]] (-0.49, fdr 1e-04), [[PPM1L]] (-0.44, fdr 1e-04), [[CDH4]] (-0.44, fdr 1e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[YWHAEP7-1]] → it (grade B ⚠); 5 go from it, the strongest it → [[EML6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5781.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +13.6 | 2e-39 | 19/35 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.36×** | +6.7 | 8e-09 | 16/37 (HOP62, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.9 | 2e-04 | 11/30 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +4.8 | 2e-04 | 12/37 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.37×** | +4.7 | 3e-04 | 7/37 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.6 | 4e-04 | 10/37 (A498, C-33 A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.35×** | +4.6 | 4e-04 | 10/34 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 6e-04 | 9/37 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +4.4 | 6e-04 | 12/36 (C32, SW 900, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.003 | 9/36 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.003 | 6/36 (NCI-H2347, SW 900, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.32×** | +3.9 | 0.004 | 8/32 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.005 | 5/36 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.008 | 9/34 (SW 900, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.013 | 6/37 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.20× | +3.5 | 0.015 | 6/37 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.019 | 6/35 (C32, HepG2/C3A, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.028 | 4/35 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.041 | 13/33 (C32, HepG2/C3A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5781.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.396×** | -13.5 | 7e-39 | 27/36 (COLO 205, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.544×** | -9.2 | 8e-18 | 23/37 (SW480, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.562×** | -8.7 | 4e-16 | 22/34 (RPMI-7951, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.588×** | -8.0 | 1e-13 | 21/36 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.620×** | -7.3 | 4e-11 | 19/36 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.641×** | -6.8 | 1e-09 | 20/34 (COLO 205, SK-MEL-2, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.765×** | -5.8 | 7e-07 | 19/36 (COLO 205, SK-MEL-2, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.709×** | -5.2 | 1e-05 | 19/35 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.735×** | -4.7 | 2e-04 | 12/33 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.724×** | -4.7 | 2e-04 | 9/37 (COLO 205, SK-MEL-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.612×** | -3.9 | 0.005 | 12/35 (NCI-H1792, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | **0.774×** | -3.7 | 0.009 | 10/28 (SW 900, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.790×** | -3.6 | 0.015 | 14/36 (COLO 205, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.795×** | -3.5 | 0.020 | 7/36 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | **0.809×** | -3.2 | 0.050 | 3/34 (NCI-H460, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.814×** | -3.1 | 0.063 | 15/35 (COLO 205, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5781. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 88.5 | 9 (1 ⚠) | 5 (3 ⚠) | [[Binimetinib (drug)]] 5 µM 3.30× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.109× (z -18.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.152× (z -15.4) |
| [[COLO 205 (line)]] | alt | 46.3 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0298× (z -20.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 40.9 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.239× (z -9.6) |
| [[SW 900 (line)]] | alt | 27.3 | 0 | 6 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0877× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[HOP62 (line)]] | alt | 18.4 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 16.8 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 82.9 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.233× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 29.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 5.98 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 10.4 | 0 | 2 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0724× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.172× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.221× (z -9.0) |
| [[A-172 (line)]] | wt | 4.99 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 4.43 | 0 | 1 (1 ⚠) | — | [[Rimonabant (Hydrochloride) (drug)]] 0.5 µM 0.0699× (z -8.5) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 7.28 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 4.01 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0670× (z -9.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 6.33 | 0 | 1 | — | [[Arbutin (drug)]] 5 µM 0.0892× (z -8.7) |
| [[PANC-1 (line)]] | alt | 5.72 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SNU-423 (line)]] | alt | 9.96 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.140× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[A-427 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5781), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAXDC2]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[LINC02609]] | +0.50 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[MAP7D2]] | +0.50 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[ABCC6]] | +0.50 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[LINC01482]] | +0.49 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[RHOXF1-AS1]] | +0.49 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[FLJ46284]] | +0.48 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[CCL28]] | +0.48 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[TMPRSS5]] | +0.46 | +0.37 / +0.51 | both halves | 7e-05 |  |
| [[TF]] | +0.46 | +0.51 / +0.32 | both halves | 2e-04 |  |
| [[PLCD4]] | +0.46 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[ADHFE1]] | +0.46 | +0.40 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC13A]] | -0.49 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[PPM1L]] | -0.44 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[CDH4]] | -0.44 | -0.40 / -0.32 | both halves | 1e-04 |  |
| [[TAF1B]] | -0.44 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[TLN2]] | -0.43 | -0.41 / -0.21 | both halves | 7e-04 |  |
| [[EML6]] | -0.42 | -0.43 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[LINC02742]] | -0.42 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[SEMA3A]] | -0.42 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[NRXN3]] | -0.41 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[IQCH]] | -0.41 | -0.20 / -0.42 | both halves | 7e-04 |  |
| [[THSD4]] | -0.41 | -0.46 / -0.35 | both halves | 1e-04 | pathway: Diseases of metabolism |
| [[ITGA6]] | -0.41 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[TRAPPC9]] | -0.40 | -0.35 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YWHAEP7-1]] | B | YWHAEP7-1 activity raises CYP27A1's level | lines that do not express YWHAEP7-1 (13) vs lines expressing it (37) | 2.94× lower at baseline in the lines without YWHAEP7-1 | 0.004 | ⚠ within organs, on part of the lines; also absent: OCA2, ALK, SPDYE10; maybe low, not absent |
| [[SHROOM4]] | B | SHROOM4 activity raises CYP27A1's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 2.81× lower at baseline in the lines without SHROOM4 | 0.005 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[SHROOM4]] | B | SHROOM4 activity strengthens CYP27A1's drug response | lines that do not express SHROOM4 (21) vs lines expressing it (17) | the lines without SHROOM4 respond 0.47× as strongly (z diff +1.74); strongest at Homoharringtonine 5 µM: 0.93x vs 0.51x (z diff +4.8) | 0.011 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539; target measured in part of the lines; artifact flags |
| [[CFI]] | B | CFI activity raises CYP27A1's level | lines that do not express CFI (31) vs lines expressing it (19) | 1.94× lower at baseline in the lines without CFI | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[CCL28]] | B | CCL28 activity raises CYP27A1's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without CCL28 | 0.051 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74 |
| [[WFDC2]] | B | WFDC2 activity raises CYP27A1's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 1.29× lower at baseline in the lines without WFDC2 | 0.070 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers CYP27A1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[ZNF529-AS1]] | B | ZNF529-AS1 activity raises CYP27A1's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 2.23× lower at baseline in the lines without ZNF529-AS1 | 0.0996 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EML6]] | B | CYP27A1 activity strengthens EML6's drug response | lines that do not express CYP27A1 (9) vs lines expressing it (35) | the lines without CYP27A1 respond 0.54× as strongly (z diff +2.72); strongest at Belinostat 5 µM: 1.43x vs 4.07x (z diff +5.3) | 0.010 | ⚠ within organs, on part of the lines; also absent: RNF217, ENSG00000224905, ESYT3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[EML6]] | B | CYP27A1 activity lowers EML6's level | lines that do not express CYP27A1 (10) vs lines expressing it (40) | 2.46× higher at baseline in the lines without CYP27A1 | 0.036 | ⚠ within organs, on part of the lines; also absent: RNF217, ENSG00000224905, ESYT3; maybe low, not absent |
| [[ADAM20]] | B | CYP27A1 activity raises ADAM20's level | lines that do not express CYP27A1 (10) vs lines expressing it (40) | 1.31× lower at baseline in the lines without CYP27A1 | 0.071 | ⚠ within organs, on part of the lines; also absent: RNF217, ENSG00000224905, ESYT3; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 5 µM | B | CYP27A1 activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express CYP27A1 (10) vs lines expressing it (38) | the lines without CYP27A1: 0.55× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: RNF217, ENSG00000224905, ESYT3; maybe low, not absent |
| [[MAP7D2]] | B | CYP27A1 activity raises MAP7D2's level | lines that do not express CYP27A1 (10) vs lines expressing it (40) | 1.94× lower at baseline in the lines without CYP27A1 | 0.093 | ⚠ within organs, on part of the lines; also absent: RNF217, ENSG00000224905, ESYT3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.473). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.7, -16.2); signed map (12.0, 3.0). **Vector** length 77.4, 15.1% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +4.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +4.1 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | -0.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.3 | -13.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.1 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -7.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.4 | -8.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 27 subfamily A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:218,781,749-218,815,293 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CTX, CP27; previously CYP27 |
| Gene groups (HGNC) | Cytochrome P450 family 27 |
| Hallmark sets | BILE_ACID_METABOLISM, XENOBIOTIC_METABOLISM |
| Reactome | 13 pathways, smallest: Synthesis of bile acids and bile salts via 27-hydroxycholesterol; Synthesis of bile acids and bile salts via 24-hydroxycholesterol; Endogenous sterols |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02318](https://www.uniprot.org/uniprotkb/Q02318) (Sterol 26-hydroxylase, mitochondrial):

> Cytochrome P450 monooxygenase that catalyzes regio- and stereospecific hydroxylation of cholesterol and its derivatives. Hydroxylates (with R stereochemistry) the terminal methyl group of cholesterol side-chain in a three step reaction to yield at first a C26 alcohol, then a C26 aldehyde and finally a C26 acid. Regulates cholesterol homeostasis by catalyzing the conversion of excess cholesterol to bile acids via both the 'neutral' (classic) and the 'acid' (alternative) pathways. May also …

**Summary**, from NCBI Gene [1593](https://www.ncbi.nlm.nih.gov/gene/1593):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This mitochondrial protein oxidizes cholesterol intermediates as part of the bile synthesis pathway. Since the conversion of cholesterol to bile acids is the major route for removing cholesterol from the body, this protein is important for overall cholesterol …

**Accessions** — [HGNC:2605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2605) · Entrez [1593](https://www.ncbi.nlm.nih.gov/gene/1593) · UniProt [Q02318](https://www.uniprot.org/uniprotkb/Q02318) · Ensembl [ENSG00000135929](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135929)

## Data

Gene col 5781: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5781); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5781, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5781]; `tensor/DDL_lfc|DDL_z.npy` [5781]; `embed/gene_vectors.npy` [5781]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5781 or target_col == 5781). Every well: [[CYP27A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP27A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
