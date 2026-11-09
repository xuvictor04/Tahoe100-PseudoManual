---
symbol: "DCDC2"
type: "gene"
col: 7055
ensembl_id: "ENSG00000146038"
name: "doublecortin domain containing 2"
location: "6p22.3"
module: 27
arm: "+"
pooled_cpm: 15.01
n_lines_expressing: 25
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 21
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# DCDC2

*doublecortin domain containing 2* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.07× (z +21.0, q 0e+00, up in 12 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.738× (z -4.1, q 0.026, down in 9 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (C-33 A 0.271×, HepG2/C3A 0.278×, HEC-1-A 0.451×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.247×, C-33 A 0.247×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (HEC-1-A 0.344×, C-33 A 0.250×; ⚠ cell-cycle shift, explains ~0% of this change); [[Clopidogrel (drug)]] 0.5 µM in 1 line (A-427 0.0590×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.247×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SORL1]] (+0.58, fdr 1e-05), [[PPM1H]] (+0.58, fdr 1e-05), [[HAVCR1]] (+0.57, fdr 1e-05); moves opposite to [[CCM2]] (-0.48, fdr 4e-05), [[FBH1]] (-0.47, fdr 1e-04), [[SENP5]] (-0.47, fdr 4e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[PPP1R9A]] → it (grade B ⚠); 21 go from it, the strongest it → [[ABCC6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7055.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.07×** | +21.0 | 0e+00 | 12/22 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +13.4 | 3e-38 | 5/21 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +12.8 | 4e-35 | 10/17 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +11.4 | 4e-28 | 9/14 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +11.3 | 1e-27 | 14/22 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +8.8 | 1e-16 | 6/15 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +8.2 | 2e-14 | 7/21 (RPMI-7951, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +6.6 | 3e-09 | 12/22 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +6.1 | 7e-08 | 12/23 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +5.7 | 8e-07 | 6/18 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.6 | 2e-04 | 0/20 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.36×** | +4.2 | 0.001 | 5/22 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.67×** | +3.6 | 0.013 | 10/20 (CFPAC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.016 | 13/22 (HEC-1-A, A549, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.028 | 6/23 (HEC-1-A, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.028 | 7/23 (HEC-1-A, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.028 | 2/22 (SNU-423, A-427) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.044 | 8/23 (HEC-1-A, HepG2/C3A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.061 | 6/22 (HEC-1-A, SW480, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7055.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (C-33 A 0.271×, HepG2/C3A 0.278×, HEC-1-A 0.451×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.247×, C-33 A 0.247×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (HEC-1-A 0.344×, C-33 A 0.250×; ⚠ cell-cycle shift, explains ~0% of this change); [[Clopidogrel (drug)]] 0.5 µM in 1 line (A-427 0.0590×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.247×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.738×** | -4.1 | 0.026 | 9/23 (SW480, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.776× | -3.4 | 0.18 | 4/23 (A498, A-172, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.640× | -3.1 | 0.32 | 9/21 (LoVo, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7055. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 250 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0518× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 128 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -13.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -12.0) |
| [[LoVo (line)]] | wt | 15.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.245× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 12.6 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.211× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~90% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.282× (z -9.0) |
| [[A-427 (line)]] | wt | 5.76 | 0 | 1 | — | [[Clopidogrel (drug)]] 0.5 µM 0.0590× (z -10.1) |
| [[HCT15 (line)]] | alt | 43.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0668× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 4.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 4.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 5.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +9.7) | — |
| [[A-172 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7055), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORL1]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[PPM1H]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[HAVCR1]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PLCB4]] | +0.56 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[SLC7A8]] | +0.56 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[MPP7]] | +0.55 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[PRLR]] | +0.55 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[RPS6KA6]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[DLEU1]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[LINC02147]] | +0.53 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[LINC01091]] | +0.52 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[KSR2]] | +0.52 | +0.45 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCM2]] | -0.48 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[FBH1]] | -0.47 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[SENP5]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[ZNF549]] | -0.47 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[SLC38A9]] | -0.46 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[GBA2]] | -0.45 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[PITPNA]] | -0.44 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[SS18L1]] | -0.44 | -0.39 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R9A]] | B | PPP1R9A activity raises DCDC2's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 2.72× lower at baseline in the lines without PPP1R9A | 0.017 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[PLCH1]] | B | PLCH1 activity raises DCDC2's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 2.52× lower at baseline in the lines without PLCH1 | 0.042 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NMNAT3]] | B | NMNAT3 activity raises DCDC2's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 1.84× lower at baseline in the lines without NMNAT3 | 0.047 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C |
| [[PKD1L2]] | B | PKD1L2 activity raises DCDC2's level | lines that do not express PKD1L2 (13) vs lines expressing it (37) | 1.41× lower at baseline in the lines without PKD1L2 | 0.082 | ⚠ within organs, on part of the lines; also absent: SPDYE10; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers DCDC2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[GPR143]] | C | GPR143 activity raises DCDC2's level | lines that do not express GPR143 (19) vs lines expressing it (31) | 3.01× lower at baseline in the lines without GPR143 | 0.005 | ⚠ within organs, on part of the lines; also absent: SHROOM2, DCDC2, SCN5A; maybe low, not absent; co-absent with the target |
| [[TIMD4]] | C | TIMD4 activity raises DCDC2's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 5.11× lower at baseline in the lines without TIMD4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[HAVCR1]] | C | HAVCR1 activity raises DCDC2's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 4.53× lower at baseline in the lines without HAVCR1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[RHEX]] | C | RHEX activity raises DCDC2's level | lines that do not express RHEX (43) vs lines expressing it (7) | 5.40× lower at baseline in the lines without RHEX | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB; co-absent with the target |
| [[ENPP5]] | C | ENPP5 activity raises DCDC2's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 2.27× lower at baseline in the lines without ENPP5 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004; co-absent with the target |
| [[DSCAML1]] | C | DSCAML1 activity raises DCDC2's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.74× lower at baseline in the lines without DSCAML1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 14, C 7. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCC6]] | B | DCDC2 activity raises ABCC6's level | lines that do not express DCDC2 (25) vs lines expressing it (25) | 1.93× lower at baseline in the lines without DCDC2 | 0.011 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| [[RAB17]] | B | DCDC2 activity raises RAB17's level | lines that do not express DCDC2 (25) vs lines expressing it (25) | 2.35× lower at baseline in the lines without DCDC2 | 0.026 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| [[EPCAM-DT]] | B | DCDC2 activity raises EPCAM-DT's level | lines that do not express DCDC2 (25) vs lines expressing it (25) | 1.77× lower at baseline in the lines without DCDC2 | 0.033 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| cells under [[Lactate (calcium) (drug)]] 0.05 µM | B | DCDC2 activity lowers the cells' numbers under Lactate (calcium) 0.05 µM (makes them more sensitive) | lines that do not express DCDC2 (25) vs lines expressing it (23) | the lines without DCDC2: 1.13× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| [[ARSL]] | B | DCDC2 activity raises ARSL's level | lines that do not express DCDC2 (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without DCDC2 | 0.055 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| [[PKD1L2]] | B | DCDC2 activity raises PKD1L2's level | lines that do not express DCDC2 (25) vs lines expressing it (25) | 1.68× lower at baseline in the lines without DCDC2 | 0.055 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| cells under [[Macitentan (drug)]] 5 µM | B | DCDC2 activity raises the cells' numbers under Macitentan 5 µM (protects the cells) | lines that do not express DCDC2 (25) vs lines expressing it (23) | the lines without DCDC2: 0.88× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| cells under [[γ-Oryzanol (drug)]] 0.05 µM | B | DCDC2 activity lowers the cells' numbers under γ-Oryzanol 0.05 µM (makes them more sensitive) | lines that do not express DCDC2 (25) vs lines expressing it (23) | the lines without DCDC2: 1.10× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM | B | DCDC2 activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 0.05 µM (makes them more sensitive) | lines that do not express DCDC2 (25) vs lines expressing it (23) | the lines without DCDC2: 1.13× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| cells under [[Ivermectin (drug)]] 0.5 µM | B | DCDC2 activity raises the cells' numbers under Ivermectin 0.5 µM (protects the cells) | lines that do not express DCDC2 (25) vs lines expressing it (23) | the lines without DCDC2: 0.90× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| cells under [[Sodium Salicylate (drug)]] 5 µM | B | DCDC2 activity raises the cells' numbers under Sodium Salicylate 5 µM (protects the cells) | lines that do not express DCDC2 (25) vs lines expressing it (23) | the lines without DCDC2: 0.94× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| cells under [[Clopidogrel (drug)]] 0.05 µM | B | DCDC2 activity lowers the cells' numbers under Clopidogrel 0.05 µM (makes them more sensitive) | lines that do not express DCDC2 (25) vs lines expressing it (23) | the lines without DCDC2: 1.22× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.563). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.1, 46.0); signed map (52.2, 2.4). **Vector** length 55.7, 12.7% of its response variance represented; |z| ≥ 3 in 543 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +21.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +6.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +3.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.5 | +2.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.6 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.6 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -4.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -3.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -2.8 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -0.9 | -1.4 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | doublecortin domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:24,171,755-24,358,059 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RU2, KIAA1154, DCDC2A, NPHP19; previously DFNB66 |
| Gene groups (HGNC) | Doublecortin superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHG0](https://www.uniprot.org/uniprotkb/Q9UHG0) (Doublecortin domain-containing protein 2):

> Protein that plays a role in the inhibition of canonical Wnt signaling pathway. May be involved in neuronal migration during development of the cerebral neocortex (By similarity). Involved in the control of ciliogenesis and ciliary length.

**Summary**, from NCBI Gene [51473](https://www.ncbi.nlm.nih.gov/gene/51473):

> This gene encodes a doublecortin domain-containing family member. The doublecortin domain has been demonstrated to bind tubulin and enhance microtubule polymerization. This family member is thought to function in neuronal migration where it may affect the signaling of primary cilia. Mutations in this gene have been associated with reading disability (RD) type 2, also referred to as developmental dyslexia. Alternatively spliced transcript variants encoding the same protein have been found for …

**Accessions** — [HGNC:18141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18141) · Entrez [51473](https://www.ncbi.nlm.nih.gov/gene/51473) · UniProt [Q9UHG0](https://www.uniprot.org/uniprotkb/Q9UHG0) · Ensembl [ENSG00000146038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146038)

## Data

Gene col 7055: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7055); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7055, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7055]; `tensor/DDL_lfc|DDL_z.npy` [7055]; `embed/gene_vectors.npy` [7055]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7055 or target_col == 7055). Every well: [[DCDC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCDC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
