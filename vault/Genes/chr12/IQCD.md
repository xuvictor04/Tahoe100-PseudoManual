---
symbol: "IQCD"
type: "gene"
col: 9333
ensembl_id: "ENSG00000166578"
name: "dynein regulatory complex subunit 10"
location: "12q24.13"
module: 1
arm: "-"
pooled_cpm: 5.46
n_lines_expressing: 46
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# IQCD

*dynein regulatory complex subunit 10* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.05× (z +24.0, q 0e+00, up in 37 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.668× (z -6.0, q 1e-06, down in 23 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SW480 0.0540×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A549 0.0346×; ⚠ cell-cycle shift, would explain all of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (J82 0.0801×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPCN1]] (+0.66, fdr 1e-05, ⚠ same locus), [[KLHL15]] (+0.57, fdr 1e-05), [[FOSB]] (+0.55, fdr 1e-05), [[CCNL1]] (+0.52, fdr 3e-05); moves opposite to [[POGK]] (-0.54, fdr 4e-05), [[TSEN15]] (-0.50, fdr 2e-04), [[DCAF17]] (-0.50, fdr 4e-04).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LSR]] → it (grade B ⚠); 2 go from it, the strongest it → [[EPAS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9333.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.05×** | +24.0 | 0e+00 | 37/37 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **6.21×** | +19.2 | 0e+00 | 42/43 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.92×** | +16.7 | 0e+00 | 41/42 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.05×** | +14.7 | 0e+00 | 36/41 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.40×** | +12.4 | 5e-33 | 27/33 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.78×** | +10.3 | 7e-23 | 6/10 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.67×** | +9.9 | 3e-21 | 26/34 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.88×** | +9.3 | 6e-19 | 23/44 (SW1417, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.33×** | +8.1 | 4e-14 | 30/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +7.4 | 1e-11 | 24/42 (PANC-1, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +7.2 | 2e-11 | 16/37 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.92×** | +6.8 | 4e-10 | 11/22 (SW480, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.86×** | +6.0 | 6e-08 | 6/13 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.79×** | +5.9 | 1e-07 | 9/25 (SW1417, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.74×** | +5.8 | 2e-07 | 16/37 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.6 | 1e-04 | 13/38 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.16×** | +4.2 | 8e-04 | 5/40 (PANC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.002 | 9/41 (MIA PaCa-2, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.004 | 14/42 (NCI-H1573, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9333.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SW480 0.0540×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A549 0.0346×; ⚠ cell-cycle shift, would explain all of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (J82 0.0801×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.668×** | -6.0 | 1e-06 | 23/42 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.657×** | -4.4 | 0.003 | 18/43 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.697×** | -3.8 | 0.030 | 13/42 (HT-29, KATO III, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.695×** | -3.7 | 0.033 | 4/42 (H4, HepG2/C3A, …) | top dose only | plate-row cell shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.709×** | -3.5 | 0.059 | 10/37 (SK-MEL-2, SNU-423, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.651× | -3.2 | 0.12 | 6/43 (NCI-H2030, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.742× | -3.1 | 0.14 | 5/43 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9333. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.55 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +13.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0540× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 4.93 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.68× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.0346× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 5.51 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.41× (z +10.5) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0801× (z -10.1) |
| [[SW1417 (line)]] | alt | 8.23 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.19× (z +11.4) | — |
| [[AsPC-1 (line)]] | alt | 7.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.47× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 4.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 13.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 3.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.11× (z +10.8) | — |
| [[KATO III (line)]] | alt | 2.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +9.4) | — |
| [[LoVo (line)]] | wt | 1.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.8× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 1.92 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 31.1× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.30× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 1.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +12.4) | — |
| [[A-172 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.21 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9333), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPCN1]] | +0.66 | +0.57 / +0.69 | both halves | 1e-05 | STRING 497; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[KLHL15]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[FOSB]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CCNL1]] | +0.52 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[ITGB2]] | +0.52 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[ANKRD42]] | +0.51 | +0.47 / +0.38 | both halves | 6e-05 |  |
| [[NR4A2]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[CTNNB1]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[DALRD3]] | +0.51 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[SMAD3]] | +0.51 | +0.31 / +0.39 | both halves | 2e-04 |  |
| [[CTSV]] | +0.51 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[CST3]] | +0.50 | +0.34 / +0.45 | both halves | 1e-04 |  |
| [[STK17B]] | +0.49 | +0.43 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGK]] | -0.54 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[TSEN15]] | -0.50 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[DCAF17]] | -0.50 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[PDCD2]] | -0.49 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[DPH5]] | -0.49 | -0.19 / -0.46 | ⚠ not reproduced | 8e-04 |  |
| [[EIF3M]] | -0.49 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[ACSF3]] | -0.48 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[RIOX2]] | -0.48 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[FSD1L]] | -0.48 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[C19orf12]] | -0.45 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[VPS50]] | -0.45 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[FKTN]] | -0.45 | -0.24 / -0.43 | both halves | 4e-04 |  |
| [[CENATAC]] | -0.45 | -0.24 / -0.39 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSR]] | B | LSR activity raises IQCD's level | lines that do not express LSR (19) vs lines expressing it (31) | 1.65× lower at baseline in the lines without LSR | 0.025 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN |
| [[TOP2A]] | B | TOP2A activity lowers IQCD's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CTSV]] | B | CTSV activity raises IQCD's level | lines that do not express CTSV (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without CTSV | 0.057 | ⚠ within organs, on part of the lines; also absent: RASSF7, BMP8B, ZDHHC11B; maybe low, not absent |
| [[UPK1B]] | B | UPK1B activity raises IQCD's level | lines that do not express UPK1B (39) vs lines expressing it (11) | 1.77× lower at baseline in the lines without UPK1B | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CES1, CGA, SLC15A5; maybe low, not absent |
| [[HMGCR]] | B | HMGCR activity raises IQCD's level | compounds that target HMGCR: 2 of 2 lower it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPAS1]] | C | IQCD activity raises EPAS1's level | lines that do not express IQCD (4) vs lines expressing it (46) | 4.48× lower at baseline in the lines without IQCD | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with TGFBR2, BRCA2; also absent: RBMS1, ENSG00000235978, FBXL2; maybe low, not absent; its own permutation p |
| [[OTUD5]] | C | IQCD activity raises OTUD5's level | lines that do not express IQCD (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without IQCD | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with TGFBR2, BRCA2; also absent: RBMS1, ENSG00000235978, FBXL2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.391). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (30.2, -27.9); signed map (2.1, 16.2). **Vector** length 54.6, 7.66% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +24.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.6 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +3.2 | +6.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +9.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +12.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +7.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.8 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.1 | -0.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | dynein regulatory complex subunit 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:113,195,441-113,221,094 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DRC10, CFAP84 |
| Gene groups (HGNC) | Dynein regulatory complex; Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DY2](https://www.uniprot.org/uniprotkb/Q96DY2) (Dynein regulatory complex subunit 10):

> Component of the nexin-dynein regulatory complex (N-DRC), a key regulator of ciliary/flagellar motility which maintains the alignment and integrity of the distal axoneme and regulates microtubule sliding in motile axonemes.

**Summary**, from NCBI Gene [115811](https://www.ncbi.nlm.nih.gov/gene/115811):

> Predicted to be involved in flagellated sperm motility. Located in ciliary basal body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25168) · Entrez [115811](https://www.ncbi.nlm.nih.gov/gene/115811) · UniProt [Q96DY2](https://www.uniprot.org/uniprotkb/Q96DY2) · Ensembl [ENSG00000166578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166578)

## Data

Gene col 9333: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9333); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9333, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9333]; `tensor/DDL_lfc|DDL_z.npy` [9333]; `embed/gene_vectors.npy` [9333]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9333 or target_col == 9333). Every well: [[IQCD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQCD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
