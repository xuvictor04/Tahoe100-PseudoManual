---
symbol: "OPA3"
type: "gene"
col: 4654
ensembl_id: "ENSG00000125741"
name: "outer mitochondrial membrane lipid metabolism regulator OPA3"
location: "19q13.32"
module: 182
arm: "-"
pooled_cpm: 42.82
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# OPA3

*outer mitochondrial membrane lipid metabolism regulator OPA3* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.63× (z +11.6, q 2e-28, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.537× (z -14.8, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IBA57]] (+0.65, fdr 7e-06), [[KCNJ14]] (+0.63, fdr 1e-05), [[WDR82]] (+0.61, fdr 1e-05); moves opposite to [[LTA4H]] (-0.64, fdr 7e-06), [[PAPSS1]] (-0.63, fdr 1e-05), [[SPOPL]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 182]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4654.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +11.6 | 2e-28 | 42/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +11.5 | 2e-28 | 42/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +10.7 | 2e-24 | 38/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +10.0 | 1e-21 | 40/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.20×** | +4.4 | 0.001 | 14/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.20×** | +4.3 | 0.002 | 21/47 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +4.1 | 0.004 | 12/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.12× | +3.8 | 0.010 | 17/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.056 | 6/48 (Hs 766T, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.096 | 7/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.14× | +3.1 | 0.10 | 13/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4654.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.537×** | -14.8 | 0e+00 | 44/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.567×** | -13.5 | 7e-39 | 45/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -10.9 | 1e-25 | 37/47 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.645×** | -10.4 | 3e-23 | 42/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.658×** | -10.0 | 3e-21 | 39/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -9.3 | 2e-18 | 32/48 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.710×** | -8.1 | 4e-14 | 34/47 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.797×** | -7.6 | 2e-12 | 28/48 (Hs 766T, A-172, …) | top dose only | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.575×** | -6.9 | 4e-10 | 31/48 (PANC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.827×** | -6.4 | 1e-08 | 22/48 (LoVo, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.785×** | -5.8 | 4e-07 | 23/45 (COLO 205, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.842× | -5.7 | 4e-07 | 22/48 (NCI-H2030, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.821×** | -4.7 | 1e-04 | 20/48 (SW 1088, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.826×** | -4.3 | 6e-04 | 20/47 (HepG2/C3A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 0.838× | -4.2 | 0.001 | 19/48 (NCI-H2030, C32, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.870× | -3.3 | 0.030 | 11/48 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.911× | -3.1 | 0.052 | 8/48 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 0.873× | -3.0 | 0.064 | 9/47 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.881× | -3.0 | 0.069 | 10/48 (PANC-1, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.1 | 11 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.47× (z +24.5) | — |
| [[A-427 (line)]] | wt | 43.2 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -11.3) |
| [[HOP62 (line)]] | alt | 88.9 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.73× (z +13.1) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 82.6 | 2 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.369× (z -12.2) |
| [[PANC-1 (line)]] | alt | 44.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.250× (z -18.2) |
| [[MIA PaCa-2 (line)]] | alt | 45.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.376× (z -10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.382× (z -10.0) |
| [[A498 (line)]] | wt | 39.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 48.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -12.9) |
| [[HS-578T (line)]] | alt | 43.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -9.1) |
| [[LoVo (line)]] | wt | 40.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.424× (z -9.5) |
| [[A549 (line)]] | wt | 59.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -9.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 54.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 44.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -14.1) |
| [[Hs 766T (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.395× (z -11.6) ⚠ cell-cycle shift, explains ~15% of this change |
| [[J82 (line)]] | alt | 48.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.431× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 64.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -9.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 39.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SNU-1 (line)]] | wt | 49.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -10.7) |
| [[SW 900 (line)]] | alt | 45.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.373× (z -9.1) |
| [[A-172 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 40.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IBA57]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[KCNJ14]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[WDR82]] | +0.61 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PPP6R2]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[RBX1]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[NCOA5]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[CPSF7]] | +0.58 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[PROSER3]] | +0.58 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[DDX19A]] | +0.58 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[CRK]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TERF2]] | +0.58 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[XIAP]] | +0.58 | +0.56 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTA4H]] | -0.64 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[PAPSS1]] | -0.63 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[SPOPL]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[MINDY3]] | -0.61 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[FXR1]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[CSNK1G3]] | -0.57 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[PRKAB2]] | -0.57 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[NTAN1]] | -0.56 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[OTULIN]] | -0.55 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[USP3]] | -0.55 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[KDM1A]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[RTCA]] | -0.54 | -0.56 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises OPA3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **-** arm (projection on the module's main direction -0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-4.8, -7.2); signed map (1.7, -6.0). **Vector** length 98.8, 23.3% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +7.9 | +11.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.7 | +10.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.4 | +11.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.9 | +4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +10.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.0 | +3.1 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +1.9 | +2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +0.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -4.5 | -7.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.2 | -4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -9.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.4 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.5 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | outer mitochondrial membrane lipid metabolism regulator OPA3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,527,767-45,602,212 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22187, MGA3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6K4](https://www.uniprot.org/uniprotkb/Q9H6K4) (Optic atrophy 3 protein):

> May play some role in mitochondrial processes.

**Summary**, from NCBI Gene [80207](https://www.ncbi.nlm.nih.gov/gene/80207):

> The mouse ortholog of this protein co-purifies with the mitochondrial inner membrane. Mutations in this gene have been shown to result in 3-methylglutaconic aciduria type III and autosomal dominant optic atrophy and cataract. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:8142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8142) · Entrez [80207](https://www.ncbi.nlm.nih.gov/gene/80207) · UniProt [Q9H6K4](https://www.uniprot.org/uniprotkb/Q9H6K4) · Ensembl [ENSG00000125741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125741)

## Data

Gene col 4654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4654); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4654]; `tensor/DDL_lfc|DDL_z.npy` [4654]; `embed/gene_vectors.npy` [4654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4654 or target_col == 4654). Every well: [[OPA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OPA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
