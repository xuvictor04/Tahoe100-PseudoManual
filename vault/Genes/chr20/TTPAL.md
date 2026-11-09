---
symbol: "TTPAL"
type: "gene"
col: 4482
ensembl_id: "ENSG00000124120"
name: "alpha tocopherol transfer protein like"
location: "20q13.12"
module: 16
arm: "+"
pooled_cpm: 20.23
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 5
n_dd_up_clean: 22
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# TTPAL

*alpha tocopherol transfer protein like* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.12× (z +11.4, q 1e-27, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.93× (z +9.6, q 2e-19, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.542× (z -9.3, q 6e-18, down in 30 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.794× (z -5.0, q 1e-04, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM185B]] (+0.75, fdr 7e-06), [[ZKSCAN2]] (+0.65, fdr 7e-06), [[EIF6]] (+0.64, fdr 1e-05); moves opposite to [[CNNM2]] (-0.66, fdr 7e-06), [[ZFP14]] (-0.63, fdr 1e-05), [[UBE4B]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4482.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.12×** | +11.4 | 1e-27 | 44/48 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.11×** | +11.3 | 2e-27 | 40/48 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +9.6 | 2e-19 | 37/47 (BT-474, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +8.5 | 2e-15 | 33/46 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.87×** | +8.1 | 6e-14 | 34/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +8.0 | 1e-13 | 32/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +7.6 | 2e-12 | 33/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.68×** | +7.6 | 2e-12 | 37/44 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +7.3 | 1e-11 | 24/47 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.61×** | +7.2 | 3e-11 | 29/47 (SW480, Hs 766T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +6.5 | 3e-09 | 25/47 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~24% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.5 | 2e-06 | 20/48 (SW480, A-427, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.49×** | +5.1 | 1e-05 | 24/47 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +5.1 | 2e-05 | 23/48 (C32, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.37×** | +4.8 | 7e-05 | 19/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.011 | 14/44 (A-427, C32, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.017 | 9/48 (SW480, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.017 | 16/47 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.017 | 6/45 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.018 | 10/45 (SW480, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.018 | 10/47 (A-427, SW480, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.025 | 5/48 (SW48, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4482.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.542×** | -9.3 | 6e-18 | 30/46 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.693×** | -5.4 | 2e-05 | 24/42 (J82, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.794×** | -5.0 | 1e-04 | 25/48 (C32, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.727×** | -4.9 | 2e-04 | 20/47 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -4.3 | 0.002 | 4/48 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.766×** | -4.1 | 0.005 | 20/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.867× | -3.1 | 0.17 | 12/48 (PANC-1, KATO III, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4482. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 18.5 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.5) | [[Saquinavir (drug)]] 5 µM 0.356× (z -8.7) |
| [[SW480 (line)]] | alt | 18.9 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +8.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 19.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 56.5 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.38× (z +8.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.291× (z -8.7) ⚠ toxic |
| [[C32 (line)]] | wt | 18.6 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0881× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 54.3 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -11.4) ⚠ cell-cycle shift, explains ~76% of this change |
| [[SW48 (line)]] | wt | 16.7 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0644× (z -10.7) |
| [[A-172 (line)]] | wt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +8.8) | — |
| [[A498 (line)]] | wt | 16.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.59× (z +8.6) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.05 µM 0.0481× (z -11.3) |
| [[J82 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.229× (z -10.4) ⚠ toxic |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0754× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.319× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -8.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4482), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185B]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[ZKSCAN2]] | +0.65 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[EIF6]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[SOWAHC]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SLC35A4]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ZNF121]] | +0.60 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TRMT6]] | +0.59 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[KRT8P12]] | +0.59 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[GSS]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[EIF2S1]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ZNF562]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ETS1]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNNM2]] | -0.66 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[ZFP14]] | -0.63 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[UBE4B]] | -0.61 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[APTR]] | -0.61 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[CACUL1]] | -0.60 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[TESK2]] | -0.60 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[MZT2B]] | -0.59 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[HOXB5]] | -0.59 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[PPP1R12B]] | -0.59 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.59 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[BNIPL]] | -0.58 | -0.42 / -0.60 | both halves | 4e-05 | same gene group |
| [[AGAP3]] | -0.58 | -0.67 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TTPAL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HOXB5]], [[HOXB6]] | B | HOXB5, HOXB6 activity lowers TTPAL's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 1.24× higher at baseline in the lines without HOXB5, HOXB6 | 0.097 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-2.7, -18.6); signed map (0.7, -31.5). **Vector** length 97.8, 22.6% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.2 | +8.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.7 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +5.0 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +8.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +2.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -9.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.5 | -5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -5.0 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | -3.1 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.7 | -1.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | alpha tocopherol transfer protein like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:44,475,874-44,494,603 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ179M20.3; previously C20orf121 |
| Gene groups (HGNC) | CRAL-TRIO lipid binding domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTX7](https://www.uniprot.org/uniprotkb/Q9BTX7) (Alpha-tocopherol transfer protein-like):

> May act as a protein that binds a hydrophobic ligand.

**Summary**, from NCBI Gene [79183](https://www.ncbi.nlm.nih.gov/gene/79183):

> Predicted to enable phosphatidylinositol bisphosphate binding activity. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16114) · Entrez [79183](https://www.ncbi.nlm.nih.gov/gene/79183) · UniProt [Q9BTX7](https://www.uniprot.org/uniprotkb/Q9BTX7) · Ensembl [ENSG00000124120](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124120)

## Data

Gene col 4482: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4482); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4482, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4482]; `tensor/DDL_lfc|DDL_z.npy` [4482]; `embed/gene_vectors.npy` [4482]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4482 or target_col == 4482). Every well: [[TTPAL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTPAL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
