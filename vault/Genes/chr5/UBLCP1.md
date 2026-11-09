---
symbol: "UBLCP1"
type: "gene"
col: 8933
ensembl_id: "ENSG00000164332"
name: "ubiquitin like domain containing CTD phosphatase 1"
location: "5q33.3"
module: 28
arm: "+"
pooled_cpm: 33.72
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# UBLCP1

*ubiquitin like domain containing CTD phosphatase 1* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.55× (z +14.1, q 2e-42, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 0.772× (z -3.9, q 0.049, down in 19 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ritonavir (drug)]] 0.5 µM in 1 line (SW 1271 0.0695×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.242×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Bortezomib (drug)]] 5 µM in 1 line (SHP-77 0.0898×; ⚠ toxic; cell-cycle shift, explains ~32% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 1271 0.114×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATAD1]] (+0.58, fdr 2e-05), [[MTMR6]] (+0.58, fdr 1e-05), [[TMEM128]] (+0.56, fdr 1e-05); moves opposite to [[HSPA1B]] (-0.50, fdr 3e-05), [[BCO2]] (-0.47, fdr 1e-04), [[GLA]] (-0.46, fdr 1e-04).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8933.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.55×** | +14.1 | 2e-42 | 46/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +12.6 | 1e-33 | 39/48 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.19×** | +11.8 | 8e-30 | 45/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.25×** | +11.8 | 8e-30 | 46/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.11×** | +11.2 | 3e-27 | 45/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +11.1 | 9e-27 | 41/46 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +10.1 | 4e-22 | 42/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +8.2 | 1e-14 | 35/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +8.0 | 5e-14 | 35/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.76×** | +8.0 | 7e-14 | 24/32 (SW480, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.63×** | +7.1 | 7e-11 | 34/48 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +7.0 | 1e-10 | 3/48 (C32, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.17×** | +6.1 | 5e-08 | 30/49 (LoVo, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +6.0 | 6e-08 | 31/48 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.52×** | +6.0 | 6e-08 | 31/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +5.8 | 2e-07 | 33/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.7 | 5e-07 | 28/48 (HOP62, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +5.4 | 2e-06 | 24/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +5.0 | 2e-05 | 31/48 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.76×** | +4.4 | 2e-04 | 21/48 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.007 | 18/47 (A498, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.4 | 0.013 | 16/48 (HT-29, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8933.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ritonavir (drug)]] 0.5 µM in 1 line (SW 1271 0.0695×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.242×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Bortezomib (drug)]] 5 µM in 1 line (SHP-77 0.0898×; ⚠ toxic; cell-cycle shift, explains ~32% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 1271 0.114×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.772×** | -3.9 | 0.049 | 19/48 (HEC-1-A, HOP62, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | 0.653× | -3.4 | 0.21 | 18/43 (HepG2/C3A, RKO, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.749× | -3.1 | 0.33 | 11/48 (RPMI-7951, PANC-1, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8933. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.0 | 8 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.84× (z +13.1) | — |
| [[HEC-1-A (line)]] | alt | 26.2 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.02× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 78.0 | 4 (4 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.42× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | [[Dinaciclib (drug)]] 5 µM 0.242× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 33.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.6) | — |
| [[A498 (line)]] | wt | 30.9 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.36× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 28.1 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.65× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 24.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 52.3 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.70× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 44.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +8.9) | — |
| [[SW 1271 (line)]] | alt | 70.2 | 0 | 2 | — | [[Ritonavir (drug)]] 0.5 µM 0.0695× (z -10.4) |
| [[SW 900 (line)]] | alt | 27.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 32.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 34.5 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.99× (z +8.5) | — |
| [[KATO III (line)]] | alt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.1) | — |
| [[LoVo (line)]] | wt | 40.8 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.92× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 41.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0898× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 60.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.63× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 20.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.03× (z +8.5) | — |
| [[A-427 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8933), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAD1]] | +0.58 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[MTMR6]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[TMEM128]] | +0.56 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[RNF141]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[CHAMP1]] | +0.53 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[DGUOK]] | +0.50 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[AAGAB]] | +0.49 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ERMARD]] | +0.49 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[INTS12]] | +0.48 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[TMEM209]] | +0.48 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[ARV1]] | +0.48 | +0.56 / +0.38 | both halves | 6e-05 |  |
| [[ZNF81]] | +0.47 | +0.56 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA1B]] | -0.50 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[BCO2]] | -0.47 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[GLA]] | -0.46 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[HSPA1A]] | -0.45 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[DNAJA1]] | -0.44 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[TUBB3]] | -0.43 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[PDXK]] | -0.43 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[WHRN]] | -0.43 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[HSP90AB1]] | -0.41 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[CDRT4]] | -0.40 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[DNAJB1]] | -0.40 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[HSPE1]] | -0.40 | -0.36 / -0.43 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UBLCP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[WHRN]] | C | WHRN activity raises UBLCP1's level | lines that do not express WHRN (4) vs lines expressing it (46) | 2.02× lower at baseline in the lines without WHRN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.282). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.3, 20.6); signed map (7.0, -27.7). **Vector** length 87.2, 21.8% of its response variance represented; |z| ≥ 3 in 1,168 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +10.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +11.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.6 | +6.1 |
|  | [[Lopinavir (drug)]] 5 µM |  | +2.2 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +0.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.9 | +1.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | +0.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | -3.5 | -1.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | +1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -0.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin like domain containing CTD phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:159,263,290-159,286,036 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10067, CPUB1 |
| Gene groups (HGNC) | CTD family phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVY7](https://www.uniprot.org/uniprotkb/Q8WVY7) (Ubiquitin-like domain-containing CTD phosphatase 1):

> Dephosphorylates 26S nuclear proteasomes, thereby decreasing their proteolytic activity. Recruited to the 19S regulatory particle of the 26S proteasome through its interaction with 19S component PSMD2/RPN1. Once recruited, dephosphorylates 19S component PSMC2/RPT1 which impairs PSMC2 ATPase activity and disrupts 26S proteasome assembly. Has also been reported to stimulate the proteolytic activity of the 26S proteasome.

**Summary**, from NCBI Gene [134510](https://www.ncbi.nlm.nih.gov/gene/134510):

> Enables proteasome regulatory particle binding activity and protein serine/threonine phosphatase activity. Involved in negative regulation of ATP-dependent activity and regulation of proteasome assembly. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28110](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28110) · Entrez [134510](https://www.ncbi.nlm.nih.gov/gene/134510) · UniProt [Q8WVY7](https://www.uniprot.org/uniprotkb/Q8WVY7) · Ensembl [ENSG00000164332](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164332)

## Data

Gene col 8933: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8933); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8933, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8933]; `tensor/DDL_lfc|DDL_z.npy` [8933]; `embed/gene_vectors.npy` [8933]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8933 or target_col == 8933). Every well: [[UBLCP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBLCP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
