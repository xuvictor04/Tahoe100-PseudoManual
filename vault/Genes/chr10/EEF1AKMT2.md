---
symbol: "EEF1AKMT2"
type: "gene"
col: 12789
ensembl_id: "ENSG00000203791"
name: "EEF1A lysine methyltransferase 2"
location: "10q26.13"
module: 57
arm: "+"
pooled_cpm: 60.58
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# EEF1AKMT2

*EEF1A lysine methyltransferase 2* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.63× (z +8.2, q 1e-13, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.550× (z -14.1, q 2e-42, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPHOSPH9]] (+0.64, fdr 1e-05), [[PARPBP]] (+0.63, fdr 1e-05), [[RPA1]] (+0.63, fdr 1e-05); moves opposite to [[TRIM47]] (-0.65, fdr 1e-05), [[LETM2]] (-0.57, fdr 3e-05), [[FAM200A]] (-0.57, fdr 6e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12789.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +8.2 | 1e-13 | 38/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +5.0 | 2e-04 | 32/48 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +4.9 | 2e-04 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.4 | 0.001 | 25/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.086 | 19/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12789.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.550×** | -14.1 | 2e-42 | 47/48 (SNU-1, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.557×** | -13.8 | 8e-41 | 43/48 (C32, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.440×** | -13.7 | 2e-40 | 45/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.538×** | -10.4 | 6e-23 | 39/48 (hTERT-HPNE, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.609×** | -8.0 | 2e-13 | 42/48 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.728×** | -7.5 | 7e-12 | 37/48 (A498, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.672×** | -6.6 | 3e-09 | 38/48 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -6.1 | 7e-08 | 34/49 (NCI-H2347, SW 900, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.702×** | -5.9 | 2e-07 | 34/48 (PANC-1, NCI-H2030, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.781×** | -4.1 | 0.002 | 26/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.788×** | -4.0 | 0.004 | 22/48 (PANC-1, NCI-H2030, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.794×** | -3.8 | 0.006 | 24/48 (PANC-1, HOP62, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.799×** | -3.7 | 0.008 | 21/48 (A498, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.693×** | -3.2 | 0.057 | 18/48 (NCI-H661, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.820×** | -3.2 | 0.058 | 21/48 (A498, hTERT-HPNE, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.835× | -3.0 | 0.097 | 18/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 60.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -14.4) |
| [[H4 (line)]] | wt | 92.9 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.222× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 73.6 | 1 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -10.2) |
| [[C32 (line)]] | wt | 49.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -15.5) |
| [[C-33 A (line)]] | alt | 86.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 65.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -10.7) |
| [[HOP62 (line)]] | alt | 51.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -10.7) |
| [[LoVo (line)]] | wt | 53.5 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -14.5) |
| [[NCI-H23 (line)]] | alt | 58.8 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.259× (z -13.2) |
| [[PANC-1 (line)]] | alt | 94.3 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +15.0) | [[Panobinostat (drug)]] 0.5 µM 0.523× (z -9.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.565× (z -8.5) |
| [[SW 900 (line)]] | alt | 75.9 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -10.5) |
| [[A-172 (line)]] | wt | 38.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -10.1) |
| [[A-427 (line)]] | wt | 56.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 51.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -13.6) |
| [[CHP-212 (line)]] | wt | 63.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 59.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -11.8) |
| [[KATO III (line)]] | alt | 42.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.92× (z +13.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 79.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 65.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 51.4 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.234× (z -11.3) |
| [[SNU-1 (line)]] | wt | 77.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -15.1) |
| [[CFPAC-1 (line)]] | alt | 66.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -12.5) |
| [[HCT15 (line)]] | alt | 77.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.6) |
| [[Hs 766T (line)]] | wt | 58.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.9) |
| [[J82 (line)]] | alt | 44.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -15.0) |
| [[LOX-IMVI (line)]] | wt | 55.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -10.4) |
| [[LS 180 (line)]] | wt | 50.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 58.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 57.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 69.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 49.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 52.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.377× (z -9.0) |
| [[RKO (line)]] | wt | 58.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.346× (z -9.1) |
| [[SHP-77 (line)]] | alt | 71.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.404× (z -8.8) |
| [[SNU-423 (line)]] | alt | 69.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.260× (z -13.0) |
| [[SW480 (line)]] | alt | 62.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.283× (z -15.3) |
| [[A549 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH9]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PARPBP]] | +0.63 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[RPA1]] | +0.63 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[NUDT21]] | +0.63 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[PPIH]] | +0.62 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[DCAF16]] | +0.61 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[TCTN3]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[POFUT1]] | +0.61 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[SHQ1]] | +0.60 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[BCL7C]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[IMMP1L]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SKP2]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM47]] | -0.65 | -0.71 / -0.55 | both halves | 1e-05 |  |
| [[LETM2]] | -0.57 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[FAM200A]] | -0.57 | -0.72 / -0.38 | both halves | 6e-05 |  |
| [[REST]] | -0.57 | -0.49 / -0.62 | both halves | 2e-05 |  |
| [[MAFF]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[NEPRO-AS1]] | -0.56 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[UTP3]] | -0.55 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[LINC02307]] | -0.55 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[STYXL1]] | -0.55 | -0.69 / -0.43 | both halves | 3e-05 |  |
| [[DYNLRB2-AS1]] | -0.55 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[SLC22A1]] | -0.55 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[SLFN5]] | -0.55 | -0.62 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises EEF1AKMT2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.586). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-32.5, -36.4); signed map (-39.8, -22.9). **Vector** length 103, 27.9% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | +0.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.2 | +8.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.0 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.7 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +1.0 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.9 | -13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.1 | -13.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -8.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | EEF1A lysine methyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:124,748,149-124,791,887 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Efm4; previously C10orf138, METTL10 |
| Gene groups (HGNC) | 7BS protein lysine methyltransferases; Non-histone lysine methyltransferases |
| Reactome | 1 pathways, smallest: Protein methylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JPI9](https://www.uniprot.org/uniprotkb/Q5JPI9) (EEF1A lysine methyltransferase 2):

> [Isoform 2]: Protein-lysine methyltransferase that selectively catalyzes the trimethylation of EEF1A at 'Lys-318'.

**Summary**, from NCBI Gene [399818](https://www.ncbi.nlm.nih.gov/gene/399818):

> Enables protein-lysine N-methyltransferase activity. Involved in peptidyl-lysine methylation. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33787) · Entrez [399818](https://www.ncbi.nlm.nih.gov/gene/399818) · UniProt [Q5JPI9](https://www.uniprot.org/uniprotkb/Q5JPI9) · Ensembl [ENSG00000203791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203791)

## Data

Gene col 12789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12789); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12789]; `tensor/DDL_lfc|DDL_z.npy` [12789]; `embed/gene_vectors.npy` [12789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12789 or target_col == 12789). Every well: [[EEF1AKMT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEF1AKMT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
