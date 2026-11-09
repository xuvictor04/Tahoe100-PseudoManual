---
symbol: "SLC9A2"
type: "gene"
col: 3702
ensembl_id: "ENSG00000115616"
name: "solute carrier family 9 member A2"
location: "2q12.1"
module: 73
arm: "+"
pooled_cpm: 13.25
n_lines_expressing: 31
n_dd_up: 25
n_dd_down: 7
n_dd_up_clean: 21
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 5
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# SLC9A2

*solute carrier family 9 member A2* — 2q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.49× (z +16.9, q 0e+00, up in 23 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.554× (z -7.7, q 8e-12, down in 21 of 28 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A9]] (+0.53, fdr 1e-05), [[PRTG]] (+0.53, fdr 1e-05), [[DSG4]] (+0.52, fdr 4e-05); moves opposite to [[TTC28-AS1]] (-0.47, fdr 4e-05), [[LINC02649]] (-0.46, fdr 3e-05), [[TNXB]] (-0.44, fdr 5e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PKP1]] → it (grade B ⚠); 5 go from it, the strongest it → [[LINC00592]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3702.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **2.49×** | +16.9 | 0e+00 | 23/28 (PANC-1, SW1417, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +13.1 | 7e-37 | 16/25 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **2.64×** | +12.7 | 2e-34 | 27/28 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.98×** | +12.6 | 2e-34 | 18/27 (SW480, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **2.26×** | +10.7 | 2e-24 | 24/27 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +10.6 | 4e-24 | 9/20 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +10.1 | 5e-22 | 5/13 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.99×** | +9.0 | 2e-17 | 24/28 (SW1417, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +8.4 | 4e-15 | 13/25 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +8.0 | 6e-14 | 18/28 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +7.7 | 6e-13 | 8/15 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.55×** | +5.5 | 1e-06 | 9/27 (NCI-H1573, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +5.5 | 1e-06 | 11/28 (SW 900, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.0 | 2e-05 | 11/27 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 9e-04 | 11/28 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +3.9 | 0.003 | 7/27 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.005 | 5/27 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.015 | 5/26 (LS 180, NCI-H1573, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3702.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.554×** | -7.7 | 8e-12 | 21/28 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.592×** | -6.8 | 3e-09 | 19/25 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.606×** | -6.5 | 1e-08 | 18/27 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.714×** | -4.4 | 0.002 | 21/26 (SNU-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.721×** | -4.3 | 0.002 | 8/27 (LS 180, HEC-1-A, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.746×** | -3.7 | 0.023 | 12/25 (HEC-1-A, LoVo, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.757×** | -3.6 | 0.024 | 9/27 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Rifaximin (drug)]] 0.05 µM |  | 0.775× | -3.1 | 0.15 | 3/26 (AsPC-1, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3702. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 97.1 | 0 | 10 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.419× (z -10.3) |
| [[A-427 (line)]] | wt | 20.8 | 1 | 7 (3 ⚠) | [[Selinexor (drug)]] 5 µM 2.57× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.144× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.218× (z -10.9) |
| [[SW1417 (line)]] | alt | 17.6 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 37.7 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.321× (z -10.5) |
| [[PANC-1 (line)]] | alt | 5.65 | 3 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 7.02× (z +15.1) | [[Digitoxin (drug)]] 5 µM 0.203× (z -8.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 5.86 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.99× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 55.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 7.18 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0592× (z -11.0) |
| [[KATO III (line)]] | alt | 25.4 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.71× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 9.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +9.0) | — |
| [[A-172 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3702), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A9]] | +0.53 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PRTG]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[DSG4]] | +0.52 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[SPINK13]] | +0.49 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[LINC00592]] | +0.49 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[NOSTRIN]] | +0.49 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[LGALSL]] | +0.48 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[IL1R2]] | +0.48 | +0.45 / +0.40 | both halves | 4e-05 |  |
| [[ZNF736P9Y]] | +0.47 | +0.47 / +0.34 | both halves | 1e-04 |  |
| [[AP1S3]] | +0.47 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[KLHL13]] | +0.47 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[PDE8B]] | +0.47 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC28-AS1]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[LINC02649]] | -0.46 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[TNXB]] | -0.44 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[NARF]] | -0.44 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[SNED1-AS1]] | -0.44 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[DCAF11]] | -0.43 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[SRGAP2B]] | -0.42 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[ARHGAP19]] | -0.42 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[PPP1R32]] | -0.41 | -0.46 / -0.32 | both halves | 1e-04 |  |
| [[TAF5]] | -0.41 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[GNB2]] | -0.40 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[GLYR1]] | -0.40 | -0.29 / -0.39 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKP1]] | B | PKP1 activity raises SLC9A2's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.69× lower at baseline in the lines without PKP1 | 0.014 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[IGFL2]] | B | IGFL2 activity raises SLC9A2's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 2.35× lower at baseline in the lines without IGFL2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[MARCOL]], [[SPINK13]] | B | MARCOL, SPINK13 activity raises SLC9A2's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 3.00× lower at baseline in the lines without MARCOL, SPINK13 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent genes |
| [[SCARA5]] | B | SCARA5 activity raises SLC9A2's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 2.79× lower at baseline in the lines without SCARA5 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5 |
| [[XK]] | B | XK activity raises SLC9A2's level | lines that do not express XK (18) vs lines expressing it (32) | 2.43× lower at baseline in the lines without XK | 0.070 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| [[DSG4]] | B | DSG4 activity raises SLC9A2's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 4.18× lower at baseline in the lines without DSG4 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[NOSTRIN]] | C | NOSTRIN activity raises SLC9A2's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.89× lower at baseline in the lines without NOSTRIN | 0.055 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00592]] | B | SLC9A2 activity raises LINC00592's level | lines that do not express SLC9A2 (19) vs lines expressing it (31) | 1.70× lower at baseline in the lines without SLC9A2 | 0.010 | ⚠ within organs, on part of the lines; also absent: TC2N, MAP7, ENSG00000262302 |
| [[SH3RF2]] | B | SLC9A2 activity raises SH3RF2's level | lines that do not express SLC9A2 (19) vs lines expressing it (31) | 2.26× lower at baseline in the lines without SLC9A2 | 0.033 | ⚠ within organs, on part of the lines; also absent: TC2N, MAP7, ENSG00000262302 |
| cells under [[Apalutamide (drug)]] 0.5 µM | B | SLC9A2 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express SLC9A2 (19) vs lines expressing it (29) | the lines without SLC9A2: 1.20× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: TC2N, MAP7, ENSG00000262302 |
| [[KRT80]] | C | SLC9A2 activity raises KRT80's level | lines that do not express SLC9A2 (19) vs lines expressing it (31) | 3.11× lower at baseline in the lines without SLC9A2 | 0.035 | ⚠ within organs, on part of the lines; also absent: TC2N, MAP7, ENSG00000262302; co-absent with the target |
| [[NOSTRIN]] | C | SLC9A2 activity raises NOSTRIN's level | lines that do not express SLC9A2 (19) vs lines expressing it (31) | 2.54× lower at baseline in the lines without SLC9A2 | 0.092 | ⚠ within organs, on part of the lines; also absent: TC2N, MAP7, ENSG00000262302; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.466). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.4, 52.7); signed map (59.4, 21.2). **Vector** length 84.4, 21.3% of its response variance represented; |z| ≥ 3 in 822 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.7 | +16.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +12.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.3 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +10.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.4 | +9.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.1 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -7.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.7 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 9 member A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.1 — chr2:102,619,553-102,711,355 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NHE2 |
| Gene groups (HGNC) | Solute carrier family 9 |
| Reactome | 4 pathways, smallest: Sodium/Proton exchangers; Metal ion SLC transporters; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBY0](https://www.uniprot.org/uniprotkb/Q9UBY0) (Sodium/hydrogen exchanger 2):

> Plasma membrane Na(+)/H(+) antiporter. Mediates the electroneutral exchange of intracellular H(+) ions for extracellular Na(+). Major apical Na(+)/H(+) exchanger in the base of the colonic crypt. Controls in the colonic crypt intracellular pH (pHi) to direct colonic epithelial cell differentiation into the absorptive enterocyte lineage at the expense of the secretory lineage (By similarity).

**Summary**, from NCBI Gene [6549](https://www.ncbi.nlm.nih.gov/gene/6549):

> This gene encodes a member of the sodium-hydrogen exchanger (NHE) protein family. These proteins are involved in sodium-ion transport by exchanging intracellular hydrogen ions to external sodium ions and help in the regulation of cell pH and volume. The encoded protein is localized to the apical membrane and is involved in apical absorption of sodium. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:11072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11072) · Entrez [6549](https://www.ncbi.nlm.nih.gov/gene/6549) · UniProt [Q9UBY0](https://www.uniprot.org/uniprotkb/Q9UBY0) · Ensembl [ENSG00000115616](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115616)

## Data

Gene col 3702: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3702); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3702, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3702]; `tensor/DDL_lfc|DDL_z.npy` [3702]; `embed/gene_vectors.npy` [3702]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3702 or target_col == 3702). Every well: [[SLC9A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC9A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
