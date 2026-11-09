---
symbol: "SMC6"
type: "gene"
col: 8620
ensembl_id: "ENSG00000163029"
name: "structural maintenance of chromosomes 6"
location: "2p24.2"
module: 179
arm: "-"
pooled_cpm: 103.4
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# SMC6

*structural maintenance of chromosomes 6* — 2p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.57× (z +13.6, q 2e-39, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.86× (z +12.7, q 1e-34, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.336× (z -12.1, q 4e-31, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL13B]] (+0.68, fdr 1e-05), [[SCMH1]] (+0.64, fdr 1e-05), [[EEA1]] (+0.58, fdr 1e-05); moves opposite to [[WDR5B-DT]] (-0.59, fdr 1e-05), [[MYL6B]] (-0.58, fdr 1e-05), [[CDC26]] (-0.54, fdr 1e-05).
> It sits in the **-** arm of [[Module 179]] (RHOA GTPase cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.57×** | +13.6 | 2e-39 | 37/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +12.7 | 1e-34 | 45/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.59×** | +9.9 | 7e-21 | 39/48 (A498, C32, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.59×** | +9.9 | 9e-21 | 40/48 (A498, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +9.8 | 2e-20 | 37/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.56×** | +9.4 | 4e-19 | 37/49 (SW480, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.55×** | +9.3 | 9e-19 | 39/48 (A498, SW 900, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **1.44×** | +7.4 | 8e-12 | 31/43 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +7.4 | 9e-12 | 38/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.31×** | +5.8 | 4e-07 | 29/48 (CFPAC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.30×** | +5.3 | 6e-06 | 28/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.28×** | +5.2 | 9e-06 | 25/48 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.27×** | +5.1 | 1e-05 | 27/48 (SW 900, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.17× | +4.8 | 5e-05 | 18/49 (C32, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +4.7 | 1e-04 | 27/49 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.002 | 23/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +3.9 | 0.003 | 22/48 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.005 | 15/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +3.0 | 0.063 | 9/48 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.22×** | +2.9 | 0.078 | 14/48 (MIA PaCa-2, SW 900, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.086 | 15/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8620.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.336×** | -12.1 | 4e-31 | 45/49 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.339×** | -12.1 | 5e-31 | 44/48 (A-427, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.772×** | -7.8 | 1e-12 | 33/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.744×** | -6.3 | 4e-08 | 32/48 (RKO, NCI-H2030, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.806×** | -4.6 | 5e-04 | 24/48 (LOX-IMVI, A498, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -4.4 | 8e-04 | 0/50 | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.841× | -3.7 | 0.019 | 13/48 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | 0.846× | -3.4 | 0.053 | 18/48 (A498, C-33 A, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.855× | -3.3 | 0.053 | 10/49 (A498, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.758× | -3.1 | 0.12 | 19/49 (CHP-212, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | 0.761× | -3.0 | 0.12 | 17/47 (A498, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | 0.763× | -3.0 | 0.12 | 20/45 (RKO, A-427, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 186 | 4 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +30.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.10× (z +21.4) | [[TAK-901 (drug)]] 5 µM 0.327× (z -11.5) |
| [[A498 (line)]] | wt | 101 | 3 (3 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.28× (z +10.8) ⚠ cell-cycle shift, explains ~50% of this change | [[Selinexor (drug)]] 5 µM 0.490× (z -13.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.261× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 54.6 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +17.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 148 | 0 | 5 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.225× (z -11.8) |
| [[SW480 (line)]] | alt | 105 | 5 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.19× (z +10.1) | — |
| [[A-172 (line)]] | wt | 158 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.92× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -10.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A-427 (line)]] | wt | 228 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.117× (z -16.5) |
| [[A549 (line)]] | wt | 171 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.26× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 93.6 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.02× (z +8.9) | [[TAK-901 (drug)]] 5 µM 0.265× (z -8.7) |
| [[C32 (line)]] | wt | 86.8 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.0) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[HEC-1-A (line)]] | alt | 86.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 102 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.52× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 77.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 58.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +17.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +10.0) | — |
| [[RKO (line)]] | wt | 91.5 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.5) ⚠ cell-cycle shift, explains ~33% of this change | [[PH-797804 (drug)]] 5 µM 0.181× (z -10.7) |
| [[SNU-423 (line)]] | alt | 68.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +16.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 48.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HOP62 (line)]] | alt | 72.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 82.1 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.160× (z -11.2) |
| [[SHP-77 (line)]] | alt | 130 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +9.6) | [[TAK-901 (drug)]] 5 µM 0.233× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 84.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.74× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 100 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.557× (z -9.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[KATO III (line)]] | alt | 105 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.224× (z -9.3) |
| [[LoVo (line)]] | wt | 80.3 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.248× (z -8.7) |
| [[LS 180 (line)]] | wt | 79.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.246× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 90.6 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.238× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 107 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.312× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 91.6 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.60× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 47.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +8.8) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[AN3 CA (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 144 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 78.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 81.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL13B]] | +0.68 | +0.55 / +0.72 | both halves | 1e-05 | **novel candidate** |
| [[SCMH1]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[EEA1]] | +0.58 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SPECC1L]] | +0.56 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[MAP7D3]] | +0.53 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CENPP]] | +0.53 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[EIF5B]] | +0.53 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CNTRL]] | +0.52 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SMC1A]] | +0.51 | +0.47 / +0.54 | both halves | 2e-05 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 759 |
| [[YEATS4]] | +0.51 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PPM1G]] | +0.51 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[MRPS16]] | +0.50 | +0.64 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR5B-DT]] | -0.59 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[MYL6B]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[CDC26]] | -0.54 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[COMMD9]] | -0.54 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[EAF1]] | -0.54 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[EPM2AIP1]] | -0.53 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[DDX49]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[MRPS22]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[SDHD]] | -0.52 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[EDRF1]] | -0.51 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[UBOX5]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[GSTM2]] | -0.50 | -0.32 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **-** arm (projection on the module's main direction -0.611). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (3.4, -32.1); signed map (7.0, -46.4). **Vector** length 120, 38.0% of its response variance represented; |z| ≥ 3 in 1,176 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +12.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +4.9 | +5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +4.2 | +5.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | +4.2 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +1.9 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -11.3 | -12.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -11.1 | -7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -10.0 | -6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -9.4 | -12.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -5.9 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | structural maintenance of chromosomes 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.2 — chr2:17,663,812-17,800,242 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22116; previously SMC6L1 |
| Gene groups (HGNC) | Structural maintenance of chromosomes proteins; SMC5/6 complex |
| Hallmark sets | E2F_TARGETS |
| Reactome | 3 pathways, smallest: SUMOylation of DNA damage response and repair proteins; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SB8](https://www.uniprot.org/uniprotkb/Q96SB8) (Structural maintenance of chromosomes protein 6):

> Core component of the SMC5-SMC6 complex, a complex involved in DNA double-strand breaks by homologous recombination. The complex may promote sister chromatid homologous recombination by recruiting the SMC1-SMC3 cohesin complex to double-strand breaks. The complex is required for telomere maintenance via recombination in ALT (alternative lengthening of telomeres) cell lines and mediates sumoylation of shelterin complex (telosome) components which is proposed to lead to shelterin complex …

**Summary**, from NCBI Gene [79677](https://www.ncbi.nlm.nih.gov/gene/79677):

> Enables DNA secondary structure binding activity and ubiquitin protein ligase binding activity. Involved in several processes, including cellular senescence; host-mediated suppression of viral genome replication; and telomere maintenance via recombination. Located in chromosome and nuclear body. Part of Smc5-Smc6 complex. Is active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20466) · Entrez [79677](https://www.ncbi.nlm.nih.gov/gene/79677) · UniProt [Q96SB8](https://www.uniprot.org/uniprotkb/Q96SB8) · Ensembl [ENSG00000163029](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163029)

## Data

Gene col 8620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8620); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8620]; `tensor/DDL_lfc|DDL_z.npy` [8620]; `embed/gene_vectors.npy` [8620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8620 or target_col == 8620). Every well: [[SMC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
