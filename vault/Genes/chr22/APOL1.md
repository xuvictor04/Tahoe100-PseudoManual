---
symbol: "APOL1"
type: "gene"
col: 1931
ensembl_id: "ENSG00000100342"
name: "apolipoprotein L1"
location: "22q12.3"
module: 70
arm: "+"
pooled_cpm: 89.96
n_lines_expressing: 26
n_dd_up: 25
n_dd_down: 25
n_dd_up_clean: 21
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 62
direction_downstream: 69
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# APOL1

*apolipoprotein L1* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.88× (z +7.6, q 2e-11, up in 22 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.345× (z -18.9, q 0e+00, down in 23 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPSTI1]] (+0.81, fdr 7e-06), [[CFB]] (+0.78, fdr 7e-06), [[TRIM22]] (+0.76, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 62 arrows point to it, the strongest [[IFI44]] → it (grade B ⚠); 69 go from it, the strongest it → [[APOL6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1931.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.88×** | +7.6 | 2e-11 | 22/23 (AsPC-1, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.80×** | +7.1 | 4e-10 | 21/24 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.72×** | +7.0 | 5e-10 | 23/25 (AsPC-1, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.56×** | +6.7 | 4e-09 | 24/24 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +6.1 | 1e-07 | 14/24 (Hs 766T, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.46×** | +5.8 | 7e-07 | 24/25 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.45×** | +5.6 | 2e-06 | 21/24 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.55×** | +5.5 | 3e-06 | 18/25 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.36×** | +5.3 | 7e-06 | 19/25 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.49×** | +5.0 | 4e-05 | 20/23 (AsPC-1, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +4.7 | 1e-04 | 6/25 (J82, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.005 | 15/24 (SNU-423, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.006 | 15/24 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +3.8 | 0.007 | 3/21 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.007 | 15/24 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.37×** | +3.7 | 0.008 | 14/24 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.008 | 3/24 (Hs 766T, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 0.05 µM |  | **1.36×** | +3.6 | 0.009 | 13/25 (AsPC-1, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1931.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.345×** | -18.9 | 0e+00 | 23/24 (A498, COLO 205, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.393×** | -11.8 | 1e-29 | 23/24 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.393×** | -11.7 | 1e-29 | 21/24 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.418×** | -10.6 | 6e-24 | 21/24 (COLO 205, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.462×** | -9.7 | 3e-20 | 22/24 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.499×** | -8.7 | 2e-16 | 24/24 (A498, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.555×** | -7.1 | 9e-11 | 20/23 (COLO 205, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.587×** | -6.7 | 1e-09 | 19/24 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.614×** | -6.1 | 6e-08 | 18/24 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.675×** | -4.9 | 4e-05 | 21/25 (A549, LoVo, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.495×** | -4.6 | 2e-04 | 16/24 (COLO 205, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.772×** | -4.6 | 2e-04 | 19/25 (KATO III, COLO 205, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.800×** | -4.0 | 0.003 | 17/25 (KATO III, COLO 205, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.734×** | -3.9 | 0.004 | 18/25 (KATO III, A549, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.739×** | -3.8 | 0.005 | 18/24 (KATO III, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.814×** | -3.7 | 0.008 | 11/24 (A549, COLO 205, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1931. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 310 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0266× (z -35.8) |
| [[A498 (line)]] | wt | 465 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0659× (z -35.8) |
| [[A549 (line)]] | wt | 75.1 | 1 | 9 (1 ⚠) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 3.54× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.0886× (z -24.8) |
| [[AsPC-1 (line)]] | alt | 73.4 | 8 | 2 (1 ⚠) | [[Trametinib (drug)]] 0.5 µM 4.39× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.9) |
| [[LoVo (line)]] | wt | 127 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -22.8) |
| [[HEC-1-A (line)]] | alt | 228 | 1 | 7 | [[Trametinib (drug)]] 0.5 µM 2.25× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -26.8) |
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0661× (z -24.7) |
| [[KATO III (line)]] | alt | 144 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.0533× (z -27.7) |
| [[CFPAC-1 (line)]] | alt | 919 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0600× (z -32.9) |
| [[HT-29 (line)]] | alt | 116 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -15.0) |
| [[A-172 (line)]] | wt | 80.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -18.3) |
| [[SNU-423 (line)]] | alt | 112 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -27.4) |
| [[SW 1088 (line)]] | alt | 124 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0751× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0906× (z -8.9) |
| [[H4 (line)]] | wt | 63.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0961× (z -20.9) |
| [[NCI-H1792 (line)]] | alt | 48.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0575× (z -29.2) |
| [[RPMI-7951 (line)]] | alt | 39.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -13.3) |
| [[C32 (line)]] | wt | 32.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -11.3) |
| [[Hs 766T (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -9.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 57.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -21.7) |
| [[Panc 03.27 (line)]] | alt | 45.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -14.6) |
| [[SK-MEL-2 (line)]] | alt | 32.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -14.9) |
| [[A-427 (line)]] | wt | 7.42 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.99 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 21.5 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.7 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 20.2 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.78 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 22.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.47 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.88 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.69 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 18.9 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.96 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.55 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1931), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPSTI1]] | +0.81 | +0.73 / +0.82 | both halves | 7e-06 |  |
| [[CFB]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[TRIM22]] | +0.76 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[TNFSF10]] | +0.76 | +0.69 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[PLAAT4]] | +0.75 | +0.76 / +0.66 | both halves | 7e-06 | STRING 437 |
| [[TMEM140]] | +0.75 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[IFI35]] | +0.73 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[TLR3]] | +0.73 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[GBP4]] | +0.72 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[SLC15A3]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[UBA7]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[PSMB10]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 29, C 33. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI44]] | B | IFI44 activity raises APOL1's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.98× lower at baseline in the lines without IFI44 | 0.012 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[RSAD2]] | B | RSAD2 activity raises APOL1's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.67× lower at baseline in the lines without RSAD2 | 0.014 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[TLR3]] | B | TLR3 activity raises APOL1's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 3.28× lower at baseline in the lines without TLR3 | 0.016 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[CASP10]] | B | CASP10 activity raises APOL1's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.83× lower at baseline in the lines without CASP10 | 0.016 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[APOL6]] | B | APOL6 activity raises APOL1's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 4.29× lower at baseline in the lines without APOL6 | 0.018 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[STEAP4]] | B | STEAP4 activity raises APOL1's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.45× lower at baseline in the lines without STEAP4 | 0.021 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[OAS1]] | B | OAS1 activity raises APOL1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.26× lower at baseline in the lines without OAS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[GBP3]] | B | GBP3 activity raises APOL1's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 3.27× lower at baseline in the lines without GBP3 | 0.036 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[OASL]] | B | OASL activity raises APOL1's level | lines that do not express OASL (10) vs lines expressing it (40) | 2.46× lower at baseline in the lines without OASL | 0.038 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[UBA7]] | B | UBA7 activity raises APOL1's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 4.11× lower at baseline in the lines without UBA7 | 0.040 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[IFIT2]] | B | IFIT2 activity raises APOL1's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 3.26× lower at baseline in the lines without IFIT2 | 0.042 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[LGALS9]] | B | LGALS9 activity raises APOL1's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 3.33× lower at baseline in the lines without LGALS9 | 0.047 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |

### Downstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 44, C 25. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOL6]] | B | APOL1 activity raises APOL6's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.85× lower at baseline in the lines without APOL1 | 0.004 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[B2M]] | B | APOL1 activity raises B2M's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.19× lower at baseline in the lines without APOL1 | 0.005 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[SAMD9]] | B | APOL1 activity raises SAMD9's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 3.38× lower at baseline in the lines without APOL1 | 0.005 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[UBA7]] | B | APOL1 activity raises UBA7's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without APOL1 | 0.005 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[APOL2]] | B | APOL1 activity raises APOL2's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.25× lower at baseline in the lines without APOL1 | 0.006 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[TMEM140]] | B | APOL1 activity raises TMEM140's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without APOL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[NLRC5]] | B | APOL1 activity raises NLRC5's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without APOL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[SEC16B]] | B | APOL1 activity raises SEC16B's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.29× lower at baseline in the lines without APOL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[PLSCR4]] | B | APOL1 activity raises PLSCR4's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.36× lower at baseline in the lines without APOL1 | 0.011 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[OASL]] | B | APOL1 activity raises OASL's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.24× lower at baseline in the lines without APOL1 | 0.012 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[IFI44]] | B | APOL1 activity raises IFI44's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.74× lower at baseline in the lines without APOL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[GBP3]] | B | APOL1 activity raises GBP3's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.77× lower at baseline in the lines without APOL1 | 0.016 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.6, 51.2); signed map (61.5, 29.3). **Vector** length 114, 39.3% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.55 to 25); *interferon alpha response* (hallmark, mean cos +0.52 to 19); *Antigen processing-Cross presentation* (reactome, mean cos +0.55 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +5.2 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.0 | +7.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.0 | +6.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.7 | +7.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -4.8 | -4.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.2 | -4.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.7 | -3.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.4 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein L1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:36,253,071-36,267,530 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously APOL |
| Gene groups (HGNC) | Apolipoproteins |
| Reactome | 5 pathways, smallest: Scavenging of heme from plasma; Binding and Uptake of Ligands by Scavenger Receptors; Post-translational protein phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O14791](https://www.uniprot.org/uniprotkb/O14791) (Apolipoprotein L1):

> May play a role in lipid exchange and transport throughout the body. May participate in reverse cholesterol transport from peripheral cells to the liver. A component of trypanosome lytic factor of human serum; plays a crucial role in killing Trypanosoma brucei by forming pores in parasite lysosomal membranes and sensitizing T.brucei to oxidation-stimulated osmotic lysis.

**Summary**, from NCBI Gene [8542](https://www.ncbi.nlm.nih.gov/gene/8542):

> This gene encodes a secreted high density lipoprotein which binds to apolipoprotein A-I. Apolipoprotein A-I is a relatively abundant plasma protein and is the major apoprotein of HDL. It is involved in the formation of most cholesteryl esters in plasma and also promotes efflux of cholesterol from cells. This apolipoprotein L family member may play a role in lipid exchange and transport throughout the body, as well as in reverse cholesterol transport from peripheral cells to the liver. Several …

**Accessions** — [HGNC:618](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:618) · Entrez [8542](https://www.ncbi.nlm.nih.gov/gene/8542) · UniProt [O14791](https://www.uniprot.org/uniprotkb/O14791) · Ensembl [ENSG00000100342](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100342)

## Data

Gene col 1931: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1931); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1931, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1931]; `tensor/DDL_lfc|DDL_z.npy` [1931]; `embed/gene_vectors.npy` [1931]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1931 or target_col == 1931). Every well: [[APOL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
