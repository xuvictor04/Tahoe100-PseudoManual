---
symbol: "ARPC1A"
type: "gene"
col: 14283
ensembl_id: "ENSG00000241685"
name: "actin related protein 2/3 complex subunit 1A"
location: "7q22.1"
module: 168
arm: "+"
pooled_cpm: 104.01
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# ARPC1A

*actin related protein 2/3 complex subunit 1A* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.31× (z +5.7, q 5e-06, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.523× (z -19.4, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLD3]] (+0.70, fdr 9e-06), [[LCMT1]] (+0.68, fdr 3e-05), [[SDHAP2]] (+0.68, fdr 1e-05); moves opposite to [[ATXN7]] (-0.65, fdr 1e-05), [[LEKR1]] (-0.63, fdr 6e-05), [[WARS2-AS1]] (-0.63, fdr 1e-04).
> It sits in the **+** arm of [[Module 168]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CACHD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14283.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +5.7 | 5e-06 | 31/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +5.6 | 5e-06 | 29/48 (NCI-H23, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.7 | 5e-04 | 19/37 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.004 | 23/48 (SW480, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **1.20×** | +3.8 | 0.016 | 22/47 (H4, RPMI-7951, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.066 | 17/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.075 | 12/49 (PANC-1, KATO III, …) | two highest doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.075 | 19/47 (NCI-H460, RKO, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.075 | 23/49 (SK-MEL-2, C32, …) | two highest doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.091 | 18/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14283.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.523×** | -19.4 | 0e+00 | 43/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -14.2 | 2e-43 | 35/49 (A-172, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.573×** | -11.3 | 2e-27 | 37/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.652×** | -9.1 | 2e-17 | 37/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.707×** | -7.4 | 2e-11 | 35/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.797×** | -6.8 | 1e-09 | 28/48 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.921× | -6.2 | 5e-08 | 2/50 (CHP-212, SW 1088) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.813×** | -4.0 | 0.004 | 24/47 (A-172, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Demeclocycline (drug)]] 5 µM |  | 0.881× | -3.8 | 0.009 | 7/48 (NCI-H23, SW48, …) | top dose only | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | 0.847× | -3.5 | 0.027 | 15/48 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.857× | -3.3 | 0.057 | 14/48 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | 0.862× | -3.0 | 0.12 | 18/47 (SNU-423, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14283. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 95.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -20.0) |
| [[HS-578T (line)]] | alt | 79.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -19.5) |
| [[AsPC-1 (line)]] | alt | 1,330 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -14.1) |
| [[hTERT-HPNE (line)]] | wt | 62.6 | 0 | 4 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.471× (z -9.6) |
| [[HOP62 (line)]] | alt | 80.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -17.1) |
| [[LoVo (line)]] | wt | 90.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 83.6 | 1 (1 ⚠) | 2 | [[Lonafarnib (drug)]] 5 µM 5.16× (z +8.6) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 131 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -15.4) |
| [[CFPAC-1 (line)]] | alt | 101 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -11.9) |
| [[H4 (line)]] | wt | 69.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -11.3) |
| [[HT-29 (line)]] | alt | 82.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -10.2) |
| [[KATO III (line)]] | alt | 99.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -12.1) |
| [[LS 180 (line)]] | wt | 90.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 83.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 74.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 67.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 51.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -12.5) |
| [[SW1417 (line)]] | alt | 84.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -12.0) |
| [[A498 (line)]] | wt | 87.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -12.3) |
| [[A549 (line)]] | wt | 74.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -10.6) |
| [[BT-474 (line)]] | alt | 46.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -10.2) |
| [[C32 (line)]] | wt | 111 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -11.0) |
| [[Hs 766T (line)]] | wt | 105 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -11.0) |
| [[J82 (line)]] | alt | 62.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 56.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 69.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -10.7) |
| [[SHP-77 (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 76.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -13.4) |
| [[SW 1088 (line)]] | alt | 146 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -8.7) |
| [[SW 1271 (line)]] | alt | 71.6 | 0 | 1 | — | [[Saquinavir (drug)]] 5 µM 0.237× (z -8.5) |
| [[A-427 (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 99.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 68.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14283), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLD3]] | +0.70 | +0.59 / +0.57 | both halves | 9e-06 | pathway: Fcgamma receptor (FCGR) dependent phagocytosis |
| [[LCMT1]] | +0.68 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[SDHAP2]] | +0.68 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[SDHAP1]] | +0.67 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[PCMT1]] | +0.67 | +0.70 / +0.39 | both halves | 6e-05 |  |
| [[F11R]] | +0.67 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[SDHAP4]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[SEC11A]] | +0.66 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[RAP1A]] | +0.66 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[CCZ1B]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.63 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[C1orf52]] | +0.63 | +0.69 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN7]] | -0.65 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[LEKR1]] | -0.63 | -0.70 / -0.39 | both halves | 6e-05 |  |
| [[WARS2-AS1]] | -0.63 | -0.66 / -0.36 | both halves | 1e-04 |  |
| [[ZNF747]] | -0.63 | -0.64 / -0.30 | both halves | 2e-04 |  |
| [[MEPCE]] | -0.62 | -0.66 / -0.36 | both halves | 1e-04 |  |
| [[DCAF8]] | -0.62 | -0.66 / -0.39 | both halves | 5e-05 | same gene group |
| [[ZNF827]] | -0.61 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[IQCH-AS1]] | -0.61 | -0.70 / -0.21 | both halves | 7e-04 |  |
| [[PATL2]] | -0.61 | -0.66 / -0.28 | both halves | 3e-04 |  |
| [[TSC22D1]] | -0.60 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[SIX5]] | -0.60 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[USP13]] | -0.60 | -0.63 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACHD1]] | B | CACHD1 activity lowers ARPC1A's level | lines that do not express CACHD1 (7) vs lines expressing it (43) | 1.60× higher at baseline in the lines without CACHD1 | 0.041 | ⚠ within organs, on part of the lines; also absent: KCNK15-AS1 |
| [[HDAC6]] | B | HDAC6 activity lowers ARPC1A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FZD7]] | C | FZD7 activity raises ARPC1A's level | lines that do not express FZD7 (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without FZD7 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2; its own permutation p |
| [[WARS2-AS1]] | C | WARS2-AS1 activity lowers ARPC1A's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 3.50× higher at baseline in the lines without WARS2-AS1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (0.1, -14.7); signed map (-37.9, 0.2). **Vector** length 129, 36.7% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +8.1 | +5.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.9 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.2 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | +3.5 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +0.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.0 | +2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.9 | -11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -19.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.3 | -7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -14.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.7 | -9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -6.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 2/3 complex subunit 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,325,898-99,366,262 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SOP2Hs, SOP2L, Arc40 |
| Gene groups (HGNC) | Actin related protein 2/3 complex subunits; WD repeat domain containing |
| Reactome | 19 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; EPHB-mediated forward signaling; FCGR3A-mediated phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92747](https://www.uniprot.org/uniprotkb/Q92747) (Actin-related protein 2/3 complex subunit 1A):

> Probably functions as a component of the Arp2/3 complex which is involved in regulation of actin polymerization and together with an activating nucleation-promoting factor (NPF) mediates the formation of branched actin networks.

**Summary**, from NCBI Gene [10552](https://www.ncbi.nlm.nih.gov/gene/10552):

> This gene encodes one of seven subunits of the human Arp2/3 protein complex. This subunit is a member of the SOP2 family of proteins and is most similar to the protein encoded by gene ARPC1B. The similarity between these two proteins suggests that they both may function as p41 subunit of the human Arp2/3 complex that has been implicated in the control of actin polymerization in cells. It is possible that the p41 subunit is involved in assembling and maintaining the structure of the Arp2/3 …

**Accessions** — [HGNC:703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:703) · Entrez [10552](https://www.ncbi.nlm.nih.gov/gene/10552) · UniProt [Q92747](https://www.uniprot.org/uniprotkb/Q92747) · Ensembl [ENSG00000241685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241685)

## Data

Gene col 14283: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14283); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14283, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14283]; `tensor/DDL_lfc|DDL_z.npy` [14283]; `embed/gene_vectors.npy` [14283]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14283 or target_col == 14283). Every well: [[ARPC1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARPC1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
