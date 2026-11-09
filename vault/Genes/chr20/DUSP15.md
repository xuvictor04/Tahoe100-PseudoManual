---
symbol: "DUSP15"
type: "gene"
col: 7396
ensembl_id: "ENSG00000149599"
name: "dual specificity phosphatase 15"
location: "20q11.21"
module: 94
arm: "+"
pooled_cpm: 2.22
n_lines_expressing: 35
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 9
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# DUSP15

*dual specificity phosphatase 15* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 7.40× (z +18.8, q 0e+00, up in 28 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.427× (z -5.7, q 9e-06, down in 18 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (J82 0.0427×); [[Digitoxin (drug)]] 0.05 µM in 1 line (PANC-1 0.0412×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0489×; ⚠ cell-cycle shift, explains ~59% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK32A]] (+0.75, fdr 7e-06), [[TRPM4]] (+0.73, fdr 3e-05), [[NGFR]] (+0.72, fdr 7e-06); moves opposite to [[ILF2]] (-0.54, fdr 2e-04), [[CHID1]] (-0.52, fdr 3e-05), [[ADAM10]] (-0.51, fdr 6e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ZNF442]] → it (grade B ⚠); 9 go from it, the strongest it → [[RRAGD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7396.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **7.40×** | +18.8 | 0e+00 | 28/30 (SW1417, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.08×** | +15.3 | 0e+00 | 18/23 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **8.85×** | +14.5 | 3e-45 | 29/31 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **8.22×** | +14.0 | 3e-42 | 24/24 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **5.31×** | +11.1 | 2e-26 | 23/26 (PANC-1, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **4.19×** | +9.1 | 6e-18 | 20/26 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.24×** | +7.5 | 5e-12 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.43×** | +5.9 | 3e-07 | 12/23 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +5.0 | 4e-05 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.01×** | +4.6 | 2e-04 | 13/29 (SW1417, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +3.4 | 0.037 | 4/26 (PANC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Osimertinib (mesylate) (drug)]] 0.5 µM |  | **1.65×** | +3.3 | 0.043 | 6/26 (A-172, LoVo, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +3.1 | 0.078 | 1/8 (A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7396.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (J82 0.0427×); [[Digitoxin (drug)]] 0.05 µM in 1 line (PANC-1 0.0412×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0489×; ⚠ cell-cycle shift, explains ~59% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.427×** | -5.7 | 9e-06 | 18/25 (J82, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.590× | -3.5 | 0.13 | 6/22 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7396. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.22 | 3 | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 11.0× (z +11.8) | [[Digitoxin (drug)]] 0.05 µM 0.0412× (z -11.0) |
| [[SW1417 (line)]] | alt | 15.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +19.0) | — |
| [[SW480 (line)]] | alt | 5.50 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.49× (z +13.7) | — |
| [[A-172 (line)]] | wt | 3.66 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +8.7) | — |
| [[J82 (line)]] | alt | 7.30 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +10.9) | [[Digitoxin (drug)]] 0.5 µM 0.0427× (z -12.9) |
| [[HepG2_C3A (line)]] | wt | 1.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.1× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 5.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.66× (z +9.5) | — |
| [[A-427 (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.302 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.744 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.653 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.837 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.829 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.741 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.616 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.587 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.684 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.674 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.275 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.313 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7396), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK32A]] | +0.75 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[TRPM4]] | +0.73 | +0.43 / +0.86 | both halves | 3e-05 |  |
| [[NGFR]] | +0.72 | +0.59 / +0.80 | both halves | 7e-06 |  |
| [[PCLO]] | +0.69 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[TATDN3]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[ZNF433]] | +0.69 | +0.57 / +0.78 | both halves | 9e-06 |  |
| [[SLC44A2]] | +0.68 | +0.50 / +0.78 | both halves | 1e-05 |  |
| [[ZNF44]] | +0.68 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[ZNF442]] | +0.67 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[NUDT16]] | +0.65 | +0.57 / +0.73 | both halves | 9e-06 |  |
| [[SDSL]] | +0.65 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[SLC43A2]] | +0.63 | +0.52 / +0.77 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILF2]] | -0.54 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[CHID1]] | -0.52 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ADAM10]] | -0.51 | -0.62 / -0.38 | both halves | 6e-05 |  |
| [[PGP]] | -0.51 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[NIPA2]] | -0.51 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TBC1D4]] | -0.50 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF442]] | B | ZNF442 activity raises DUSP15's level | lines that do not express ZNF442 (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without ZNF442 | 0.046 | ⚠ within organs, on part of the lines; also absent: ZNF563, ENSG00000286098, ENSG00000268870 |
| [[ZNF563]] | B | ZNF563 activity raises DUSP15's level | lines that do not express ZNF563 (9) vs lines expressing it (41) | 1.74× lower at baseline in the lines without ZNF563 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF442, ZNF433, ENSG00000269755 |
| [[ZNF441]] | B | ZNF441 activity raises DUSP15's level | lines that do not express ZNF441 (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without ZNF441 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000286098, ZNF442, ZNF433 |
| [[ZSCAN12]] | B | ZSCAN12 activity raises DUSP15's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.78× lower at baseline in the lines without ZSCAN12 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[ZNF433]] | B | ZNF433 activity raises DUSP15's level | lines that do not express ZNF433 (8) vs lines expressing it (42) | 2.04× lower at baseline in the lines without ZNF433 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF563, ZNF442 |
| [[NGFR]] | C | NGFR activity raises DUSP15's level | lines that do not express NGFR (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without NGFR | 0.004 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRAGD]] | B | DUSP15 activity raises RRAGD's level | lines that do not express DUSP15 (15) vs lines expressing it (35) | 2.73× lower at baseline in the lines without DUSP15 | 0.017 | ⚠ within organs, on part of the lines; also absent: DLK2, ETNK2, C11orf96 |
| [[ZNF442]] | B | DUSP15 activity raises ZNF442's level | lines that do not express DUSP15 (15) vs lines expressing it (35) | 1.87× lower at baseline in the lines without DUSP15 | 0.062 | ⚠ within organs, on part of the lines; also absent: DLK2, ETNK2, C11orf96 |
| [[ZNF182]] | B | DUSP15 activity raises ZNF182's level | lines that do not express DUSP15 (15) vs lines expressing it (35) | 1.45× lower at baseline in the lines without DUSP15 | 0.069 | ⚠ within organs, on part of the lines; also absent: DLK2, ETNK2, C11orf96 |
| [[TPPP]] | B | DUSP15 activity raises TPPP's level | lines that do not express DUSP15 (15) vs lines expressing it (35) | 1.36× lower at baseline in the lines without DUSP15 | 0.084 | ⚠ within organs, on part of the lines; also absent: DLK2, ETNK2, C11orf96 |
| [[ZNF138]] | B | DUSP15 activity raises ZNF138's level | lines that do not express DUSP15 (15) vs lines expressing it (35) | 1.18× lower at baseline in the lines without DUSP15 | 0.085 | ⚠ within organs, on part of the lines; also absent: DLK2, ETNK2, C11orf96 |
| [[ZNF441]] | B | DUSP15 activity raises ZNF441's level | lines that do not express DUSP15 (15) vs lines expressing it (35) | 1.67× lower at baseline in the lines without DUSP15 | 0.090 | ⚠ within organs, on part of the lines; also absent: DLK2, ETNK2, C11orf96 |
| [[SEC62]] | B | DUSP15 activity weakens SEC62's drug response | lines that do not express DUSP15 (15) vs lines expressing it (34) | the lines without DUSP15 respond 1.24× as strongly (z diff -0.74); strongest at Ouabain (Octahydrate) 5 µM: 1.66x vs 1.37x (z diff -2.0) | 0.096 | ⚠ within organs, on part of the lines; also absent: DLK2, ETNK2, C11orf96; target measured in part of the lines; artifact flags |
| [[CERS4]] | C | DUSP15 activity raises CERS4's level | lines that do not express DUSP15 (15) vs lines expressing it (35) | 3.62× lower at baseline in the lines without DUSP15 | 0.031 | ⚠ within organs, on part of the lines; also absent: DLK2, ETNK2, C11orf96; co-absent with the target |
| [[NGFR]] | C | DUSP15 activity raises NGFR's level | lines that do not express DUSP15 (15) vs lines expressing it (35) | 3.68× lower at baseline in the lines without DUSP15 | 0.052 | ⚠ within organs, on part of the lines; also absent: DLK2, ETNK2, C11orf96; co-absent with the target |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.844). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.5, 24.5); signed map (14.8, -16.2). **Vector** length 65.3, 15.2% of its response variance represented; |z| ≥ 3 in 696 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.3 | +18.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.1 | +14.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +15.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.2 | +14.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +9.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.6 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -5.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -0.3 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:31,847,637-31,870,664 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA243J16.6, VHY, FLJ20645, bA243J16.5; previously C20orf57 |
| Gene groups (HGNC) | Atypical dual specificity phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1R2](https://www.uniprot.org/uniprotkb/Q9H1R2) (Dual specificity protein phosphatase 15):

> May dephosphorylate MAPK13, ATF2, ERBB3, PDGFRB and SNX6.; [Isoform 3]: May play a role in the regulation of oligodendrocyte differentiation. May play a role in the regulation of myelin formation (By similarity). Involved in the regulation of Erk1/2 phosphorylation in Schwann cells; the signaling may be linked to the regulation of myelination (By similarity).

**Summary**, from NCBI Gene [128853](https://www.ncbi.nlm.nih.gov/gene/128853):

> The protein encoded by this gene has both protein-tyrosine phophatase activity and serine/threonine-specific phosphatase activity, and therefore is known as a dual specificity phosphatase. This protein may function in the differentiation of oligodendrocytes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:16236](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16236) · Entrez [128853](https://www.ncbi.nlm.nih.gov/gene/128853) · UniProt [Q9H1R2](https://www.uniprot.org/uniprotkb/Q9H1R2) · Ensembl [ENSG00000149599](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149599)

## Data

Gene col 7396: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7396); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7396, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7396]; `tensor/DDL_lfc|DDL_z.npy` [7396]; `embed/gene_vectors.npy` [7396]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7396 or target_col == 7396). Every well: [[DUSP15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
