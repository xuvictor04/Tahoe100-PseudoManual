---
symbol: "MED21"
type: "gene"
col: 7672
ensembl_id: "ENSG00000152944"
name: "mediator complex subunit 21"
location: "12p11.23"
module: 15
arm: "+"
pooled_cpm: 46.81
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# MED21

*mediator complex subunit 21* — 12p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.27× (z +19.3, q 0e+00, up in 45 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.07× (z +17.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.775× (z -6.2, q 3e-07, down in 25 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.689× (z -4.8, q 5e-04, down in 19 of 48 measured lines).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRG1HP]] (+0.58, fdr 2e-05), [[H3-3A-DT]] (+0.55, fdr 1e-05), [[LINC00115]] (+0.53, fdr 2e-04); moves opposite to [[GNL2]] (-0.52, fdr 4e-05), [[GNL3]] (-0.48, fdr 2e-04), [[NAT10]] (-0.44, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[INTS13]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7672.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +19.3 | 0e+00 | 45/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.07×** | +17.8 | 0e+00 | 47/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +16.3 | 0e+00 | 46/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.93×** | +16.1 | 0e+00 | 45/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +14.9 | 0e+00 | 39/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +10.7 | 6e-25 | 36/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +9.0 | 2e-17 | 27/48 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +8.4 | 2e-15 | 29/45 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +8.1 | 4e-14 | 36/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +8.0 | 8e-14 | 30/48 (COLO 205, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +7.8 | 2e-13 | 30/47 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.5 | 3e-12 | 29/48 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **1.37×** | +7.4 | 6e-12 | 24/41 (LS 180, AsPC-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +6.5 | 3e-09 | 30/47 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +6.3 | 1e-08 | 17/48 (C32, RKO, …) | top dose only | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +6.0 | 9e-08 | 24/48 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +5.4 | 2e-06 | 25/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +4.8 | 5e-05 | 23/48 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +4.6 | 1e-04 | 22/48 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7672.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.775×** | -6.2 | 3e-07 | 25/48 (SW480, KATO III, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.689×** | -4.8 | 5e-04 | 19/48 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.790×** | -4.1 | 0.008 | 17/48 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.730×** | -4.0 | 0.008 | 18/48 (SHP-77, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.740×** | -3.8 | 0.013 | 18/48 (SNU-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.811×** | -3.7 | 0.024 | 7/48 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.829×** | -3.3 | 0.086 | 11/48 (PANC-1, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | 0.786× | -3.1 | 0.14 | 11/47 (A-427, LoVo, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7672. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 129 | 5 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.24× (z +13.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.59× (z +11.3) | — |
| [[LoVo (line)]] | wt | 61.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.60× (z +13.2) | — |
| [[A-427 (line)]] | wt | 73.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -23.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.402× (z -14.9) |
| [[A498 (line)]] | wt | 28.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 29.9 | 3 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.44× (z +9.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 3.07× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 36.7 | 3 (1 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.78× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 31.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.41× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 53.1 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.95× (z +11.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 2.11× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 49.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 25.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 49.7 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.78× (z +9.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 50.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 29.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.0) | [[Docetaxel (drug)]] 0.05 µM 0.123× (z -13.8) ⚠ transcription drop; cell-cycle shift, explains ~3% of this change |
| [[SW 900 (line)]] | alt | 77.1 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.13× (z +10.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +10.0) | — |
| [[A-172 (line)]] | wt | 26.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 59.6 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.183× (z -8.8) |
| [[C-33 A (line)]] | alt | 55.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[C32 (line)]] | wt | 25.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 31.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.84× (z +8.5) ⚠ toxic | — |
| [[KATO III (line)]] | alt | 42.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.55× (z +12.4) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 34.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.57× (z +9.8) ⚠ toxic | — |
| [[NCI-H1573 (line)]] | alt | 39.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.04× (z +10.1) ⚠ toxic | — |
| [[NCI-H2347 (line)]] | alt | 37.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.64× (z +10.2) ⚠ toxic | — |
| [[RKO (line)]] | wt | 54.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.76× (z +11.9) ⚠ toxic | — |
| [[SHP-77 (line)]] | alt | 51.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 39.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 40.9 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.292× (z -8.6) |
| [[SW1417 (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.75× (z +9.5) ⚠ toxic | — |
| [[A549 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7672), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRG1HP]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[H3-3A-DT]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[LINC00115]] | +0.53 | +0.31 / +0.43 | both halves | 2e-04 |  |
| [[ZBTB44]] | +0.52 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[PPM1A]] | +0.51 | +0.30 / +0.43 | both halves | 2e-04 |  |
| [[C8orf44-SGK3]] | +0.50 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[ZNF740]] | +0.50 | +0.27 / +0.48 | both halves | 3e-04 |  |
| [[YIPF4]] | +0.49 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[ZBTB26]] | +0.49 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[NPIPB2]] | +0.49 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[NIPSNAP3A]] | +0.48 | +0.32 / +0.39 | both halves | 2e-04 |  |
| [[CCNY-AS1]] | +0.48 | +0.37 / +0.44 | both halves | 8e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL2]] | -0.52 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[GNL3]] | -0.48 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[NAT10]] | -0.44 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[PIK3R1]] | -0.44 | -0.24 / -0.35 | both halves | 4e-04 |  |
| [[TRIM16]] | -0.44 | -0.17 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[SCFD2]] | -0.43 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[RIN1]] | -0.43 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[GALE]] | -0.42 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[SND1]] | -0.42 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[RPF2]] | -0.42 | -0.21 / -0.46 | both halves | 7e-04 |  |
| [[GPHN]] | -0.42 | -0.10 / -0.49 | ⚠ not reproduced | 0.003 |  |
| [[DMXL2]] | -0.41 | -0.26 / -0.35 | both halves | 3e-04 |  |
| [[IMP4]] | -0.41 | -0.29 / -0.31 | both halves | 2e-04 |  |
| [[CCDC28B]] | -0.41 | -0.25 / -0.27 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MED21's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INTS13]] | C | MED21's natural level strengthens INTS13's drug response | MED21's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.13; direction not clear | 0.031 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.354). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-6.6, 24.3); signed map (0.8, -0.2). **Vector** length 78.3, 16.2% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.4 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +8.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.2 | +6.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.1 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.8 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.2 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.6 | -6.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +0.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.2 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.1 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.23 — chr12:27,022,546-27,066,343 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRB7; previously SURB7 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 8 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13503](https://www.uniprot.org/uniprotkb/Q13503) (Mediator of RNA polymerase II transcription subunit 21):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [9412](https://www.ncbi.nlm.nih.gov/gene/9412):

> This gene encodes a member of the mediator complex subunit 21 family. The encoded protein interacts with the human RNA polymerase II holoenzyme and is involved in transcriptional regulation of RNA polymerase II transcribed genes. A pseudogene of this gene is located on chromosome 8. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:11473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11473) · Entrez [9412](https://www.ncbi.nlm.nih.gov/gene/9412) · UniProt [Q13503](https://www.uniprot.org/uniprotkb/Q13503) · Ensembl [ENSG00000152944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152944)

## Data

Gene col 7672: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7672); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7672, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7672]; `tensor/DDL_lfc|DDL_z.npy` [7672]; `embed/gene_vectors.npy` [7672]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7672 or target_col == 7672). Every well: [[MED21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
