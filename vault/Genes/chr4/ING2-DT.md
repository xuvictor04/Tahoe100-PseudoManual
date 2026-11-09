---
symbol: "ING2-DT"
type: "gene"
col: 13856
ensembl_id: "ENSG00000232648"
name: "ING2 divergent transcript"
location: "4q35.1"
module: 15
arm: "+"
pooled_cpm: 5.67
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ING2-DT

*ING2 divergent transcript* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.47× (z +27.8, q 0e+00, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.515× (z -7.7, q 1e-11, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMNAT1]] (+0.65, fdr 1e-05), [[FKBP14-AS1]] (+0.65, fdr 1e-05), [[SPESP1]] (+0.65, fdr 1e-05); moves opposite to [[CCDC6]] (-0.54, fdr 2e-04), [[ARAF]] (-0.54, fdr 5e-05), [[TTC5]] (-0.54, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[AT7519 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13856.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.47×** | +27.8 | 0e+00 | 40/40 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.41×** | +16.5 | 0e+00 | 38/39 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.82×** | +11.5 | 2e-28 | 32/38 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +8.6 | 1e-15 | 18/31 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +6.0 | 2e-07 | 21/46 (AsPC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.003 | 9/46 (SW480, Panc 03.27, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.1 | 0.003 | 12/41 (A549, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +4.0 | 0.005 | 6/47 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.018 | 10/47 (SW480, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.024 | 7/46 (C-33 A, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +3.4 | 0.029 | 3/44 (LoVo, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.34×** | +3.4 | 0.030 | 12/47 (A498, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.34×** | +3.1 | 0.086 | 4/16 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13856.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.515×** | -7.7 | 1e-11 | 26/47 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.563×** | -6.4 | 5e-08 | 21/34 (AsPC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.399×** | -5.5 | 5e-06 | 16/38 (SNU-423, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.419×** | -5.3 | 2e-05 | 18/43 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.644×** | -5.1 | 4e-05 | 18/37 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.660×** | -4.8 | 1e-04 | 17/47 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.468×** | -4.6 | 4e-04 | 12/34 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.692×** | -4.3 | 0.001 | 15/40 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.664×** | -4.0 | 0.005 | 12/46 (C32, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.725×** | -3.6 | 0.021 | 11/47 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.747×** | -3.2 | 0.061 | 14/46 (NCI-H23, HEC-1-A, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.759×** | -3.2 | 0.067 | 6/47 (NCI-H2030, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.754×** | -3.1 | 0.089 | 10/43 (HEC-1-A, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Hesperidin (drug)]] 0.05 µM |  | **0.751×** | -3.1 | 0.089 | 7/43 (COLO 205, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13856. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[SW480 (line)]] | alt | 4.43 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.63× (z +13.2) | [[Digitoxin (drug)]] 5 µM 0.165× (z -8.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 4.22 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.60× (z +8.8) | [[Cytarabine (drug)]] 5 µM 0.0681× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 9.21 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0539× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 7.61 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 3.27 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0939× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[NCI-H460 (line)]] | wt | 6.45 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +12.1) | — |
| [[A-172 (line)]] | wt | 8.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +11.4) | — |
| [[A498 (line)]] | wt | 4.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.63× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 3.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 5.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.54× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 4.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 4.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.90× (z +9.5) | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.140× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 4.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.07× (z +11.9) | — |
| [[LOX-IMVI (line)]] | wt | 5.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 3.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.21× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 7.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 3.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.93× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 7.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +12.3) | — |
| [[RKO (line)]] | wt | 4.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.92× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 2.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +10.3) | — |
| [[A-427 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13856), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMNAT1]] | +0.65 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[FKBP14-AS1]] | +0.65 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SPESP1]] | +0.65 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[DARS1-AS1]] | +0.64 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CATSPER2P1]] | +0.64 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[DHX32]] | +0.63 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[GATD1-DT]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 | same gene group |
| [[DPY19L2P3]] | +0.62 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[PHC2-AS1]] | +0.60 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[PPP1R26-AS1]] | +0.60 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[RHCE]] | +0.60 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[POC1B-AS1]] | +0.60 | +0.37 / +0.60 | both halves | 9e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC6]] | -0.54 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[ARAF]] | -0.54 | -0.39 / -0.61 | both halves | 5e-05 |  |
| [[TTC5]] | -0.54 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[RBM18]] | -0.53 | -0.29 / -0.53 | both halves | 3e-04 |  |
| [[EXOC3]] | -0.51 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[EHMT2]] | -0.51 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[GCOM1]] | -0.51 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[ECHS1]] | -0.50 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[VTA1]] | -0.50 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[WDR7]] | -0.50 | -0.17 / -0.42 | ⚠ not reproduced | 0.001 |  |
| [[STX8]] | -0.50 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[COG2]] | -0.50 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[WDR70]] | -0.50 | -0.26 / -0.38 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ING2-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[AT7519 (drug)]] 5 µM | C | ING2-DT's natural level raises the cells' numbers under AT7519 5 µM (protects the cells) | ING2-DT's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63 | 0.406 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.1, 22.0); signed map (17.4, -4.4). **Vector** length 70.7, 11.7% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +27.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +16.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.9 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.0 | +4.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.6 |
|  | [[NG25 (drug)]] 5 µM |  | -2.4 | -4.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ING2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q35.1 — chr4:183,494,884-183,504,494 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55723) · Entrez [389247](https://www.ncbi.nlm.nih.gov/gene/389247) · Ensembl [ENSG00000232648](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232648)

## Data

Gene col 13856: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13856); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13856, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13856]; `tensor/DDL_lfc|DDL_z.npy` [13856]; `embed/gene_vectors.npy` [13856]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13856 or target_col == 13856). Every well: [[ING2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ING2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
