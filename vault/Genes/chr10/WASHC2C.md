---
symbol: "WASHC2C"
type: "gene"
col: 10278
ensembl_id: "ENSG00000172661"
name: "WASH complex subunit 2C"
location: "10q11.22"
module: 122
arm: "+"
pooled_cpm: 22.52
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# WASHC2C

*WASH complex subunit 2C* — 10q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +11.6, q 3e-28, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.531× (z -17.8, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASHC2A]] (+0.98, fdr 7e-06), [[ATP6V1C1]] (+0.76, fdr 7e-06), [[RRAGB]] (+0.74, fdr 7e-06); moves opposite to [[LSM4]] (-0.56, fdr 1e-05), [[JPT1]] (-0.51, fdr 4e-04), [[CD320]] (-0.51, fdr 3e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10278.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +11.6 | 3e-28 | 27/47 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.49×** | +11.2 | 1e-26 | 35/47 (NCI-H460, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +9.5 | 3e-19 | 29/46 (HT-29, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.55×** | +8.7 | 6e-16 | 37/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +8.2 | 2e-14 | 22/33 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +6.8 | 8e-10 | 22/40 (C32, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +6.4 | 1e-08 | 23/46 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.41×** | +6.3 | 2e-08 | 23/47 (PANC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.36×** | +6.1 | 7e-08 | 21/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +5.5 | 2e-06 | 22/47 (A-172, KATO III, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.20× | +5.0 | 4e-05 | 13/47 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.18× | +4.5 | 3e-04 | 14/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.35×** | +4.4 | 5e-04 | 9/47 (NCI-H460, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.25×** | +4.3 | 6e-04 | 12/47 (SNU-423, PANC-1, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.17× | +4.2 | 8e-04 | 9/47 (PANC-1, Hs 766T, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.003 | 13/47 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.005 | 13/46 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.005 | 9/47 (BT-474, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.006 | 12/47 (LoVo, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.011 | 11/47 (A-172, C32, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.013 | 13/45 (RPMI-7951, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.026 | 11/45 (NCI-H2030, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10278.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.531×** | -17.8 | 0e+00 | 45/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.558×** | -11.6 | 1e-28 | 39/47 (SW48, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.727×** | -6.1 | 2e-07 | 23/45 (SNU-423, AN3 CA, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.752×** | -5.7 | 2e-06 | 20/47 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **0.790×** | -4.7 | 3e-04 | 19/45 (LS 180, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.794×** | -4.6 | 4e-04 | 18/47 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.814×** | -4.1 | 0.003 | 15/47 (SNU-423, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.830×** | -3.7 | 0.013 | 9/47 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.843× | -3.4 | 0.039 | 10/46 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.658×** | -3.3 | 0.063 | 5/45 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.663×** | -3.2 | 0.069 | 9/45 (MIA PaCa-2, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.853× | -3.2 | 0.069 | 14/45 (SNU-423, SW 900, …) | rises with dose |  |
| [[Olanzapine (drug)]] 5 µM |  | 0.899× | -3.0 | 0.11 | 6/47 (SW 1271, A-427, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10278. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.84× (z +30.4) | — |
| [[A-427 (line)]] | wt | 21.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 25.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[SNU-423 (line)]] | alt | 73.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.0) | [[Belinostat (drug)]] 5 µM 0.377× (z -9.7) ⚠ cell-cycle shift, explains ~89% of this change |
| [[A-172 (line)]] | wt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.8) | — |
| [[A498 (line)]] | wt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 57.2 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0637× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0903× (z -9.3) |
| [[COLO 205 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 15.5 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.437× (z -8.6) |
| [[Hs 766T (line)]] | wt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +15.4) | — |
| [[HT-29 (line)]] | alt | 19.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.48× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.173× (z -10.3) |
| [[J82 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +12.8) | — |
| [[LOX-IMVI (line)]] | wt | 20.7 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.334× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +16.4) | — |
| [[PANC-1 (line)]] | alt | 32.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.26× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 23.4 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.243× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +10.3) | — |
| [[SW48 (line)]] | wt | 20.6 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0912× (z -11.2) |
| [[SW480 (line)]] | alt | 29.2 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.389× (z -12.9) |
| [[A549 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10278), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASHC2A]] | +0.98 | +0.96 / +0.98 | both halves | 7e-06 | same gene group; STRING 963 |
| [[ATP6V1C1]] | +0.76 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[RRAGB]] | +0.74 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[HEXA]] | +0.71 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[VPS33A]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[HPS1]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[VPS11]] | +0.65 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[CLN3]] | +0.65 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[SLC38A7]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[AP5Z1]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ALG1]] | +0.62 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[TMEM192]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM4]] | -0.56 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[JPT1]] | -0.51 | -0.25 / -0.59 | both halves | 4e-04 |  |
| [[CD320]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[CCNYL1]] | -0.50 | -0.28 / -0.61 | both halves | 3e-04 |  |
| [[EXTL3]] | -0.50 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[TXNDC17]] | -0.50 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[EHD4]] | -0.49 | -0.51 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers WASHC2C's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises WASHC2C's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises WASHC2C's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.866). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-19.2, 14.0); signed map (-9.7, -19.3). **Vector** length 110, 26.1% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +8.7 | +11.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +7.3 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +8.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +3.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.7 | -17.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.8 | -11.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.1 | -5.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | WASH complex subunit 2C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.22 — chr10:45,727,200-45,792,964 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VPEF, KIAA0592; previously FAM21C |
| Gene groups (HGNC) | WASH complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4E1](https://www.uniprot.org/uniprotkb/Q9Y4E1) (WASH complex subunit 2C):

> Acts as a component of the WASH core complex that functions as a nucleation-promoting factor (NPF) at the surface of endosomes, where it recruits and activates the Arp2/3 complex to induce actin polymerization, playing a key role in the fission of tubules that serve as transport intermediates during endosome sorting. Mediates the recruitment of the WASH core complex to endosome membranes via binding to phospholipids and VPS35 of the retromer CSC. Mediates the recruitment of the F-actin-capping …

**Summary**, from NCBI Gene [253725](https://www.ncbi.nlm.nih.gov/gene/253725):

> Enables phosphatidylinositol phosphate binding activity; phosphatidylinositol-3,4-bisphosphate binding activity; and retromer complex binding activity. Involved in several processes, including endosomal transport; negative regulation of barbed-end actin filament capping; and regulation of substrate adhesion-dependent cell spreading. Located in early endosome. Part of WASH complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23414](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23414) · Entrez [253725](https://www.ncbi.nlm.nih.gov/gene/253725) · UniProt [Q9Y4E1](https://www.uniprot.org/uniprotkb/Q9Y4E1) · Ensembl [ENSG00000172661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172661)

## Data

Gene col 10278: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10278); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10278, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10278]; `tensor/DDL_lfc|DDL_z.npy` [10278]; `embed/gene_vectors.npy` [10278]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10278 or target_col == 10278). Every well: [[WASHC2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WASHC2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
