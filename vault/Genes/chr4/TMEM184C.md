---
symbol: "TMEM184C"
type: "gene"
col: 8889
ensembl_id: "ENSG00000164168"
name: "transmembrane protein 184C"
location: "4q31.23"
module: 7
arm: "+"
pooled_cpm: 35.04
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TMEM184C

*transmembrane protein 184C* — 4q31.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.39× (z +21.9, q 0e+00, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (NCI-H460 0.202×, SW 900 0.0811×, SK-MEL-2 0.136×, A-427 0.239×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (SW480 0.147×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (C32 0.327×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIMOC1]] (+0.67, fdr 3e-05), [[GIN1]] (+0.61, fdr 1e-05), [[UBE2Q1]] (+0.60, fdr 1e-05); moves opposite to [[RSKR]] (-0.52, fdr 3e-05), [[CMC2]] (-0.51, fdr 3e-05), [[NPHP4]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8889.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.39×** | +21.9 | 0e+00 | 46/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.33×** | +21.3 | 0e+00 | 48/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +20.1 | 0e+00 | 42/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +15.7 | 0e+00 | 45/48 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +13.9 | 7e-42 | 40/46 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +12.3 | 7e-33 | 39/48 (RKO, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.47×** | +11.9 | 1e-30 | 40/49 (BT-474, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +11.3 | 1e-27 | 36/47 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +11.1 | 7e-27 | 37/48 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +10.2 | 2e-22 | 37/47 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +9.9 | 3e-21 | 32/48 (NCI-H23, BT-474, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +9.5 | 1e-19 | 32/48 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +8.9 | 2e-17 | 27/48 (SHP-77, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +8.9 | 2e-17 | 27/48 (HOP62, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +7.0 | 9e-11 | 24/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +6.9 | 2e-10 | 27/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8889.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (NCI-H460 0.202×, SW 900 0.0811×, SK-MEL-2 0.136×, A-427 0.239×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (SW480 0.147×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (C32 0.327×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.868× | -3.6 | 0.19 | 18/47 (SW480, KATO III, …) | all doses, flat |  |
| [[AT7519 (drug)]] 5 µM |  | 0.789× | -3.1 | 0.36 | 5/48 (H4, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.877× | -3.1 | 0.36 | 16/42 (NCI-H460, SW 900, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.888× | -3.0 | 0.36 | 9/47 (SW480, NCI-H2030, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8889. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 39.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.0) | — |
| [[A498 (line)]] | wt | 42.6 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 30.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 45.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.3) | [[Lonafarnib (drug)]] 5 µM 0.147× (z -13.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 37.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.4) | — |
| [[J82 (line)]] | alt | 25.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +13.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 24.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 25.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.2) | — |
| [[C32 (line)]] | wt | 31.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HOP62 (line)]] | alt | 29.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.47× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 26.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.02× (z +9.5) | — |
| [[LoVo (line)]] | wt | 39.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.41× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 20.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 56.9 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 50.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.65× (z +9.1) | — |
| [[RKO (line)]] | wt | 39.4 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.42× (z +9.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.84× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 39.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 17.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.71× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 48.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 48.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.23× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 53.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0811× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8889), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIMOC1]] | +0.67 | +0.78 / +0.43 | both halves | 3e-05 |  |
| [[GIN1]] | +0.61 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[UBE2Q1]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[THAP6]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[PLRG1]] | +0.59 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[BROX]] | +0.58 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[CHURC1]] | +0.58 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[ASNSD1]] | +0.58 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[TRUB1]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[VPS33A]] | +0.57 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[ERAL1]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ZNF845]] | +0.56 | +0.59 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSKR]] | -0.52 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[CMC2]] | -0.51 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[NPHP4]] | -0.50 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[FANCA]] | -0.50 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[DONSON]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ST6GALNAC6-1]] | -0.49 | -0.55 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMEM184C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF606]] | B | ZNF606 activity raises TMEM184C's level | lines that do not express ZNF606 (13) vs lines expressing it (37) | 1.06× lower at baseline in the lines without ZNF606 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, C19orf18, ZNF569 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-27.3, 6.9); signed map (6.2, -23.2). **Vector** length 70.8, 13.6% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.6 | +12.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +11.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +13.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.0 | +6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +3.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +1.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.6 | +5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.5 | -3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.9 | +8.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +4.4 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -1.3 | -1.1 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 184C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.23 — chr4:147,617,386-147,672,044 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10846, SLC51C3; previously TMEM34 |
| Gene groups (HGNC) | Solute carrier family 51 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVA4](https://www.uniprot.org/uniprotkb/Q9NVA4) (Transmembrane protein 184C):

> Possible tumor suppressor which may play a role in cell growth.

**Summary**, from NCBI Gene [55751](https://www.ncbi.nlm.nih.gov/gene/55751):

> Predicted to enable transmembrane transporter activity. Predicted to be involved in transmembrane transport. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25587) · Entrez [55751](https://www.ncbi.nlm.nih.gov/gene/55751) · UniProt [Q9NVA4](https://www.uniprot.org/uniprotkb/Q9NVA4) · Ensembl [ENSG00000164168](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164168)

## Data

Gene col 8889: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8889); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8889, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8889]; `tensor/DDL_lfc|DDL_z.npy` [8889]; `embed/gene_vectors.npy` [8889]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8889 or target_col == 8889). Every well: [[TMEM184C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM184C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
