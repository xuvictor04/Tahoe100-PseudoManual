---
symbol: "TXNDC5"
type: "gene"
col: 14184
ensembl_id: "ENSG00000239264"
name: "thioredoxin domain containing 5"
location: "6p24.3"
module: 20
arm: "+"
pooled_cpm: 49.36
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# TXNDC5

*thioredoxin domain containing 5* — 6p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.63× (z +10.9, q 4e-25, up in 37 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.59× (z +5.5, q 7e-06, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.434× (z -13.5, q 1e-38, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPN1]] (+0.89, fdr 7e-06), [[BPNT2]] (+0.79, fdr 7e-06), [[UGGT1]] (+0.76, fdr 7e-06); moves opposite to [[MRPS18C]] (-0.76, fdr 7e-06), [[CROCCP2-1]] (-0.73, fdr 7e-06), [[SMIM26]] (-0.72, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[FDX2]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14184.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +10.9 | 4e-25 | 37/38 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +9.0 | 6e-17 | 45/48 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +7.4 | 2e-11 | 37/45 (SNU-423, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +5.5 | 7e-06 | 37/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +5.4 | 7e-06 | 35/48 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +4.2 | 0.002 | 32/48 (HS-578T, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.022 | 24/48 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.6 | 0.022 | 18/34 (HS-578T, HOP62, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.4 | 0.049 | 22/47 (SNU-423, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14184.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.434×** | -13.5 | 1e-38 | 46/48 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.513×** | -7.6 | 9e-12 | 42/48 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.584×** | -6.4 | 4e-08 | 39/48 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.594×** | -6.2 | 1e-07 | 38/48 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.649×** | -5.1 | 4e-05 | 34/48 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.662×** | -4.9 | 1e-04 | 30/48 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.680×** | -4.6 | 4e-04 | 31/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.770×** | -4.2 | 0.002 | 30/48 (LS 180, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.723×** | -3.9 | 0.007 | 27/48 (SNU-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.586×** | -3.8 | 0.008 | 26/48 (HOP62, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.728×** | -3.8 | 0.009 | 24/48 (A-172, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -3.7 | 0.012 | 33/48 (SW 1088, HOP62, …) | all doses, flat | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | **0.757×** | -3.3 | 0.042 | 24/48 (NCI-H2347, HOP62, …) | all doses, flat | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.772×** | -3.1 | 0.086 | 23/48 (NCI-H1573, AsPC-1, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.775×** | -3.0 | 0.096 | 22/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 37.9 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -16.5) |
| [[HOP62 (line)]] | alt | 83.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 40.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -9.1) |
| [[SNU-423 (line)]] | alt | 38.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.73× (z +12.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 33.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 35.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.3) |
| [[CHP-212 (line)]] | wt | 46.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 49.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -9.1) |
| [[J82 (line)]] | alt | 50.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.4) |
| [[LOX-IMVI (line)]] | wt | 32.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 49.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.42× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 69.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -17.1) |
| [[NCI-H23 (line)]] | alt | 36.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -19.2) |
| [[Panc 03.27 (line)]] | alt | 26.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.73× (z +12.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 76.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 24.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -13.2) |
| [[SNU-1 (line)]] | wt | 63.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -16.8) |
| [[SW480 (line)]] | alt | 42.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -10.6) |
| [[BT-474 (line)]] | alt | 37.0 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.244× (z -8.8) |
| [[C32 (line)]] | wt | 31.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.05× (z +9.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 30.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +8.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 82.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -13.5) |
| [[HS-578T (line)]] | alt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.341× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 76.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.8) |
| [[LoVo (line)]] | wt | 65.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 50.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -16.5) |
| [[NCI-H2347 (line)]] | alt | 44.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -8.8) |
| [[PANC-1 (line)]] | alt | 51.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 59.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -12.2) |
| [[SW 900 (line)]] | alt | 41.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -8.9) |
| [[A498 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 83.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPN1]] | +0.89 | +0.87 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[BPNT2]] | +0.79 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[UGGT1]] | +0.76 | +0.65 / +0.82 | both halves | 7e-06 | STRING 598 |
| [[STT3A]] | +0.76 | +0.70 / +0.81 | both halves | 7e-06 | STRING 405 |
| [[DPAGT1]] | +0.75 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[TMED7]] | +0.75 | +0.75 / +0.81 | both halves | 7e-06 |  |
| [[IPO5]] | +0.74 | +0.59 / +0.80 | both halves | 7e-06 |  |
| [[RPSA]] | +0.73 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[CRTAP]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.71 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[TM9SF3]] | +0.71 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[CMPK1]] | +0.71 | +0.62 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS18C]] | -0.76 | -0.72 / -0.76 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | -0.73 | -0.68 / -0.77 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.72 | -0.54 / -0.79 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FDX2]] | -0.70 | -0.62 / -0.76 | both halves | 7e-06 |  |
| [[TOPORS]] | -0.70 | -0.69 / -0.73 | both halves | 7e-06 |  |
| [[PIGBOS1]] | -0.69 | -0.53 / -0.74 | both halves | 1e-05 |  |
| [[MRPL46]] | -0.68 | -0.51 / -0.75 | both halves | 1e-05 |  |
| [[SCAND1]] | -0.68 | -0.49 / -0.77 | both halves | 1e-05 |  |
| [[COIL]] | -0.67 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[ANKRD49]] | -0.66 | -0.70 / -0.68 | both halves | 7e-06 |  |
| [[EID2]] | -0.65 | -0.62 / -0.74 | both halves | 7e-06 |  |
| [[PPIG]] | -0.65 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.65 | -0.63 / -0.72 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TXNDC5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.839). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-24.5, -22.9); signed map (-24.0, -40.1). **Vector** length 133, 42.4% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cap-dependent Translation Initiation* (reactome, mean cos +0.51 to 12); *Eukaryotic Translation Initiation* (reactome, mean cos +0.51 to 12); *L13a-mediated translational silencing of Ceruloplasmin expression* (reactome, mean cos +0.53 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.0 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.8 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.2 | +9.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.4 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -13.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.9 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.6 | -1.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.1 | -2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.3 — chr6:7,881,517-7,910,788 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3178, FLJ21353, FLJ90810, EndoPDI, Hcc-2, ERp46, PDIA15 |
| Gene groups (HGNC) | Protein disulfide isomerases; Thioredoxin domain containing |
| Reactome | 7 pathways, smallest: Lysosome Vesicle Biogenesis; Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBS9](https://www.uniprot.org/uniprotkb/Q8NBS9) (Thioredoxin domain-containing protein 5):

> Protein disulfide isomerase of the endoplasmic reticulum lumen involved in the formation of disulfide bonds in proteins. Can reduce insulin disulfide bonds.

**Summary**, from NCBI Gene [81567](https://www.ncbi.nlm.nih.gov/gene/81567):

> This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal endoplasmic reticulum (ER)-signal sequence, three catalytically active thioredoxin domains and a C-terminal ER-retention sequence. Its expression is induced by hypoxia and its role may be to protect hypoxic cells from apoptosis. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:21073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21073) · Entrez [81567](https://www.ncbi.nlm.nih.gov/gene/81567) · UniProt [Q8NBS9](https://www.uniprot.org/uniprotkb/Q8NBS9) · Ensembl [ENSG00000239264](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239264)

## Data

Gene col 14184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14184); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14184]; `tensor/DDL_lfc|DDL_z.npy` [14184]; `embed/gene_vectors.npy` [14184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14184 or target_col == 14184). Every well: [[TXNDC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXNDC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
