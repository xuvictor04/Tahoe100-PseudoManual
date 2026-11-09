---
symbol: "PRIM1"
type: "gene"
col: 12522
ensembl_id: "ENSG00000198056"
name: "DNA primase subunit 1"
location: "12q13.3"
module: 6
arm: "+"
pooled_cpm: 14.46
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# PRIM1

*DNA primase subunit 1* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.23× (z +11.8, q 2e-29, up in 17 of 21 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.45× (z +3.9, q 0.006, up in 19 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.501× (z -10.2, q 1e-21, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPU]] (+0.85, fdr 7e-06), [[EXO1]] (+0.84, fdr 7e-06), [[HAUS1]] (+0.84, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12522.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **3.23×** | +11.8 | 2e-29 | 17/21 (NCI-H460, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **2.95×** | +11.3 | 3e-27 | 33/38 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **2.16×** | +7.5 | 2e-11 | 21/31 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.73×** | +5.7 | 1e-06 | 27/47 (LoVo, A549, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.69×** | +5.5 | 4e-06 | 21/47 (A549, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.58×** | +4.8 | 1e-04 | 22/47 (LoVo, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~88% of this change | **1.49×** | +4.0 | 0.005 | 15/40 (CFPAC-1, SW 900, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.45×** | +3.9 | 0.006 | 19/48 (Panc 03.27, SW480, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.30×** | +3.9 | 0.007 | 16/48 (SK-MEL-2, Panc 03.27, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.44×** | +3.8 | 0.007 | 21/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.28×** | +3.7 | 0.012 | 8/48 (SW480, HT-29, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.42×** | +3.7 | 0.012 | 13/48 (Panc 03.27, A498, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.39×** | +3.3 | 0.037 | 13/46 (A-427, SW480, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.56×** | +3.3 | 0.037 | 13/34 (A-172, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.37×** | +3.3 | 0.038 | 12/47 (LOX-IMVI, Panc 03.27, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +3.2 | 0.045 | 6/48 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.066 | 11/48 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.087 | 12/46 (C32, SW480, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.089 | 15/47 (LoVo, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12522.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.501×** | -10.2 | 1e-21 | 29/46 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.474×** | -7.8 | 2e-12 | 28/44 (Panc 03.27, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.562×** | -6.0 | 4e-07 | 27/47 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.478×** | -5.5 | 5e-06 | 26/48 (A498, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -5.5 | 5e-06 | 27/46 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.597×** | -5.4 | 7e-06 | 26/47 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.603×** | -5.3 | 1e-05 | 25/46 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.451×** | -4.3 | 0.001 | 20/47 (A-427, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -4.0 | 0.004 | 21/46 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.711×** | -3.5 | 0.022 | 13/48 (CHP-212, A498, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.798×** | -3.3 | 0.047 | 18/48 (KATO III, LS 180, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.737×** | -3.2 | 0.069 | 16/46 (LS 180, A498, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.721×** | -3.1 | 0.069 | 14/47 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.563×** | -3.1 | 0.069 | 12/46 (A-427, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.564×** | -3.1 | 0.069 | 11/47 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.02 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12522. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 50.7 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.279× (z -14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0409× (z -13.0) |
| [[A498 (line)]] | wt | 12.4 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.142× (z -15.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -12.5) |
| [[SW480 (line)]] | alt | 35.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -17.3) |
| [[LS 180 (line)]] | wt | 9.19 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.173× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0735× (z -13.5) |
| [[SW48 (line)]] | wt | 14.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0558× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 33.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -11.2) |
| [[SNU-1 (line)]] | wt | 9.26 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0579× (z -9.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12522), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPU]] | +0.85 | +0.81 / +0.86 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 564 |
| [[EXO1]] | +0.84 | +0.79 / +0.86 | both halves | 7e-06 | STRING 739 |
| [[HAUS1]] | +0.84 | +0.77 / +0.81 | both halves | 7e-06 | STRING 418 |
| [[DSCC1]] | +0.83 | +0.77 / +0.83 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 856 |
| [[WDHD1]] | +0.82 | +0.78 / +0.84 | both halves | 7e-06 | STRING 737 |
| [[RRM1]] | +0.82 | +0.81 / +0.82 | both halves | 7e-06 | STRING 775 |
| [[POLQ]] | +0.81 | +0.77 / +0.82 | both halves | 7e-06 |  |
| [[BLM]] | +0.80 | +0.72 / +0.82 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 545 |
| [[FANCB]] | +0.80 | +0.72 / +0.80 | both halves | 7e-06 |  |
| [[FANCI]] | +0.80 | +0.77 / +0.78 | both halves | 7e-06 | STRING 526 |
| [[MMS22L]] | +0.80 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[DTL]] | +0.80 | +0.73 / +0.85 | both halves | 7e-06 | STRING 434 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises PRIM1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.92× lower at baseline in the lines without E2F2 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDCA7L]] | B | CDCA7L activity raises PRIM1's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.49× lower at baseline in the lines without CDCA7L | 0.058 | ⚠ within organs, on part of the lines |
| [[TCF19]] | B | TCF19 activity raises PRIM1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without TCF19 | 0.069 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises PRIM1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.67× lower at baseline in the lines without FAM111B | 0.073 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises PRIM1's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.11× lower at baseline in the lines without CDCA7 | 0.085 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises PRIM1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.36× lower at baseline in the lines without MCM10 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.848). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.9, -44.7); signed map (-36.1, -41.9). **Vector** length 105, 27.6% of its response variance represented; |z| ≥ 3 in 904 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.63 to 65); *E2F G1/S* (control, mean cos +0.65 to 23); *Cell Cycle Checkpoints* (reactome, mean cos +0.66 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +3.2 | +3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.1 | +5.7 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~88% of this change | +2.9 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +2.9 | +3.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +3.9 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.0 | +3.0 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.9 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -7.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.7 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -4.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.6 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.6 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | DNA primase subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,730,438-56,752,374 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | DNA primases; DNA primase complex subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 26 pathways, smallest: DNA replication initiation; Inhibition of replication initiation of damaged DNA by RB1/E2F1; Telomere C-strand synthesis initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [P49642](https://www.uniprot.org/uniprotkb/P49642) (DNA primase small subunit):

> Catalytic subunit of the DNA primase complex and component of the DNA polymerase alpha complex (also known as the alpha DNA polymerase-primase complex - primosome/replisome) which play an essential role in the initiation of DNA synthesis. During the S phase of the cell cycle, the DNA polymerase alpha complex (composed of a catalytic subunit POLA1, an accessory subunit POLA2 and two primase subunits, the catalytic subunit PRIM1 and the regulatory subunit PRIM2) is recruited to DNA at the …

**Summary**, from NCBI Gene [5557](https://www.ncbi.nlm.nih.gov/gene/5557):

> The replication of DNA in eukaryotic cells is carried out by a complex chromosomal replication apparatus, in which DNA polymerase alpha and primase are two key enzymatic components. Primase, which is a heterodimer of a small subunit and a large subunit, synthesizes small RNA primers for the Okazaki fragments made during discontinuous DNA replication. The protein encoded by this gene is the small, 49 kDa primase subunit. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9369](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9369) · Entrez [5557](https://www.ncbi.nlm.nih.gov/gene/5557) · UniProt [P49642](https://www.uniprot.org/uniprotkb/P49642) · Ensembl [ENSG00000198056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198056)

## Data

Gene col 12522: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12522); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12522, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12522]; `tensor/DDL_lfc|DDL_z.npy` [12522]; `embed/gene_vectors.npy` [12522]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12522 or target_col == 12522). Every well: [[PRIM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRIM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
