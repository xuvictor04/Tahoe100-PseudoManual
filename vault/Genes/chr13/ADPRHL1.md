---
symbol: "ADPRHL1"
type: "gene"
col: 7726
ensembl_id: "ENSG00000153531"
name: "ADP-ribosylhydrolase like 1"
location: "13q34"
module: 98
arm: "+"
pooled_cpm: 7.68
n_lines_expressing: 50
n_dd_up: 51
n_dd_down: 6
n_dd_up_clean: 34
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# ADPRHL1

*ADP-ribosylhydrolase like 1* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 51 drug-doses (17 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.69× (z +16.8, q 0e+00, up in 34 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.591× (z -6.3, q 2e-07, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA10]] (+0.67, fdr 7e-06), [[VSTM2L]] (+0.65, fdr 7e-06), [[WDR13]] (+0.64, fdr 1e-05); moves opposite to [[ANOS1]] (-0.55, fdr 2e-04), [[BTBD3]] (-0.51, fdr 8e-05), [[CD47]] (-0.49, fdr 5e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TLR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 51 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7726.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.69×** | +16.8 | 0e+00 | 34/41 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **2.28×** | +14.0 | 7e-42 | 29/41 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | **2.84×** | +12.5 | 1e-33 | 34/40 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.22×** | +9.5 | 2e-19 | 24/46 (A-172, NCI-H1573, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.11×** | +8.6 | 1e-15 | 25/45 (A-172, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.03×** | +8.5 | 2e-15 | 23/46 (A-172, HOP62, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **2.10×** | +8.2 | 2e-14 | 22/41 (NCI-H1573, A-172, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.61×** | +8.1 | 5e-14 | 25/48 (A-172, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +8.0 | 8e-14 | 23/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.90×** | +7.7 | 9e-13 | 21/44 (A-172, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +7.6 | 1e-12 | 6/22 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.87×** | +7.5 | 3e-12 | 23/37 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | **1.85×** | +7.4 | 7e-12 | 23/43 (HOP62, A-172, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.82×** | +7.1 | 4e-11 | 19/47 (A-172, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.74×** | +6.6 | 1e-09 | 22/48 (A-172, HOP62, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +6.6 | 2e-09 | 21/47 (A-172, HOP62, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.72×** | +6.5 | 3e-09 | 23/46 (A-172, HOP62, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.70×** | +6.3 | 7e-09 | 23/48 (HOP62, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.66×** | +6.1 | 4e-08 | 21/47 (A-172, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7726.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.591×** | -6.3 | 2e-07 | 20/47 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.603×** | -6.1 | 4e-07 | 22/46 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.612×** | -5.9 | 7e-07 | 23/48 (LS 180, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.624×** | -5.7 | 2e-06 | 20/39 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.671×** | -4.6 | 5e-04 | 19/35 (A-172, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.727×** | -3.8 | 0.013 | 15/46 (BT-474, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ferulic acid (drug)]] 0.05 µM |  | 0.754× | -3.1 | 0.14 | 4/42 (SW1417, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Procainamide (hydrochloride) (drug)]] 0.5 µM |  | 0.774× | -3.1 | 0.15 | 5/47 (A-172, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7726. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 22.1 | 5 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +11.7) ⚠ position correction uncertain · without an alert: [[Triamcinolone (drug)]] 5 µM 3.61× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.0931× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 18.9 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 27.3× (z +17.0) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 9.04× (z +10.9) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.186× (z -8.7) |
| [[HOP62 (line)]] | alt | 14.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +12.6) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 5.51× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 22.7 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +9.7) ⚠ position correction uncertain | [[Belinostat (drug)]] 5 µM 0.137× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 10.4 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +11.8) | [[Thymol (drug)]] 0.5 µM 0.260× (z -8.7) |
| [[A-427 (line)]] | wt | 5.48 | 0 | 1 | — | [[Malotilate (drug)]] 0.5 µM 0.0572× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 4.97 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.11× (z +10.1) ⚠ position correction uncertain | — |
| [[BT-474 (line)]] | alt | 8.49 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0442× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 8.98 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +10.7) ⚠ position correction uncertain | — |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0929× (z -8.8) ⚠ toxic |
| [[J82 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0537× (z -15.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 6.09 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 8.57 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0894× (z -9.0) |
| [[A498 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7726), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA10]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[VSTM2L]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[WDR13]] | +0.64 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[STXBP5-AS1]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[HIPK2]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[TG]] | +0.60 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[IL6R]] | +0.59 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[IL1R1]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[RIPOR2]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[MAFB]] | +0.58 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[RTN4RL1]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[FSTL3]] | +0.57 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANOS1]] | -0.55 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[BTBD3]] | -0.51 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[CD47]] | -0.49 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[ZDHHC20]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[GUSBP18]] | -0.48 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[PTP4A2]] | -0.48 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[PRXL2A]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[DENND11]] | -0.47 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[NR3C2]] | -0.46 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[HMGN3]] | -0.46 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[PDE8A]] | -0.46 | -0.52 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLR2]] | B | TLR2 activity raises ADPRHL1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.52× lower at baseline in the lines without TLR2 | 0.010 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[DCN]] | B | DCN activity raises ADPRHL1's level | lines that do not express DCN (39) vs lines expressing it (11) | 1.87× lower at baseline in the lines without DCN | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1 |
| [[FOXC2]] | B | FOXC2 activity raises ADPRHL1's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 1.61× lower at baseline in the lines without FOXC2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[SVEP1]] | B | SVEP1 activity raises ADPRHL1's level | lines that do not express SVEP1 (15) vs lines expressing it (35) | 1.68× lower at baseline in the lines without SVEP1 | 0.051 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent |
| [[RHCG]] | B | RHCG activity raises ADPRHL1's level | lines that do not express RHCG (33) vs lines expressing it (17) | 1.51× lower at baseline in the lines without RHCG | 0.056 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[DNER]] | B | DNER activity raises ADPRHL1's level | lines that do not express DNER (32) vs lines expressing it (18) | 1.77× lower at baseline in the lines without DNER | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC |
| [[TOP2A]] | B | TOP2A activity lowers ADPRHL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANOS1]] | B | ANOS1 activity raises ADPRHL1's level | lines that do not express ANOS1 (31) vs lines expressing it (19) | 1.84× lower at baseline in the lines without ANOS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000268119, ZYG11A, KRT7 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.724). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.7, 15.7); signed map (17.9, 32.0). **Vector** length 104, 23.9% of its response variance represented; |z| ≥ 3 in 1,580 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | +6.3 | +14.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | +6.2 | +12.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +5.4 | +8.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +5.3 | +8.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +5.2 | +9.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +5.1 | +8.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +5.0 | +6.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.5 | -4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -5.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.8 | +0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -0.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -0.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ADP-ribosylhydrolase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:113,399,611-113,453,488 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARH2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDY3](https://www.uniprot.org/uniprotkb/Q8NDY3) (Inactive ADP-ribosyltransferase ARH2):

> Required for myofibril assembly and outgrowth of the cardiac chambers in the developing heart (By similarity). Appears to be catalytically inactive, showing no activity against O-acetyl-ADP-ribose (By similarity).

**Summary**, from NCBI Gene [113622](https://www.ncbi.nlm.nih.gov/gene/113622):

> ADP-ribosylation is a reversible posttranslational modification used to regulate protein function. ADP-ribosyltransferases (see ART1; MIM 601625) transfer ADP-ribose from NAD+ to the target protein, and ADP-ribosylhydrolases, such as ADPRHL1, reverse the reaction (Glowacki et al., 2002 [PubMed 12070318]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:21303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21303) · Entrez [113622](https://www.ncbi.nlm.nih.gov/gene/113622) · UniProt [Q8NDY3](https://www.uniprot.org/uniprotkb/Q8NDY3) · Ensembl [ENSG00000153531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153531)

## Data

Gene col 7726: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7726); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7726, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7726]; `tensor/DDL_lfc|DDL_z.npy` [7726]; `embed/gene_vectors.npy` [7726]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7726 or target_col == 7726). Every well: [[ADPRHL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADPRHL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
