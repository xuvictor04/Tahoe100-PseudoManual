---
symbol: "SC5D"
type: "gene"
col: 3095
ensembl_id: "ENSG00000109929"
name: "sterol-C5-desaturase"
location: "11q23.3-q24.1"
module: 86
arm: "+"
pooled_cpm: 22.31
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 6
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# SC5D

*sterol-C5-desaturase* — 11q23.3-q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 1.98× (z +16.1, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.704× (z -5.8, q 3e-06, down in 22 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.677× (z -4.6, q 0.001, down in 20 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP51A1]] (+0.85, fdr 7e-06), [[DHCR7]] (+0.77, fdr 7e-06), [[IDI1]] (+0.73, fdr 7e-06); moves opposite to [[SMPD4BP]] (-0.43, fdr 4e-05), [[DHRS7B]] (-0.43, fdr 2e-04), [[TAF3]] (-0.42, fdr 2e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ENPP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3095.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **1.98×** | +16.1 | 0e+00 | 42/48 (NCI-H2030, LS 180, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **1.81×** | +13.9 | 1e-41 | 42/48 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +11.9 | 2e-30 | 27/31 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +10.1 | 1e-21 | 31/41 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +8.9 | 7e-17 | 29/48 (SW1417, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +8.9 | 7e-17 | 27/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +8.3 | 8e-15 | 28/48 (CFPAC-1, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +8.1 | 5e-14 | 33/48 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +7.0 | 1e-10 | 28/47 (LOX-IMVI, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.6 | 1e-06 | 25/47 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +5.5 | 2e-06 | 22/44 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.38×** | +5.3 | 4e-06 | 22/47 (NCI-H2030, A498, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.37×** | +5.2 | 7e-06 | 22/47 (A498, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +4.9 | 4e-05 | 15/34 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.35×** | +4.8 | 6e-05 | 21/48 (HS-578T, C-33 A, …) | top dose only | plate-row cell shift |
| [[Adagrasib (drug)]] 5 µM |  | **1.34×** | +4.6 | 1e-04 | 18/48 (HOP62, NCI-H2030, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.33×** | +4.6 | 1e-04 | 19/47 (HEC-1-A, hTERT-HPNE, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.20× | +4.3 | 6e-04 | 11/48 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +4.1 | 1e-03 | 16/47 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3095.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.704×** | -5.8 | 3e-06 | 22/46 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.677×** | -4.6 | 0.001 | 20/45 (COLO 205, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.809×** | -3.5 | 0.066 | 17/48 (NCI-H1792, SW480, …) | rises with dose | composition shift |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.747×** | -3.5 | 0.066 | 14/48 (AsPC-1, SW 1271, …) | two highest doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.749×** | -3.4 | 0.066 | 9/46 (PANC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.756×** | -3.3 | 0.085 | 14/46 (CHP-212, KATO III, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.825× | -3.2 | 0.11 | 14/47 (KATO III, CHP-212, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.828× | -3.1 | 0.11 | 11/48 (MIA PaCa-2, BT-474, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.829× | -3.1 | 0.11 | 15/47 (SW480, NCI-H1573, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.703× | -3.1 | 0.11 | 11/46 (C-33 A, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bergenin (drug)]] 5 µM |  | 0.878× | -3.1 | 0.11 | 7/48 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Bergenin (drug)]] 0.5 µM |  | 0.816× | -3.0 | 0.12 | 9/47 (Panc 03.27, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3095. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 21.6 | 3 | 0 | [[Berbamine (drug)]] 5 µM 2.86× (z +11.3) | — |
| [[C-33 A (line)]] | alt | 22.7 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.52× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 11.2 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.18× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 17.4 | 2 | 0 | [[Berbamine (drug)]] 5 µM 3.67× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 49.5 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.59× (z +10.6) | — |
| [[KATO III (line)]] | alt | 80.8 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.24× (z +9.7) | — |
| [[LoVo (line)]] | wt | 28.5 | 2 | 0 | [[Berbamine (drug)]] 5 µM 2.82× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 35.7 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.79× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 19.8 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.28× (z +11.8) | — |
| [[SW480 (line)]] | alt | 23.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.215× (z -14.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 32.5 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0816× (z -9.8) |
| [[Hs 766T (line)]] | wt | 17.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.56× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 55.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.94× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 3.09× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 34.6 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 1.96× (z +8.7) | — |
| [[A-172 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3095), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP51A1]] | +0.85 | +0.79 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 987 |
| [[DHCR7]] | +0.77 | +0.75 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 998 |
| [[IDI1]] | +0.73 | +0.78 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 835 |
| [[HMGCS1]] | +0.72 | +0.74 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 903 |
| [[HMGCR]] | +0.68 | +0.76 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 818 |
| [[ACSS2]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 429 |
| [[ACAT2]] | +0.68 | +0.78 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 606 |
| [[SCD]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 555 |
| [[FASN]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 517 |
| [[MSMO1]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 | same gene group; pathway: Cholesterol biosynthesis; STRING 991 |
| [[STARD4]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 535 |
| [[MMAB]] | +0.64 | +0.71 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMPD4BP]] | -0.43 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[DHRS7B]] | -0.43 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[TAF3]] | -0.42 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[MECR]] | -0.39 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[ELL]] | -0.38 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[ZC3H18]] | -0.38 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[QRICH1]] | -0.36 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[HDAC7]] | -0.36 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[SELENOH]] | -0.36 | -0.19 / -0.46 | ⚠ not reproduced | 9e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPP4]] | B | ENPP4 activity raises SC5D's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.80× lower at baseline in the lines without ENPP4 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.759). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.1, -49.4); signed map (-52.5, 32.3). **Vector** length 107, 25.6% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Lanosterol biosynthesis* (reactome, mean cos +0.61 to 10); *Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway)* (reactome, mean cos +0.58 to 7); *SREBP1 lipogenesis* (control, mean cos +0.55 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +7.3 | +16.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +11.9 |
|  | [[Berbamine (drug)]] 5 µM |  | +6.7 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +4.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +4.0 | +5.3 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +3.7 | +4.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +2.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.6 | -3.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.4 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | sterol-C5-desaturase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3-q24.1 — chr11:121,292,681-121,313,410 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SC5DL |
| Gene groups (HGNC) | Fatty acid hydroxylase domain containing |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, APOPTOSIS, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: Cholesterol biosynthesis from zymosterol (modified Kandutsch-Russell pathway); Cholesterol biosynthesis via desmosterol (Bloch pathway); Cholesterol biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O75845](https://www.uniprot.org/uniprotkb/O75845) (Lathosterol oxidase):

> Catalyzes the penultimate step of the biosynthesis of cholesterol, the dehydrogenation of lathosterol into 7-dehydrocholesterol (7-DHC). Cholesterol is the major sterol component in mammalian membranes and a precursor for bile acid and steroid hormone synthesis. In addition to its essential role in cholesterol biosynthesis, it also indirectly regulates ferroptosis through the production of 7-DHC. By diverting the spread of damage caused by peroxyl radicals from the phospholipid components to …

**Summary**, from NCBI Gene [6309](https://www.ncbi.nlm.nih.gov/gene/6309):

> This gene encodes an enzyme of cholesterol biosynthesis. The encoded protein catalyzes the conversion of lathosterol into 7-dehydrocholesterol. Mutations in this gene have been associated with lathosterolosis. Alternatively spliced transcript variants encoding the same protein have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10547](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10547) · Entrez [6309](https://www.ncbi.nlm.nih.gov/gene/6309) · UniProt [O75845](https://www.uniprot.org/uniprotkb/O75845) · Ensembl [ENSG00000109929](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109929)

## Data

Gene col 3095: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3095); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3095, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3095]; `tensor/DDL_lfc|DDL_z.npy` [3095]; `embed/gene_vectors.npy` [3095]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3095 or target_col == 3095). Every well: [[SC5D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SC5D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
