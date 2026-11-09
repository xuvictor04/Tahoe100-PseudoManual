---
symbol: "ATE1"
type: "gene"
col: 2867
ensembl_id: "ENSG00000107669"
name: "arginyltransferase 1"
location: "10q26.13"
module: 143
arm: "+"
pooled_cpm: 71.21
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# ATE1

*arginyltransferase 1* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.38× (z +5.8, q 3e-06, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.604× (z -9.0, q 1e-16, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASXL2]] (+0.69, fdr 7e-06), [[REEP3]] (+0.68, fdr 7e-06), [[TRAPPC8]] (+0.67, fdr 1e-05); moves opposite to [[RAB3A]] (-0.67, fdr 2e-05), [[SRP54]] (-0.64, fdr 1e-05), [[NPRL2]] (-0.63, fdr 1e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LOX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2867.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +5.8 | 3e-06 | 32/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +5.2 | 6e-05 | 25/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +5.1 | 8e-05 | 27/48 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +4.5 | 0.001 | 29/47 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +4.4 | 0.001 | 26/48 (NCI-H2030, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 0.001 | 24/47 (SW480, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.3 | 0.001 | 24/47 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.002 | 22/48 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.0 | 0.003 | 21/48 (NCI-H2347, RPMI-7951, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.21×** | +3.2 | 0.072 | 19/45 (RPMI-7951, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 5 µM |  | 1.38× | +3.0 | 0.12 | 12/49 (AsPC-1, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2867.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.604×** | -9.0 | 1e-16 | 38/48 (HepG2/C3A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.628×** | -8.3 | 3e-14 | 33/48 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.646×** | -7.8 | 1e-12 | 30/48 (HepG2/C3A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.603×** | -4.7 | 3e-04 | 29/47 (MIA PaCa-2, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.830×** | -4.7 | 3e-04 | 22/48 (NCI-H1573, LoVo, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.607×** | -4.7 | 3e-04 | 26/49 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.789×** | -4.2 | 0.002 | 26/48 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.792×** | -4.1 | 0.002 | 23/47 (AN3 CA, A-427, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.641×** | -4.1 | 0.002 | 24/48 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.666×** | -3.8 | 0.009 | 22/48 (PANC-1, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.765×** | -3.4 | 0.034 | 16/48 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.772×** | -3.3 | 0.048 | 13/49 (SW480, SHP-77, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.774×** | -3.3 | 0.050 | 21/48 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.717×** | -3.1 | 0.077 | 16/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2867. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 101 | 4 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.487× (z -10.3) |
| [[SNU-1 (line)]] | wt | 118 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.319× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 170 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.183× (z -18.0) ⚠ toxic; cell-cycle shift, explains ~10% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.313× (z -12.8) |
| [[HOP62 (line)]] | alt | 27.3 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.57× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.42× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -12.9) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.411× (z -10.4) |
| [[PANC-1 (line)]] | alt | 118 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.475× (z -10.7) |
| [[RKO (line)]] | wt | 92.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -13.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 76.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -18.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.388× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 97.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.206× (z -15.3) ⚠ toxic; cell-cycle shift, explains ~10% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.405× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 96.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.468× (z -9.1) |
| [[NCI-H596 (line)]] | alt | 74.1 | 2 | 0 | [[Methylthiouracil (drug)]] 0.05 µM 8.02× (z +16.6) | — |
| [[SW1417 (line)]] | alt | 67.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.443× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 68.4 | 0 | 1 | — | [[Budesonide (drug)]] 0.5 µM 0.415× (z -9.2) |
| [[HT-29 (line)]] | alt | 98.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.372× (z -11.1) |
| [[J82 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -8.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[LoVo (line)]] | wt | 78.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -9.9) ⚠ cell-cycle shift, explains ~67% of this change |
| [[LOX-IMVI (line)]] | wt | 61.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -9.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[LS 180 (line)]] | wt | 97.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.444× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 77.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.444× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 78.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.420× (z -9.0) |
| [[SW48 (line)]] | wt | 67.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -8.8) |
| [[A-172 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 84.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 130 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 70.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2867), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASXL2]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[REEP3]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TRAPPC8]] | +0.67 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[CPSF2]] | +0.67 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[TCF12]] | +0.66 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.66 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[TOR1A]] | +0.64 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[ENOX2]] | +0.64 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[TULP4]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[RCC2]] | +0.63 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[ATXN10]] | +0.62 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[ARSB]] | +0.62 | +0.58 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | -0.67 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[SRP54]] | -0.64 | -0.72 / -0.49 | both halves | 1e-05 |  |
| [[NPRL2]] | -0.63 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ACBD3]] | -0.63 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[ZNF526]] | -0.62 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[DPM1]] | -0.62 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[APAF1]] | -0.62 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[RAB1A]] | -0.62 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[AHDC1]] | -0.62 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[SEC22A]] | -0.62 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[EIF2AK3]] | -0.62 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[CDK7]] | -0.61 | -0.71 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOX]] | B | LOX activity lowers ATE1's level | lines that do not express LOX (31) vs lines expressing it (19) | 1.82× higher at baseline in the lines without LOX | 8e-04 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[LOX]] | B | LOX activity weakens ATE1's drug response | lines that do not express LOX (31) vs lines expressing it (18) | the lines without LOX respond 1.66× as strongly (z diff -1.19); strongest at Panobinostat 5 µM: 0.58x vs 0.94x (z diff -4.5) | 0.013 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; target measured in part of the lines; artifact flags |
| [[SNHG18]] | B | SNHG18 activity lowers ATE1's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.71× higher at baseline in the lines without SNHG18 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.775). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.8, 3.6); signed map (19.6, -29.2). **Vector** length 129, 37.0% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.7 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.4 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.4 | +2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.3 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.4 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +4.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.1 | -8.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | -9.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -7.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.7 | -3.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.4 | -3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.4 | -3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -4.7 |
|  | [[EX229 (drug)]] 0.5 µM |  | -3.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | arginyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:121,709,393-121,928,801 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Acyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [O95260](https://www.uniprot.org/uniprotkb/O95260) (Arginyl-tRNA--protein transferase 1):

> Involved in the post-translational conjugation of arginine to the N-terminal aspartate or glutamate of a protein. This arginylation is required for degradation of the protein via the ubiquitin pathway. Does not arginylate cysteine residues (By similarity).

**Summary**, from NCBI Gene [11101](https://www.ncbi.nlm.nih.gov/gene/11101):

> This gene encodes an arginyltransferase, an enzyme that is involved in posttranslational conjugation of arginine to N-terminal aspartate or glutamate residues. Conjugation of arginine to the N-terminal aspartate or glutamate targets proteins for ubiquitin-dependent degradation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:782) · Entrez [11101](https://www.ncbi.nlm.nih.gov/gene/11101) · UniProt [O95260](https://www.uniprot.org/uniprotkb/O95260) · Ensembl [ENSG00000107669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107669)

## Data

Gene col 2867: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2867); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2867, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2867]; `tensor/DDL_lfc|DDL_z.npy` [2867]; `embed/gene_vectors.npy` [2867]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2867 or target_col == 2867). Every well: [[ATE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
