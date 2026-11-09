---
symbol: "TMEM53"
type: "gene"
col: 4716
ensembl_id: "ENSG00000126106"
name: "transmembrane protein 53"
location: "1p34.1"
module: 86
arm: "+"
pooled_cpm: 6.39
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# TMEM53

*transmembrane protein 53* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.32× (z +4.9, q 6e-04, up in 15 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.445× (z -14.2, q 7e-43, down in 29 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNE]] (+0.53, fdr 3e-05), [[FDPS]] (+0.53, fdr 4e-05), [[HSD17B7]] (+0.52, fdr 3e-05); moves opposite to [[EGFR]] (-0.46, fdr 4e-05), [[ETS1]] (-0.45, fdr 8e-05), [[COL4A2]] (-0.44, fdr 4e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TJP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4716.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.9 | 6e-04 | 15/38 (LOX-IMVI, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.031 | 9/44 (A549, LoVo, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.054 | 10/41 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +3.5 | 0.058 | 10/41 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.4 | 0.088 | 6/40 (H4, SW 900, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.29× | +3.1 | 0.17 | 6/44 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 1.28× | +3.0 | 0.17 | 7/39 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Fulvestrant (drug)]] 0.5 µM |  | 1.28× | +3.0 | 0.17 | 1/43 (SHP-77) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4716.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.445×** | -14.2 | 7e-43 | 29/39 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.334×** | -13.0 | 2e-36 | 34/42 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.372×** | -12.2 | 5e-32 | 34/46 (COLO 205, SW1417, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.392×** | -11.6 | 7e-29 | 26/37 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.517×** | -8.2 | 4e-14 | 27/44 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.306×** | -7.6 | 2e-12 | 27/38 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.565×** | -7.1 | 1e-10 | 23/44 (SW480, H4, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.381×** | -6.2 | 3e-08 | 23/43 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.612×** | -6.1 | 8e-08 | 21/40 (SW480, AsPC-1, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.677×** | -4.7 | 2e-04 | 16/39 (SNU-423, SW 900, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.704×** | -4.3 | 7e-04 | 16/44 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.719×** | -4.1 | 0.002 | 12/46 (COLO 205, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.722×** | -4.0 | 0.002 | 13/41 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.724×** | -3.9 | 0.005 | 17/33 (NCI-H23, KATO III, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.739×** | -3.6 | 0.012 | 10/44 (SW1417, NCI-H23, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **0.772×** | -3.2 | 0.047 | 9/43 (SW48, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4716. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.41 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0695× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.286× (z -12.4) |
| [[PANC-1 (line)]] | alt | 9.59 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -13.2) |
| [[COLO 205 (line)]] | alt | 20.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0914× (z -16.4) |
| [[Panc 03.27 (line)]] | alt | 7.78 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -8.9) |
| [[A-172 (line)]] | wt | 3.62 | 0 | 2 | — | [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0748× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 6.84 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0662× (z -14.5) |
| [[HT-29 (line)]] | alt | 9.53 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -15.8) |
| [[KATO III (line)]] | alt | 10.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -10.4) |
| [[A498 (line)]] | wt | 6.40 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -11.6) |
| [[A549 (line)]] | wt | 3.98 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0666× (z -8.8) |
| [[BT-474 (line)]] | alt | 4.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 9.72 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -11.3) |
| [[J82 (line)]] | alt | 3.06 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0592× (z -9.1) |
| [[LoVo (line)]] | wt | 5.30 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.111× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 7.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 9.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 5.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -8.8) |
| [[SHP-77 (line)]] | alt | 8.16 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.103× (z -9.1) |
| [[SW1417 (line)]] | alt | 6.04 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0868× (z -11.2) |
| [[A-427 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4716), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNE]] | +0.53 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[FDPS]] | +0.53 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[HSD17B7]] | +0.52 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[RAD9A]] | +0.51 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[SUOX]] | +0.51 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[HSD17B7P2]] | +0.50 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[ADCY4]] | +0.50 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[CAPN12]] | +0.49 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[FDFT1]] | +0.49 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[MVD]] | +0.48 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[PROM2]] | +0.48 | +0.44 / +0.39 | both halves | 5e-05 |  |
| [[ZBTB3]] | +0.48 | +0.48 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGFR]] | -0.46 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ETS1]] | -0.45 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[COL4A2]] | -0.44 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[CALD1]] | -0.44 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[EVC]] | -0.42 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[SNAI2]] | -0.40 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[SEPTIN11]] | -0.40 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[RFTN1]] | -0.40 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[KIRREL1]] | -0.40 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[AGL]] | -0.40 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[TTPAL]] | -0.39 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[NOP14]] | -0.39 | -0.40 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TJP3]] | B | TJP3 activity raises TMEM53's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.48× lower at baseline in the lines without TJP3 | 0.036 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[WFDC2]] | B | WFDC2 activity strengthens TMEM53's drug response | lines that do not express WFDC2 (36) vs lines expressing it (10) | the lines without WFDC2 respond 0.56× as strongly (z diff +1.81); strongest at Homoharringtonine 5 µM: 0.48x vs 0.18x (z diff +4.9) | 0.075 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.481). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.0, -49.0); signed map (-54.6, 32.9). **Vector** length 59.7, 9.02% of its response variance represented; |z| ≥ 3 in 896 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +4.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +2.3 | +3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | -1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.2 | +1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +3.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -13.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -8.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.7 | -11.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Artemether (drug)]] 0.05 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 53 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:44,635,238-44,674,481 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22353, NET4 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P2H8](https://www.uniprot.org/uniprotkb/Q6P2H8) (Transmembrane protein 53):

> Ensures normal bone formation, through the negative regulation of bone morphogenetic protein (BMP) signaling in osteoblast lineage cells by blocking cytoplasm-nucleus translocation of phosphorylated SMAD1/5/9 proteins.

**Summary**, from NCBI Gene [79639](https://www.ncbi.nlm.nih.gov/gene/79639):

> Involved in negative regulation of BMP signaling pathway; negative regulation of ossification; and regulation of nucleocytoplasmic transport. Located in nuclear membrane. Implicated in craniotubular dysplasia Ikegawa type. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26186](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26186) · Entrez [79639](https://www.ncbi.nlm.nih.gov/gene/79639) · UniProt [Q6P2H8](https://www.uniprot.org/uniprotkb/Q6P2H8) · Ensembl [ENSG00000126106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126106)

## Data

Gene col 4716: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4716); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4716, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4716]; `tensor/DDL_lfc|DDL_z.npy` [4716]; `embed/gene_vectors.npy` [4716]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4716 or target_col == 4716). Every well: [[TMEM53 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM53.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
