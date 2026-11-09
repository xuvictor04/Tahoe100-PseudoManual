---
symbol: "DCTN5"
type: "gene"
col: 9370
ensembl_id: "ENSG00000166847"
name: "dynactin subunit 5"
location: "16p12.2"
module: 156
arm: "+"
pooled_cpm: 45.01
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# DCTN5

*dynactin subunit 5* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +21.1, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.791× (z -8.3, q 8e-14, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[URM1]] (+0.67, fdr 1e-05), [[PIGG]] (+0.65, fdr 1e-05), [[ACAD9]] (+0.65, fdr 1e-05); moves opposite to [[TTBK2]] (-0.61, fdr 4e-05), [[CHD1]] (-0.56, fdr 4e-05), [[PPP2R2A]] (-0.56, fdr 7e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PDCD6P1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9370.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +21.1 | 0e+00 | 45/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.07×** | +14.6 | 1e-45 | 43/49 (A498, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +12.0 | 5e-31 | 36/48 (LoVo, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +9.9 | 7e-21 | 36/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +7.7 | 2e-12 | 24/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.23×** | +7.2 | 5e-11 | 25/48 (A498, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +6.7 | 1e-09 | 25/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.31×** | +6.5 | 5e-09 | 24/47 (SNU-1, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +6.3 | 2e-08 | 20/48 (SW1417, A-172, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +6.0 | 1e-07 | 26/48 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +5.9 | 1e-07 | 22/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.9 | 5e-05 | 21/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.20×** | +4.6 | 2e-04 | 17/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.19× | +4.4 | 4e-04 | 15/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.3 | 6e-04 | 13/35 (SW480, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.002 | 12/47 (NCI-H23, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.005 | 7/48 (HEC-1-A, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.005 | 9/48 (NCI-H1792, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.017 | 11/48 (A498, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.024 | 6/48 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.035 | 8/48 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.060 | 3/48 (NCI-H460, A498, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9370.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.791×** | -8.3 | 8e-14 | 30/48 (J82, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.794×** | -5.8 | 2e-06 | 24/48 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.798×** | -4.0 | 0.012 | 16/47 (HCT15, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.888× | -3.2 | 0.17 | 5/48 (LOX-IMVI, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 0.882× | -3.1 | 0.20 | 6/48 (A549, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 38.9 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +14.9) | — |
| [[SW480 (line)]] | alt | 47.7 | 5 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.464× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 49.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 43.4 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.95× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 74.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +12.5) | — |
| [[LoVo (line)]] | wt | 38.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.61× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 38.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 52.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +12.7) | — |
| [[SW1417 (line)]] | alt | 60.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +12.2) | — |
| [[A-172 (line)]] | wt | 30.7 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.99× (z +8.7) | — |
| [[A549 (line)]] | wt | 39.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +12.8) | — |
| [[BT-474 (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.317× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 59.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 38.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 55.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 30.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 36.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +13.0) | — |
| [[HT-29 (line)]] | alt | 35.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.02× (z +9.8) | — |
| [[KATO III (line)]] | alt | 49.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 27.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +12.5) | — |
| [[RKO (line)]] | wt | 55.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 36.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 46.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.14× (z +9.6) ⚠ toxic; cell-cycle shift, explains ~21% of this change | — |
| [[SNU-423 (line)]] | alt | 42.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.7) | — |
| [[A-427 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[URM1]] | +0.67 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[PIGG]] | +0.65 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ACAD9]] | +0.65 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[EAF1]] | +0.64 | +0.44 / +0.52 | both halves | 3e-05 | pathway: Affinity selection of immunoglobulins |
| [[LRRC41]] | +0.64 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[MAP3K7]] | +0.63 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[GPN2]] | +0.62 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[EXOSC3]] | +0.62 | +0.37 / +0.53 | both halves | 8e-05 | pathway: Affinity selection of immunoglobulins |
| [[ERVK13-1]] | +0.62 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[ATXN1L]] | +0.61 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[UQCC1]] | +0.61 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[LY6G5B]] | +0.61 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTBK2]] | -0.61 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[CHD1]] | -0.56 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[PPP2R2A]] | -0.56 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[HNRNPDL]] | -0.55 | -0.24 / -0.49 | both halves | 4e-04 |  |
| [[USP2]] | -0.55 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[NEDD9]] | -0.52 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[CCDC112]] | -0.52 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[HPF1]] | -0.51 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[SMCHD1]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[TRIM37]] | -0.51 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[PSIP1]] | -0.50 | -0.40 / -0.48 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDCD6P1]] | C | PDCD6P1 activity strengthens DCTN5's drug response | lines that do not express PDCD6P1 (4) vs lines expressing it (45) | the lines without PDCD6P1 respond 0.83× as strongly (z diff +0.84); strongest at Ouabain (Octahydrate) 5 µM: 1.10x vs 1.60x (z diff +3.6) | 0.064 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NSUN5, KIAA1671, ENSG00000291079; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.411). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.6, 19.1); signed map (7.4, 0.3). **Vector** length 89.9, 19.2% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +21.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +12.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +14.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +4.9 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +6.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +3.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.6 | -8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.3 | -5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -5.1 | -2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | dynactin subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:23,641,466-23,677,472 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3248, p25 |
| Gene groups (HGNC) | Dynactin subunits |
| Reactome | 17 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTE1](https://www.uniprot.org/uniprotkb/Q9BTE1) (Dynactin subunit 5):

> Part of the dynactin complex that activates the molecular motor dynein for ultra-processive transport along microtubules.

**Summary**, from NCBI Gene [84516](https://www.ncbi.nlm.nih.gov/gene/84516):

> This gene encodes a subunit of dynactin, a component of the cytoplasmic dynein motor machinery involved in minus-end-directed transport. The encoded protein is a component of the pointed-end subcomplex and is thought to bind membranous cargo. A pseudogene of this gene is located on the long arm of chromosome 1. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:24594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24594) · Entrez [84516](https://www.ncbi.nlm.nih.gov/gene/84516) · UniProt [Q9BTE1](https://www.uniprot.org/uniprotkb/Q9BTE1) · Ensembl [ENSG00000166847](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166847)

## Data

Gene col 9370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9370); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9370]; `tensor/DDL_lfc|DDL_z.npy` [9370]; `embed/gene_vectors.npy` [9370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9370 or target_col == 9370). Every well: [[DCTN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCTN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
