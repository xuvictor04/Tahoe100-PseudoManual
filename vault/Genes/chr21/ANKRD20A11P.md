---
symbol: "ANKRD20A11P"
type: "gene"
col: 13269
ensembl_id: "ENSG00000215559"
name: "ankyrin repeat domain 20 family member A11, pseudogene"
location: "21q11.2"
module: 10
arm: "+"
pooled_cpm: 4.35
n_lines_expressing: 21
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 10
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ANKRD20A11P

*ankyrin repeat domain 20 family member A11, pseudogene* — 21q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.75× (z +13.5, q 7e-39, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.81× (z +13.2, q 3e-37, up in 5 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.604× (z -4.6, q 0.003, down in 8 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 2 lines (A-427 0.128×, HEC-1-A 0.196×); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.359×, HEC-1-A 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.421×); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 0.391×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD20A21P]] (+0.73, fdr 7e-06), [[LINC00466]] (+0.55, fdr 3e-05), [[FAM66C]] (+0.55, fdr 5e-05); moves opposite to [[PIGN]] (-0.44, fdr 2e-04), [[UBAC2]] (-0.42, fdr 4e-04), [[ULK4]] (-0.41, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[HES2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13269.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.75×** | +13.5 | 7e-39 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +13.2 | 3e-37 | 5/11 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.73×** | +12.8 | 2e-35 | 8/13 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.84×** | +12.1 | 1e-31 | 1/7 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.65×** | +10.8 | 4e-25 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +7.4 | 2e-11 | 9/17 (BT-474, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +7.0 | 2e-10 | 6/11 (A549, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.4 | 4e-06 | 4/8 (A549, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.21×** | +5.1 | 2e-05 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +5.1 | 2e-05 | 5/13 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.0 | 3e-05 | 3/17 (A549, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +4.9 | 4e-05 | 6/12 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.67×** | +4.6 | 2e-04 | 0/5 | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.61×** | +4.5 | 2e-04 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +4.5 | 3e-04 | 4/17 (BT-474, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.001 | 3/14 (BT-474, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +4.2 | 0.001 | 7/14 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.56×** | +4.0 | 0.002 | 1/9 (A-427) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.018 | 7/15 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.038 | 2/17 (SW 900, A549) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.38×** | +2.9 | 0.093 | 0/15 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13269.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 2 lines (A-427 0.128×, HEC-1-A 0.196×); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.359×, HEC-1-A 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.421×); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 0.391×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.604×** | -4.6 | 0.003 | 8/16 (PANC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | **0.659×** | -3.8 | 0.047 | 1/17 (SW1417) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.698× | -3.2 | 0.17 | 2/17 (A549, CHP-212) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.776× | -3.2 | 0.17 | 1/17 (PANC-1) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -11.1) |
| [[A-427 (line)]] | wt | 12.5 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.128× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.196× (z -8.5) |
| [[A549 (line)]] | wt | 7.77 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +8.5) | — |
| [[A-172 (line)]] | wt | 0.441 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.410 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.926 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.568 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.811 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.568 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD20A21P]] | +0.73 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[LINC00466]] | +0.55 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[FAM66C]] | +0.55 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[SMC1B]] | +0.54 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[ABCA17P]] | +0.52 | +0.54 / +0.34 | both halves | 1e-04 |  |
| [[ACKR2]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[SLC6A17]] | +0.51 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[CFL1P1-1]] | +0.50 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[ZNF536]] | +0.49 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[KATNAL2]] | +0.49 | +0.59 / +0.31 | both halves | 2e-04 |  |
| [[ITGB2]] | +0.49 | +0.47 / +0.13 | ⚠ not reproduced | 0.002 |  |
| [[CHRNA7]] | +0.48 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[ANKRD20A5P]] | +0.48 | +0.55 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGN]] | -0.44 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[UBAC2]] | -0.42 | -0.46 / -0.26 | both halves | 4e-04 |  |
| [[ULK4]] | -0.41 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[BLTP2]] | -0.41 | -0.47 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANKRD20A11P's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SYCP2]] | B | SYCP2 activity raises ANKRD20A11P's level | lines that do not express SYCP2 (15) vs lines expressing it (35) | 1.97× lower at baseline in the lines without SYCP2 | 0.049 | ⚠ within organs, on part of the lines; also absent: AMOT, LINC00937, DMBX1; maybe low, not absent |
| [[ABCA17P]] | B | ABCA17P activity raises ANKRD20A11P's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.93× lower at baseline in the lines without ABCA17P | 0.064 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[ANKRD20A21P]] | C | ANKRD20A21P activity raises ANKRD20A11P's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 2.31× lower at baseline in the lines without ANKRD20A21P | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P; co-absent with the target |
| [[ANKRD20A7P]] | C | ANKRD20A7P activity raises ANKRD20A11P's level | lines that do not express ANKRD20A7P (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without ANKRD20A7P | 0.072 | ⚠ within organs, on part of the lines; also absent: BNC1, MAGEA1, ENSG00000275649; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES2]] | B | ANKRD20A11P activity raises HES2's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 1.54× lower at baseline in the lines without ANKRD20A11P | 0.019 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P |
| [[ZMAT1]] | B | ANKRD20A11P activity raises ZMAT1's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 2.26× lower at baseline in the lines without ANKRD20A11P | 0.044 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P |
| [[FAM66C]] | B | ANKRD20A11P activity raises FAM66C's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 1.76× lower at baseline in the lines without ANKRD20A11P | 0.048 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P |
| [[LINC02026]] | B | ANKRD20A11P activity raises LINC02026's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 1.34× lower at baseline in the lines without ANKRD20A11P | 0.056 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P |
| [[GCAWKR]] | B | ANKRD20A11P activity raises GCAWKR's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 1.39× lower at baseline in the lines without ANKRD20A11P | 0.067 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P |
| [[LINC00466]] | B | ANKRD20A11P activity raises LINC00466's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 1.59× lower at baseline in the lines without ANKRD20A11P | 0.080 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P |
| [[LRRC36]] | B | ANKRD20A11P activity raises LRRC36's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 1.74× lower at baseline in the lines without ANKRD20A11P | 0.092 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P |
| [[ANKRD20A21P]] | C | ANKRD20A11P activity raises ANKRD20A21P's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 1.82× lower at baseline in the lines without ANKRD20A11P | 0.013 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P; co-absent with the target |
| [[RASGEF1A]] | C | ANKRD20A11P activity raises RASGEF1A's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 1.86× lower at baseline in the lines without ANKRD20A11P | 0.027 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P; co-absent with the target |
| [[CHRNA7]] | C | ANKRD20A11P activity raises CHRNA7's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 2.32× lower at baseline in the lines without ANKRD20A11P | 0.065 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.398). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.5, 30.9); signed map (36.8, -9.5). **Vector** length 29.0, 5.13% of its response variance represented; |z| ≥ 3 in 414 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +13.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +4.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.1 | -4.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -0.9 | -0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.8 | -1.4 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.8 | -1.4 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.7 | -2.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 20 family member A11, pseudogene |
| Locus type | pseudogene |
| Location | 21q11.2 — chr21:13,909,574-13,979,911 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously C21orf81 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42024) · Entrez [391267](https://www.ncbi.nlm.nih.gov/gene/391267) · Ensembl [ENSG00000215559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215559)

## Data

Gene col 13269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13269); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13269]; `tensor/DDL_lfc|DDL_z.npy` [13269]; `embed/gene_vectors.npy` [13269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13269 or target_col == 13269). Every well: [[ANKRD20A11P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD20A11P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
