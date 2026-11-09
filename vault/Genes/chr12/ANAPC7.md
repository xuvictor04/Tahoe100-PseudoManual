---
symbol: "ANAPC7"
type: "gene"
col: 12226
ensembl_id: "ENSG00000196510"
name: "anaphase promoting complex subunit 7"
location: "12q24.11"
module: 1
arm: "+"
pooled_cpm: 34.38
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ANAPC7

*anaphase promoting complex subunit 7* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.90× (z +17.1, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.744× (z -7.9, q 1e-12, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCE1]] (+0.77, fdr 7e-06), [[PPIL1]] (+0.75, fdr 7e-06), [[CPSF2]] (+0.74, fdr 7e-06); moves opposite to [[LMBR1L]] (-0.71, fdr 7e-06), [[MOSPD3]] (-0.71, fdr 7e-06), [[RNASE4]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HLA-F-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +17.1 | 0e+00 | 45/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.20×** | +14.4 | 2e-44 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +13.2 | 1e-37 | 44/47 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.91×** | +12.3 | 2e-32 | 37/48 (CFPAC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +10.8 | 3e-25 | 42/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.75×** | +10.6 | 2e-24 | 39/47 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.71×** | +10.1 | 4e-22 | 36/48 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.73×** | +9.9 | 2e-21 | 31/41 (LoVo, C32, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +9.4 | 2e-19 | 38/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.59×** | +8.8 | 1e-16 | 30/46 (LoVo, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +8.6 | 3e-16 | 31/47 (LOX-IMVI, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +6.9 | 3e-10 | 29/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +6.7 | 7e-10 | 28/47 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +6.4 | 8e-09 | 28/47 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +6.2 | 2e-08 | 29/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +6.0 | 7e-08 | 30/47 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +5.9 | 9e-08 | 24/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.2 | 7e-04 | 20/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.004 | 18/47 (C32, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12226.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -7.9 | 1e-12 | 28/48 (SW48, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.781×** | -6.6 | 1e-08 | 30/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.770×** | -5.0 | 1e-04 | 20/48 (LS 180, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.786×** | -4.6 | 7e-04 | 19/47 (C-33 A, A-172, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.724×** | -4.4 | 0.001 | 19/48 (SNU-423, hTERT-HPNE, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.823×** | -3.7 | 0.021 | 17/47 (KATO III, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.809×** | -3.7 | 0.021 | 15/48 (COLO 205, J82, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **0.826×** | -3.3 | 0.058 | 16/47 (SW1417, SW48, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 37.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.68× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.06× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 65.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -8.6) |
| [[PANC-1 (line)]] | alt | 51.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +17.6) | — |
| [[SW 900 (line)]] | alt | 21.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.35× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.44× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +13.1) | — |
| [[HEC-1-A (line)]] | alt | 34.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 28.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.6) | [[Selinexor (drug)]] 0.5 µM 0.299× (z -8.8) ⚠ cell-cycle shift, explains ~20% of this change |
| [[MIA PaCa-2 (line)]] | alt | 42.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +14.4) | — |
| [[SW48 (line)]] | wt | 41.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -11.4) |
| [[SW480 (line)]] | alt | 43.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.60× (z +10.0) | — |
| [[A498 (line)]] | wt | 27.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 40.2 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0956× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.0) | — |
| [[C32 (line)]] | wt | 19.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.70× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0791× (z -9.4) |
| [[HT-29 (line)]] | alt | 27.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 38.4 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.70× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 55.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 27.0 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.57× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 36.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 50.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SNU-1 (line)]] | wt | 40.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCE1]] | +0.77 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.75 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[CPSF2]] | +0.74 | +0.82 / +0.68 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.74 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[CTPS1]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[GPATCH4]] | +0.72 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[COA7]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[UTP20]] | +0.71 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[GFM1]] | +0.71 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[UQCC2]] | +0.69 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[IPO9]] | +0.69 | +0.60 / +0.75 | both halves | 7e-06 | STRING 443 |
| [[GNL3L]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMBR1L]] | -0.71 | -0.66 / -0.72 | both halves | 7e-06 |  |
| [[MOSPD3]] | -0.71 | -0.68 / -0.76 | both halves | 7e-06 |  |
| [[RNASE4]] | -0.70 | -0.67 / -0.70 | both halves | 7e-06 |  |
| [[MED26]] | -0.69 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[ANG]] | -0.69 | -0.71 / -0.64 | both halves | 7e-06 |  |
| [[DPM1]] | -0.69 | -0.69 / -0.64 | both halves | 7e-06 |  |
| [[FBXO33]] | -0.68 | -0.74 / -0.58 | both halves | 7e-06 |  |
| [[PLCD1]] | -0.67 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[MXI1]] | -0.67 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[CNOT8]] | -0.66 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.66 | -0.70 / -0.63 | both halves | 7e-06 |  |
| [[CDK7]] | -0.66 | -0.60 / -0.63 | both halves | 7e-06 | pathway: S Phase |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-F-AS1]] | B | HLA-F-AS1 activity lowers ANAPC7's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.44× higher at baseline in the lines without HLA-F-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[YPEL3]] | B | YPEL3 activity lowers ANAPC7's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 1.41× higher at baseline in the lines without YPEL3 | 0.095 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.701). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.4, -32.1); signed map (1.4, -42.7). **Vector** length 115, 31.3% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +6.3 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +6.3 | +9.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +14.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +10.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.9 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +6.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +3.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.8 | -6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -7.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.3 | -5.0 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.4 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.0 | -4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -0.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.3 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | anaphase promoting complex subunit 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:110,372,900-110,403,730 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APC7 |
| Gene groups (HGNC) | Anaphase promoting complex; Tetratricopeptide repeat domain containing |
| Reactome | 42 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJX3](https://www.uniprot.org/uniprotkb/Q9UJX3) (Anaphase-promoting complex subunit 7):

> Component of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated E3 ubiquitin ligase that controls progression through the cell cycle. APC/C acts by mediating ubiquitination and subsequent degradation of target proteins: it mainly mediates the formation of 'Lys-11'-linked polyubiquitin chains and, to a lower extent, the formation of 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains. APC/C catalyzes assembly of branched 'Lys-11'-/'Lys-48'-linked branched ubiquitin chains on …

**Summary**, from NCBI Gene [51434](https://www.ncbi.nlm.nih.gov/gene/51434):

> This gene encodes a tetratricopeptide repeat containing component of the anaphase promoting complex/cyclosome (APC/C), a large E3 ubiquitin ligase that controls cell cycle progression by targeting a number of cell cycle regulators such as B-type cyclins for 26S proteasome-mediated degradation through ubiquitination. The encoded protein is required for proper protein ubiquitination function of APC/C and for the interaction of APC/C with certain transcription coactivators. Multiple transcript …

**Accessions** — [HGNC:17380](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17380) · Entrez [51434](https://www.ncbi.nlm.nih.gov/gene/51434) · UniProt [Q9UJX3](https://www.uniprot.org/uniprotkb/Q9UJX3) · Ensembl [ENSG00000196510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196510)

## Data

Gene col 12226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12226); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12226]; `tensor/DDL_lfc|DDL_z.npy` [12226]; `embed/gene_vectors.npy` [12226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12226 or target_col == 12226). Every well: [[ANAPC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANAPC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
