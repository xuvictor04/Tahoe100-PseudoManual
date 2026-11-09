---
symbol: "ADAP1"
type: "gene"
col: 2693
ensembl_id: "ENSG00000105963"
name: "ArfGAP with dual PH domains 1"
location: "7p22.3"
module: 31
arm: "+"
pooled_cpm: 22.03
n_lines_expressing: 43
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 31
direction_downstream: 3
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ADAP1

*ArfGAP with dual PH domains 1* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +18.9, q 0e+00, up in 25 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.613× (z -9.9, q 3e-20, down in 26 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAIAP2L2]] (+0.66, fdr 7e-06), [[KRT86]] (+0.63, fdr 7e-06), [[GALNT8]] (+0.61, fdr 1e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 31 arrows point to it, the strongest [[LAD1]] → it (grade B ⚠); 3 go from it, the strongest it → [[NKD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +18.9 | 0e+00 | 25/40 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +9.8 | 3e-20 | 15/27 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +5.2 | 4e-05 | 13/32 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 0.001 | 13/39 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +3.7 | 0.025 | 7/40 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.14× | +3.6 | 0.027 | 4/41 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.038 | 15/39 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.038 | 4/36 (NCI-H2347, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Pentoxifylline (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.048 | 2/39 (LS 180, SW1417) | inconsistent across doses | position effect removed |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.068 | 4/41 (SW480, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2693.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.613×** | -9.9 | 3e-20 | 26/40 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.649×** | -8.4 | 1e-14 | 24/38 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.688×** | -7.6 | 7e-12 | 22/40 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[NG25 (drug)]] 5 µM |  | **0.587×** | -5.6 | 3e-06 | 12/36 (BT-474, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -5.4 | 6e-06 | 22/37 (KATO III, SW 900, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.833×** | -5.2 | 2e-05 | 15/41 (RKO, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **0.769×** | -5.1 | 3e-05 | 15/34 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.791×** | -4.7 | 2e-04 | 9/40 (H4, SW480, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.799×** | -4.5 | 4e-04 | 17/40 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.791×** | -4.5 | 5e-04 | 11/38 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.831×** | -3.7 | 0.009 | 12/40 (NCI-H2030, CFPAC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.846× | -3.4 | 0.034 | 11/40 (HT-29, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.866× | -3.3 | 0.035 | 12/41 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.848× | -3.3 | 0.035 | 9/40 (SW480, AsPC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.849× | -3.3 | 0.035 | 11/39 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.863× | -3.2 | 0.039 | 14/41 (SW480, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.744×** | -3.1 | 0.054 | 11/41 (LS 180, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | **0.747×** | -3.1 | 0.058 | 6/33 (Panc 03.27, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 0.901× | -3.0 | 0.077 | 2/41 (HT-29, A-172) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.9 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +26.2) | — |
| [[KATO III (line)]] | alt | 89.2 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -17.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -11.4) |
| [[HT-29 (line)]] | alt | 95.3 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -12.5) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -9.0) |
| [[LS 180 (line)]] | wt | 65.8 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.305× (z -11.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.322× (z -11.3) |
| [[PANC-1 (line)]] | alt | 5.66 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 65.6 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.333× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 28.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.7) | [[Lonafarnib (drug)]] 5 µM 0.153× (z -8.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 42.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.367× (z -10.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.413× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 13.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -9.8) |
| [[SW48 (line)]] | wt | 47.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -9.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.249× (z -8.7) |
| [[SW480 (line)]] | alt | 32.3 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -11.7) |
| [[A-427 (line)]] | wt | 25.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -11.4) |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -8.8) |
| [[H4 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0863× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[HCT15 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -12.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 6.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 23.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.301× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 6.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 28.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 14.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -9.8) |
| [[A-172 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.47 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.07 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAIAP2L2]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[KRT86]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[GALNT8]] | +0.61 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[LAD1]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[LSMEM2]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TNNT2]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[SLC45A3]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ABR]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 | same gene group |
| [[NANOS3]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ITGB4]] | +0.58 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ARHGAP27]] | +0.58 | +0.62 / +0.54 | both halves | 1e-05 | same gene group |
| [[UNC13D]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 30, C 1. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAD1]] | B | LAD1 activity raises ADAP1's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 3.20× lower at baseline in the lines without LAD1 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[MISP]] | B | MISP activity raises ADAP1's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.94× lower at baseline in the lines without MISP | 0.002 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[TNNT2]] | B | TNNT2 activity raises ADAP1's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 3.19× lower at baseline in the lines without TNNT2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[ITGB4]] | B | ITGB4 activity raises ADAP1's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 2.89× lower at baseline in the lines without ITGB4 | 0.002 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[KLK6]] | B | KLK6 activity raises ADAP1's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 3.17× lower at baseline in the lines without KLK6 | 0.005 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15 |
| [[SLC6A20]] | B | SLC6A20 activity raises ADAP1's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 3.64× lower at baseline in the lines without SLC6A20 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |
| [[EPS8L3]] | B | EPS8L3 activity raises ADAP1's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.58× lower at baseline in the lines without EPS8L3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[COL17A1]] | B | COL17A1 activity raises ADAP1's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 2.90× lower at baseline in the lines without COL17A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[B3GNT3]] | B | B3GNT3 activity raises ADAP1's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.60× lower at baseline in the lines without B3GNT3 | 0.012 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[DENND2D]] | B | DENND2D activity raises ADAP1's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.23× lower at baseline in the lines without DENND2D | 0.016 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[LINC00857]] | B | LINC00857 activity raises ADAP1's level | lines that do not express LINC00857 (17) vs lines expressing it (33) | 2.48× lower at baseline in the lines without LINC00857 | 0.024 | ⚠ within organs, on part of the lines; also absent: KRT18, C19orf33, OCLN |
| [[GPR35]] | B | GPR35 activity raises ADAP1's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 2.97× lower at baseline in the lines without GPR35 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NKD2]] | B | ADAP1 activity raises NKD2's level | lines that do not express ADAP1 (7) vs lines expressing it (43) | 2.97× lower at baseline in the lines without ADAP1 | 0.062 | ⚠ within organs, on part of the lines; also absent: CCDC88C, ARRDC4, LYN; maybe low, not absent |
| [[TGIF2-RAB5IF]] | B | ADAP1 activity raises TGIF2-RAB5IF's level | lines that do not express ADAP1 (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without ADAP1 | 0.076 | ⚠ within organs, on part of the lines; also absent: CCDC88C, ARRDC4, LYN; maybe low, not absent |
| [[EPHA2]] | B | ADAP1 activity raises EPHA2's level | lines that do not express ADAP1 (7) vs lines expressing it (43) | 3.22× lower at baseline in the lines without ADAP1 | 0.094 | ⚠ within organs, on part of the lines; also absent: CCDC88C, ARRDC4, LYN; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.4, 49.8); signed map (22.1, 15.1). **Vector** length 85.4, 17.0% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.3 | +9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +18.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.4 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.9 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +0.8 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.3 | -5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.8 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -2.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -1.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with dual PH domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:897,900-955,407 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCS1L; previously CENTA1 |
| Gene groups (HGNC) | ArfGAPs; Pleckstrin homology domain containing |
| Reactome | 3 pathways, smallest: Nuclear signaling by ERBB4; Signaling by ERBB4; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [O75689](https://www.uniprot.org/uniprotkb/O75689) (Arf-GAP with dual PH domain-containing protein 1):

> GTPase-activating protein for the ADP ribosylation factor family (Probable). Binds phosphatidylinositol 3,4,5-trisphosphate (PtdInsP3) and inositol 1,3,4,5-tetrakisphosphate (InsP4). Regulates the incorporation of CD63 and CD9 into multivesicular bodies.

**Summary**, from NCBI Gene [11033](https://www.ncbi.nlm.nih.gov/gene/11033):

> Enables GTPase activator activity. Predicted to be involved in cell surface receptor signaling pathway. Located in cytosol; nucleus; and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16486](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16486) · Entrez [11033](https://www.ncbi.nlm.nih.gov/gene/11033) · UniProt [O75689](https://www.uniprot.org/uniprotkb/O75689) · Ensembl [ENSG00000105963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105963)

## Data

Gene col 2693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2693); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2693]; `tensor/DDL_lfc|DDL_z.npy` [2693]; `embed/gene_vectors.npy` [2693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2693 or target_col == 2693). Every well: [[ADAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
