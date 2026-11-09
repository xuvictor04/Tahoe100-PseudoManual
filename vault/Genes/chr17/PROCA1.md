---
symbol: "PROCA1"
type: "gene"
col: 9479
ensembl_id: "ENSG00000167525"
name: "protein interacting with cyclin A1"
location: "17q11.2"
module: 35
arm: "+"
pooled_cpm: 6.22
n_lines_expressing: 47
n_dd_up: 12
n_dd_down: 29
n_dd_up_clean: 9
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PROCA1

*protein interacting with cyclin A1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.08× (z +16.1, q 0e+00, up in 31 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.365× (z -10.2, q 2e-21, down in 28 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPEN-AS1]] (+0.64, fdr 1e-05), [[INHA]] (+0.62, fdr 1e-05), [[PJVK]] (+0.61, fdr 1e-05); moves opposite to [[TXNL4A]] (-0.53, fdr 5e-05), [[CIAO1]] (-0.53, fdr 3e-04), [[RRP1B]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CD27-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9479.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.08×** | +16.1 | 0e+00 | 31/35 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.94×** | +10.5 | 2e-23 | 25/35 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.92×** | +9.4 | 2e-18 | 27/43 (PANC-1, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +8.6 | 1e-15 | 6/12 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.88×** | +6.4 | 2e-08 | 23/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.87×** | +6.4 | 2e-08 | 23/42 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +6.2 | 4e-08 | 17/37 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.52×** | +4.3 | 0.001 | 16/40 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.002 | 10/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +4.1 | 0.002 | 9/25 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Darinaparsin (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.032 | 5/43 (NCI-H1792, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.40×** | +3.1 | 0.077 | 5/30 (LoVo, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9479.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.365×** | -10.2 | 2e-21 | 28/44 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.405×** | -9.1 | 2e-17 | 29/42 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.410×** | -9.0 | 5e-17 | 30/41 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.431×** | -8.5 | 3e-15 | 23/35 (NCI-H460, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.439×** | -8.3 | 1e-14 | 27/44 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.464×** | -7.7 | 1e-12 | 23/36 (NCI-H23, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.493×** | -7.1 | 9e-11 | 23/44 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.500×** | -7.0 | 2e-10 | 26/43 (NCI-H460, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.522×** | -6.5 | 4e-09 | 22/44 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.534×** | -6.3 | 2e-08 | 20/40 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.533×** | -6.0 | 1e-07 | 19/40 (SW 900, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.542×** | -5.9 | 1e-07 | 22/41 (A498, NCI-H460, …) | two highest doses | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.556×** | -5.9 | 1e-07 | 22/44 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.560×** | -5.8 | 2e-07 | 21/41 (C-33 A, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.584×** | -5.4 | 3e-06 | 23/44 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.396×** | -4.9 | 4e-05 | 21/35 (KATO III, A498, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.757×** | -3.9 | 0.003 | 17/42 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9479. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.5 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -12.1) |
| [[PANC-1 (line)]] | alt | 8.70 | 2 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0490× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.0706× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0989× (z -10.9) |
| [[A-172 (line)]] | wt | 11.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.2) ⚠ cell-cycle shift, explains ~96% of this change |
| [[C-33 A (line)]] | alt | 21.2 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0305× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 5.55 | 0 | 2 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.115× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 6.13 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0502× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0641× (z -9.9) |
| [[A498 (line)]] | wt | 5.46 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.112× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 4.90 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0671× (z -13.0) ⚠ cell-cycle shift, explains ~96% of this change |
| [[J82 (line)]] | alt | 7.82 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.126× (z -9.5) |
| [[KATO III (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -11.5) ⚠ cell-cycle shift, explains ~96% of this change |
| [[NCI-H1792 (line)]] | alt | 4.13 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0634× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 5.96 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0600× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 4.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0730× (z -8.5) |
| [[SNU-423 (line)]] | alt | 4.43 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0498× (z -10.0) |
| [[SW 900 (line)]] | alt | 6.70 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0562× (z -10.3) |
| [[SW480 (line)]] | alt | 3.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +9.8) | — |
| [[A-427 (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9479), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPEN-AS1]] | +0.64 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[INHA]] | +0.62 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[PJVK]] | +0.61 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CD27-AS1]] | +0.59 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[DMC1]] | +0.58 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[PRRT1]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PAXBP1-AS1]] | +0.58 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[PIPOX]] | +0.57 | +0.55 / +0.39 | both halves | 6e-05 |  |
| [[TRIM7]] | +0.57 | +0.37 / +0.48 | both halves | 9e-05 |  |
| [[HOXB-AS1]] | +0.57 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[CRTC3-AS1]] | +0.57 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[KMT2E-AS1]] | +0.57 | +0.42 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNL4A]] | -0.53 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[CIAO1]] | -0.53 | -0.29 / -0.41 | both halves | 3e-04 |  |
| [[RRP1B]] | -0.51 | -0.40 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PROCA1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TLCD3B]] | B | TLCD3B activity raises PROCA1's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 1.74× lower at baseline in the lines without TLCD3B | 0.045 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[RDM1P5]] | B | RDM1P5 activity raises PROCA1's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without RDM1P5 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD27-AS1]] | C | PROCA1 activity strengthens CD27-AS1's drug response | lines that do not express PROCA1 (3) vs lines expressing it (45) | the lines without PROCA1 respond 0.49× as strongly (z diff +1.85); strongest at Idarubicin (hydrochloride) 5 µM: 1.31x vs 4.63x (z diff +6.2) | 0.030 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: LTBP3, NUAK1, BLVRA; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (4.4, 24.5); signed map (34.1, -5.6). **Vector** length 79.8, 15.6% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +16.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.5 | +9.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +10.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +6.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.7 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +6.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.4 | +1.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -7.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.9 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -8.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.8 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | protein interacting with cyclin A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,703,197-28,711,888 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC39650 |
| Matched by | ensembl_id |

UniProt [Q8NCQ7](https://www.uniprot.org/uniprotkb/Q8NCQ7) carries no function annotation.

**Summary**, from NCBI Gene [147011](https://www.ncbi.nlm.nih.gov/gene/147011):

> Enables cyclin binding activity. Predicted to be involved in arachidonate secretion and phospholipid metabolic process. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28600) · Entrez [147011](https://www.ncbi.nlm.nih.gov/gene/147011) · UniProt [Q8NCQ7](https://www.uniprot.org/uniprotkb/Q8NCQ7) · Ensembl [ENSG00000167525](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167525)

## Data

Gene col 9479: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9479); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9479, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9479]; `tensor/DDL_lfc|DDL_z.npy` [9479]; `embed/gene_vectors.npy` [9479]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9479 or target_col == 9479). Every well: [[PROCA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PROCA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
