---
symbol: "INAVA"
type: "gene"
col: 8676
ensembl_id: "ENSG00000163362"
name: "innate immunity activator"
location: "1q32.1"
module: 8
arm: "+"
pooled_cpm: 12.26
n_lines_expressing: 21
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 119
direction_downstream: 174
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# INAVA

*innate immunity activator* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +10.1, q 2e-21, up in 4 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.604× (z -6.5, q 4e-08, down in 17 of 19 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (HT-29 0.137×, KATO III 0.154×, CFPAC-1 0.204×, SW1417 0.300×, …); [[Homoharringtonine (drug)]] 5 µM in 6 lines (HT-29 0.159×, COLO 205 0.174×, KATO III 0.268×, CFPAC-1 0.348×, …); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (CFPAC-1 0.0755×, KATO III 0.0707×, HEC-1-A 0.0914×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPS8L3]] (+0.78, fdr 7e-06), [[ST14]] (+0.77, fdr 7e-06), [[OCLN]] (+0.76, fdr 7e-06); moves opposite to [[ST3GAL3]] (-0.57, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 119 arrows point to it, the strongest [[TTC28]] → it (grade B ⚠); 174 go from it, the strongest it → [[ANXA11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +10.1 | 2e-21 | 4/19 (A549, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +8.8 | 5e-16 | 3/19 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +8.2 | 4e-14 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +7.5 | 7e-12 | 1/18 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.45×** | +6.8 | 1e-09 | 7/19 (SW480, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +6.6 | 3e-09 | 1/18 (NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +3.9 | 0.008 | 9/19 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +3.9 | 0.008 | 12/19 (HEC-1-A, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +3.8 | 0.008 | 0/17 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.008 | 3/19 (AsPC-1, A498, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.025 | 1/18 (NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.039 | 1/19 (RPMI-7951) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.28×** | +3.2 | 0.051 | 5/19 (LS 180, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.30×** | +3.2 | 0.051 | 3/19 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.0 | 0.086 | 3/18 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8676.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (HT-29 0.137×, KATO III 0.154×, CFPAC-1 0.204×, SW1417 0.300×, …); [[Homoharringtonine (drug)]] 5 µM in 6 lines (HT-29 0.159×, COLO 205 0.174×, KATO III 0.268×, CFPAC-1 0.348×, …); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (CFPAC-1 0.0755×, KATO III 0.0707×, HEC-1-A 0.0914×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.604×** | -6.5 | 4e-08 | 17/19 (HT-29, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.611×** | -6.4 | 5e-08 | 16/19 (HT-29, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.757×** | -3.6 | 0.059 | 12/19 (COLO 205, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.766×** | -3.5 | 0.077 | 5/19 (SW480, SW48, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.766×** | -3.3 | 0.100 | 12/19 (HT-29, COLO 205, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 47.9 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0755× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -16.4) |
| [[HT-29 (line)]] | alt | 65.2 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0225× (z -28.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -21.9) |
| [[LoVo (line)]] | wt | 45.2 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -12.3) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -11.1) |
| [[KATO III (line)]] | alt | 44.2 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -17.3) |
| [[COLO 205 (line)]] | alt | 44.1 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -12.8) |
| [[LS 180 (line)]] | wt | 37.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0978× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 24.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -9.2) |
| [[SW1417 (line)]] | alt | 33.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 19.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0914× (z -15.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 23.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -9.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0841× (z -9.0) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -8.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0831× (z -12.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.992 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.749 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.865 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPS8L3]] | +0.78 | +0.85 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ST14]] | +0.77 | +0.70 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[OCLN]] | +0.76 | +0.68 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CDH1]] | +0.74 | +0.61 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L1]] | +0.74 | +0.77 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS2]] | +0.72 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[SPINT1]] | +0.72 | +0.72 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CLIC5]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[TMC4]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[C1orf116]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[CRYBG2]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[MYO7B]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL3]] | -0.57 | -0.62 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*119 arrows, 119 of them with an alert ⚠; grade A 0, B 20, C 99. Shown: the 12 strongest; 107 more arrows (107 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC28]] | B | TTC28 activity lowers INAVA's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 8.47× higher at baseline in the lines without TTC28 | 5e-04 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[LINC03041]] | B | LINC03041 activity lowers INAVA's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 6.54× higher at baseline in the lines without LINC03041 | 0.002 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[DCLK2]] | B | DCLK2 activity lowers INAVA's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 6.84× higher at baseline in the lines without DCLK2 | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[EPS8L1]] | B | EPS8L1 activity raises INAVA's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.69× lower at baseline in the lines without EPS8L1 | 0.009 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises INAVA's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.92× lower at baseline in the lines without SLC44A3 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[SEMA3B]] | B | SEMA3B activity raises INAVA's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.74× lower at baseline in the lines without SEMA3B | 0.016 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[GRAMD2B]] | B | GRAMD2B activity raises INAVA's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 3.76× lower at baseline in the lines without GRAMD2B | 0.017 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[MYO1D]] | B | MYO1D activity raises INAVA's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 3.77× lower at baseline in the lines without MYO1D | 0.022 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[BNC2]] | B | BNC2 activity lowers INAVA's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 4.66× higher at baseline in the lines without BNC2 | 0.025 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[GRHL3]] | B | GRHL3 activity raises INAVA's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 2.99× lower at baseline in the lines without GRHL3 | 0.037 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises INAVA's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 3.01× lower at baseline in the lines without TJP2 | 0.038 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[FBLIM1]] | B | FBLIM1 activity raises INAVA's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 2.94× lower at baseline in the lines without FBLIM1 | 0.044 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |

### Downstream of this gene

*174 arrows, 174 of them with an alert ⚠; grade A 0, B 71, C 103. Shown: the 12 strongest; 162 more arrows (162 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA11]] | B | INAVA activity raises ANXA11's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.24× lower at baseline in the lines without INAVA | 4e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[PTK2B]] | B | INAVA activity raises PTK2B's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.41× lower at baseline in the lines without INAVA | 6e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[EPS8L1]] | B | INAVA, [[MROH3P]] activity raises EPS8L1's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 3.97× lower at baseline in the lines without INAVA, MROH3P | 8e-05 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[TLDC2]] | B | INAVA, [[MROH3P]] activity raises TLDC2's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 2.52× lower at baseline in the lines without INAVA, MROH3P | 1e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[SLC44A3]] | B | INAVA activity raises SLC44A3's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.49× lower at baseline in the lines without INAVA | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[ST3GAL3]] | B | INAVA activity lowers ST3GAL3's level | lines that do not express INAVA (29) vs lines expressing it (21) | 2.49× higher at baseline in the lines without INAVA | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[KIAA1522]] | B | INAVA activity raises KIAA1522's level | lines that do not express INAVA (29) vs lines expressing it (21) | 2.97× lower at baseline in the lines without INAVA | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[PATJ]] | B | INAVA, [[MROH3P]] activity raises PATJ's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 3.35× lower at baseline in the lines without INAVA, MROH3P | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[ITPKC]] | B | INAVA, [[MROH3P]] activity raises ITPKC's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 2.96× lower at baseline in the lines without INAVA, MROH3P | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[MYO1D]] | B | INAVA activity raises MYO1D's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.58× lower at baseline in the lines without INAVA | 5e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[MYRF]] | B | INAVA activity raises MYRF's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.67× lower at baseline in the lines without INAVA | 6e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[FAM83E]] | B | INAVA, [[MROH3P]] activity raises FAM83E's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 3.44× lower at baseline in the lines without INAVA, MROH3P | 8e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.0, 56.4); signed map (57.1, 7.6). **Vector** length 77.0, 28.5% of its response variance represented; |z| ≥ 3 in 499 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.4 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +1.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -2.2 | -3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -2.0 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -0.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | +0.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | innate immunity activator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:200,891,048-200,915,742 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10901; previously C1orf106 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3KP66](https://www.uniprot.org/uniprotkb/Q3KP66) (Innate immunity activator protein):

> Expressed in peripheral macrophages and intestinal myeloid-derived cells, is required for optimal PRR (pattern recognition receptor)-induced signaling, cytokine secretion, and bacterial clearance. Upon stimulation of a broad range of PRRs (pattern recognition receptor) such as NOD2 or TLR2, TLR3, TLR4, TLR5, TLR7 and TLR9, associates with YWHAQ/14-3-3T, which in turn leads to the recruitment and activation of MAP kinases and NF-kappa-B signaling complexes that amplifies PRR-induced downstream …

**Summary**, from NCBI Gene [55765](https://www.ncbi.nlm.nih.gov/gene/55765):

> Involved in several processes, including nucleotide-binding activity oligomerization domain containing 2 signaling pathway; positive regulation of cytokine production; and positive regulation of intracellular signal transduction. Located in cytoplasm and nuclear body. Implicated in inflammatory bowel disease 29. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25599) · Entrez [55765](https://www.ncbi.nlm.nih.gov/gene/55765) · UniProt [Q3KP66](https://www.uniprot.org/uniprotkb/Q3KP66) · Ensembl [ENSG00000163362](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163362)

## Data

Gene col 8676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8676); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8676]; `tensor/DDL_lfc|DDL_z.npy` [8676]; `embed/gene_vectors.npy` [8676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8676 or target_col == 8676). Every well: [[INAVA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INAVA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
