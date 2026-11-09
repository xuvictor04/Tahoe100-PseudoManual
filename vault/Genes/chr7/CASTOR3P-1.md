---
symbol: "CASTOR3P-1"
type: "gene"
col: 16594
ensembl_id: "ENSG00000291122"
name: ""
location: ""
module: 17
arm: "-"
pooled_cpm: 11.12
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# CASTOR3P-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.45× (z +12.9, q 3e-35, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.613× (z -5.0, q 2e-04, down in 26 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.614× (z -5.0, q 2e-04, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPM1A]] (+0.58, fdr 1e-04), [[ZFTRAF1]] (+0.57, fdr 2e-05), [[QRICH2]] (+0.56, fdr 1e-05); moves opposite to [[GEMIN2]] (-0.58, fdr 5e-05), [[ELP3]] (-0.57, fdr 1e-05), [[ZNF45]] (-0.55, fdr 2e-04).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16594.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +12.9 | 3e-35 | 41/45 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +8.3 | 2e-14 | 13/18 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +8.2 | 5e-14 | 35/47 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +7.3 | 5e-11 | 32/47 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.04×** | +6.8 | 2e-09 | 32/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +6.6 | 3e-09 | 31/47 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +6.5 | 7e-09 | 15/23 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +6.4 | 9e-09 | 26/45 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.84×** | +6.2 | 3e-08 | 27/44 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +5.8 | 4e-07 | 21/35 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.29×** | +4.4 | 5e-04 | 19/48 (KATO III, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.48×** | +4.0 | 0.003 | 14/47 (A549, SW48, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.003 | 14/48 (A549, A-172, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.003 | 14/47 (SW480, HT-29, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.45×** | +3.8 | 0.006 | 14/47 (LS 180, A549, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.006 | 18/45 (HEC-1-A, SW480, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.008 | 18/46 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.029 | 14/47 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.79×** | +3.1 | 0.059 | 8/47 (HEC-1-A, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.059 | 6/48 (SW480, HEC-1-A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16594.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.613×** | -5.0 | 2e-04 | 26/45 (Panc 03.27, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.614×** | -5.0 | 2e-04 | 24/47 (A-427, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.410×** | -4.8 | 3e-04 | 20/47 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.654×** | -4.4 | 0.002 | 23/47 (PANC-1, Panc 03.27, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.667×** | -4.2 | 0.004 | 17/47 (NCI-H2030, LoVo, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.682×** | -3.9 | 0.007 | 21/43 (HS-578T, Panc 03.27, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.481×** | -3.9 | 0.007 | 13/43 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.697×** | -3.6 | 0.024 | 19/46 (Panc 03.27, NCI-H23, …) | two highest doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.727×** | -3.3 | 0.064 | 17/47 (PANC-1, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.6 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.206× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 24.2 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 14.9 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 6.18 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +10.9) | — |
| [[A-172 (line)]] | wt | 7.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +9.2) | — |
| [[A498 (line)]] | wt | 18.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +8.9) | — |
| [[A549 (line)]] | wt | 8.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.32× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 30.2 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.164× (z -9.3) |
| [[C32 (line)]] | wt | 8.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.34× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 18.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.14× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 38.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.135× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~69% of this change |
| [[HS-578T (line)]] | alt | 4.78 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0761× (z -9.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[hTERT-HPNE (line)]] | wt | 5.89 | 0 | 1 | — | [[Budesonide (drug)]] 0.5 µM 0.0641× (z -8.7) |
| [[KATO III (line)]] | alt | 7.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +8.8) | — |
| [[LoVo (line)]] | wt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 7.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.59× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0802× (z -15.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 1 | — | [[Bendamustine (drug)]] 0.05 µM 0.0713× (z -8.5) |
| [[SW480 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +9.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPM1A]] | +0.58 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[ZFTRAF1]] | +0.57 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[QRICH2]] | +0.56 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ACYP2]] | +0.56 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[GATA2-AS1]] | +0.56 | +0.58 / +0.43 | both halves | 4e-05 |  |
| [[LRP10]] | +0.56 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[LYRM1]] | +0.55 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[COPB2-DT]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[AKT2]] | +0.54 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[PIPOX]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[EOLA2-DT]] | +0.52 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[WDR45]] | +0.52 | +0.50 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEMIN2]] | -0.58 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[ELP3]] | -0.57 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ZNF45]] | -0.55 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[ARL4D]] | -0.54 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[HPF1]] | -0.54 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[TAF1A]] | -0.54 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[RIOK2]] | -0.54 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[C17orf58]] | -0.53 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[FAM133B]] | -0.53 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[LEO1]] | -0.52 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[DIXDC1]] | -0.52 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[KBTBD7]] | -0.52 | -0.29 / -0.45 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CASTOR3P-1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.496). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-18.1, -15.9); signed map (34.5, -19.8). **Vector** length 71.0, 13.0% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +12.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +4.0 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -3.8 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -2.6 | -3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.4 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | +1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -2.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.7 | -1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.7 |

## What is on record

> [!warning] No registry record
> CASTOR3P-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16594); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16594]; `tensor/DDL_lfc|DDL_z.npy` [16594]; `embed/gene_vectors.npy` [16594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16594 or target_col == 16594). Every well: [[CASTOR3P-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASTOR3P-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
