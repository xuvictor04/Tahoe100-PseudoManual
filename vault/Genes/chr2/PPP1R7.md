---
symbol: "PPP1R7"
type: "gene"
col: 3710
ensembl_id: "ENSG00000115685"
name: "protein phosphatase 1 regulatory subunit 7"
location: "2q37.3"
module: 12
arm: "+"
pooled_cpm: 30.11
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PPP1R7

*protein phosphatase 1 regulatory subunit 7* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.58× (z +13.5, q 9e-39, up in 33 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +9.5, q 3e-19, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.745× (z -6.1, q 5e-07, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIMOC1]] (+0.60, fdr 1e-05), [[PHC3]] (+0.55, fdr 2e-05), [[ABITRAM]] (+0.54, fdr 3e-05); moves opposite to [[BTNL9]] (-0.53, fdr 3e-05), [[CACNG7]] (-0.50, fdr 8e-05), [[GPR63]] (-0.50, fdr 0.002, ⚠ not reproduced), [[MCOLN2]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GALNT14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3710.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +13.5 | 9e-39 | 33/35 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.21×** | +11.8 | 2e-29 | 41/44 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +9.5 | 3e-19 | 42/47 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.70×** | +7.9 | 6e-13 | 41/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.69×** | +7.7 | 1e-12 | 37/48 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.65×** | +7.4 | 1e-11 | 42/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.58×** | +6.2 | 4e-08 | 23/37 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.1 | 6e-08 | 37/46 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.41×** | +4.9 | 6e-05 | 27/47 (PANC-1, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.41×** | +4.9 | 7e-05 | 27/48 (PANC-1, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 2e-04 | 26/48 (A-427, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +3.6 | 0.013 | 16/46 (A-172, C-33 A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.016 | 17/48 (hTERT-HPNE, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.034 | 16/48 (HS-578T, NCI-H2347, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.037 | 14/48 (LoVo, AsPC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.046 | 18/47 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.078 | 12/47 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3710.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.745×** | -6.1 | 5e-07 | 34/48 (KATO III, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.690×** | -5.5 | 1e-05 | 32/48 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.515×** | -5.1 | 6e-05 | 29/46 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.714×** | -5.0 | 9e-05 | 28/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.728×** | -4.7 | 3e-04 | 27/48 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.755×** | -4.1 | 0.003 | 26/48 (SNU-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.759×** | -3.8 | 0.010 | 22/47 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.781×** | -3.6 | 0.019 | 24/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.799×** | -3.3 | 0.058 | 18/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Roxadustat (drug)]] 5 µM |  | **0.793×** | -3.3 | 0.058 | 12/47 (SW 1271, NCI-H1573, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.804×** | -3.2 | 0.066 | 17/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3710. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 30.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A549 (line)]] | wt | 23.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.57× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 29.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.28× (z +11.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.398× (z -8.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 32.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +12.5) | — |
| [[HS-578T (line)]] | alt | 26.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +9.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 28.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 37.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.08× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[COLO 205 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 35.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 25.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 32.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 35.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.4) | — |
| [[SW480 (line)]] | alt | 39.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3710), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIMOC1]] | +0.60 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[PHC3]] | +0.55 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ABITRAM]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[MORN2]] | +0.53 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TOX4]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[COG4]] | +0.53 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[LMBRD2]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[UEVLD]] | +0.52 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SYNRG]] | +0.51 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ZNF252P]] | +0.51 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[BAD]] | +0.51 | +0.29 / +0.60 | both halves | 2e-04 |  |
| [[DNAL4]] | +0.50 | +0.55 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTNL9]] | -0.53 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[CACNG7]] | -0.50 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[GPR63]] | -0.50 | -0.11 / -0.47 | ⚠ not reproduced | 0.002 |  |
| [[MCOLN2]] | -0.48 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[PRKCQ]] | -0.48 | -0.23 / -0.48 | both halves | 5e-04 |  |
| [[CELF5]] | -0.46 | -0.07 / -0.53 | ⚠ one half (not replicated) | 0.004 |  |
| [[MEGF11]] | -0.45 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[ZNF692]] | -0.45 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[UCK2]] | -0.45 | -0.44 / -0.43 | both halves | 3e-05 | STRING 776 |
| [[GRB14]] | -0.45 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[GALNT14]] | -0.44 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[ASIC1]] | -0.44 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[SNHG15]] | -0.44 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[LINC00937]] | -0.44 | -0.28 / -0.44 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT14]] | B | GALNT14 activity raises PPP1R7's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.13× lower at baseline in the lines without GALNT14 | 0.068 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[TOP2A]] | B | TOP2A activity lowers PPP1R7's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.251). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.5, 4.6); signed map (-4.6, -7.3). **Vector** length 65.9, 12.5% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.5 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.4 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +1.6 | +11.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +1.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +3.6 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.2 | -0.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.2 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.6 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -3.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,149,576-241,183,652 (+) |
| Ensembl biotype | protein_coding |
| Also known as | sds22 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15435](https://www.uniprot.org/uniprotkb/Q15435) (Protein phosphatase 1 regulatory subunit 7):

> Regulatory subunit of protein phosphatase 1.

**Summary**, from NCBI Gene [5510](https://www.ncbi.nlm.nih.gov/gene/5510):

> This gene encodes a protein subunit that regulates the activity of the serine/threonine phosphatase, protein phosphatase-1. The encoded protein is required for completion of the mitotic cycle and for targeting protein phosphatase-1 to mitotic kinetochores. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:9295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9295) · Entrez [5510](https://www.ncbi.nlm.nih.gov/gene/5510) · UniProt [Q15435](https://www.uniprot.org/uniprotkb/Q15435) · Ensembl [ENSG00000115685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115685)

## Data

Gene col 3710: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3710); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3710, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3710]; `tensor/DDL_lfc|DDL_z.npy` [3710]; `embed/gene_vectors.npy` [3710]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3710 or target_col == 3710). Every well: [[PPP1R7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
