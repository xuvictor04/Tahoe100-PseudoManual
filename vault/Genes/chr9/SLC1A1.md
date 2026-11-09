---
symbol: "SLC1A1"
type: "gene"
col: 2795
ensembl_id: "ENSG00000106688"
name: "solute carrier family 1 member 1"
location: "9p24.2"
module: 49
arm: "+"
pooled_cpm: 33.26
n_lines_expressing: 39
n_dd_up: 2
n_dd_down: 45
n_dd_up_clean: 2
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 6
direction_downstream: 21
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SLC1A1

*solute carrier family 1 member 1* — 9p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.43× (z +6.0, q 9e-07, up in 21 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.163× (z -42.9, q 0e+00, down in 37 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMCO4]] (+0.57, fdr 1e-05), [[SLC25A32]] (+0.56, fdr 3e-05), [[PDIA5]] (+0.56, fdr 2e-05); moves opposite to [[ZSCAN31]] (-0.50, fdr 4e-05), [[ABCC2]] (-0.50, fdr 4e-05), [[ATP6V1C1]] (-0.49, fdr 3e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SH3GL3]] → it (grade B ⚠); 21 go from it, the strongest it → [[TMED3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2795.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +6.0 | 9e-07 | 21/37 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +5.6 | 8e-06 | 19/37 (SW1417, HOP62, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.22× | +3.3 | 0.18 | 7/37 (RKO, A498, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.28 | 5/36 (COLO 205, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2795.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.163×** | -42.9 | 0e+00 | 37/37 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.139×** | -31.8 | 0e+00 | 37/37 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.210×** | -26.1 | 0e+00 | 37/37 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.232×** | -24.5 | 0e+00 | 34/36 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.330×** | -18.5 | 0e+00 | 34/35 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.378×** | -16.3 | 0e+00 | 31/37 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.370×** | -16.0 | 0e+00 | 33/36 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.409×** | -15.0 | 0e+00 | 33/37 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.423×** | -14.4 | 3e-45 | 35/37 (C32, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.429×** | -14.2 | 1e-43 | 36/37 (C32, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.455×** | -13.2 | 5e-38 | 27/37 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.464×** | -12.9 | 3e-36 | 28/37 (LS 180, HS-578T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.245×** | -12.3 | 4e-33 | 34/38 (SW 900, A498, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.482×** | -12.2 | 1e-32 | 29/37 (HT-29, SW48, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.493×** | -11.8 | 1e-30 | 30/37 (LS 180, HS-578T, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.497×** | -11.0 | 8e-27 | 31/37 (C32, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.355×** | -9.1 | 4e-18 | 25/36 (SW48, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.737×** | -7.2 | 2e-11 | 23/37 (C32, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2795. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 83.9 | 0 | 23 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0298× (z -45.1) |
| [[C32 (line)]] | wt | 81.1 | 0 | 21 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0362× (z -32.6) |
| [[A-172 (line)]] | wt | 49.1 | 0 | 19 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0472× (z -38.2) |
| [[HS-578T (line)]] | alt | 142 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0376× (z -44.6) |
| [[C-33 A (line)]] | alt | 48.3 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -21.3) |
| [[A549 (line)]] | wt | 26.0 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0626× (z -25.1) |
| [[HOP62 (line)]] | alt | 26.1 | 0 | 10 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0415× (z -22.3) |
| [[hTERT-HPNE (line)]] | wt | 86.8 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0754× (z -26.9) |
| [[SW 900 (line)]] | alt | 43.0 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0667× (z -29.0) |
| [[HEC-1-A (line)]] | alt | 24.5 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -21.7) |
| [[HT-29 (line)]] | alt | 69.0 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -18.9) |
| [[J82 (line)]] | alt | 42.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0867× (z -30.3) |
| [[LoVo (line)]] | wt | 73.7 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -19.8) |
| [[NCI-H1573 (line)]] | alt | 28.8 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -20.8) |
| [[SNU-1 (line)]] | wt | 44.8 | 0 | 8 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0312× (z -18.7) |
| [[HCT15 (line)]] | alt | 66.2 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -19.2) |
| [[KATO III (line)]] | alt | 33.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -16.1) |
| [[LS 180 (line)]] | wt | 126 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.332× (z -15.4) |
| [[NCI-H1792 (line)]] | alt | 21.8 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -20.2) |
| [[NCI-H2030 (line)]] | alt | 34.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0505× (z -28.0) |
| [[SW48 (line)]] | wt | 45.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -17.9) |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -16.7) |
| [[AsPC-1 (line)]] | alt | 30.0 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.0590× (z -18.6) |
| [[H4 (line)]] | wt | 31.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -15.9) |
| [[RKO (line)]] | wt | 31.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -21.3) |
| [[SK-MEL-2 (line)]] | alt | 28.1 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0463× (z -19.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.0625× (z -17.1) |
| [[A-427 (line)]] | wt | 15.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -13.4) |
| [[AN3 CA (line)]] | alt | 57.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0909× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.194× (z -10.4) |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 44.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -21.6) |
| [[RPMI-7951 (line)]] | alt | 20.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -14.9) |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.132× (z -10.8) |
| [[SW1417 (line)]] | alt | 9.15 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.0) |
| [[CHP-212 (line)]] | wt | 6.12 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.81 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.33 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.89 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2795), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMCO4]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[SLC25A32]] | +0.56 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[PDIA5]] | +0.56 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[KDELR3]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[TMEM243]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[COL13A1]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[C1orf21]] | +0.52 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[HM13]] | +0.52 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[ZCCHC24]] | +0.51 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[MAP3K21]] | +0.51 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[MFSD2A]] | +0.51 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[NAA35]] | +0.50 | +0.57 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN31]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ABCC2]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 | pathway: Disorders of transmembrane transporters |
| [[ATP6V1C1]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PLXNB3-AS1]] | -0.48 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[MR1]] | -0.48 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[GUCY1B2]] | -0.47 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[TCTN1]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[IDNK]] | -0.46 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[LINC00649]] | -0.46 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[TIGD6]] | -0.45 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[DNAJC8]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[GLDN]] | -0.44 | -0.36 / -0.39 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3GL3]] | B | SH3GL3 activity raises SLC1A1's level | lines that do not express SH3GL3 (21) vs lines expressing it (29) | 1.79× lower at baseline in the lines without SH3GL3 | 0.033 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |
| [[TNIK]] | B | TNIK activity raises SLC1A1's level | lines that do not express TNIK (11) vs lines expressing it (39) | 2.72× lower at baseline in the lines without TNIK | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |
| [[TOP2A]] | B | TOP2A activity raises SLC1A1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TMEM158]] | B | TMEM158 activity raises SLC1A1's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 1.32× lower at baseline in the lines without TMEM158 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[C1orf21]] | B | C1orf21 activity raises SLC1A1's level | lines that do not express C1orf21 (9) vs lines expressing it (41) | 2.90× lower at baseline in the lines without C1orf21 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, GALNT8 |
| [[LRRC8C]] | B | LRRC8C activity raises SLC1A1's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 2.33× lower at baseline in the lines without LRRC8C | 0.095 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMED3]] | B | SLC1A1 activity raises TMED3's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.95× lower at baseline in the lines without SLC1A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[TMEM184B]] | B | SLC1A1 activity raises TMEM184B's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without SLC1A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[ALDH18A1]] | B | SLC1A1 activity raises ALDH18A1's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without SLC1A1 | 0.009 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[SH3GL3]] | B | SLC1A1 activity raises SH3GL3's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 3.06× lower at baseline in the lines without SLC1A1 | 0.014 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[KDELR3]] | B | SLC1A1 activity raises KDELR3's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without SLC1A1 | 0.022 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[PDXDC1]] | B | SLC1A1 activity raises PDXDC1's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.69× lower at baseline in the lines without SLC1A1 | 0.025 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[CSNK1E]] | B | SLC1A1 activity raises CSNK1E's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.35× lower at baseline in the lines without SLC1A1 | 0.031 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[SMCO4]] | B | SLC1A1 activity strengthens SMCO4's drug response | lines that do not express SLC1A1 (10) vs lines expressing it (36) | the lines without SLC1A1 respond 0.55× as strongly (z diff +1.22); strongest at Homoharringtonine 5 µM: 1.15x vs 0.62x (z diff +4.8) | 0.041 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[POLG]] | B | SLC1A1 activity raises POLG's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.30× lower at baseline in the lines without SLC1A1 | 0.058 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[TMEM158]] | B | SLC1A1 activity raises TMEM158's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 2.13× lower at baseline in the lines without SLC1A1 | 0.058 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[KDELR2]] | B | SLC1A1 activity strengthens KDELR2's drug response | lines that do not express SLC1A1 (11) vs lines expressing it (38) | the lines without SLC1A1 respond 0.66× as strongly (z diff +2.11); strongest at Panobinostat 5 µM: 0.84x vs 0.58x (z diff +3.9) | 0.058 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[HM13]] | B | SLC1A1 activity raises HM13's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.39× lower at baseline in the lines without SLC1A1 | 0.059 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.430). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.4, -34.0); signed map (-50.7, 8.1). **Vector** length 94.5, 25.7% of its response variance represented; |z| ≥ 3 in 1,291 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +6.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.1 | +1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.5 | -8.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +1.5 | +0.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.1 | -7.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | +0.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -3.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.1 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 1 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.2 — chr9:4,490,468-4,587,469 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EAAC1, EAAT3, hEAAC1 |
| Gene groups (HGNC) | Solute carrier family 1 |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 9 pathways, smallest: Glutamate Neurotransmitter Release Cycle; SLC-mediated transport of amino acids; Neurotransmitter release cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P43005](https://www.uniprot.org/uniprotkb/P43005) (Excitatory amino acid transporter 3):

> Sodium-dependent, high-affinity amino acid transporter that mediates the uptake of L-glutamate and also L-aspartate and D-aspartate. Can also transport L-cysteine. Functions as a symporter that transports one amino acid molecule together with two or three Na(+) ions and one proton, in parallel with the counter-transport of one K(+) ion. Mediates Cl(-) flux that is not coupled to amino acid transport; this avoids the accumulation of negative charges due to aspartate and Na(+) symport. Plays an …

**Summary**, from NCBI Gene [6505](https://www.ncbi.nlm.nih.gov/gene/6505):

> This gene encodes a member of the high-affinity glutamate transporters that play an essential role in transporting glutamate across plasma membranes. In brain, these transporters are crucial in terminating the postsynaptic action of the neurotransmitter glutamate, and in maintaining extracellular glutamate concentrations below neurotoxic levels. This transporter also transports aspartate, and mutations in this gene are thought to cause dicarboxylicamino aciduria, also known as …

**Accessions** — [HGNC:10939](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10939) · Entrez [6505](https://www.ncbi.nlm.nih.gov/gene/6505) · UniProt [P43005](https://www.uniprot.org/uniprotkb/P43005) · Ensembl [ENSG00000106688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106688)

## Data

Gene col 2795: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2795); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2795, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2795]; `tensor/DDL_lfc|DDL_z.npy` [2795]; `embed/gene_vectors.npy` [2795]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2795 or target_col == 2795). Every well: [[SLC1A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC1A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
