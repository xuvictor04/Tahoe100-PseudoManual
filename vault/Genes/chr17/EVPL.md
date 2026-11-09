---
symbol: "EVPL"
type: "gene"
col: 9553
ensembl_id: "ENSG00000167880"
name: "envoplakin"
location: "17q25.1"
module: 27
arm: "+"
pooled_cpm: 15.32
n_lines_expressing: 34
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 9
direction_downstream: 12
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# EVPL

*envoplakin* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.63× (z +7.6, q 2e-11, up in 15 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.48× (z +6.1, q 2e-07, up in 17 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.577× (z -8.6, q 4e-15, down in 21 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSH3]] (+0.57, fdr 1e-05), [[DMTN]] (+0.55, fdr 1e-05), [[ADAP1]] (+0.55, fdr 1e-05); moves opposite to [[SRGAP2B]] (-0.44, fdr 7e-05), [[RB1]] (-0.41, fdr 2e-04), [[CDKL5]] (-0.41, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LAD1]] → it (grade B ⚠); 12 go from it, the strongest it → [[PSD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9553.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +7.6 | 2e-11 | 15/28 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +7.2 | 1e-10 | 15/20 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +6.1 | 2e-07 | 17/32 (SW48, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +5.8 | 7e-07 | 15/32 (NCI-H460, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.25×** | +4.9 | 1e-04 | 14/32 (COLO 205, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.003 | 9/32 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.019 | 12/32 (A-427, NCI-H460, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.065 | 5/32 (MIA PaCa-2, LS 180, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.092 | 5/31 (A549, Panc 03.27, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | 1.15× | +3.0 | 0.15 | 6/32 (CFPAC-1, COLO 205, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9553.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.577×** | -8.6 | 4e-15 | 21/32 (NCI-H2347, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.584×** | -8.4 | 1e-14 | 24/32 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.586×** | -8.4 | 1e-14 | 21/32 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.599×** | -8.0 | 2e-13 | 20/32 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.637×** | -7.1 | 2e-10 | 22/32 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -6.7 | 2e-09 | 19/31 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.689×** | -5.8 | 5e-07 | 18/32 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.690×** | -5.8 | 5e-07 | 18/32 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.614×** | -5.7 | 8e-07 | 17/32 (MIA PaCa-2, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.720×** | -5.1 | 2e-05 | 18/32 (PANC-1, COLO 205, …) | two highest doses | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.646×** | -5.1 | 2e-05 | 14/32 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.799×** | -4.9 | 5e-05 | 15/32 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.812×** | -4.5 | 3e-04 | 18/32 (COLO 205, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.783×** | -3.3 | 0.036 | 4/32 (HT-29, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9553. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 29.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -9.7) |
| [[LoVo (line)]] | wt | 29.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.253× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 48.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -9.4) |
| [[A-427 (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -15.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 60.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -13.9) ⚠ cell-cycle shift, explains ~9% of this change |
| [[HCT15 (line)]] | alt | 29.2 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.211× (z -8.7) |
| [[Hs 766T (line)]] | wt | 5.67 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0639× (z -10.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -11.6) ⚠ cell-cycle shift, explains ~9% of this change |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -8.9) |
| [[RKO (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 37.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -9.1) |
| [[SW480 (line)]] | alt | 15.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.345× (z -8.9) |
| [[A-172 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9553), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSH3]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[DMTN]] | +0.55 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[ADAP1]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[EPS8L2]] | +0.53 | +0.55 / +0.50 | both halves | 1e-05 | same gene group |
| [[MYO18A]] | +0.53 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[SEMA4D]] | +0.53 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[KCNQ4]] | +0.52 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[ERBB2]] | +0.51 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[LRP5]] | +0.51 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[PWWP2B]] | +0.51 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[LAD1]] | +0.51 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[FUT10]] | +0.50 | +0.53 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP2B]] | -0.44 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[RB1]] | -0.41 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[CDKL5]] | -0.41 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[SRGAP2C]] | -0.40 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[TIMP1]] | -0.40 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[TMEM50A]] | -0.40 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[RELL1]] | -0.40 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[BRK1]] | -0.40 | -0.36 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAD1]] | B | LAD1 activity raises EVPL's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 3.33× lower at baseline in the lines without LAD1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[EPS8L1]] | B | EPS8L1 activity raises EVPL's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 1.81× lower at baseline in the lines without EPS8L1 | 0.081 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers EVPL's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SPTBN2]] | B | SPTBN2 activity raises EVPL's level | lines that do not express SPTBN2 (9) vs lines expressing it (41) | 2.97× lower at baseline in the lines without SPTBN2 | 0.089 | ⚠ within organs, on part of the lines; also absent: CCDC88C, HID1, ASS1; maybe low, not absent |
| [[DMTN]] | C | DMTN activity raises EVPL's level | lines that do not express DMTN (14) vs lines expressing it (36) | 3.66× lower at baseline in the lines without DMTN | 0.013 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent; co-absent with the target |
| [[INAVA]] | C | INAVA activity raises EVPL's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.22× lower at baseline in the lines without INAVA | 0.028 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3; co-absent with the target |
| [[PKP3]] | C | PKP3 activity raises EVPL's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 3.73× lower at baseline in the lines without PKP3 | 0.032 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent; co-absent with the target |
| [[FAM83H]] | C | FAM83H activity raises EVPL's level | lines that do not express FAM83H (13) vs lines expressing it (37) | 4.06× lower at baseline in the lines without FAM83H | 0.076 | ⚠ within organs, on part of the lines; also absent: IQANK1, EVPL, OCLN; co-absent with the target |
| [[ARHGEF16]] | C | ARHGEF16 activity raises EVPL's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 3.83× lower at baseline in the lines without ARHGEF16 | 0.079 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 7, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSD4]] | B | EVPL activity raises PSD4's level | lines that do not express EVPL (16) vs lines expressing it (34) | 2.71× lower at baseline in the lines without EVPL | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN |
| [[LRP5]] | B | EVPL activity raises LRP5's level | lines that do not express EVPL (16) vs lines expressing it (34) | 3.02× lower at baseline in the lines without EVPL | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN |
| [[TMEM184A]] | B | EVPL activity raises TMEM184A's level | lines that do not express EVPL (16) vs lines expressing it (34) | 2.74× lower at baseline in the lines without EVPL | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN |
| [[SPTBN2]] | B | EVPL activity raises SPTBN2's level | lines that do not express EVPL (16) vs lines expressing it (34) | 2.14× lower at baseline in the lines without EVPL | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN |
| [[PLXNB1]] | B | EVPL activity raises PLXNB1's level | lines that do not express EVPL (16) vs lines expressing it (34) | 1.53× lower at baseline in the lines without EVPL | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN |
| [[MYO18A]] | B | EVPL activity raises MYO18A's level | lines that do not express EVPL (16) vs lines expressing it (34) | 1.50× lower at baseline in the lines without EVPL | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN |
| [[UNC13D]] | B | EVPL activity raises UNC13D's level | lines that do not express EVPL (16) vs lines expressing it (34) | 1.81× lower at baseline in the lines without EVPL | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN |
| [[PKP3]] | C | EVPL activity raises PKP3's level | lines that do not express EVPL (16) vs lines expressing it (34) | 3.88× lower at baseline in the lines without EVPL | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN; co-absent with the target |
| [[DMTN]] | C | EVPL activity raises DMTN's level | lines that do not express EVPL (16) vs lines expressing it (34) | 2.58× lower at baseline in the lines without EVPL | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN; co-absent with the target |
| [[EPS8L2]] | C | EVPL activity raises EPS8L2's level | lines that do not express EVPL (16) vs lines expressing it (34) | 2.98× lower at baseline in the lines without EVPL | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN; co-absent with the target |
| [[FAM83H]] | C | EVPL activity raises FAM83H's level | lines that do not express EVPL (16) vs lines expressing it (34) | 4.57× lower at baseline in the lines without EVPL | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN; co-absent with the target |
| [[ARHGEF16]] | C | EVPL activity raises ARHGEF16's level | lines that do not express EVPL (16) vs lines expressing it (34) | 2.88× lower at baseline in the lines without EVPL | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.225). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.2, 56.0); signed map (22.5, 15.5). **Vector** length 70.8, 16.3% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.2 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.0 | +2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.9 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -0.5 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.3 | -1.3 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.3 | -0.5 |
|  | [[Riluzole hydrochloride (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | envoplakin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,004,502-76,027,306 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EVPK |
| Gene groups (HGNC) | Plakins; Spectrin repeat containing; SH3 domain containing |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92817](https://www.uniprot.org/uniprotkb/Q92817) (Envoplakin):

> Component of the cornified envelope of keratinocytes. May link the cornified envelope to desmosomes and intermediate filaments.

**Summary**, from NCBI Gene [2125](https://www.ncbi.nlm.nih.gov/gene/2125):

> This gene encodes a member of the plakin family of proteins that forms a component of desmosomes and the epidermal cornified envelope. This gene is located in the tylosis oesophageal cancer locus on chromosome 17q25, and its deletion is associated with both familial and sporadic forms of oesophageal squamous cell carcinoma. Patients suffering from the autoimmune mucocutaneous disorder, paraneoplastic pemphigus, develop antibodies against the encoded protein. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:3503](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3503) · Entrez [2125](https://www.ncbi.nlm.nih.gov/gene/2125) · UniProt [Q92817](https://www.uniprot.org/uniprotkb/Q92817) · Ensembl [ENSG00000167880](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167880)

## Data

Gene col 9553: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9553); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9553, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9553]; `tensor/DDL_lfc|DDL_z.npy` [9553]; `embed/gene_vectors.npy` [9553]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9553 or target_col == 9553). Every well: [[EVPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EVPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
