---
symbol: "GAR1"
type: "gene"
col: 3059
ensembl_id: "ENSG00000109534"
name: "GAR1 ribonucleoprotein"
location: "4q25"
module: 1
arm: "+"
pooled_cpm: 36.92
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# GAR1

*GAR1 ribonucleoprotein* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.89× (z +8.5, q 7e-15, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.583× (z -7.3, q 2e-10, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRIX1]] (+0.70, fdr 7e-06), [[YRDC]] (+0.68, fdr 7e-06), [[SMARCAD1]] (+0.67, fdr 7e-06); moves opposite to [[LAMP2]] (-0.56, fdr 1e-05), [[TWSG1]] (-0.55, fdr 1e-05), [[PSAP]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NOL6]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3059.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +8.5 | 7e-15 | 36/48 (NCI-H1573, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.02×** | +7.8 | 2e-12 | 43/48 (NCI-H1573, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +6.4 | 2e-08 | 37/48 (Panc 03.27, SHP-77, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.48×** | +6.4 | 2e-08 | 32/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.58×** | +6.1 | 9e-08 | 32/46 (PANC-1, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.52×** | +5.4 | 7e-06 | 31/47 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.9 | 9e-05 | 29/46 (LOX-IMVI, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.37×** | +4.3 | 0.001 | 24/48 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.32×** | +3.8 | 0.010 | 21/48 (LS 180, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.3 | 0.048 | 20/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.27×** | +3.3 | 0.057 | 19/48 (LS 180, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.060 | 17/48 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.57×** | +3.2 | 0.060 | 18/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3059.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.583×** | -7.3 | 2e-10 | 38/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.715×** | -6.4 | 5e-08 | 40/48 (A498, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.633×** | -6.2 | 1e-07 | 32/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.656×** | -5.7 | 2e-06 | 33/48 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.669×** | -5.4 | 7e-06 | 37/48 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -5.4 | 8e-06 | 30/48 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.742×** | -3.9 | 0.009 | 23/48 (H4, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.756×** | -3.8 | 0.012 | 23/48 (LS 180, CHP-212, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.609×** | -3.5 | 0.030 | 22/48 (A498, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.834× | -3.4 | 0.041 | 18/48 (NCI-H1573, SW480, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.784×** | -3.3 | 0.053 | 21/48 (C-33 A, J82, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.780×** | -3.2 | 0.060 | 18/47 (LoVo, hTERT-HPNE, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.778×** | -3.1 | 0.078 | 14/48 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.797×** | -3.1 | 0.089 | 19/47 (LoVo, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3059. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 80.2 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -16.2) |
| [[H4 (line)]] | wt | 59.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.51× (z +9.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 40.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.60× (z +11.1) | — |
| [[RKO (line)]] | wt | 49.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -9.9) |
| [[SW48 (line)]] | wt | 46.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -9.1) |
| [[A-427 (line)]] | wt | 42.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 56.9 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.158× (z -9.0) |
| [[BT-474 (line)]] | alt | 20.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0879× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 30.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.29× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 37.4 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.105× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 27.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.04× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0834× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 28.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.42× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 27.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.72× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 40.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.366× (z -9.5) |
| [[SHP-77 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3059), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRIX1]] | +0.70 | +0.67 / +0.62 | both halves | 7e-06 | STRING 517 |
| [[YRDC]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[SMARCAD1]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[TRMT44]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[UTP6]] | +0.66 | +0.73 / +0.60 | both halves | 7e-06 | pathway: rRNA modification in the nucleus and cytosol |
| [[DDX18]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 | STRING 626 |
| [[MPHOSPH10]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 | pathway: rRNA modification in the nucleus and cytosol; STRING 868 |
| [[IMP4]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 | pathway: rRNA modification in the nucleus and cytosol; STRING 403 |
| [[NIFK]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 | STRING 638 |
| [[UTP14A]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 | pathway: rRNA modification in the nucleus and cytosol; STRING 413 |
| [[SCFD2]] | +0.62 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[GNL2]] | +0.62 | +0.69 / +0.50 | both halves | 1e-05 | STRING 413 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMP2]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[TWSG1]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[PSAP]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ADAM9]] | -0.52 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[ITM2B]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOL6]] | C | NOL6's natural level strengthens GAR1's drug response | NOL6's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse -0.17; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.3, -40.6); signed map (-14.5, -22.1). **Vector** length 87.6, 22.0% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.8 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +6.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +2.6 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.0 | -0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -2.9 | +3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | +1.8 |
|  | [[Cyclosporin A (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Adenine (drug)]] 5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | GAR1 ribonucleoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:109,815,510-109,824,740 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NOLA1 |
| Gene groups (HGNC) | H/ACA ribonucleoprotein complex; Telomerase holoenzyme subunits |
| Reactome | 9 pathways, smallest: Telomere Extension By Telomerase; Extension of Telomeres; rRNA modification in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY12](https://www.uniprot.org/uniprotkb/Q9NY12) (H/ACA ribonucleoprotein complex subunit 1):

> Required for ribosome biogenesis and telomere maintenance. Part of the H/ACA small nucleolar ribonucleoprotein (H/ACA snoRNP) complex, which catalyzes pseudouridylation of rRNA. This involves the isomerization of uridine such that the ribose is subsequently attached to C5, instead of the normal N1. Each rRNA can contain up to 100 pseudouridine ('psi') residues, which may serve to stabilize the conformation of rRNAs. May also be required for correct processing or intranuclear trafficking of …

**Summary**, from NCBI Gene [54433](https://www.ncbi.nlm.nih.gov/gene/54433):

> This gene is a member of the H/ACA snoRNPs (small nucleolar ribonucleoproteins) gene family. snoRNPs are involved in various aspects of rRNA processing and modification and have been classified into two families: C/D and H/ACA. The H/ACA snoRNPs also include the DKC1, NOLA2 and NOLA3 proteins. These four H/ACA snoRNP proteins localize to the dense fibrillar components of nucleoli and to coiled (Cajal) bodies in the nucleus. Both 18S rRNA production and rRNA pseudouridylation are impaired if any …

**Accessions** — [HGNC:14264](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14264) · Entrez [54433](https://www.ncbi.nlm.nih.gov/gene/54433) · UniProt [Q9NY12](https://www.uniprot.org/uniprotkb/Q9NY12) · Ensembl [ENSG00000109534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109534)

## Data

Gene col 3059: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3059); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3059, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3059]; `tensor/DDL_lfc|DDL_z.npy` [3059]; `embed/gene_vectors.npy` [3059]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3059 or target_col == 3059). Every well: [[GAR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
