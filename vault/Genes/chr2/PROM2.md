---
symbol: "PROM2"
type: "gene"
col: 7865
ensembl_id: "ENSG00000155066"
name: "prominin 2"
location: "2q11.1"
module: 44
arm: "+"
pooled_cpm: 2.32
n_lines_expressing: 29
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 73
direction_downstream: 31
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PROM2

*prominin 2* — 2q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.37× (z +11.0, q 1e-25, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.44× (z +4.0, q 0.004, up in 3 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.436× (z -6.3, q 2e-07, down in 10 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC5B]] (+0.76, fdr 7e-06), [[ST6GALNAC1]] (+0.73, fdr 7e-06), [[TSPAN1]] (+0.73, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 73 arrows point to it, the strongest [[SLC28A3]] → it (grade B ⚠); 31 go from it, the strongest it → [[IQANK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7865.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.37×** | +11.0 | 1e-25 | 4/5 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +8.7 | 8e-16 | 1/5 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +7.6 | 4e-12 | 3/8 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +6.0 | 4e-07 | 3/11 (CFPAC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.10×** | +5.7 | 1e-06 | 2/9 (HEC-1-A, NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.53×** | +5.2 | 2e-05 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.74×** | +4.1 | 0.003 | 1/8 (HEC-1-A) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.004 | 3/20 (LS 180, HCT15, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.62×** | +3.9 | 0.006 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.71×** | +3.9 | 0.006 | 1/11 (LS 180) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.2 | 0.077 | 2/11 (BT-474, NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7865.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.436×** | -6.3 | 2e-07 | 10/16 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.566×** | -4.5 | 0.002 | 9/17 (BT-474, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.604×** | -4.0 | 0.014 | 11/14 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.630×** | -3.6 | 0.038 | 7/21 (COLO 205, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.636×** | -3.6 | 0.042 | 3/22 (Panc 03.27, COLO 205, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.680× | -3.0 | 0.22 | 8/18 (COLO 205, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7865. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 19.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0913× (z -15.1) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0757× (z -11.5) |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -16.5) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 6.36 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0325× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 9.81 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0462× (z -12.2) |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -9.2) ⚠ cell-cycle shift, explains ~81% of this change |
| [[CFPAC-1 (line)]] | alt | 7.21 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -13.6) ⚠ cell-cycle shift, explains ~81% of this change |
| [[HT-29 (line)]] | alt | 7.82 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0626× (z -16.2) ⚠ cell-cycle shift, explains ~81% of this change |
| [[KATO III (line)]] | alt | 3.99 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0438× (z -9.7) |
| [[A-172 (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.173 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.518 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.683 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.599 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.658 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.194 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.823 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.156 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.710 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.760 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.817 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.210 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.896 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.858 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.220 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7865), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC5B]] | +0.76 | +0.73 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ST6GALNAC1]] | +0.73 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[TSPAN1]] | +0.73 | +0.68 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[ELMO3]] | +0.70 | +0.69 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[CYP4F3]] | +0.69 | +0.60 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CYP4F12]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[BCL2L15]] | +0.69 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[SLC44A4]] | +0.69 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ITGB6]] | +0.67 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[MANSC1]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[FXYD3]] | +0.66 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[RNF183]] | +0.66 | +0.56 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*73 arrows, 73 of them with an alert ⚠; grade A 0, B 57, C 16. Shown: the 12 strongest; 61 more arrows (61 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC28A3]] | B | SLC28A3 activity raises PROM2's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.52× lower at baseline in the lines without SLC28A3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[ST6GALNAC1]] | B | ST6GALNAC1 activity raises PROM2's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 2.97× lower at baseline in the lines without ST6GALNAC1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[SIDT1]] | B | SIDT1 activity raises PROM2's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.74× lower at baseline in the lines without SIDT1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[TCN1]] | B | TCN1 activity raises PROM2's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.89× lower at baseline in the lines without TCN1 | 0.001 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[MUC5B]] | B | MUC5B activity raises PROM2's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 3.18× lower at baseline in the lines without MUC5B | 0.001 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[ITGB6]] | B | ITGB6 activity raises PROM2's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 2.94× lower at baseline in the lines without ITGB6 | 0.003 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[BSPRY]] | B | BSPRY activity raises PROM2's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 2.54× lower at baseline in the lines without BSPRY | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[ADGRF1]] | B | ADGRF1 activity raises PROM2's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 2.80× lower at baseline in the lines without ADGRF1 | 0.003 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[NECTIN4]] | B | NECTIN4 activity raises PROM2's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 2.69× lower at baseline in the lines without NECTIN4 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[P2RY2]] | B | P2RY2 activity raises PROM2's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.44× lower at baseline in the lines without P2RY2 | 0.007 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[CYP4F3]] | B | CYP4F3 activity raises PROM2's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.34× lower at baseline in the lines without CYP4F3 | 0.007 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[SLC44A4]] | B | SLC44A4 activity raises PROM2's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.59× lower at baseline in the lines without SLC44A4 | 0.007 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 19, C 12. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IQANK1]] | B | PROM2 activity raises IQANK1's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 2.53× lower at baseline in the lines without PROM2 | 0.028 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[SPINT1-AS1]] | B | PROM2 activity raises SPINT1-AS1's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 2.10× lower at baseline in the lines without PROM2 | 0.030 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[SAMD12]] | B | PROM2 activity raises SAMD12's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 3.42× lower at baseline in the lines without PROM2 | 0.033 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[KLF8]] | B | PROM2 activity raises KLF8's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 1.87× lower at baseline in the lines without PROM2 | 0.037 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[TP53I11]] | B | PROM2 activity raises TP53I11's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 2.00× lower at baseline in the lines without PROM2 | 0.038 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[SPINT1]] | B | PROM2 activity raises SPINT1's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 3.54× lower at baseline in the lines without PROM2 | 0.040 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[ELMO3]] | B | PROM2 activity raises ELMO3's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 1.69× lower at baseline in the lines without PROM2 | 0.045 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[CLDN3]] | B | PROM2 activity raises CLDN3's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 2.66× lower at baseline in the lines without PROM2 | 0.046 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[SAMD12-AS1]] | B | PROM2 activity raises SAMD12-AS1's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 2.48× lower at baseline in the lines without PROM2 | 0.050 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[SSH3]] | B | PROM2 activity raises SSH3's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 1.41× lower at baseline in the lines without PROM2 | 0.050 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[TMC4]] | B | PROM2 activity raises TMC4's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 2.49× lower at baseline in the lines without PROM2 | 0.065 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[SLC28A3]] | B | PROM2 activity raises SLC28A3's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 2.16× lower at baseline in the lines without PROM2 | 0.067 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.5, 55.7); signed map (60.2, 6.8). **Vector** length 43.1, 10.4% of its response variance represented; |z| ≥ 3 in 465 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.50 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.50 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.5 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.2 | -3.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -0.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | prominin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.1 — chr2:95,274,449-95,291,308 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Prominin family |
| Matched by | ensembl_id |

UniProt [Q8N271](https://www.uniprot.org/uniprotkb/Q8N271) carries no function annotation.

**Summary**, from NCBI Gene [150696](https://www.ncbi.nlm.nih.gov/gene/150696):

> This gene encodes a member of the prominin family of pentaspan membrane glycoproteins. The encoded protein localizes to basal epithelial cells and may be involved in the organization of plasma membrane microdomains. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:20685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20685) · Entrez [150696](https://www.ncbi.nlm.nih.gov/gene/150696) · UniProt [Q8N271](https://www.uniprot.org/uniprotkb/Q8N271) · Ensembl [ENSG00000155066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155066)

## Data

Gene col 7865: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7865); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7865, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7865]; `tensor/DDL_lfc|DDL_z.npy` [7865]; `embed/gene_vectors.npy` [7865]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7865 or target_col == 7865). Every well: [[PROM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PROM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
