---
symbol: "MSC-AS1"
type: "gene"
col: 14025
ensembl_id: "ENSG00000235531"
name: "MSC antisense RNA 1"
location: "8q13.3-q21.11"
module: 108
arm: "+"
pooled_cpm: 84.73
n_lines_expressing: 23
n_dd_up: 16
n_dd_down: 29
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 44
direction_downstream: 47
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# MSC-AS1

*MSC antisense RNA 1* — 8q13.3-q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 1.58× (z +6.4, q 7e-08, up in 19 of 23 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 1.65× (z +6.3, q 7e-08, up in 16 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (16 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.467× (z -10.0, q 1e-20, down in 19 of 21 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.766× (z -4.9, q 5e-05, down in 14 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSC]] (+0.73, fdr 7e-06, ⚠ same locus), [[MIR3171HG]] (+0.70, fdr 7e-06), [[APBB1IP]] (+0.69, fdr 7e-06), [[OR9Q1]] (+0.67, fdr 7e-06).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 44 arrows point to it, the strongest [[NOXA1]] → it (grade B ⚠); 47 go from it, the strongest it → [[TMEM45A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.58×** | +6.4 | 7e-08 | 19/23 (HOP62, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.65×** | +6.3 | 7e-08 | 16/21 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +6.0 | 5e-07 | 1/22 (NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +5.6 | 2e-06 | 4/21 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.46×** | +5.6 | 2e-06 | 17/21 (HOP62, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.49×** | +5.1 | 4e-05 | 15/22 (HOP62, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +4.7 | 2e-04 | 16/20 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.37×** | +4.2 | 0.002 | 7/22 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.002 | 15/22 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.007 | 18/20 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.008 | 15/21 (HOP62, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.014 | 0/22 | top dose only | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.6 | 0.014 | 12/20 (HOP62, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.024 | 0/21 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.059 | 12/21 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14025.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.467×** | -10.0 | 1e-20 | 19/21 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.560×** | -7.6 | 9e-12 | 20/21 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.562×** | -7.5 | 9e-12 | 19/21 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.696×** | -6.7 | 3e-09 | 18/21 (NCI-H1573, C32, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.601×** | -6.7 | 3e-09 | 17/21 (NCI-H1573, J82, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.621×** | -6.2 | 4e-08 | 18/21 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.623×** | -6.0 | 2e-07 | 17/21 (NCI-H1573, C32, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.659×** | -5.5 | 3e-06 | 13/21 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.766×** | -4.9 | 5e-05 | 14/21 (NCI-H1573, SHP-77, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.692×** | -4.8 | 9e-05 | 11/21 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **0.705×** | -4.6 | 2e-04 | 18/21 (NCI-H1573, LOX-IMVI, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.698×** | -4.5 | 3e-04 | 15/21 (HOP62, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.723×** | -4.2 | 1e-03 | 13/21 (LOX-IMVI, C32, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.746×** | -3.8 | 0.005 | 5/21 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.754×** | -3.7 | 0.009 | 15/21 (RPMI-7951, NCI-H1573, …) | two highest doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.758×** | -3.6 | 0.010 | 7/21 (SW 1088, NCI-H1573, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.765×** | -3.5 | 0.013 | 5/21 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.757×** | -3.5 | 0.013 | 16/22 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.829×** | -3.5 | 0.013 | 8/21 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.767×** | -3.5 | 0.013 | 8/21 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.770×** | -3.4 | 0.016 | 5/21 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.632×** | -3.1 | 0.038 | 11/22 (A549, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -3.1 | 0.048 | 3/21 (NCI-H1573, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 255 | 0 | 16 (14 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0897× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 209 | 0 | 15 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0602× (z -33.4) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -19.1) |
| [[HOP62 (line)]] | alt | 160 | 9 (2 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.89× (z +13.0) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 4.97× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -8.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[hTERT-HPNE (line)]] | wt | 350 | 0 | 10 (10 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -12.5) ⚠ cell-cycle shift, explains ~53% of this change |
| [[C32 (line)]] | wt | 283 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0947× (z -25.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 284 | 0 | 9 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -14.9) ⚠ cell-cycle shift, explains ~54% of this change |
| [[H4 (line)]] | wt | 200 | 0 | 8 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[A549 (line)]] | wt | 86.5 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -13.5) ⚠ cell-cycle shift, explains ~54% of this change |
| [[J82 (line)]] | alt | 62.0 | 0 | 7 (7 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.151× (z -11.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A498 (line)]] | wt | 359 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -12.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[RPMI-7951 (line)]] | alt | 316 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -11.8) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A-172 (line)]] | wt | 62.0 | 0 | 5 (5 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0383× (z -13.5) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 136 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -11.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SK-MEL-2 (line)]] | alt | 186 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -11.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 129 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -12.3) ⚠ cell-cycle shift, explains ~53% of this change |
| [[HS-578T (line)]] | alt | 549 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.151× (z -12.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H460 (line)]] | wt | 21.9 | 2 | 1 (1 ⚠) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 4.22× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -12.4) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SHP-77 (line)]] | alt | 51.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -18.4) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A-427 (line)]] | wt | 4.74 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.64 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.28 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.01 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.49 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.70 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.23 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.50 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.94 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.40 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.05 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.82 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.87 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.03 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.42 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.69 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.37 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.65 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSC]] | +0.73 | +0.72 / +0.68 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MIR3171HG]] | +0.70 | +0.61 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[APBB1IP]] | +0.69 | +0.67 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[OR9Q1]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[PTPRD]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[MIR548XHG]] | +0.65 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[KC6]] | +0.65 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[LINC00648]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[TRPA1]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ADAM12]] | +0.64 | +0.69 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[TEX41]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[LINC02377]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[PAPPA]] | +0.60 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[RARB]] | +0.60 | +0.53 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 4, C 40. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOXA1]] | B | NOXA1 activity lowers MSC-AS1's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 12.64× higher at baseline in the lines without NOXA1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers MSC-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[APCDD1L]] | B | APCDD1L activity strengthens MSC-AS1's drug response | lines that do not express APCDD1L (7) vs lines expressing it (16) | the lines without APCDD1L respond 1.00× as strongly (z diff +0.22); strongest at Panobinostat 5 µM: 0.42x vs 0.21x (z diff +4.0) | 0.065 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; target measured in part of the lines; artifact flags |
| [[LINC02882]] | B | LINC02882 activity raises MSC-AS1's level | lines that do not express LINC02882 (28) vs lines expressing it (22) | 2.40× lower at baseline in the lines without LINC02882 | 0.0997 | ⚠ within organs, on part of the lines; also absent: VGLL3, ANXA10, DDX43 |
| [[MSC]] | C | MSC activity raises MSC-AS1's level | lines that do not express MSC (34) vs lines expressing it (16) | 15.51× lower at baseline in the lines without MSC | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises MSC-AS1's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 13.26× lower at baseline in the lines without ADAM12 | 0.001 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises MSC-AS1's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 11.94× lower at baseline in the lines without APCDD1L | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[EBF1]] | C | EBF1 activity raises MSC-AS1's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 9.44× lower at baseline in the lines without EBF1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[CNRIP1]] | C | CNRIP1 activity raises MSC-AS1's level | lines that do not express CNRIP1 (25) vs lines expressing it (25) | 10.24× lower at baseline in the lines without CNRIP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047; co-absent with the target |
| [[TRPA1]] | C | TRPA1 activity raises MSC-AS1's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 9.04× lower at baseline in the lines without TRPA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises MSC-AS1's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 9.05× lower at baseline in the lines without PAPPA | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[RARB]] | C | RARB activity raises MSC-AS1's level | lines that do not express RARB (28) vs lines expressing it (22) | 8.55× lower at baseline in the lines without RARB | 0.010 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA; co-absent with the target |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 7, C 40. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM45A]] | B | MSC-AS1 activity raises TMEM45A's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 4.74× lower at baseline in the lines without MSC-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2 |
| [[STAT4]] | B | MSC-AS1 activity raises STAT4's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 2.11× lower at baseline in the lines without MSC-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2 |
| [[NREP]] | B | MSC-AS1 activity raises NREP's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 4.18× lower at baseline in the lines without MSC-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2 |
| [[STEAP1B]] | B | MSC-AS1 activity raises STEAP1B's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 2.02× lower at baseline in the lines without MSC-AS1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2 |
| [[NOXA1]] | B | MSC-AS1 activity lowers NOXA1's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 2.25× higher at baseline in the lines without MSC-AS1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2 |
| [[NR3C1]] | B | MSC-AS1 activity raises NR3C1's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 4.48× lower at baseline in the lines without MSC-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2 |
| cells under [[Peretinoin (drug)]] 0.5 µM | B | MSC-AS1 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express MSC-AS1 (27) vs lines expressing it (21) | the lines without MSC-AS1: 1.43× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2 |
| [[ADAM7-AS1]] | C | MSC-AS1 activity raises ADAM7-AS1's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 4.12× lower at baseline in the lines without MSC-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[PAPPA]] | C | MSC-AS1 activity raises PAPPA's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 7.38× lower at baseline in the lines without MSC-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[RARB]] | C | MSC-AS1 activity raises RARB's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 6.69× lower at baseline in the lines without MSC-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[DOCK10]] | C | MSC-AS1 activity raises DOCK10's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 9.32× lower at baseline in the lines without MSC-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[EBF1]] | C | MSC-AS1 activity raises EBF1's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 6.98× lower at baseline in the lines without MSC-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.7, 25.5); signed map (32.9, 42.8). **Vector** length 115, 48.2% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +9.0 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +9.0 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.5 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.4 | +6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +4.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.1 | -3.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.7 | -2.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MSC antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q13.3-q21.11 — chr8:71,828,167-72,118,393 (+) |
| Ensembl biotype | lncRNA |
| Also known as | MAT1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48724) · Entrez [100132891](https://www.ncbi.nlm.nih.gov/gene/100132891) · Ensembl [ENSG00000235531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235531)

## Data

Gene col 14025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14025); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14025]; `tensor/DDL_lfc|DDL_z.npy` [14025]; `embed/gene_vectors.npy` [14025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14025 or target_col == 14025). Every well: [[MSC-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSC-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
