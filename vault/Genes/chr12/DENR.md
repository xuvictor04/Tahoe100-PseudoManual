---
symbol: "DENR"
type: "gene"
col: 6341
ensembl_id: "ENSG00000139726"
name: "density regulated re-initiation and release factor"
location: "12q24.31"
module: 18
arm: "+"
pooled_cpm: 121.94
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# DENR

*density regulated re-initiation and release factor* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.39× (z +7.6, q 9e-12, up in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~22% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.38× (z +7.6, q 9e-12, up in 32 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.211×, NCI-H23 0.532×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SW 1271 0.0653×); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.753×; ⚠ position not correctable); [[Hydroxyfasudil (drug)]] 5 µM in 1 line (CHP-212 0.0722×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H8]] (+0.54, fdr 3e-05), [[TMED8]] (+0.53, fdr 3e-05), [[FEZ2]] (+0.52, fdr 1e-05); moves opposite to [[PPP3CA]] (-0.48, fdr 6e-05), [[SIK2]] (-0.47, fdr 7e-05), [[C1QTNF3]] (-0.47, fdr 5e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PLD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6341.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.39×** | +7.6 | 9e-12 | 36/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +7.6 | 9e-12 | 32/48 (SW480, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +7.4 | 3e-11 | 41/48 (SW480, PANC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +6.9 | 7e-10 | 37/48 (SW480, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +6.8 | 1e-09 | 29/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.23×** | +6.8 | 1e-09 | 23/49 (AsPC-1, COLO 205, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +6.5 | 7e-09 | 34/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.33×** | +6.0 | 2e-07 | 29/48 (HS-578T, COLO 205, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +6.0 | 2e-07 | 32/48 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.7 | 8e-07 | 32/47 (NCI-H460, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.30×** | +5.4 | 4e-06 | 27/50 (LS 180, COLO 205, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.25×** | +5.2 | 1e-05 | 28/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.22×** | +4.7 | 1e-04 | 24/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.7 | 1e-04 | 17/48 (CFPAC-1, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.22×** | +4.6 | 1e-04 | 25/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.43×** | +4.4 | 3e-04 | 27/49 (HS-578T, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +4.3 | 6e-04 | 24/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.41×** | +4.2 | 9e-04 | 23/48 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.001 | 25/48 (SW1417, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.012 | 20/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.19× | +3.5 | 0.012 | 15/49 (NCI-H1573, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.2 | 0.030 | 8/49 (CFPAC-1, A-427, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.043 | 13/48 (PANC-1, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.043 | 4/48 (BT-474, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6341.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.211×, NCI-H23 0.532×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SW 1271 0.0653×); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.753×; ⚠ position not correctable); [[Hydroxyfasudil (drug)]] 5 µM in 1 line (CHP-212 0.0722×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 0.860× | -3.6 | 0.17 | 15/48 (NCI-H1792, LS 180, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.905× | -3.3 | 0.17 | 12/49 (RKO, NCI-H23, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.856× | -3.3 | 0.17 | 13/47 (J82, AsPC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.771× | -3.2 | 0.17 | 17/49 (C32, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.878× | -3.1 | 0.20 | 7/47 (HEC-1-A, SNU-423, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6341. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 148 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +13.9) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.92× (z +10.4) | — |
| [[SW480 (line)]] | alt | 133 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +15.3) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +14.0) | — |
| [[AsPC-1 (line)]] | alt | 103 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +15.5) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 78.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.6) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 74.3 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.34× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A498 (line)]] | wt | 80.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.75× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 81.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +10.4) | — |
| [[SNU-1 (line)]] | wt | 179 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 120 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.22× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[CFPAC-1 (line)]] | alt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.00× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 1 | — | [[Hydroxyfasudil (drug)]] 5 µM 0.0722× (z -8.9) |
| [[LS 180 (line)]] | wt | 102 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.1) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[NCI-H2030 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +8.8) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[NCI-H23 (line)]] | alt | 266 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.532× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 85.8 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0822× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 124 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0653× (z -14.1) |
| [[SW48 (line)]] | wt | 212 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 85.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 175 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 188 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 80.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 126 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 221 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 199 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6341), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H8]] | +0.54 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[TMED8]] | +0.53 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[FEZ2]] | +0.52 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MIX23]] | +0.52 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[MLH3]] | +0.52 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[R3HCC1L]] | +0.51 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[HPRT1]] | +0.50 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[PLEKHH1]] | +0.50 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[FAM216A]] | +0.49 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[PCOLCE2]] | +0.49 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[RAB11FIP2]] | +0.48 | +0.36 / +0.49 | both halves | 9e-05 |  |
| [[PARVB]] | +0.48 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP3CA]] | -0.48 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[SIK2]] | -0.47 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[C1QTNF3]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[THBS3-AS1]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[LINC00511]] | -0.44 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[NUP98]] | -0.43 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[PNPLA2]] | -0.42 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[TCF7L2]] | -0.42 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[NR4A1]] | -0.42 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[H2AZ2]] | -0.42 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[SPIRE2]] | -0.42 | -0.40 / -0.32 | both halves | 1e-04 |  |
| [[PNKD]] | -0.41 | -0.39 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLD1]] | B | PLD1 activity lowers DENR's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 1.80× higher at baseline in the lines without PLD1 | 0.002 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[LINC00511]] | B | LINC00511 activity lowers DENR's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 1.56× higher at baseline in the lines without LINC00511 | 0.002 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.343). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-15.8, 19.7); signed map (-23.4, 46.3). **Vector** length 105, 29.5% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.0 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +4.9 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.8 | +6.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.4 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +4.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -6.7 | -1.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -4.2 | +0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -2.8 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.4 | +4.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | density regulated re-initiation and release factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,752,824-122,771,064 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DRP, DRP1, SMAP-3 |
| Matched by | ensembl_id |

**Function**, from UniProt [O43583](https://www.uniprot.org/uniprotkb/O43583) (Density-regulated protein):

> Translation regulator forming a complex with MCTS1 to promote translation reinitiation. Translation reinitiation is the process where the small ribosomal subunit remains attached to the mRNA following termination of translation of a regulatory upstream ORF (uORF), and resume scanning on the same mRNA molecule to initiate translation of a downstream ORF, usually the main ORF (mORF). The MCTS1/DENR complex is pivotal to two linked mechanisms essential for translation reinitiation. Firstly, the …

**Summary**, from NCBI Gene [8562](https://www.ncbi.nlm.nih.gov/gene/8562):

> This gene encodes a protein whose expression was found to increase in cultured cells at high density but not during growth arrest. This gene was also shown to have increased expression in cells overexpressing HER-2/neu proto-oncogene. The protein contains an SUI1 domain. In budding yeast, SUI1 is a translation initiation factor that along with eIF-2 and the initiator tRNA-Met, directs the ribosome to the proper translation start site. Proteins similar to SUI have been found in mammals, insects, …

**Accessions** — [HGNC:2769](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2769) · Entrez [8562](https://www.ncbi.nlm.nih.gov/gene/8562) · UniProt [O43583](https://www.uniprot.org/uniprotkb/O43583) · Ensembl [ENSG00000139726](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139726)

## Data

Gene col 6341: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6341); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6341, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6341]; `tensor/DDL_lfc|DDL_z.npy` [6341]; `embed/gene_vectors.npy` [6341]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6341 or target_col == 6341). Every well: [[DENR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
