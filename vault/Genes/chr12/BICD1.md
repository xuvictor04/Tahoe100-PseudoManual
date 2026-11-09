---
symbol: "BICD1"
type: "gene"
col: 7562
ensembl_id: "ENSG00000151746"
name: "BICD cargo adaptor 1"
location: "12p11.21"
module: 4
arm: "+"
pooled_cpm: 165.48
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# BICD1

*BICD cargo adaptor 1* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.97× (z +9.9, q 2e-20, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.679× (z -7.9, q 1e-12, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTHFD2L]] (+0.64, fdr 7e-06), [[ZNF562]] (+0.64, fdr 1e-05), [[EIF3J]] (+0.63, fdr 1e-05); moves opposite to [[APAF1]] (-0.62, fdr 1e-05), [[PLEKHH3]] (-0.60, fdr 1e-05), [[MXI1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7562.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.97×** | +9.9 | 2e-20 | 35/47 (H4, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +9.1 | 4e-17 | 35/47 (NCI-H1573, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.83×** | +8.8 | 2e-16 | 33/47 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.78×** | +8.0 | 2e-13 | 38/47 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +7.2 | 7e-11 | 34/47 (AsPC-1, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.007 | 22/47 (NCI-H1573, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.010 | 26/47 (LS 180, MIA PaCa-2, …) | top dose only |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.027 | 24/47 (RPMI-7951, HOP62, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.14 | 15/48 (HEC-1-A, Panc 03.27, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.27× | +3.0 | 0.14 | 21/47 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7562.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -7.9 | 1e-12 | 33/48 (NCI-H23, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.605×** | -7.3 | 8e-11 | 35/47 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.621×** | -6.9 | 8e-10 | 36/47 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.503×** | -5.2 | 2e-05 | 39/46 (SW48, C32, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.699×** | -5.2 | 2e-05 | 28/47 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.724×** | -4.7 | 3e-04 | 31/47 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.779×** | -4.3 | 0.001 | 26/47 (AsPC-1, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.784×** | -4.0 | 0.005 | 27/49 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.746×** | -3.9 | 0.007 | 26/48 (C32, AsPC-1, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.758×** | -3.6 | 0.015 | 28/47 (NCI-H2030, AN3 CA, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.781×** | -3.6 | 0.015 | 25/48 (AsPC-1, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.770×** | -3.6 | 0.017 | 23/47 (AsPC-1, C32, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **0.791×** | -3.4 | 0.032 | 22/47 (PANC-1, LoVo, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.801×** | -3.4 | 0.032 | 22/47 (C32, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.789×** | -3.3 | 0.037 | 22/49 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7562. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 147 | 6 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +16.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.352× (z -12.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.467× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 135 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.05× (z +20.6) | — |
| [[NCI-H23 (line)]] | alt | 294 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -19.8) |
| [[C32 (line)]] | wt | 208 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -13.5) |
| [[PANC-1 (line)]] | alt | 189 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -18.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -12.5) |
| [[SW480 (line)]] | alt | 189 | 2 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.01× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.335× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 402 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 120 | 2 | 3 | [[Auranofin (drug)]] 5 µM 3.64× (z +10.6) | [[Trametinib (drug)]] 5 µM 0.312× (z -10.2) |
| [[KATO III (line)]] | alt | 79.7 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.53× (z +11.4) | — |
| [[SW48 (line)]] | wt | 176 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -13.3) |
| [[A498 (line)]] | wt | 361 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -16.4) |
| [[HT-29 (line)]] | alt | 70.1 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.17× (z +11.4) | — |
| [[H4 (line)]] | wt | 146 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.61× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 96.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.44× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 238 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.45× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 116 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.06× (z +12.8) | — |
| [[RKO (line)]] | wt | 148 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -11.2) |
| [[SW 900 (line)]] | alt | 329 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +11.2) | — |
| [[A-172 (line)]] | wt | 145 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.67× (z +9.0) | — |
| [[A-427 (line)]] | wt | 129 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -9.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -8.5) |
| [[CHP-212 (line)]] | wt | 365 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -10.5) |
| [[J82 (line)]] | alt | 138 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.327× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[LS 180 (line)]] | wt | 104 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.53× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 211 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 223 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -10.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -9.4) |
| [[SW 1088 (line)]] | alt | 148 | 0 | 2 (1 ⚠) | — | [[Fostamatinib (disodium hexahydrate) (drug)]] 5 µM 0.0968× (z -9.2) ⚠ unreliable plate only · without an alert: [[Sildenafil (drug)]] 0.05 µM 0.0872× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 63.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.53× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 378 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.653× (z -9.9) ⚠ position not correctable |
| [[LOX-IMVI (line)]] | wt | 101 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.95× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 97.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.76× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 297 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 90.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.60× (z +8.5) | — |
| [[SW 1271 (line)]] | alt | 334 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -8.7) |
| [[A549 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 134 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 150 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.3 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7562), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFD2L]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ZNF562]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[EIF3J]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[PCNX2]] | +0.62 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[BACH1]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[UGGT2]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[TANGO6]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[MTAP]] | +0.60 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[CYTOR]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[GCLM]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[DNAJC11]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APAF1]] | -0.62 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.60 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[MXI1]] | -0.59 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[ARNT]] | -0.59 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[PAIP2B]] | -0.59 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[EFNA3]] | -0.59 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[KDM3A]] | -0.59 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[ALDH6A1]] | -0.58 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[PLAG1]] | -0.57 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[SLC25A23]] | -0.57 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CCDC115]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[GID8]] | -0.57 | -0.57 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers BICD1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[C6orf141]] | B | C6orf141 activity lowers BICD1's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 1.43× higher at baseline in the lines without C6orf141 | 0.098 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[SNHG26]] | B | SNHG26 activity raises BICD1's level | lines that do not express SNHG26 (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without SNHG26 | 0.098 | ⚠ within organs, on part of the lines; also absent: HEG1, GPR63, FAM171A1 |
| [[SSBP2]] | C | SSBP2 activity raises BICD1's level | lines that do not express SSBP2 (4) vs lines expressing it (46) | 2.50× lower at baseline in the lines without SSBP2 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENAH, AGPAT4, ANKRD44; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.496). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.8, -30.9); signed map (3.9, -45.9). **Vector** length 152, 51.1% of its response variance represented; |z| ≥ 3 in 1,260 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.7 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.0 | +9.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.0 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.3 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.0 | +9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +2.1 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | +3.6 | +2.9 |
|  | [[Brimonidine (drug)]] 5 µM |  | +3.6 | +3.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.5 | -7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -7.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.0 | -6.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.9 | -4.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -5.8 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.4 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.9 | -3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.8 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | BICD cargo adaptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.21 — chr12:32,106,835-32,383,633 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | BICD family cargo adaptors |
| Reactome | 5 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96G01](https://www.uniprot.org/uniprotkb/Q96G01) (Protein bicaudal D homolog 1):

> Regulates coat complex coatomer protein I (COPI)-independent Golgi-endoplasmic reticulum transport by recruiting the dynein-dynactin motor complex.

**Summary**, from NCBI Gene [636](https://www.ncbi.nlm.nih.gov/gene/636):

> This gene encodes an adaptor protein that belongs to the bicaudal D family of dynein cargo adaptors. The encoded protein acts as an intracellular cargo transport cofactor that regulates the microtubule-based loading of cargo onto the dynein motor complex. It also controls dynein motor activity and coordination. It has a domain architecture consisting of coiled-coil domains at the N- and C-termini that are highly conserved in other family members. Naturally occurring mutations in this gene are …

**Accessions** — [HGNC:1049](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1049) · Entrez [636](https://www.ncbi.nlm.nih.gov/gene/636) · UniProt [Q96G01](https://www.uniprot.org/uniprotkb/Q96G01) · Ensembl [ENSG00000151746](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151746)

## Data

Gene col 7562: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7562); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7562, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7562]; `tensor/DDL_lfc|DDL_z.npy` [7562]; `embed/gene_vectors.npy` [7562]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7562 or target_col == 7562). Every well: [[BICD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BICD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
