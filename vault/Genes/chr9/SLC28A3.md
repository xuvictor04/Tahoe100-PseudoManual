---
symbol: "SLC28A3"
type: "gene"
col: 12409
ensembl_id: "ENSG00000197506"
name: "solute carrier family 28 member 3"
location: "9q21.32-q21.33"
module: 8
arm: "+"
pooled_cpm: 3.5
n_lines_expressing: 16
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 77
direction_downstream: 93
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SLC28A3

*solute carrier family 28 member 3* — 9q21.32-q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.79× (z +12.8, q 1e-34, up in 2 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +6.9, q 6e-10, up in 2 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.536× (z -5.1, q 2e-04, down in 10 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LS 180 0.0724×, KATO III 0.0655×, COLO 205 0.0539×, BT-474 0.105×); [[Auranofin (drug)]] 5 µM in 2 lines (Panc 03.27 0.0230×, BT-474 0.0186×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (BT-474 0.0230×, NCI-H1573 0.0305×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM45B]] (+0.75, fdr 7e-06), [[ITGB6]] (+0.75, fdr 7e-06), [[CATSPERB]] (+0.72, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 77 arrows point to it, the strongest [[SERPINB7]] → it (grade B ⚠); 93 go from it, the strongest it → [[PROM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.79×** | +12.8 | 1e-34 | 2/9 (LOX-IMVI, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.71×** | +12.2 | 1e-31 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.60×** | +9.7 | 8e-20 | 2/7 (Panc 03.27, KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +6.9 | 6e-10 | 2/13 (SNU-423, J82) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +6.8 | 1e-09 | 2/13 (HS-578T, SNU-423) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.97×** | +6.4 | 2e-08 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +5.1 | 3e-05 | 1/10 (HS-578T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.01×** | +4.7 | 2e-04 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.3 | 9e-04 | 2/9 (KATO III, LOX-IMVI) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.68×** | +4.2 | 0.001 | 0/9 | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.8 | 0.006 | 1/12 (HS-578T) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +3.5 | 0.024 | 0/7 | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.4 | 0.024 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.024 | 1/14 (HS-578T) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.027 | 3/14 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.75×** | +3.3 | 0.037 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.46×** | +3.1 | 0.060 | 2/14 (NCI-H2347, BT-474) | inconsistent across doses |  |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.094 | 0/13 | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.43×** | +2.9 | 0.094 | 0/10 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12409.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LS 180 0.0724×, KATO III 0.0655×, COLO 205 0.0539×, BT-474 0.105×); [[Auranofin (drug)]] 5 µM in 2 lines (Panc 03.27 0.0230×, BT-474 0.0186×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (BT-474 0.0230×, NCI-H1573 0.0305×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.536×** | -5.1 | 2e-04 | 10/14 (BT-474, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Ipatasertib (drug)]] 5 µM |  | **0.406×** | -3.9 | 0.032 | 3/14 (BT-474, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.656× | -3.5 | 0.10 | 7/14 (NCI-H1573, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.674× | -3.2 | 0.17 | 2/14 (HS-578T, J82) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.690× | -3.0 | 0.27 | 11/14 (BT-474, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 32.4 | 0 | 19 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0181× (z -16.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0186× (z -15.9) |
| [[COLO 205 (line)]] | alt | 25.6 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0539× (z -15.4) |
| [[HT-29 (line)]] | alt | 28.5 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -12.4) |
| [[LS 180 (line)]] | wt | 16.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0724× (z -16.6) |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0305× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0230× (z -16.1) |
| [[KATO III (line)]] | alt | 14.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0655× (z -15.7) |
| [[A-172 (line)]] | wt | 0.856 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.395 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.728 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.875 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.356 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM45B]] | +0.75 | +0.69 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ITGB6]] | +0.75 | +0.70 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[CATSPERB]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CEACAM5]] | +0.70 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[LGALS9]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[CDH3]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[TMC5]] | +0.66 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[SMIM31]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[HSH2D]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ADCY4]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SLC44A4]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 | pathway: SLC-mediated transmembrane transport |
| [[TC2N]] | +0.63 | +0.64 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 12, C 65. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB7]] | B | SERPINB7 activity raises SLC28A3's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 1.67× lower at baseline in the lines without SERPINB7 | 0.034 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[TMC4]] | B | TMC4 activity raises SLC28A3's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 1.93× lower at baseline in the lines without TMC4 | 0.046 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[ELF3]] | B | ELF3 activity raises SLC28A3's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.10× lower at baseline in the lines without ELF3 | 0.050 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[XDH]] | B | XDH activity raises SLC28A3's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.32× lower at baseline in the lines without XDH | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[PROM2]] | B | PROM2 activity raises SLC28A3's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 2.16× lower at baseline in the lines without PROM2 | 0.067 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[MUC3A]] | B | MUC3A activity raises SLC28A3's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 1.82× lower at baseline in the lines without MUC3A | 0.074 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[SRMS]] | B | SRMS activity raises SLC28A3's level | lines that do not express SRMS (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without SRMS | 0.076 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[ARHGAP30]] | B | ARHGAP30 activity raises SLC28A3's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 2.32× lower at baseline in the lines without ARHGAP30 | 0.077 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[SPINT1]] | B | SPINT1 activity raises SLC28A3's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 2.31× lower at baseline in the lines without SPINT1 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[LRATD2]] | B | LRATD2 activity raises SLC28A3's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 2.02× lower at baseline in the lines without LRATD2 | 0.082 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[POU5F1B]] | B | POU5F1B activity raises SLC28A3's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 1.88× lower at baseline in the lines without POU5F1B | 0.083 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[NSUN7]] | B | NSUN7 activity raises SLC28A3's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 1.72× lower at baseline in the lines without NSUN7 | 0.083 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent |

### Downstream of this gene

*93 arrows, 93 of them with an alert ⚠; grade A 0, B 31, C 62. Shown: the 12 strongest; 81 more arrows (81 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PROM2]] | B | SLC28A3 activity raises PROM2's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.52× lower at baseline in the lines without SLC28A3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[ARHGAP30]] | B | SLC28A3 activity raises ARHGAP30's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.53× lower at baseline in the lines without SLC28A3 | 0.003 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[FAM83E]] | B | SLC28A3 activity raises FAM83E's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.52× lower at baseline in the lines without SLC28A3 | 0.003 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[LRATD2]] | B | SLC28A3 activity raises LRATD2's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.30× lower at baseline in the lines without SLC28A3 | 0.005 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[CARD14]] | B | SLC28A3 activity raises CARD14's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 1.94× lower at baseline in the lines without SLC28A3 | 0.007 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[XDH]] | B | SLC28A3 activity raises XDH's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.31× lower at baseline in the lines without SLC28A3 | 0.010 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[TMC4]] | B | SLC28A3 activity raises TMC4's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 1.92× lower at baseline in the lines without SLC28A3 | 0.014 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[OCLN]] | B | SLC28A3 activity raises OCLN's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.09× lower at baseline in the lines without SLC28A3 | 0.016 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[ELF3]] | B | SLC28A3 activity raises ELF3's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.28× lower at baseline in the lines without SLC28A3 | 0.017 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[SPINT1]] | B | SLC28A3 activity raises SPINT1's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.93× lower at baseline in the lines without SLC28A3 | 0.019 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[KLHL2P1]] | B | SLC28A3 activity raises KLHL2P1's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 1.60× lower at baseline in the lines without SLC28A3 | 0.019 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[PCAT1]] | B | SLC28A3 activity raises PCAT1's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 1.88× lower at baseline in the lines without SLC28A3 | 0.020 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.6, 56.4); signed map (59.4, 7.4). **Vector** length 55.9, 18.1% of its response variance represented; |z| ≥ 3 in 459 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +1.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -0.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -3.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 28 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.32-q21.33 — chr9:84,275,457-84,340,758 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CNT3 |
| Gene groups (HGNC) | Solute carrier family 28 |
| Reactome | 7 pathways, smallest: Ribavirin ADME; Transport of nucleosides and free purine and pyrimidine bases across the plasma membrane; Azathioprine ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAS3](https://www.uniprot.org/uniprotkb/Q9HAS3) (Solute carrier family 28 member 3):

> Sodium-dependent, pyrimidine- and purine-selective. Involved in the homeostasis of endogenous nucleosides. Exhibits the transport characteristics of the nucleoside transport system cib or N3 subtype (N3/cib) (with marked transport of both thymidine and inosine). Employs a 2:1 sodium/nucleoside ratio. Transports uridine. Also able to transport gemcitabine, 3'-azido-3'-deoxythymidine (AZT), ribavirin and 3-deazauridine.

**Summary**, from NCBI Gene [64078](https://www.ncbi.nlm.nih.gov/gene/64078):

> Nucleoside transporters, such as SLC28A3, regulate multiple cellular processes, including neurotransmission, vascular tone, adenosine concentration in the vicinity of cell surface receptors, and transport and metabolism of nucleoside drugs. SLC28A3 shows broad specificity for pyrimidine and purine nucleosides (Ritzel et al., 2001 [PubMed 11032837]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:16484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16484) · Entrez [64078](https://www.ncbi.nlm.nih.gov/gene/64078) · UniProt [Q9HAS3](https://www.uniprot.org/uniprotkb/Q9HAS3) · Ensembl [ENSG00000197506](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197506)

## Data

Gene col 12409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12409); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12409]; `tensor/DDL_lfc|DDL_z.npy` [12409]; `embed/gene_vectors.npy` [12409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12409 or target_col == 12409). Every well: [[SLC28A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC28A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
