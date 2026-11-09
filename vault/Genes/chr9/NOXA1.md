---
symbol: "NOXA1"
type: "gene"
col: 12046
ensembl_id: "ENSG00000188747"
name: "NADPH oxidase activator 1"
location: "9q34.3"
module: 31
arm: "+"
pooled_cpm: 6.9
n_lines_expressing: 42
n_dd_up: 1
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 22
direction_downstream: 27
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# NOXA1

*NADPH oxidase activator 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.30× (z +4.4, q 0.006, up in 11 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.362× (z -12.2, q 2e-31, down in 30 of 40 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.536× (z -7.5, q 9e-12, down in 24 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACBD4]] (+0.59, fdr 1e-05), [[TMEM184A]] (+0.56, fdr 1e-05), [[NUDT14]] (+0.51, fdr 3e-05); moves opposite to [[WNT5A]] (-0.48, fdr 5e-05), [[ABL1]] (-0.48, fdr 1e-04), [[ZNF521]] (-0.47, fdr 4e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[EPS8L2]] → it (grade B ⚠); 27 go from it, the strongest it → [[WNT5A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12046.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.4 | 0.006 | 11/38 (HOP62, A498, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.37× | +3.5 | 0.13 | 10/35 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.72× | +3.4 | 0.13 | 3/19 (KATO III, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.33× | +3.2 | 0.21 | 5/17 (SW480, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.43× | +3.1 | 0.24 | 6/29 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12046.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.362×** | -12.2 | 2e-31 | 30/40 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.564×** | -9.7 | 9e-20 | 25/34 (LoVo, A549, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.487×** | -8.6 | 1e-15 | 27/36 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.525×** | -7.7 | 2e-12 | 23/36 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.536×** | -7.5 | 9e-12 | 24/37 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -7.4 | 1e-11 | 20/34 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.308×** | -7.4 | 1e-11 | 24/36 (PANC-1, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.555×** | -7.1 | 1e-10 | 23/37 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.559×** | -7.0 | 2e-10 | 21/34 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.567×** | -6.8 | 6e-10 | 22/35 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.361×** | -6.4 | 9e-09 | 24/35 (KATO III, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.597×** | -6.2 | 3e-08 | 16/38 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.630×** | -5.5 | 1e-06 | 19/40 (SK-MEL-2, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.650×** | -5.2 | 1e-05 | 15/36 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.627×** | -5.1 | 1e-05 | 19/29 (A549, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.660×** | -5.0 | 2e-05 | 18/34 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.647×** | -4.9 | 3e-05 | 15/35 (J82, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.487×** | -4.5 | 2e-04 | 13/32 (SNU-423, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.779×** | -4.2 | 7e-04 | 11/37 (NCI-H2347, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.561×** | -3.6 | 0.008 | 8/35 (NCI-H23, A498, …) | rises with dose | noisy plate (z scaled) |
| [[ML264 (drug)]] 0.05 µM |  | **0.738×** | -3.4 | 0.015 | 4/37 (BT-474, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12046. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.6 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0741× (z -21.9) |
| [[A549 (line)]] | wt | 9.33 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0716× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~41% of this change |
| [[LoVo (line)]] | wt | 16.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -18.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 24.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -10.2) |
| [[C-33 A (line)]] | alt | 6.62 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0681× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 4.66 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0675× (z -11.6) |
| [[Hs 766T (line)]] | wt | 4.12 | 0 | 1 | — | [[Sodium Salicylate (drug)]] 0.05 µM 0.0592× (z -8.5) |
| [[J82 (line)]] | alt | 3.66 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0298× (z -11.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 6.44 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.228× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 8.67 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.117× (z -8.9) |
| [[PANC-1 (line)]] | alt | 3.89 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0292× (z -8.7) |
| [[SW 900 (line)]] | alt | 5.39 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0743× (z -8.8) |
| [[SW1417 (line)]] | alt | 7.77 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.244× (z -9.0) |
| [[SW480 (line)]] | alt | 8.10 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.218× (z -8.9) |
| [[A-172 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.836 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12046), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACBD4]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[TMEM184A]] | +0.56 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[NUDT14]] | +0.51 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[METTL27]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[EPS8L2]] | +0.50 | +0.51 / +0.41 | both halves | 4e-05 | same gene group |
| [[LYRM9]] | +0.49 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[PRSS16]] | +0.49 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[MYO15B]] | +0.49 | +0.39 / +0.52 | both halves | 6e-05 | same gene group |
| [[EPHA10]] | +0.49 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[TESMIN]] | +0.48 | +0.53 / +0.34 | both halves | 1e-04 |  |
| [[ADAMTS13]] | +0.47 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[LENG9]] | +0.47 | +0.33 / +0.49 | both halves | 1e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WNT5A]] | -0.48 | -0.47 / -0.39 | both halves | 5e-05 | pathway: Killing mechanisms; STRING 509 |
| [[ABL1]] | -0.48 | -0.36 / -0.50 | both halves | 1e-04 | same gene group; pathway: Leishmania infection |
| [[ZNF521]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[GLIS3]] | -0.47 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[SETBP1]] | -0.46 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[POLE3]] | -0.44 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[ADAM12]] | -0.44 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[CNRIP1]] | -0.44 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[PRRX1]] | -0.43 | -0.47 / -0.29 | both halves | 3e-04 |  |
| [[HAS2]] | -0.42 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[NAV1]] | -0.41 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[FBN1]] | -0.41 | -0.44 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L2]] | B | EPS8L2 activity raises NOXA1's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 2.39× lower at baseline in the lines without EPS8L2 | 0.004 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[EPHA10]] | B | EPHA10 activity raises NOXA1's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 2.45× lower at baseline in the lines without EPHA10 | 0.005 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[MISP]] | B | MISP activity raises NOXA1's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.39× lower at baseline in the lines without MISP | 0.007 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[KIAA1522]] | B | KIAA1522 activity raises NOXA1's level | lines that do not express KIAA1522 (5) vs lines expressing it (45) | 2.89× lower at baseline in the lines without KIAA1522 | 0.022 | ⚠ across organs; also absent: ENSG00000257489, TRIB3, PBX4 |
| [[HAS2]] | B | HAS2 activity lowers NOXA1's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 1.81× higher at baseline in the lines without HAS2 | 0.024 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[ALS2CL]] | B | ALS2CL activity raises NOXA1's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.07× lower at baseline in the lines without ALS2CL | 0.025 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[MLXIPL]] | B | MLXIPL activity raises NOXA1's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 2.64× lower at baseline in the lines without MLXIPL | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |
| [[WNT5A]] | B | WNT5A activity lowers NOXA1's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 2.08× higher at baseline in the lines without WNT5A | 0.043 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[FBN1]] | B | FBN1 activity lowers NOXA1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 1.94× higher at baseline in the lines without FBN1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[LINC01748]] | B | LINC01748 activity raises NOXA1's level | lines that do not express LINC01748 (34) vs lines expressing it (16) | 2.04× lower at baseline in the lines without LINC01748 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CALB1, ATP10B, CLRN3 |
| [[PRSS16]] | B | PRSS16 activity raises NOXA1's level | lines that do not express PRSS16 (13) vs lines expressing it (37) | 2.13× lower at baseline in the lines without PRSS16 | 0.060 | ⚠ within organs, on part of the lines; also absent: STXBP2, MAP3K21, LINC00857 |
| [[ZNF521]] | B | ZNF521 activity lowers NOXA1's level | lines that do not express ZNF521 (27) vs lines expressing it (23) | 1.89× higher at baseline in the lines without ZNF521 | 0.061 | ⚠ within organs, on part of the lines; also absent: LEF1, SNAI2, ITGA4 |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 27, C 0. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT5A]] | B | NOXA1 activity lowers WNT5A's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 12.18× higher at baseline in the lines without NOXA1 | 0.013 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[PRRX1]] | B | NOXA1 activity lowers PRRX1's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 12.90× higher at baseline in the lines without NOXA1 | 0.021 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[CACFD1]] | B | NOXA1 activity raises CACFD1's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without NOXA1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[PAPPA]] | B | NOXA1 activity lowers PAPPA's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 5.53× higher at baseline in the lines without NOXA1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[HAS2]] | B | NOXA1 activity lowers HAS2's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 5.77× higher at baseline in the lines without NOXA1 | 0.024 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[CNRIP1]] | B | NOXA1 activity lowers CNRIP1's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 6.61× higher at baseline in the lines without NOXA1 | 0.024 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[MSC-AS1]] | B | NOXA1 activity lowers MSC-AS1's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 12.64× higher at baseline in the lines without NOXA1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[PRR36]] | B | NOXA1 activity raises PRR36's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 2.68× lower at baseline in the lines without NOXA1 | 0.038 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[ARHGEF16]] | B | NOXA1 activity raises ARHGEF16's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 3.19× lower at baseline in the lines without NOXA1 | 0.042 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[FBN1]] | B | NOXA1 activity lowers FBN1's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 9.25× higher at baseline in the lines without NOXA1 | 0.047 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[EPS8L2]] | B | NOXA1 activity raises EPS8L2's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 3.45× lower at baseline in the lines without NOXA1 | 0.055 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[NUDT14]] | B | NOXA1 activity raises NUDT14's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without NOXA1 | 0.057 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.441). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.4, 42.7); signed map (-6.0, 18.2). **Vector** length 58.7, 10.0% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.1 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +3.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.2 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.8 | -6.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -7.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.1 | -7.4 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | NADPH oxidase activator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,423,350-137,434,406 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NY-CO-31, FLJ25475; previously SDCCAG31 |
| Gene groups (HGNC) | SH3 domain containing |
| Reactome | 11 pathways, smallest: Killing mechanisms; WNT5:FZD7-mediated leishmania damping; RHO GTPases Activate NADPH Oxidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UR1](https://www.uniprot.org/uniprotkb/Q86UR1) (NADPH oxidase activator 1):

> Functions as an activator of NOX1, a superoxide-producing NADPH oxidase. Functions in the production of reactive oxygen species (ROS) which participate in a variety of biological processes including host defense, hormone biosynthesis, oxygen sensing and signal transduction. May also activate CYBB/gp91phox and NOX3.

**Summary**, from NCBI Gene [10811](https://www.ncbi.nlm.nih.gov/gene/10811):

> This gene encodes a protein which activates NADPH oxidases, enzymes which catalyze a reaction generating reactive oxygen species. The encoded protein contains four N-terminal tetratricopeptide domains and a C-terminal Src homology 3 domain. Interaction between the encoded protein and proteins in the oxidase regulatory complex occur via the tetratricopeptide domains. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:10668](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10668) · Entrez [10811](https://www.ncbi.nlm.nih.gov/gene/10811) · UniProt [Q86UR1](https://www.uniprot.org/uniprotkb/Q86UR1) · Ensembl [ENSG00000188747](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188747)

## Data

Gene col 12046: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12046); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12046, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12046]; `tensor/DDL_lfc|DDL_z.npy` [12046]; `embed/gene_vectors.npy` [12046]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12046 or target_col == 12046). Every well: [[NOXA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOXA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
