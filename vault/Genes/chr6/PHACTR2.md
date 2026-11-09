---
symbol: "PHACTR2"
type: "gene"
col: 3370
ensembl_id: "ENSG00000112419"
name: "phosphatase and actin regulator 2"
location: "6q24.2"
module: 137
arm: "+"
pooled_cpm: 78.65
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# PHACTR2

*phosphatase and actin regulator 2* — 6q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.57× (z +17.0, q 0e+00, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.756× (z -7.5, q 2e-11, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM169A]] (+0.72, fdr 7e-06), [[GTF3C6]] (+0.68, fdr 4e-05), [[TMCO4]] (+0.67, fdr 3e-05); moves opposite to [[OGG1]] (-0.68, fdr 1e-05), [[MTMR14]] (-0.66, fdr 1e-05), [[SLC27A1]] (-0.65, fdr 7e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3370.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +17.0 | 0e+00 | 32/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.90×** | +16.5 | 0e+00 | 37/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +12.8 | 4e-35 | 31/46 (PANC-1, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +12.5 | 2e-33 | 32/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +10.4 | 3e-23 | 31/46 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.47×** | +10.3 | 8e-23 | 35/47 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +8.3 | 6e-15 | 30/46 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +7.9 | 2e-13 | 25/47 (NCI-H2347, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +7.4 | 7e-12 | 25/46 (HS-578T, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.31×** | +7.2 | 4e-11 | 28/46 (SW1417, HepG2/C3A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +7.0 | 2e-10 | 21/46 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.32×** | +7.0 | 2e-10 | 23/43 (NCI-H1792, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.7 | 7e-10 | 30/45 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +5.9 | 1e-07 | 20/45 (AsPC-1, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +5.8 | 2e-07 | 25/46 (A549, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +5.3 | 4e-06 | 21/45 (AsPC-1, A549, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +5.3 | 4e-06 | 19/46 (PANC-1, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3370.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.756×** | -7.5 | 2e-11 | 24/46 (SW1417, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.587×** | -7.5 | 2e-11 | 26/47 (COLO 205, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.597×** | -7.2 | 8e-11 | 28/46 (LS 180, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.795×** | -6.2 | 9e-08 | 24/46 (LS 180, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.814×** | -5.5 | 4e-06 | 21/46 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.872× | -5.2 | 2e-05 | 9/46 (KATO III, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -4.7 | 2e-04 | 21/46 (SW1417, LS 180, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.871× | -3.7 | 0.015 | 8/46 (NCI-H2030, SNU-1, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.886× | -3.3 | 0.070 | 12/45 (RPMI-7951, CHP-212, …) | rises with dose |  |
| [[Pimitespib (drug)]] 5 µM |  | 0.807× | -3.0 | 0.14 | 6/46 (LoVo, NCI-H23, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 159 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.371× (z -11.3) |
| [[SW480 (line)]] | alt | 140 | 4 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +20.0) | [[Belinostat (drug)]] 5 µM 0.515× (z -11.2) |
| [[PANC-1 (line)]] | alt | 65.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +23.3) | — |
| [[SW1417 (line)]] | alt | 207 | 2 | 4 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.61× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -17.4) |
| [[LoVo (line)]] | wt | 90.5 | 2 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +12.3) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.54× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.427× (z -11.2) |
| [[RKO (line)]] | wt | 159 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.391× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.474× (z -10.3) |
| [[A-427 (line)]] | wt | 123 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +17.6) | [[Panobinostat (drug)]] 5 µM 0.492× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 130 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -11.8) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.146× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 40.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 19.9 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +15.8) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +11.3) | — |
| [[SNU-1 (line)]] | wt | 168 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.107× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.399× (z -9.1) |
| [[A498 (line)]] | wt | 28.2 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.9) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 49.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 45.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +15.9) | — |
| [[Hs 766T (line)]] | wt | 67.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.0) | — |
| [[HT-29 (line)]] | alt | 121 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.406× (z -9.8) |
| [[C-33 A (line)]] | alt | 89.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.4) | — |
| [[KATO III (line)]] | alt | 116 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.1) | — |
| [[NCI-H2030 (line)]] | alt | 137 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -12.0) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.513× (z -9.5) |
| [[A-172 (line)]] | wt | 81.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.9) | — |
| [[CHP-212 (line)]] | wt | 192 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -10.8) ⚠ cell-cycle shift, explains ~4% of this change |
| [[HS-578T (line)]] | alt | 60.5 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.51× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 59.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.37× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 39.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 83.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.22× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 69.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.6) | — |
| [[A549 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 188 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 93.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 75.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 77.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM169A]] | +0.72 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[GTF3C6]] | +0.68 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[TMCO4]] | +0.67 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[PARD3B]] | +0.66 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[LACTB2]] | +0.66 | +0.68 / +0.29 | both halves | 3e-04 |  |
| [[GRIP1]] | +0.65 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[SLC25A21]] | +0.64 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[IQCH-AS1]] | +0.64 | +0.65 / +0.35 | both halves | 1e-04 |  |
| [[FAIM]] | +0.63 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[DENND2D]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SLC16A9]] | +0.63 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[HNF4G]] | +0.62 | +0.57 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OGG1]] | -0.68 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[MTMR14]] | -0.66 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[SLC27A1]] | -0.65 | -0.66 / -0.38 | both halves | 7e-05 |  |
| [[GNAI2]] | -0.64 | -0.69 / -0.31 | both halves | 2e-04 | pathway: Platelet activation, signaling and aggregation |
| [[ARID3B]] | -0.63 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[DNAAF3]] | -0.63 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[ATG4B]] | -0.63 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[GNAI3]] | -0.61 | -0.68 / -0.38 | both halves | 6e-05 | pathway: Platelet activation, signaling and aggregation |
| [[PCMT1]] | -0.60 | -0.63 / -0.26 | both halves | 4e-04 |  |
| [[SH3GL1]] | -0.60 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[ATG101]] | -0.60 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[LCMT1]] | -0.60 | -0.55 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PHACTR2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KBTBD12]] | B | KBTBD12 activity lowers PHACTR2's level | lines that do not express KBTBD12 (34) vs lines expressing it (16) | 1.43× higher at baseline in the lines without KBTBD12 | 0.099 | ⚠ within organs, on part of the lines; also absent: GLP2R, SLC19A3, TSPYL5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.717). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-4.7, 7.7); signed map (24.9, -31.4). **Vector** length 127, 35.1% of its response variance represented; |z| ≥ 3 in 1,310 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +12.1 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.0 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.4 | +16.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +17.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +7.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.8 | +5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.3 | +5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +4.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.7 | -7.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.3 | -5.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.4 | -7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -7.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.4 | -3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.0 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | phosphatase and actin regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.2 — chr6:143,536,845-143,831,185 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0680; previously C6orf56 |
| Gene groups (HGNC) | Phosphatase and actin regulators |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

UniProt [O75167](https://www.uniprot.org/uniprotkb/O75167) carries no function annotation.

**Summary**, from NCBI Gene [9749](https://www.ncbi.nlm.nih.gov/gene/9749):

> Predicted to enable actin binding activity. Predicted to be involved in actin cytoskeleton organization. Predicted to be located in plasma membrane and platelet alpha granule membrane. Implicated in Parkinson's disease and multiple sclerosis. Biomarker of Alzheimer's disease. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20956) · Entrez [9749](https://www.ncbi.nlm.nih.gov/gene/9749) · UniProt [O75167](https://www.uniprot.org/uniprotkb/O75167) · Ensembl [ENSG00000112419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112419)

## Data

Gene col 3370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3370); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3370]; `tensor/DDL_lfc|DDL_z.npy` [3370]; `embed/gene_vectors.npy` [3370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3370 or target_col == 3370). Every well: [[PHACTR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHACTR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
