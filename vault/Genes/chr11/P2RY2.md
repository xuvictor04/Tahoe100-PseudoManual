---
symbol: "P2RY2"
type: "gene"
col: 10627
ensembl_id: "ENSG00000175591"
name: "purinergic receptor P2Y2"
location: "11q13.4"
module: 31
arm: "+"
pooled_cpm: 4.31
n_lines_expressing: 23
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 62
direction_downstream: 104
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# P2RY2

*purinergic receptor P2Y2* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.04× (z +9.2, q 1e-17, up in 1 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.44× (z +4.6, q 4e-04, up in 7 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.532× (z -5.2, q 1e-04, down in 13 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA1]] (+0.72, fdr 1e-05), [[CORO2A]] (+0.70, fdr 7e-06), [[CEACAM6]] (+0.65, fdr 1e-05); moves opposite to [[ZNF785]] (-0.49, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 62 arrows point to it, the strongest [[SRMS]] → it (grade B ⚠); 104 go from it, the strongest it → [[PTK2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10627.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.04×** | +9.2 | 1e-17 | 1/7 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +6.7 | 5e-09 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +5.6 | 5e-06 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.81×** | +5.3 | 2e-05 | 2/15 (Panc 03.27, NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.20×** | +5.0 | 6e-05 | 0/11 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +4.6 | 4e-04 | 7/21 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +3.6 | 0.021 | 0/11 | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.040 | 0/16 | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.67×** | +3.3 | 0.067 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.067 | 1/17 (NCI-H2030) | two highest doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.076 | 5/18 (HEC-1-A, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +3.1 | 0.088 | 1/7 (AsPC-1) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10627.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.532×** | -5.2 | 1e-04 | 13/21 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[BAY1125976 (drug)]] 5 µM |  | **0.364×** | -4.7 | 7e-04 | 4/20 (AsPC-1, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.614×** | -4.3 | 0.003 | 13/21 (BT-474, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.627×** | -4.1 | 0.005 | 13/17 (CFPAC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.632×** | -4.1 | 0.005 | 10/21 (BT-474, NCI-H1573, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.648×** | -3.8 | 0.012 | 12/19 (BT-474, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.481×** | -3.4 | 0.054 | 4/21 (Hs 766T, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.686×** | -3.3 | 0.061 | 11/20 (BT-474, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.508×** | -3.1 | 0.095 | 4/19 (CFPAC-1, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.701×** | -3.1 | 0.095 | 5/21 (KATO III, BT-474, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.705×** | -3.1 | 0.096 | 13/19 (HT-29, LoVo, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.706×** | -3.1 | 0.096 | 10/20 (BT-474, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.712× | -3.0 | 0.11 | 2/21 (BT-474, LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10627. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 45.8 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0167× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.114× (z -10.9) |
| [[Hs 766T (line)]] | wt | 34.0 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0927× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[GSK1059615 (drug)]] 5 µM 0.0139× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0331× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0754× (z -11.5) |
| [[LS 180 (line)]] | wt | 3.95 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0985× (z -10.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Vandetanib (drug)]] 0.5 µM 0.0599× (z -9.2) |
| [[HT-29 (line)]] | alt | 21.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0691× (z -18.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0467× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 7.28 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -13.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0637× (z -10.6) |
| [[A498 (line)]] | wt | 3.43 | 0 | 2 | — | [[Celecoxib (drug)]] 0.05 µM 0.0631× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 7.49 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0815× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0576× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 5.95 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -9.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 6.04 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0750× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[LoVo (line)]] | wt | 4.61 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -11.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.306 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.363 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.655 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10627), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA1]] | +0.72 | +0.72 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[CORO2A]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CEACAM6]] | +0.65 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[GSDMC]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.64 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[CDH3]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[PROM2]] | +0.62 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[ELMO3]] | +0.62 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[HS3ST1]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[PTK6]] | +0.61 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[TC2N]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ARHGEF16]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF785]] | -0.49 | -0.48 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 3, C 59. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRMS]] | B | SRMS activity raises P2RY2's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.19× lower at baseline in the lines without SRMS | 0.037 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[ALS2CL]] | B | ALS2CL activity raises P2RY2's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.30× lower at baseline in the lines without ALS2CL | 0.080 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[FBXO17]] | B | FBXO17 activity lowers P2RY2's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 2.61× higher at baseline in the lines without FBXO17 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG |
| [[CEACAM6]] | C | CEACAM6 activity raises P2RY2's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 4.60× lower at baseline in the lines without CEACAM6 | 7e-04 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[FAM83A]] | C | FAM83A activity raises P2RY2's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 4.28× lower at baseline in the lines without FAM83A | 0.001 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9; co-absent with the target |
| [[CYP4F12]] | C | CYP4F12 activity raises P2RY2's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 3.60× lower at baseline in the lines without CYP4F12 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13; co-absent with the target |
| [[C6orf132]] | C | C6orf132 activity raises P2RY2's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 3.58× lower at baseline in the lines without C6orf132 | 0.001 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1; co-absent with the target |
| [[LAMA3]] | C | LAMA3 activity raises P2RY2's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 3.26× lower at baseline in the lines without LAMA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B; co-absent with the target |
| [[SERPINB5]] | C | SERPINB5 activity raises P2RY2's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 3.07× lower at baseline in the lines without SERPINB5 | 0.002 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |
| [[P2RY6]] | C | P2RY6 activity raises P2RY2's level | lines that do not express P2RY6 (29) vs lines expressing it (21) | 2.89× lower at baseline in the lines without P2RY6 | 0.002 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, FGG; co-absent with the target |
| [[TTC22]] | C | TTC22 activity raises P2RY2's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 3.01× lower at baseline in the lines without TTC22 | 0.003 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5; co-absent with the target |
| [[HS3ST1]] | C | HS3ST1 activity raises P2RY2's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 2.61× lower at baseline in the lines without HS3ST1 | 0.003 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4; co-absent with the target |

### Downstream of this gene

*104 arrows, 104 of them with an alert ⚠; grade A 0, B 35, C 69. Shown: the 12 strongest; 92 more arrows (92 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTK2B]] | B | P2RY2 activity raises PTK2B's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 3.32× lower at baseline in the lines without P2RY2 | 3e-04 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[ELMO3]] | B | P2RY2 activity raises ELMO3's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.53× lower at baseline in the lines without P2RY2 | 5e-04 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[FAM83E]] | B | P2RY2 activity raises FAM83E's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 3.25× lower at baseline in the lines without P2RY2 | 0.001 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[IL22RA1]] | B | P2RY2 activity raises IL22RA1's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.87× lower at baseline in the lines without P2RY2 | 0.002 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[KIF13B]] | B | P2RY2 activity raises KIF13B's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.07× lower at baseline in the lines without P2RY2 | 0.003 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[TMC6]] | B | P2RY2 activity raises TMC6's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 3.27× lower at baseline in the lines without P2RY2 | 0.003 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[CORO2A]] | B | P2RY2 activity raises CORO2A's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without P2RY2 | 0.004 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[ALS2CL]] | B | P2RY2 activity raises ALS2CL's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 3.43× lower at baseline in the lines without P2RY2 | 0.005 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[CYRIB]] | B | P2RY2 activity raises CYRIB's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 1.62× lower at baseline in the lines without P2RY2 | 0.006 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[PROM2]] | B | P2RY2 activity raises PROM2's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.44× lower at baseline in the lines without P2RY2 | 0.007 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[LMTK3]] | B | P2RY2 activity raises LMTK3's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.66× lower at baseline in the lines without P2RY2 | 0.007 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[MMP15]] | B | P2RY2 activity raises MMP15's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.34× lower at baseline in the lines without P2RY2 | 0.008 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.6, 54.8); signed map (59.1, 9.2). **Vector** length 64.4, 18.9% of its response variance represented; |z| ≥ 3 in 564 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +6.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.2 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +1.6 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.4 | -4.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -0.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | purinergic receptor P2Y2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:73,218,281-73,242,427 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P2U |
| Gene groups (HGNC) | P2Y receptors |
| Hallmark sets | INFLAMMATORY_RESPONSE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 12 pathways, smallest: P2Y receptors; Nucleotide-like (purinergic) receptors; Surfactant metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P41231](https://www.uniprot.org/uniprotkb/P41231) (P2Y purinoceptor 2):

> Receptor for ATP and UTP coupled to G proteins that activate a phosphatidylinositol-calcium second messenger system. The affinity range is UTP = ATP > ATP-gamma-S >> 2-methylthio-ATP = ADP.

**Summary**, from NCBI Gene [5029](https://www.ncbi.nlm.nih.gov/gene/5029):

> The product of this gene belongs to the family of P2 receptors, which is activated by extracellular nucleotides and subdivided into P2X ligand-gated ion channels and P2Y G-protein coupled receptors. This family has several receptor subtypes with different pharmacological selectivity, which overlaps in some cases, for various adenosine and uridine nucleotides. This receptor, found on many cell types, is activated by ATP and UTP and is reported to be overexpressed on some cancer cell types. It is …

**Accessions** — [HGNC:8541](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8541) · Entrez [5029](https://www.ncbi.nlm.nih.gov/gene/5029) · UniProt [P41231](https://www.uniprot.org/uniprotkb/P41231) · Ensembl [ENSG00000175591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175591)

## Data

Gene col 10627: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10627); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10627, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10627]; `tensor/DDL_lfc|DDL_z.npy` [10627]; `embed/gene_vectors.npy` [10627]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10627 or target_col == 10627). Every well: [[P2RY2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/P2RY2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
