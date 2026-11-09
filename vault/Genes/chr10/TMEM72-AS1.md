---
symbol: "TMEM72-AS1"
type: "gene"
col: 13420
ensembl_id: "ENSG00000224812"
name: "TMEM72 antisense RNA 1"
location: "10q11.21"
module: 26
arm: "+"
pooled_cpm: 5.24
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 13
n_dd_up_clean: 37
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# TMEM72-AS1

*TMEM72 antisense RNA 1* — 10q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.25× (z +19.4, q 0e+00, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.429× (z -8.0, q 6e-13, down in 33 of 46 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.651× (z -4.1, q 0.004, down in 18 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7-DT]] (+0.69, fdr 7e-06), [[CIBAR1-DT]] (+0.68, fdr 2e-05), [[CDNF]] (+0.67, fdr 2e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 5 with an alert ⚠; shown: the 15 strongest. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13420.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.25×** | +19.4 | 0e+00 | 37/38 (HEC-1-A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +8.8 | 3e-16 | 20/38 (C32, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +7.8 | 2e-12 | 24/35 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +6.6 | 5e-09 | 24/44 (KATO III, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.93×** | +6.2 | 4e-08 | 28/46 (C-33 A, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +6.2 | 4e-08 | 24/47 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.9 | 2e-07 | 18/46 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +5.8 | 4e-07 | 17/38 (MIA PaCa-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +5.4 | 4e-06 | 19/45 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.50×** | +5.3 | 6e-06 | 19/44 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +5.3 | 6e-06 | 18/44 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **1.71×** | +5.1 | 1e-05 | 17/47 (A-172, SW480, …) | all doses, flat | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.72×** | +5.0 | 3e-05 | 16/43 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.52×** | +4.8 | 8e-05 | 18/44 (SW480, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.71×** | +4.7 | 1e-04 | 15/46 (SK-MEL-2, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13420.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.429×** | -8.0 | 6e-13 | 33/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.529×** | -6.0 | 4e-07 | 20/34 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.590×** | -5.0 | 1e-04 | 18/46 (A-427, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.601×** | -4.8 | 2e-04 | 16/46 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.598×** | -4.7 | 3e-04 | 17/31 (A-172, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.637×** | -4.3 | 0.002 | 15/44 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.651×** | -4.1 | 0.004 | 18/43 (A-427, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.668×** | -3.8 | 0.009 | 15/46 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.664×** | -3.7 | 0.011 | 16/44 (LoVo, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.687×** | -3.4 | 0.033 | 12/44 (NCI-H1573, COLO 205, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.699×** | -3.4 | 0.034 | 13/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose | position effect removed |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.795×** | -3.1 | 0.093 | 6/48 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.540×** | -3.1 | 0.096 | 5/35 (HS-578T, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13420. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.93 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0978× (z -13.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HEC-1-A (line)]] | alt | 8.48 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.12× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 8.48 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.0568× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 4.99 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0492× (z -10.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0664× (z -9.2) |
| [[A498 (line)]] | wt | 7.77 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +10.4) | — |
| [[A-172 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 4.27 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0458× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 2.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.0× (z +12.6) | — |
| [[CFPAC-1 (line)]] | alt | 6.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.26× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0815× (z -8.7) |
| [[HOP62 (line)]] | alt | 4.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.05× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 6.46 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0625× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HS-578T (line)]] | alt | 4.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 4.64 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0721× (z -8.7) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 3.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +9.9) | — |
| [[LoVo (line)]] | wt | 2.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.18× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 2.64 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0437× (z -9.5) ⚠ cell-cycle shift, explains ~88% of this change |
| [[Panc 03.27 (line)]] | alt | 7.23 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0685× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 5.41 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 9.07 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.111× (z -9.9) |
| [[SW480 (line)]] | alt | 4.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13420), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7-DT]] | +0.69 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CIBAR1-DT]] | +0.68 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[CDNF]] | +0.67 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[INTS6-AS1]] | +0.67 | +0.64 / +0.55 | both halves | 1e-05 | same gene group |
| [[SPESP1]] | +0.67 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[DRAIC]] | +0.66 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[KLF3-AS1]] | +0.65 | +0.49 / +0.51 | both halves | 1e-05 | same gene group |
| [[MAILR]] | +0.65 | +0.71 / +0.37 | both halves | 7e-05 |  |
| [[USP38-DT]] | +0.65 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[PSMG3-AS1]] | +0.64 | +0.66 / +0.54 | both halves | 1e-05 | same gene group |
| [[SAXO1]] | +0.64 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SLC9B1]] | +0.64 | +0.65 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMEM72-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.7, 18.8); signed map (28.0, -4.8). **Vector** length 63.2, 9.81% of its response variance represented; |z| ≥ 3 in 1,152 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +19.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +8.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +5.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +4.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.5 | +2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.8 | +4.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +3.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.1 | +0.6 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | TMEM72 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q11.21 — chr10:44,793,119-44,959,724 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27349) · Entrez [220980](https://www.ncbi.nlm.nih.gov/gene/220980) · Ensembl [ENSG00000224812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224812)

## Data

Gene col 13420: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13420); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13420, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13420]; `tensor/DDL_lfc|DDL_z.npy` [13420]; `embed/gene_vectors.npy` [13420]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13420 or target_col == 13420). Every well: [[TMEM72-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM72-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
