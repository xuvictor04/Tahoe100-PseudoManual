---
symbol: "PCED1B"
type: "gene"
col: 11052
ensembl_id: "ENSG00000179715"
name: "PC-esterase domain containing 1B"
location: "12q13.11"
module: 120
arm: "+"
pooled_cpm: 85.52
n_lines_expressing: 39
n_dd_up: 0
n_dd_down: 56
n_dd_up_clean: 0
n_dd_down_clean: 39
in_vector_space: true
direction_upstream: 15
direction_downstream: 30
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# PCED1B

*PC-esterase domain containing 1B* — 12q13.11

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 56 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.320× (z -19.1, q 0e+00, down in 35 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AMIGO2]] (+0.79, fdr 7e-06, ⚠ same locus), [[ABCC3]] (+0.60, fdr 1e-05), [[MBP]] (+0.58, fdr 2e-05), [[GPR39]] (+0.54, fdr 1e-05); moves opposite to [[SRPX]] (-0.50, fdr 3e-05), [[ZDHHC9]] (-0.50, fdr 4e-05), [[GYS1]] (-0.49, fdr 1e-04).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[GPR39]] → it (grade B ⚠); 30 go from it, the strongest it → [[SMARCD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11052.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | 1.34× | +3.5 | 0.15 | 18/37 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.33× | +3.5 | 0.15 | 16/37 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.20× | +3.1 | 0.29 | 15/37 (PANC-1, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 56 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11052.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.320×** | -19.1 | 0e+00 | 35/37 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.250×** | -16.4 | 0e+00 | 36/37 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.271×** | -15.5 | 0e+00 | 36/37 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.272×** | -15.4 | 0e+00 | 35/37 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.185×** | -10.5 | 1e-23 | 36/38 (HT-29, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.430×** | -10.0 | 2e-21 | 34/37 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.456×** | -9.3 | 1e-18 | 35/37 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.491×** | -8.4 | 3e-15 | 28/37 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.270×** | -8.1 | 3e-14 | 31/37 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.503×** | -7.8 | 3e-13 | 27/36 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.522×** | -7.7 | 8e-13 | 28/37 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.512×** | -7.5 | 4e-12 | 29/37 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.563×** | -6.8 | 5e-10 | 22/37 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.562×** | -6.3 | 1e-08 | 23/34 (HT-29, NCI-H460, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.600×** | -5.8 | 2e-07 | 25/36 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.620×** | -5.6 | 5e-07 | 25/37 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.419×** | -5.4 | 2e-06 | 28/37 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.428×** | -5.3 | 4e-06 | 32/37 (LoVo, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.644×** | -5.2 | 5e-06 | 19/37 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.663×** | -4.8 | 3e-05 | 21/37 (BT-474, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11052. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 163 | 0 | 28 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -21.5) |
| [[LoVo (line)]] | wt | 116 | 0 | 23 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -27.7) |
| [[NCI-H1573 (line)]] | alt | 144 | 0 | 22 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0530× (z -35.0) |
| [[LS 180 (line)]] | wt | 123 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -25.9) |
| [[HT-29 (line)]] | alt | 302 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -23.8) |
| [[BT-474 (line)]] | alt | 137 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -16.7) |
| [[COLO 205 (line)]] | alt | 370 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0931× (z -32.3) |
| [[SW480 (line)]] | alt | 61.9 | 0 | 14 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.218× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 228 | 0 | 13 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.102× (z -23.1) |
| [[PANC-1 (line)]] | alt | 85.3 | 0 | 11 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -12.7) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.278× (z -11.5) |
| [[J82 (line)]] | alt | 86.2 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.253× (z -9.7) |
| [[SW1417 (line)]] | alt | 62.6 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -21.4) |
| [[SW48 (line)]] | wt | 50.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.0) |
| [[A549 (line)]] | wt | 162 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 97.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -17.1) |
| [[SHP-77 (line)]] | alt | 95.9 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.257× (z -11.3) |
| [[A-172 (line)]] | wt | 53.5 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.291× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 141 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 53.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -11.4) |
| [[Hs 766T (line)]] | wt | 110 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.5) |
| [[SW 900 (line)]] | alt | 102 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 49.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.4) |
| [[H4 (line)]] | wt | 59.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -9.0) |
| [[HS-578T (line)]] | alt | 60.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.261× (z -8.8) |
| [[KATO III (line)]] | alt | 27.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 56.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -18.5) |
| [[SNU-423 (line)]] | alt | 61.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -9.7) |
| [[SW 1271 (line)]] | alt | 165 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -10.8) |
| [[A498 (line)]] | wt | 62.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -14.5) |
| [[CHP-212 (line)]] | wt | 73.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0796× (z -11.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 44.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 57.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.2) |
| [[A-427 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.35 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.89 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.74 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.54 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.45 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 71.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11052), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMIGO2]] | +0.79 | +0.79 / +0.75 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ABCC3]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[MBP]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[GPR39]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LINC00472]] | +0.54 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[TNFSF15]] | +0.54 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[ADGRL4]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SERTAD4]] | +0.51 | +0.36 / +0.47 | both halves | 1e-04 |  |
| [[RFX3]] | +0.51 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[SRGAP1]] | +0.50 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[HIVEP1]] | +0.50 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[SLC35F3]] | +0.49 | +0.47 / +0.49 | both halves | 2e-05 | same gene group |
| [[DUSP4]] | +0.49 | +0.41 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPX]] | -0.50 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ZDHHC9]] | -0.50 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[GYS1]] | -0.49 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[HACE1]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[IL17RC]] | -0.48 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[CD109]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[TRAM2]] | -0.47 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[STRA6LP]] | -0.47 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[SEPTIN5]] | -0.47 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[TBCE]] | -0.47 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[DIXDC1]] | -0.47 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[COPS8]] | -0.46 | -0.38 / -0.47 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR39]] | B | GPR39 activity raises PCED1B's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 3.88× lower at baseline in the lines without GPR39 | 0.011 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[RIN2]] | B | RIN2 activity raises PCED1B's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 3.10× lower at baseline in the lines without RIN2 | 0.012 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[LYPD1]] | B | LYPD1 activity raises PCED1B's level | lines that do not express LYPD1 (21) vs lines expressing it (29) | 2.35× lower at baseline in the lines without LYPD1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SETBP1, FRMPD4, NCKAP5 |
| [[DUSP4]] | B | DUSP4 activity raises PCED1B's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.14× lower at baseline in the lines without DUSP4 | 0.033 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[ABCC3]] | B | ABCC3 activity raises PCED1B's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 3.00× lower at baseline in the lines without ABCC3 | 0.041 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[ARHGAP26]] | B | ARHGAP26 activity raises PCED1B's level | lines that do not express ARHGAP26 (6) vs lines expressing it (44) | 3.86× lower at baseline in the lines without ARHGAP26 | 0.049 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[LINP1]] | B | LINP1 activity raises PCED1B's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 2.00× lower at baseline in the lines without LINP1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1 |
| [[SEPTIN5]] | B | SEPTIN5 activity lowers PCED1B's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.92× higher at baseline in the lines without SEPTIN5 | 0.057 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[LINC00589]] | B | LINC00589 activity raises PCED1B's level | lines that do not express LINC00589 (28) vs lines expressing it (22) | 1.68× lower at baseline in the lines without LINC00589 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8 |
| [[DOCK10]] | B | DOCK10 activity raises PCED1B's level | lines that do not express DOCK10 (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without DOCK10 | 0.067 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1 |
| [[STARD9]] | B | STARD9 activity lowers PCED1B's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 2.72× higher at baseline in the lines without STARD9 | 0.078 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[SLC35F3]] | B | SLC35F3 activity raises PCED1B's level | lines that do not express SLC35F3 (27) vs lines expressing it (23) | 2.19× lower at baseline in the lines without SLC35F3 | 0.080 | ⚠ within organs, on part of the lines; also absent: RHCG, THBD, NR2E3 |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 29, C 1. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMARCD3]] | B | PCED1B activity lowers SMARCD3's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 2.74× higher at baseline in the lines without PCED1B | 0.009 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[RIN2]] | B | PCED1B activity raises RIN2's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 3.20× lower at baseline in the lines without PCED1B | 0.011 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[SHANK3]] | B | PCED1B activity lowers SHANK3's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 2.31× higher at baseline in the lines without PCED1B | 0.014 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[PTPRK]] | B | PCED1B activity raises PTPRK's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without PCED1B | 0.018 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[GPR39]] | B | PCED1B activity raises GPR39's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 3.09× lower at baseline in the lines without PCED1B | 0.020 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[ABCC3]] | B | PCED1B activity raises ABCC3's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 4.04× lower at baseline in the lines without PCED1B | 0.026 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| cells under [[Riluzole hydrochloride (drug)]] 5 µM | B | PCED1B activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express PCED1B (11) vs lines expressing it (37) | the lines without PCED1B: 0.87× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| cells under [[Dinaciclib (drug)]] 0.5 µM | B | PCED1B activity raises the cells' numbers under Dinaciclib 0.5 µM (protects the cells) | lines that do not express PCED1B (11) vs lines expressing it (37) | the lines without PCED1B: 0.33× the cells of the other lines | 0.048 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| cells under [[Topotecan (hydrochloride) (drug)]] 5 µM | B | PCED1B activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express PCED1B (11) vs lines expressing it (37) | the lines without PCED1B: 0.51× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[ARHGAP26]] | B | PCED1B activity raises ARHGAP26's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without PCED1B | 0.055 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[EIF4G3]] | B | PCED1B activity lowers EIF4G3's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 1.59× higher at baseline in the lines without PCED1B | 0.057 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[DDX41]] | B | PCED1B activity lowers DDX41's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 1.65× higher at baseline in the lines without PCED1B | 0.057 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.477). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.9, 11.1); signed map (12.1, 43.2). **Vector** length 111, 37.0% of its response variance represented; |z| ≥ 3 in 1,453 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +7.3 | -3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | +0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | -0.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +3.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -9.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.0 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.9 | -3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -10.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.6 | -10.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -3.4 | -4.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.3 | -3.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.3 | -3.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | PC-esterase domain containing 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:47,079,603-47,236,662 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC16044; previously FAM113B |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q96HM7](https://www.uniprot.org/uniprotkb/Q96HM7) carries no function annotation.

**Summary**, from NCBI Gene [91523](https://www.ncbi.nlm.nih.gov/gene/91523):

> This gene encodes a protein that belongs to the GDSL/SGNH-like acyl-esterase family. Members of this family are hydrolases thought to function in modification of biopolymers on the cell surface. Alternate splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:28255](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28255) · Entrez [91523](https://www.ncbi.nlm.nih.gov/gene/91523) · UniProt [Q96HM7](https://www.uniprot.org/uniprotkb/Q96HM7) · Ensembl [ENSG00000179715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179715)

## Data

Gene col 11052: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11052); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11052, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11052]; `tensor/DDL_lfc|DDL_z.npy` [11052]; `embed/gene_vectors.npy` [11052]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11052 or target_col == 11052). Every well: [[PCED1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCED1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
