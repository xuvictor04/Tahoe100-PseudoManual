---
symbol: "TC2N"
type: "gene"
col: 9210
ensembl_id: "ENSG00000165929"
name: "tandem C2 domains, nuclear"
location: "14q32.12"
module: 8
arm: "+"
pooled_cpm: 63.89
n_lines_expressing: 22
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 156
direction_downstream: 171
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TC2N

*tandem C2 domains, nuclear* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.50× (z +10.3, q 3e-22, up in 6 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.546× (z -10.5, q 8e-23, down in 17 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CATSPERB]] (+0.84, fdr 7e-06, ⚠ same locus), [[SLC44A4]] (+0.80, fdr 7e-06), [[ST14]] (+0.79, fdr 7e-06), [[GCNT3]] (+0.79, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 156 arrows point to it, the strongest [[ATP8B1]] → it (grade B ⚠); 171 go from it, the strongest it → [[ANXA11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9210.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +10.3 | 3e-22 | 6/20 (A549, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +8.9 | 1e-16 | 10/21 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +8.6 | 2e-15 | 0/20 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +7.5 | 1e-11 | 3/18 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +6.5 | 7e-09 | 1/18 (NCI-H460) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.32×** | +5.1 | 4e-05 | 3/20 (KATO III, LS 180, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 0.002 | 6/20 (SW 900, SW480, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.002 | 10/20 (Panc 03.27, SW48, …) | two highest doses | low cells (technical?) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.002 | 6/20 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.018 | 8/21 (NCI-H1573, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.038 | 5/20 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.21×** | +3.4 | 0.038 | 9/20 (A549, Panc 03.27, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9210.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.546×** | -10.5 | 8e-23 | 17/20 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.630×** | -8.3 | 3e-14 | 18/20 (LS 180, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.659×** | -7.5 | 1e-11 | 20/20 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.662×** | -7.4 | 2e-11 | 13/20 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.673×** | -7.1 | 1e-10 | 18/20 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -6.2 | 7e-08 | 14/20 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.824×** | -4.9 | 9e-05 | 11/20 (LoVo, AsPC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.760×** | -4.7 | 2e-04 | 18/20 (SW 900, LoVo, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.770×** | -4.7 | 2e-04 | 13/20 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.771×** | -4.7 | 2e-04 | 11/20 (LoVo, SW 900, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.05 µM |  | **0.764×** | -4.5 | 3e-04 | 2/20 (NCI-H460, HT-29) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.779×** | -4.5 | 4e-04 | 13/20 (LoVo, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.801×** | -4.0 | 0.003 | 14/20 (LoVo, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.802×** | -3.9 | 0.003 | 11/20 (COLO 205, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.803×** | -3.9 | 0.003 | 10/21 (NCI-H2347, SW 900, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.798×** | -3.9 | 0.004 | 2/20 (CFPAC-1, LoVo) | top dose only |  |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.806×** | -3.6 | 0.009 | 0/20 | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.701×** | -3.3 | 0.026 | 9/20 (LoVo, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.831×** | -3.3 | 0.026 | 10/20 (LoVo, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9210. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 355 | 0 | 15 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -24.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -15.5) |
| [[BT-474 (line)]] | alt | 471 | 0 | 11 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.350× (z -9.7) |
| [[COLO 205 (line)]] | alt | 264 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0695× (z -24.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.150× (z -12.0) |
| [[LS 180 (line)]] | wt | 233 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -26.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -20.0) |
| [[NCI-H2347 (line)]] | alt | 133 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -18.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 39.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -10.1) |
| [[KATO III (line)]] | alt | 189 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -26.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -16.9) |
| [[NCI-H1573 (line)]] | alt | 106 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -14.3) |
| [[SW 900 (line)]] | alt | 59.6 | 0 | 5 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -11.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.293× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 229 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -16.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 34.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -10.1) |
| [[HT-29 (line)]] | alt | 121 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.341× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 168 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -17.8) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 53.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 24.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -10.1) |
| [[SW1417 (line)]] | alt | 53.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 94.9 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -15.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.86 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.66 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.49 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.92 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.12 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.21 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.25 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.60 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.54 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.46 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.71 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.05 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.86 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.32 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.77 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9210), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPERB]] | +0.84 | +0.82 / +0.88 | both halves | 7e-06 | STRING 690; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SLC44A4]] | +0.80 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[ST14]] | +0.79 | +0.81 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS4]] | +0.77 | +0.75 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[TMEM45B]] | +0.76 | +0.72 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[TJP3]] | +0.75 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SIDT1]] | +0.75 | +0.72 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[CYP4F12]] | +0.74 | +0.63 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[POF1B]] | +0.73 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[ADGRF1]] | +0.71 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[ITGB6]] | +0.71 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[HSH2D]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*156 arrows, 156 of them with an alert ⚠; grade A 0, B 14, C 142. Shown: the 12 strongest; 144 more arrows (144 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP8B1]] | B | ATP8B1 activity raises TC2N's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 4.22× lower at baseline in the lines without ATP8B1 | 0.016 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[TJP2]] | B | TJP2 activity raises TC2N's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.60× lower at baseline in the lines without TJP2 | 0.019 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[LGALS9]] | B | LGALS9 activity raises TC2N's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 3.49× lower at baseline in the lines without LGALS9 | 0.034 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[EPS8L1]] | B | EPS8L1 activity raises TC2N's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.46× lower at baseline in the lines without EPS8L1 | 0.038 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[C4orf19]] | B | C4orf19 activity raises TC2N's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.92× lower at baseline in the lines without C4orf19 | 0.045 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[NOSTRIN]] | B | NOSTRIN activity raises TC2N's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 4.07× lower at baseline in the lines without NOSTRIN | 0.049 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[POU5F1B]] | B | POU5F1B activity raises TC2N's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 3.78× lower at baseline in the lines without POU5F1B | 0.056 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[GPRC5A]] | B | GPRC5A activity raises TC2N's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.66× lower at baseline in the lines without GPRC5A | 0.058 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[GAREM1]] | B | GAREM1 activity raises TC2N's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 4.54× lower at baseline in the lines without GAREM1 | 0.070 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[TNFRSF21]] | B | TNFRSF21 activity raises TC2N's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 3.61× lower at baseline in the lines without TNFRSF21 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[FAM83E]] | B | FAM83E activity raises TC2N's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 3.75× lower at baseline in the lines without FAM83E | 0.087 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[IKZF2]] | B | IKZF2 activity raises TC2N's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 2.04× lower at baseline in the lines without IKZF2 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |

### Downstream of this gene

*171 arrows, 171 of them with an alert ⚠; grade A 0, B 52, C 119. Shown: the 12 strongest; 159 more arrows (159 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA11]] | B | TC2N activity raises ANXA11's level | lines that do not express TC2N (28) vs lines expressing it (22) | 3.02× lower at baseline in the lines without TC2N | 3e-04 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[EPS8L1]] | B | TC2N activity raises EPS8L1's level | lines that do not express TC2N (28) vs lines expressing it (22) | 4.18× lower at baseline in the lines without TC2N | 4e-04 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[ST3GAL3]] | B | TC2N activity lowers ST3GAL3's level | lines that do not express TC2N (28) vs lines expressing it (22) | 2.55× higher at baseline in the lines without TC2N | 6e-04 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[RHPN2]] | B | TC2N activity raises RHPN2's level | lines that do not express TC2N (28) vs lines expressing it (22) | 2.96× lower at baseline in the lines without TC2N | 0.003 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[ARHGEF16]] | B | TC2N activity raises ARHGEF16's level | lines that do not express TC2N (28) vs lines expressing it (22) | 3.12× lower at baseline in the lines without TC2N | 0.004 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[PLEKHA7]] | B | TC2N activity raises PLEKHA7's level | lines that do not express TC2N (28) vs lines expressing it (22) | 3.12× lower at baseline in the lines without TC2N | 0.005 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[KIAA1522]] | B | TC2N activity raises KIAA1522's level | lines that do not express TC2N (28) vs lines expressing it (22) | 3.00× lower at baseline in the lines without TC2N | 0.005 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[PIK3C2B]] | B | TC2N activity raises PIK3C2B's level | lines that do not express TC2N (28) vs lines expressing it (22) | 2.22× lower at baseline in the lines without TC2N | 0.007 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[FAM83E]] | B | TC2N activity raises FAM83E's level | lines that do not express TC2N (28) vs lines expressing it (22) | 3.49× lower at baseline in the lines without TC2N | 0.008 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[TMEM51-AS1]] | B | TC2N activity raises TMEM51-AS1's level | lines that do not express TC2N (28) vs lines expressing it (22) | 1.87× lower at baseline in the lines without TC2N | 0.009 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[LGALS9]] | B | TC2N activity raises LGALS9's level | lines that do not express TC2N (28) vs lines expressing it (22) | 2.60× lower at baseline in the lines without TC2N | 0.010 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[NOSTRIN]] | B | TC2N activity raises NOSTRIN's level | lines that do not express TC2N (28) vs lines expressing it (22) | 2.95× lower at baseline in the lines without TC2N | 0.011 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.787). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.3, 54.6); signed map (59.8, 5.8). **Vector** length 100, 38.3% of its response variance represented; |z| ≥ 3 in 711 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.51 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +8.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +0.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +4.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +5.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -10.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -8.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -7.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | +0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -3.9 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -1.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | tandem C2 domains, nuclear |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:91,779,746-91,867,536 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36557, Tac2-N, C2CD1; previously C14orf47, MTAC2D1 |
| Gene groups (HGNC) | Synaptotagmin like tandem C2 proteins |
| Matched by | ensembl_id |

UniProt [Q8N9U0](https://www.uniprot.org/uniprotkb/Q8N9U0) carries no function annotation.

**Summary**, from NCBI Gene [123036](https://www.ncbi.nlm.nih.gov/gene/123036):

> Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19859) · Entrez [123036](https://www.ncbi.nlm.nih.gov/gene/123036) · UniProt [Q8N9U0](https://www.uniprot.org/uniprotkb/Q8N9U0) · Ensembl [ENSG00000165929](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165929)

## Data

Gene col 9210: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9210); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9210, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9210]; `tensor/DDL_lfc|DDL_z.npy` [9210]; `embed/gene_vectors.npy` [9210]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9210 or target_col == 9210). Every well: [[TC2N — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TC2N.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
