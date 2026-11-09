---
symbol: "SIM2"
type: "gene"
col: 8240
ensembl_id: "ENSG00000159263"
name: "SIM bHLH transcription factor 2"
location: "21q22.13"
module: 46
arm: "+"
pooled_cpm: 19.62
n_lines_expressing: 41
n_dd_up: 5
n_dd_down: 27
n_dd_up_clean: 3
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# SIM2

*SIM bHLH transcription factor 2* — 21q22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +12.4, q 2e-32, up in 26 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.341× (z -19.4, q 0e+00, down in 32 of 38 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIX4]] (+0.58, fdr 3e-05), [[TRIM8]] (+0.57, fdr 2e-05), [[EPS15-AS1]] (+0.57, fdr 7e-05); moves opposite to [[COMMD2]] (-0.53, fdr 2e-04), [[VTA1]] (-0.52, fdr 1e-04), [[SMIM8]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KCNQ4]] → it (grade B ⚠); 2 go from it, the strongest it → [[AGK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8240.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +12.4 | 2e-32 | 26/38 (SW1417, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.4 | 4e-08 | 16/36 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +5.3 | 2e-05 | 17/38 (CFPAC-1, H4, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.3 | 0.003 | 12/37 (KATO III, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.22×** | +3.5 | 0.048 | 6/39 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.15 | 3/39 (NCI-H460, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8240.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.341×** | -19.4 | 0e+00 | 32/38 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.391×** | -16.9 | 0e+00 | 33/38 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.480×** | -13.2 | 1e-37 | 32/38 (LoVo, LS 180, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.586×** | -9.6 | 8e-20 | 27/38 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.612×** | -8.5 | 2e-15 | 21/34 (A-427, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.444×** | -7.6 | 2e-12 | 22/37 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.756×** | -7.2 | 7e-11 | 23/39 (LS 180, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.676×** | -7.1 | 1e-10 | 19/38 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.516×** | -6.2 | 3e-08 | 21/36 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.519×** | -6.2 | 3e-08 | 20/36 (SW48, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.703×** | -6.1 | 5e-08 | 18/37 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.537×** | -5.9 | 2e-07 | 17/36 (Panc 03.27, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.585×** | -5.0 | 2e-05 | 18/34 (SW480, HCT15, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -5.0 | 2e-05 | 14/38 (LS 180, HOP62, …) | two highest doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.603×** | -4.8 | 7e-05 | 15/35 (A549, A-427, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.693×** | -4.7 | 8e-05 | 11/39 (LoVo, A549, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.761×** | -4.7 | 1e-04 | 14/37 (LoVo, PANC-1, …) | all doses, flat | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **0.626×** | -4.4 | 3e-04 | 15/35 (SW1417, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.731×** | -4.0 | 0.002 | 9/37 (SNU-423, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 105 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.202× (z -15.0) |
| [[MIA PaCa-2 (line)]] | alt | 30.5 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0562× (z -21.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0963× (z -17.5) |
| [[Hs 766T (line)]] | wt | 53.7 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -14.9) |
| [[LoVo (line)]] | wt | 27.1 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -14.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.238× (z -11.0) |
| [[A-427 (line)]] | wt | 14.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -11.7) |
| [[KATO III (line)]] | alt | 35.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.136× (z -16.1) |
| [[SW1417 (line)]] | alt | 35.9 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.347× (z -9.6) |
| [[C-33 A (line)]] | alt | 38.8 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -11.8) |
| [[HOP62 (line)]] | alt | 32.7 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -11.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.248× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 29.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -10.2) |
| [[RKO (line)]] | wt | 40.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.310× (z -8.6) |
| [[A549 (line)]] | wt | 23.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -9.0) |
| [[BT-474 (line)]] | alt | 48.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -10.9) |
| [[C32 (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.154× (z -8.6) ⚠ cell-cycle shift, explains ~17% of this change |
| [[CFPAC-1 (line)]] | alt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +13.8) | — |
| [[H4 (line)]] | wt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 14.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.185× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -8.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 19.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -12.8) |
| [[PANC-1 (line)]] | alt | 15.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.0) | — |
| [[SW48 (line)]] | wt | 38.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +10.2) | — |
| [[SW480 (line)]] | alt | 9.01 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIX4]] | +0.58 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[TRIM8]] | +0.57 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[EPS15-AS1]] | +0.57 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[SETD1B]] | +0.55 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[ZIC2]] | +0.55 | +0.58 / +0.29 | both halves | 3e-04 |  |
| [[CABLES1]] | +0.54 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[DPY19L2P3]] | +0.53 | +0.29 / +0.48 | both halves | 3e-04 |  |
| [[MACROD1]] | +0.52 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[FOXP4-AS1]] | +0.50 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[MTURN]] | +0.50 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[HOXC9]] | +0.50 | +0.29 / +0.44 | both halves | 2e-04 |  |
| [[KLRK1-AS1]] | +0.50 | +0.28 / +0.29 | both halves | 3e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD2]] | -0.53 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[VTA1]] | -0.52 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[SMIM8]] | -0.51 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[ATG5]] | -0.50 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[PPIL2]] | -0.48 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[TMEM161B]] | -0.48 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[POT1]] | -0.48 | -0.37 / -0.32 | both halves | 1e-04 |  |
| [[NDUFA12]] | -0.48 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[ASCC2]] | -0.47 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[GUSBP1]] | -0.47 | -0.29 / -0.30 | both halves | 3e-04 |  |
| [[TBC1D7]] | -0.46 | -0.26 / -0.46 | both halves | 3e-04 |  |
| [[AP2S1]] | -0.46 | -0.46 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[AGK]] | -0.46 | -0.28 / -0.46 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNQ4]] | B | KCNQ4 activity raises SIM2's level | lines that do not express KCNQ4 (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without KCNQ4 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000248993; maybe low, not absent; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGK]] | B | SIM2 activity raises AGK's level | lines that do not express SIM2 (9) vs lines expressing it (41) | 1.06× lower at baseline in the lines without SIM2 | 0.057 | ⚠ within organs, on part of the lines; also absent: SMC1B |
| [[KMT2E-AS1]] | B | SIM2 activity raises KMT2E-AS1's level | lines that do not express SIM2 (9) vs lines expressing it (41) | 1.31× lower at baseline in the lines without SIM2 | 0.064 | ⚠ within organs, on part of the lines; also absent: SMC1B |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.476). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (15.0, 8.8); signed map (19.2, -8.4). **Vector** length 79.2, 15.5% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +12.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.2 | +1.3 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.1 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.9 | +1.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -19.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.0 | -16.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -9.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -6.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -6.2 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -7.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.7 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | SIM bHLH transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.13 — chr21:36,699,115-36,749,917 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC119447, bHLHe15; previously SIM |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; PAS domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14190](https://www.uniprot.org/uniprotkb/Q14190) (Single-minded homolog 2):

> Transcription factor that may be a master gene of CNS development in cooperation with Arnt. It may have pleiotropic effects in the tissues expressed during development.

**Summary**, from NCBI Gene [6493](https://www.ncbi.nlm.nih.gov/gene/6493):

> This gene represents a homolog of the Drosophila single-minded (sim) gene, which encodes a transcription factor that is a master regulator of neurogenesis. The encoded protein is ubiquitinated by RING-IBR-RING-type E3 ubiquitin ligases, including the parkin RBR E3 ubiquitin protein ligase. This gene maps within the so-called Down syndrome chromosomal region, and is thus thought to contribute to some specific Down syndrome phenotypes. Alternative splicing of this gene results in multiple …

**Accessions** — [HGNC:10883](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10883) · Entrez [6493](https://www.ncbi.nlm.nih.gov/gene/6493) · UniProt [Q14190](https://www.uniprot.org/uniprotkb/Q14190) · Ensembl [ENSG00000159263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159263)

## Data

Gene col 8240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8240); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8240]; `tensor/DDL_lfc|DDL_z.npy` [8240]; `embed/gene_vectors.npy` [8240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8240 or target_col == 8240). Every well: [[SIM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
