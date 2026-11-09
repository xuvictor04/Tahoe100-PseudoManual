---
symbol: "SAA2-SAA4"
type: "gene"
col: 14914
ensembl_id: "ENSG00000255071"
name: "SAA2-SAA4 readthrough"
location: "11p15.1"
module: 139
arm: "+"
pooled_cpm: 7.99
n_lines_expressing: 28
n_dd_up: 53
n_dd_down: 2
n_dd_up_clean: 43
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 21
direction_downstream: 34
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# SAA2-SAA4

*SAA2-SAA4 readthrough* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 53 drug-doses (10 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 5.04× (z +13.8, q 8e-41, up in 24 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.540× (z -5.3, q 6e-05, down in 18 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Tofacitinib (drug)]] 5 µM in 3 lines (COLO 205 0.105×, A498 0.244×, SNU-423 0.150×); [[Auranofin (drug)]] 5 µM in 3 lines (A498 0.0589×, CFPAC-1 0.0490×, Panc 03.27 0.0749×); [[Ponatinib (drug)]] 5 µM in 2 lines (A498 0.0942×, COLO 205 0.111×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAA2]] (+0.98, fdr 7e-06, ⚠ same locus), [[SAA4]] (+0.97, fdr 7e-06, ⚠ same locus), [[SAA1]] (+0.92, fdr 7e-06, ⚠ same locus), [[C3]] (+0.73, fdr 7e-06), [[NNMT]] (+0.72, fdr 7e-06), [[BCL6]] (+0.69, fdr 7e-06); moves opposite to [[DPP9]] (-0.49, fdr 3e-05), [[HHIP]] (-0.48, fdr 3e-05), [[DCBLD2]] (-0.48, fdr 3e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[HLA-DRB1]] → it (grade B ⚠); 34 go from it, the strongest it → [[ZC3H12A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 53 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **5.04×** | +13.8 | 8e-41 | 24/24 (A498, J82, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.23×** | +12.3 | 2e-32 | 16/23 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | **5.27×** | +10.1 | 2e-21 | 21/24 (A498, A549, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **2.94×** | +9.2 | 5e-18 | 9/21 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.47×** | +9.1 | 1e-17 | 24/24 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.65×** | +7.8 | 5e-13 | 18/24 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.59×** | +7.7 | 9e-13 | 18/24 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM | ⚠ position correction uncertain | **3.50×** | +7.6 | 3e-12 | 16/24 (A498, SNU-423, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **2.36×** | +7.3 | 1e-11 | 16/24 (A498, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.21×** | +7.1 | 1e-10 | 16/24 (J82, A498, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **2.99×** | +6.6 | 2e-09 | 17/24 (A498, A549, …) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **3.02×** | +6.4 | 7e-09 | 15/24 (A549, A498, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.73×** | +6.1 | 6e-08 | 16/24 (A498, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **2.89×** | +5.9 | 1e-07 | 16/23 (A498, A549, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.63×** | +5.8 | 2e-07 | 13/24 (J82, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.59×** | +5.8 | 3e-07 | 16/24 (A498, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.57×** | +5.7 | 4e-07 | 14/24 (SNU-423, A498, …) | all doses, flat | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +5.6 | 5e-07 | 15/24 (A498, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14914.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Tofacitinib (drug)]] 5 µM in 3 lines (COLO 205 0.105×, A498 0.244×, SNU-423 0.150×); [[Auranofin (drug)]] 5 µM in 3 lines (A498 0.0589×, CFPAC-1 0.0490×, Panc 03.27 0.0749×); [[Ponatinib (drug)]] 5 µM in 2 lines (A498 0.0942×, COLO 205 0.111×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.540×** | -5.3 | 6e-05 | 18/24 (COLO 205, A498, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.457×** | -4.8 | 5e-04 | 15/24 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.576× | -3.4 | 0.11 | 15/24 (SNU-423, COLO 205, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.577× | -3.4 | 0.11 | 14/24 (A498, SW 900, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.588× | -3.2 | 0.12 | 12/25 (A498, COLO 205, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | 0.579× | -3.2 | 0.12 | 16/24 (SNU-423, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 60.1 | 10 (2 ⚠) | 11 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 12.2× (z +17.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0202× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0589× (z -14.0) |
| [[COLO 205 (line)]] | alt | 49.6 | 0 | 12 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.105× (z -14.1) |
| [[J82 (line)]] | alt | 12.6 | 8 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 20.7× (z +13.9) | — |
| [[SNU-423 (line)]] | alt | 33.5 | 3 (1 ⚠) | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.99× (z +9.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0553× (z -9.9) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.150× (z -9.6) |
| [[A-172 (line)]] | wt | 8.21 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +10.8) ⚠ position correction uncertain · without an alert: [[Tucidinostat (drug)]] 5 µM 18.5× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 26.2 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.18× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.0490× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 2.52 | 2 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 6.16× (z +11.3) ⚠ position not correctable · without an alert: [[Tucidinostat (drug)]] 5 µM 33.2× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 5.07 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 11.1× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0590× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[Panc 03.27 (line)]] | alt | 30.8 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0749× (z -11.2) |
| [[HT-29 (line)]] | alt | 2.41 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 91.2× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0415× (z -9.0) |
| [[SW 900 (line)]] | alt | 10.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.69× (z +8.6) | — |
| [[SW480 (line)]] | alt | 3.38 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0549× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[A-427 (line)]] | wt | 0.506 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.802 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.874 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.833 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.627 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.729 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAA2]] | +0.98 | +0.97 / +0.99 | both halves | 7e-06 | STRING 753; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SAA4]] | +0.97 | +0.97 / +0.97 | both halves | 7e-06 | STRING 703; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SAA1]] | +0.92 | +0.92 / +0.93 | both halves | 7e-06 | STRING 803; ⚠ same locus (17.6 kb: neighbours can correlate without regulation) |
| [[C3]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[NNMT]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[BCL6]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CEBPD]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[SLPI]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[C1RL]] | +0.67 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[IRAK3]] | +0.66 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[STOM]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[NAMPT]] | +0.65 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[FGA]] | +0.65 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[BIRC3]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[TLR2]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 | STRING 468 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP9]] | -0.49 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[HHIP]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[DCBLD2]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[PTHLH]] | -0.47 | -0.57 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 5, C 16. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-DRB1]] | B | HLA-DRB1 activity raises SAA2-SAA4's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.87× lower at baseline in the lines without HLA-DRB1 | 0.029 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[SH3TC1]] | B | SH3TC1 activity raises SAA2-SAA4's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.77× lower at baseline in the lines without SH3TC1 | 0.065 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[TRIM22]] | B | TRIM22 activity raises SAA2-SAA4's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.51× lower at baseline in the lines without TRIM22 | 0.068 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[TOP2A]] | B | TOP2A activity lowers SAA2-SAA4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CCL20]] | B | CCL20 activity raises SAA2-SAA4's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.34× lower at baseline in the lines without CCL20 | 0.099 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[SAA1]] | C | SAA1 activity raises SAA2-SAA4's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 4.00× lower at baseline in the lines without SAA1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11; co-absent with the target |
| [[SAA2]] | C | SAA2 activity raises SAA2-SAA4's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 4.08× lower at baseline in the lines without SAA2 | 6e-04 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3; co-absent with the target |
| [[TNFSF14]] | C | TNFSF14 activity raises SAA2-SAA4's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 3.94× lower at baseline in the lines without TNFSF14 | 7e-04 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent; co-absent with the target |
| [[C3]] | C | C3 activity raises SAA2-SAA4's level | lines that do not express C3 (32) vs lines expressing it (18) | 3.87× lower at baseline in the lines without C3 | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11; co-absent with the target |
| [[CFB]] | C | CFB activity raises SAA2-SAA4's level | lines that do not express CFB (20) vs lines expressing it (30) | 2.97× lower at baseline in the lines without CFB | 0.014 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises SAA2-SAA4's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.03× lower at baseline in the lines without STEAP4 | 0.014 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises SAA2-SAA4's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.03× lower at baseline in the lines without WFDC2 | 0.019 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 20, C 14. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC3H12A]] | B | SAA2-SAA4, [[SAA4]] activity raises ZC3H12A's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.38× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.012 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[FTH1]] | B | SAA2-SAA4 activity raises FTH1's level | lines that do not express SAA2-SAA4 (22) vs lines expressing it (28) | 2.31× lower at baseline in the lines without SAA2-SAA4 | 0.012 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SAA2, SAA1, LMO2 |
| [[CEBPD]] | B | SAA2-SAA4, [[SAA4]] activity raises CEBPD's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.86× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.020 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[BATF]] | B | SAA2-SAA4, [[SAA4]] activity raises BATF's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.00× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.037 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[ZMYND8]] | B | SAA2-SAA4, [[SAA4]] activity raises ZMYND8's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.72× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.038 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[TRIM29]] | B | SAA2-SAA4, [[SAA4]] activity raises TRIM29's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.98× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.042 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[SERPINA3]] | B | SAA2-SAA4, [[SAA4]] activity raises SERPINA3's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.33× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.046 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[CCND3]] | B | SAA2-SAA4, [[SAA4]] activity raises CCND3's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.58× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.046 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[ZFAND5]] | B | SAA2-SAA4 activity raises ZFAND5's level | lines that do not express SAA2-SAA4 (22) vs lines expressing it (28) | 1.24× lower at baseline in the lines without SAA2-SAA4 | 0.050 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SAA2, SAA1, LMO2 |
| [[MAOA]] | B | SAA2-SAA4, [[SAA4]] activity raises MAOA's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.82× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.053 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[LCN2]] | B | SAA2-SAA4, [[SAA4]] activity raises LCN2's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.02× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.054 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[CARD14]] | B | SAA2-SAA4, [[SAA4]] activity raises CARD14's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.53× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.059 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.917). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.2, 16.0); signed map (16.8, 28.7). **Vector** length 110, 34.6% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.63 to 6); *interferon gamma response* (hallmark, mean cos +0.57 to 6); *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.62 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +13.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +9.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | +5.0 | +10.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM | ⚠ position correction uncertain | +4.2 | +7.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.1 | +5.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.9 | +5.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -5.3 | -5.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.7 | -3.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.6 | -2.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.4 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | SAA2-SAA4 readthrough |
| Locus type | readthrough (other) |
| Location | 11p15.1 — chr11:18,231,423-18,248,635 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100528017](https://www.ncbi.nlm.nih.gov/gene/100528017):

> This locus represents naturally occurring read-through transcription between the neighboring serum amyloid A2 and serum amyloid A4 genes on chromosome 11. The read-through transcript produces a fusion protein that shares sequence identity with each individual gene product. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:39550](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39550) · Entrez [100528017](https://www.ncbi.nlm.nih.gov/gene/100528017) · Ensembl [ENSG00000255071](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255071)

## Data

Gene col 14914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14914); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14914]; `tensor/DDL_lfc|DDL_z.npy` [14914]; `embed/gene_vectors.npy` [14914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14914 or target_col == 14914). Every well: [[SAA2-SAA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAA2-SAA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
