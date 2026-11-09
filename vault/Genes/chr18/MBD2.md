---
symbol: "MBD2"
type: "gene"
col: 5501
ensembl_id: "ENSG00000134046"
name: "methyl-CpG binding domain protein 2"
location: "18q21.2"
module: 188
arm: "+"
pooled_cpm: 83.28
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# MBD2

*methyl-CpG binding domain protein 2* — 18q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.57× (z +11.5, q 1e-27, up in 36 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.68× (z +7.2, q 2e-10, up in 33 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (LoVo 2.69×, RKO 2.13×; ⚠ toxic).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.580× (z -20.5, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX4]] (+0.71, fdr 7e-06), [[REPS1]] (+0.68, fdr 1e-05), [[RFXAP]] (+0.67, fdr 7e-06); moves opposite to [[ZNF335]] (-0.67, fdr 1e-05), [[ERCC6L2]] (-0.59, fdr 5e-05), [[DPH1-AS1]] (-0.58, fdr 1e-05).
> It is in [[Module 188]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TSPAN33]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5501.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (LoVo 2.69×, RKO 2.13×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +11.5 | 1e-27 | 36/46 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +7.2 | 2e-10 | 33/47 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +6.6 | 6e-09 | 28/48 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +6.1 | 1e-07 | 18/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.7 | 3e-04 | 16/47 (H4, HT-29, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +3.7 | 0.024 | 15/47 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.14× | +3.3 | 0.093 | 13/46 (H4, RPMI-7951, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.13× | +3.2 | 0.10 | 10/47 (LS 180, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5501.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.580×** | -20.5 | 0e+00 | 38/47 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.611×** | -18.6 | 0e+00 | 45/48 (SW48, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.580×** | -14.5 | 1e-45 | 43/47 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.654×** | -11.3 | 1e-27 | 39/47 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.750×** | -7.7 | 2e-12 | 32/47 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.768×** | -6.8 | 1e-09 | 27/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.790×** | -6.3 | 3e-08 | 29/47 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.866× | -5.4 | 4e-06 | 14/47 (BT-474, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.811×** | -5.4 | 5e-06 | 22/49 (LS 180, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.826×** | -5.1 | 2e-05 | 23/47 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.851× | -4.3 | 9e-04 | 20/47 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.847× | -4.3 | 9e-04 | 22/47 (HS-578T, LS 180, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | 0.855× | -4.0 | 0.002 | 19/43 (KATO III, NCI-H2347, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | 0.862× | -3.8 | 0.005 | 18/46 (SW 1271, NCI-H2347, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.867× | -3.8 | 0.005 | 11/47 (LS 180, NCI-H1792, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.895× | -3.0 | 0.088 | 4/47 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 60.9 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 61.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 146 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -16.5) |
| [[BT-474 (line)]] | alt | 93.1 | 0 | 4 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.132× (z -12.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.509× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 128 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -11.8) |
| [[HS-578T (line)]] | alt | 142 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -14.4) |
| [[HT-29 (line)]] | alt | 70.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -12.2) |
| [[LS 180 (line)]] | wt | 133 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 94.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -16.2) |
| [[CFPAC-1 (line)]] | alt | 78.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -15.5) |
| [[hTERT-HPNE (line)]] | wt | 96.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -13.6) |
| [[LoVo (line)]] | wt | 73.8 | 1 (1 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 2.69× (z +13.6) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -12.3) |
| [[HCT15 (line)]] | alt | 139 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -14.1) |
| [[HOP62 (line)]] | alt | 46.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -13.7) |
| [[LOX-IMVI (line)]] | wt | 120 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 146 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -17.7) |
| [[NCI-H460 (line)]] | wt | 76.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -12.9) |
| [[RKO (line)]] | wt | 91.9 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.13× (z +8.8) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -9.4) |
| [[SW 1271 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -12.7) |
| [[A-427 (line)]] | wt | 91.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.448× (z -12.0) |
| [[COLO 205 (line)]] | alt | 46.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -11.0) |
| [[Hs 766T (line)]] | wt | 65.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -8.7) |
| [[J82 (line)]] | alt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -13.8) |
| [[KATO III (line)]] | alt | 86.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[NCI-H1573 (line)]] | alt | 47.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 141 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 74.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.577× (z -9.4) |
| [[PANC-1 (line)]] | alt | 54.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.645× (z -9.7) |
| [[SHP-77 (line)]] | alt | 67.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 87.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -11.4) |
| [[SNU-423 (line)]] | alt | 61.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -13.3) |
| [[SW48 (line)]] | wt | 73.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -15.4) |
| [[A498 (line)]] | wt | 81.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 71.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 119 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 81.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 87.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 45.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX4]] | +0.71 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[REPS1]] | +0.68 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[RFXAP]] | +0.67 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[CCNY]] | +0.67 | +0.80 / +0.49 | both halves | 1e-05 |  |
| [[OTULIN]] | +0.65 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[SERAC1]] | +0.65 | +0.75 / +0.42 | both halves | 4e-05 |  |
| [[RTCA]] | +0.64 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[RAP1A]] | +0.64 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[MFSD14CP]] | +0.63 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[ALG9]] | +0.62 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[FAR1]] | +0.62 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[CDS2]] | +0.62 | +0.77 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF335]] | -0.67 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.59 | -0.73 / -0.40 | both halves | 5e-05 |  |
| [[DPH1-AS1]] | -0.58 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[MPDU1]] | -0.57 | -0.68 / -0.47 | both halves | 2e-05 |  |
| [[KDM6B]] | -0.56 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[SYS1]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[SON]] | -0.55 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[TUT7]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[FOSB]] | -0.53 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[KDSR]] | -0.53 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[MCL1]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[MYSM1]] | -0.53 | -0.53 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity weakens MBD2's drug response | lines that do not express TSPAN33 (12) vs lines expressing it (36) | the lines without TSPAN33 respond 1.21× as strongly (z diff -0.56); strongest at Homoharringtonine 5 µM: 0.48x vs 0.64x (z diff -2.3) | 0.053 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[DUBR]] | B | DUBR activity raises MBD2's level | lines that do not express DUBR (8) vs lines expressing it (42) | 1.75× lower at baseline in the lines without DUBR | 0.055 | ⚠ within organs, on part of the lines; also absent: ATP10D, LRP12, CYP46A1 |
| [[HDAC6]] | B | HDAC6 activity raises MBD2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.743). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.7, -11.0); signed map (-34.2, -17.1). **Vector** length 94.1, 23.0% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.7 | +11.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.3 | +6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +0.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.5 | -7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -20.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +1.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -6.8 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | -1.8 | -2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.8 | -1.8 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.7 | -3.0 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | methyl-CpG binding domain protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.2 — chr18:54,151,606-54,224,669 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Methyl-CpG binding domain containing; NuRD complex subunits; Small nucleolar RNA protein coding host genes |
| Reactome | 11 pathways, smallest: RNA Polymerase I Promoter Opening; Interaction of NuRD complexes with transcription factors; NuRD complex assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBB5](https://www.uniprot.org/uniprotkb/Q9UBB5) (Methyl-CpG-binding domain protein 2):

> Binds CpG islands in promoters where the DNA is methylated at position 5 of cytosine within CpG dinucleotides. Binds hemimethylated DNA as well. Recruits histone deacetylases and DNA methyltransferases to chromatin. Acts as a component of the histone deacetylase NuRD complex which participates in the remodeling of chromatin. Acts as a transcriptional repressor and plays a role in gene silencing. Functions as a scaffold protein, targeting GATAD2A and GATAD2B to chromatin to promote repression. …

**Summary**, from NCBI Gene [8932](https://www.ncbi.nlm.nih.gov/gene/8932):

> DNA methylation is the major modification of eukaryotic genomes and plays an essential role in mammalian development. Human proteins MECP2, MBD1, MBD2, MBD3, and MBD4 comprise a family of nuclear proteins related by the presence in each of a methyl-CpG binding domain (MBD). Each of these proteins, with the exception of MBD3, is capable of binding specifically to methylated DNA. MECP2, MBD1 and MBD2 can also repress transcription from methylated gene promoters. The protein encoded by this gene …

**Accessions** — [HGNC:6917](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6917) · Entrez [8932](https://www.ncbi.nlm.nih.gov/gene/8932) · UniProt [Q9UBB5](https://www.uniprot.org/uniprotkb/Q9UBB5) · Ensembl [ENSG00000134046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134046)

## Data

Gene col 5501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5501); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5501]; `tensor/DDL_lfc|DDL_z.npy` [5501]; `embed/gene_vectors.npy` [5501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5501 or target_col == 5501). Every well: [[MBD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
