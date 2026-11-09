---
symbol: "ELP1"
type: "gene"
col: 937
ensembl_id: "ENSG00000070061"
name: "elongator acetyltransferase complex subunit 1"
location: "9q31.3"
module: 57
arm: "+"
pooled_cpm: 63.06
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# ELP1

*elongator acetyltransferase complex subunit 1* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.34× (z +14.0, q 2e-41, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.765× (z -6.2, q 3e-07, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POT1]] (+0.77, fdr 7e-06), [[GTPBP3]] (+0.76, fdr 7e-06), [[SKP2]] (+0.76, fdr 7e-06); moves opposite to [[MED13]] (-0.74, fdr 3e-05), [[MMADHC-DT]] (-0.71, fdr 3e-05), [[CCDC90B-AS1]] (-0.71, fdr 6e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.34×** | +14.0 | 2e-41 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +11.8 | 2e-29 | 45/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +11.6 | 5e-29 | 47/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.49×** | +10.8 | 8e-25 | 44/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.62×** | +8.3 | 1e-14 | 36/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.8 | 1e-09 | 1/49 (A498) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +6.2 | 5e-08 | 29/48 (MIA PaCa-2, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +4.9 | 9e-05 | 27/48 (SK-MEL-2, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +4.8 | 1e-04 | 28/48 (RKO, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +3.9 | 0.006 | 24/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.012 | 22/49 (AsPC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +3.1 | 0.079 | 22/48 (NCI-H460, SW480, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 937.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -6.2 | 3e-07 | 32/49 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.704×** | -5.8 | 2e-06 | 32/49 (NCI-H23, SW 1271, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -5.3 | 3e-05 | 31/50 (LS 180, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -5.2 | 3e-05 | 29/48 (A498, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.782×** | -3.8 | 0.019 | 22/45 (NCI-H23, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.807×** | -3.6 | 0.035 | 23/48 (SW480, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.812×** | -3.4 | 0.046 | 20/48 (J82, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Thymol (drug)]] 5 µM |  | 0.865× | -3.4 | 0.051 | 14/48 (KATO III, SW 1271, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.747×** | -3.3 | 0.051 | 18/48 (HCT15, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.813×** | -3.3 | 0.056 | 18/47 (H4, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 77.0 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +11.1) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.41× (z +10.8) | — |
| [[SW480 (line)]] | alt | 73.5 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.61× (z +13.0) | — |
| [[RKO (line)]] | wt | 89.4 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.01× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -11.6) |
| [[HT-29 (line)]] | alt | 39.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +10.0) | — |
| [[LoVo (line)]] | wt | 50.0 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 68.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.60× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 67.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +13.3) | — |
| [[NCI-H2347 (line)]] | alt | 56.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.83× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 38.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.07× (z +10.5) | — |
| [[A-172 (line)]] | wt | 62.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.29× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.437× (z -8.8) ⚠ cell-cycle shift, explains ~13% of this change |
| [[A549 (line)]] | wt | 71.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -10.7) |
| [[COLO 205 (line)]] | alt | 43.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 15.9× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 84.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.14× (z +9.9) | — |
| [[J82 (line)]] | alt | 78.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.46× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 55.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 54.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -18.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 39.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.84× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 50.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.76× (z +9.0) | — |
| [[A-427 (line)]] | wt | 40.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.94× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 36.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 37.4 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.14× (z +8.6) | — |
| [[C32 (line)]] | wt | 45.5 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0908× (z -10.4) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 73.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -8.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 96.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.46× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 49.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.9) | — |
| [[KATO III (line)]] | alt | 52.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.18× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 33.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -9.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 62.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.81× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 96.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 74.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.317× (z -11.5) |
| [[SW 1271 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0946× (z -11.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 56.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -12.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 83.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.91× (z +9.4) | — |
| [[A498 (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 71.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 82.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POT1]] | +0.77 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[GTPBP3]] | +0.76 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SKP2]] | +0.76 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[TAF5L]] | +0.73 | +0.72 / +0.50 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[PAPSS1]] | +0.73 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[ANAPC5]] | +0.73 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[PIK3R2]] | +0.72 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[POGLUT2]] | +0.72 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SKIC3]] | +0.71 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ATG4C]] | +0.70 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[THYN1]] | +0.70 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[SLC35A3]] | +0.70 | +0.66 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED13]] | -0.74 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[MMADHC-DT]] | -0.71 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | -0.71 | -0.62 / -0.38 | both halves | 6e-05 |  |
| [[LINC01004]] | -0.71 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[ZNF341-AS1]] | -0.69 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ZBED5]] | -0.69 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[PPP1R12A-AS2]] | -0.69 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[GCNT4]] | -0.69 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[KANSL1L]] | -0.67 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[BAZ2B]] | -0.66 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[ARRDC3-AS1]] | -0.66 | -0.57 / -0.29 | both halves | 2e-04 |  |
| [[LINC00571]] | -0.66 | -0.54 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ELP1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HACE1]] | C | HACE1 activity raises ELP1's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.61× lower at baseline in the lines without HACE1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.780). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.5, -7.7); signed map (-38.3, -12.7). **Vector** length 107, 31.3% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.9 | +14.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.6 | +11.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.6 | +11.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.8 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | -5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +8.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.5 | +0.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.7 | -2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -6.0 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | elongator acetyltransferase complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:108,866,898-108,934,328 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IKAP, TOT1, IKI3; previously DYS, IKBKAP |
| Gene groups (HGNC) | Elongator acetyltransferase complex |
| Hallmark sets | P53_PATHWAY |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O95163](https://www.uniprot.org/uniprotkb/O95163) (Elongator complex protein 1):

> Component of the elongator complex which is required for multiple tRNA modifications, including mcm5U (5-methoxycarbonylmethyl uridine), mcm5s2U (5-methoxycarbonylmethyl-2-thiouridine), and ncm5U (5-carbamoylmethyl uridine). The elongator complex catalyzes the formation of carboxymethyluridine in the wobble base at position 34 in tRNAs. Regulates the migration and branching of projection neurons in the developing cerebral cortex, through a process depending on alpha-tubulin acetylation (By …

**Summary**, from NCBI Gene [8518](https://www.ncbi.nlm.nih.gov/gene/8518):

> The protein encoded by this gene is a scaffold protein and a regulator for three different kinases involved in proinflammatory signaling. The encoded protein can bind NF-kappa-B-inducing kinase and I-kappa-B kinases through separate domains and assemble them into an active kinase complex. Mutations in this gene have been associated with familial dysautonomia. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:5959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5959) · Entrez [8518](https://www.ncbi.nlm.nih.gov/gene/8518) · UniProt [O95163](https://www.uniprot.org/uniprotkb/O95163) · Ensembl [ENSG00000070061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070061)

## Data

Gene col 937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 937); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 937]; `tensor/DDL_lfc|DDL_z.npy` [937]; `embed/gene_vectors.npy` [937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 937 or target_col == 937). Every well: [[ELP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
