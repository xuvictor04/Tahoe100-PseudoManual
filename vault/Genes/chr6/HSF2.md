---
symbol: "HSF2"
type: "gene"
col: 360
ensembl_id: "ENSG00000025156"
name: "heat shock transcription factor 2"
location: "6q22.31"
module: 146
arm: "+"
pooled_cpm: 19.95
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 13
n_dd_up_clean: 26
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# HSF2

*heat shock transcription factor 2* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.05× (z +13.6, q 2e-39, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.595× (z -7.0, q 2e-09, down in 28 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 0.05 µM: 0.728× (z -4.3, q 0.004, down in 16 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPS4]] (+0.69, fdr 7e-06), [[C16orf87]] (+0.69, fdr 7e-06), [[FBXO7]] (+0.68, fdr 1e-05); moves opposite to [[TUT7]] (-0.64, fdr 7e-06), [[ERCC1]] (-0.64, fdr 7e-06), [[GPATCH2L]] (-0.63, fdr 8e-06).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NIPAL1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Adagrasib (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 360.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +13.6 | 2e-39 | 43/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.63×** | +12.9 | 7e-36 | 44/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.49×** | +12.2 | 4e-32 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +12.1 | 2e-31 | 37/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.16×** | +11.5 | 1e-28 | 45/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.35×** | +11.5 | 2e-28 | 44/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.32×** | +11.3 | 2e-27 | 43/47 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +10.6 | 2e-24 | 38/46 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.16×** | +9.8 | 1e-20 | 43/48 (PANC-1, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.00×** | +9.3 | 7e-19 | 38/48 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.49×** | +8.8 | 9e-17 | 35/46 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.82×** | +8.0 | 5e-14 | 30/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.69×** | +7.1 | 8e-11 | 31/47 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +7.0 | 9e-11 | 33/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +6.8 | 3e-10 | 29/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +6.7 | 8e-10 | 32/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +6.4 | 6e-09 | 32/47 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +6.2 | 2e-08 | 30/48 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 360.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.595×** | -7.0 | 2e-09 | 28/42 (SW1417, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.595×** | -6.7 | 5e-09 | 22/30 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.728×** | -4.3 | 0.004 | 16/47 (SW1417, A549, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.751×** | -3.8 | 0.017 | 14/47 (SW1417, NCI-H1792, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.775×** | -3.4 | 0.059 | 11/47 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.777×** | -3.4 | 0.059 | 16/47 (A498, SW 900, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -3.4 | 0.059 | 10/48 (SW1417, RPMI-7951, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.781×** | -3.3 | 0.059 | 14/47 (RPMI-7951, HS-578T, …) | two highest doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.774×** | -3.3 | 0.059 | 8/47 (LOX-IMVI, C32, …) | rises with dose |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.785×** | -3.3 | 0.062 | 10/47 (A498, HOP62, …) | two highest doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.787×** | -3.2 | 0.062 | 13/47 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.780×** | -3.2 | 0.062 | 16/47 (NCI-H1792, RPMI-7951, …) | top dose only | plate-row cell shift |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **0.797×** | -3.1 | 0.097 | 12/47 (J82, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 360. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.9 | 10 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.93× (z +14.5) | — |
| [[SW480 (line)]] | alt | 30.3 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +11.7) | — |
| [[KATO III (line)]] | alt | 18.1 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.19× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.49× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 16.0 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.76× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +9.7) | — |
| [[LoVo (line)]] | wt | 14.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.54× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 38.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -11.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +8.7) | — |
| [[A549 (line)]] | wt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +10.9) | — |
| [[AN3 CA (line)]] | alt | 75.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -8.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 12.3 | 0 | 1 | — | [[Baicalin (drug)]] 0.05 µM 0.0482× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0960× (z -15.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 14.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.58× (z +8.8) | — |
| [[J82 (line)]] | alt | 22.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.06× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -9.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -10.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +8.6) | — |
| [[A-172 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 360), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS4]] | +0.69 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[C16orf87]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[FBXO7]] | +0.68 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[NAA16]] | +0.68 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[KCTD3]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[MLLT10]] | +0.67 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[KCTD6]] | +0.67 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[KDM1A]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[BLMH]] | +0.65 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[TADA1]] | +0.65 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[REPS1]] | +0.64 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[PDS5B]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUT7]] | -0.64 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[ERCC1]] | -0.64 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[GPATCH2L]] | -0.63 | -0.57 / -0.69 | both halves | 8e-06 |  |
| [[MCL1]] | -0.62 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[SETX]] | -0.61 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[KCTD5]] | -0.61 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[CRK]] | -0.61 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[NABP1]] | -0.60 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ZNF674]] | -0.59 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[MYSM1]] | -0.58 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[SAP30BP]] | -0.58 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[ZNF432]] | -0.58 | -0.52 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIPAL1]] | B | NIPAL1 activity lowers HSF2's level | lines that do not express NIPAL1 (5) vs lines expressing it (45) | 2.00× higher at baseline in the lines without NIPAL1 | 0.009 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[ZNF618]] | B | ZNF618 activity raises HSF2's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 1.76× lower at baseline in the lines without ZNF618 | 0.023 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |
| [[LRP3]] | B | LRP3 activity raises HSF2's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without LRP3 | 0.043 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[MEOX2]] | B | MEOX2 activity raises HSF2's level | lines that do not express MEOX2 (36) vs lines expressing it (14) | 1.56× lower at baseline in the lines without MEOX2 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, MMRN1, ENSG00000232252 |
| [[NABP1]] | C | NABP1 activity lowers HSF2's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 3.00× higher at baseline in the lines without NABP1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Adagrasib (drug)]] 0.5 µM | C | HSF2's natural level raises the cells' numbers under Adagrasib 0.5 µM (protects the cells) | HSF2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.339 over the table, 0.039 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.8, -8.5); signed map (-29.3, -16.3). **Vector** length 79.8, 19.3% of its response variance represented; |z| ≥ 3 in 1,190 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +1.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.7 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.5 | +12.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +5.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.6 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | +6.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.4 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | heat shock transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31 — chr6:122,399,551-122,433,119 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Heat shock transcription factor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03933](https://www.uniprot.org/uniprotkb/Q03933) (Heat shock factor protein 2):

> DNA-binding protein that specifically binds heat shock promoter elements (HSE) and activates transcription. In higher eukaryotes, HSF is unable to bind to the HSE unless the cells are heat shocked.

**Summary**, from NCBI Gene [3298](https://www.ncbi.nlm.nih.gov/gene/3298):

> The protein encoded by this gene belongs to the HSF family of transcription factors that bind specifically to the heat-shock promoter element and activate transcription. Heat shock transcription factors activate heat-shock response genes under conditions of heat or other stresses. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2011]

**Accessions** — [HGNC:5225](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5225) · Entrez [3298](https://www.ncbi.nlm.nih.gov/gene/3298) · UniProt [Q03933](https://www.uniprot.org/uniprotkb/Q03933) · Ensembl [ENSG00000025156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000025156)

## Data

Gene col 360: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 360); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 360, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 360]; `tensor/DDL_lfc|DDL_z.npy` [360]; `embed/gene_vectors.npy` [360]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 360 or target_col == 360). Every well: [[HSF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
