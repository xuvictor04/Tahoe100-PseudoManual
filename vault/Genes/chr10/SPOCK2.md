---
symbol: "SPOCK2"
type: "gene"
col: 2874
ensembl_id: "ENSG00000107742"
name: "SPARC (osteonectin), cwcv and kazal like domains proteoglycan 2"
location: "10q22.1"
module: 39
arm: "+"
pooled_cpm: 5.1
n_lines_expressing: 44
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 13
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# SPOCK2

*SPARC (osteonectin), cwcv and kazal like domains proteoglycan 2* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.96× (z +14.8, q 0e+00, up in 27 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.392× (z -9.0, q 9e-17, down in 27 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC6A13]] (+0.77, fdr 7e-06), [[TMEM236]] (+0.75, fdr 7e-06), [[ANKDD1B]] (+0.75, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 13 go from it, the strongest it → [[STAC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2874.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.96×** | +14.8 | 0e+00 | 27/32 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +9.0 | 7e-17 | 1/4 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **2.10×** | +7.1 | 2e-10 | 20/41 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.6 | 6e-09 | 11/38 (SW480, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +6.1 | 1e-07 | 4/13 (NCI-H23, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +6.0 | 2e-07 | 4/6 (NCI-H23, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +5.8 | 4e-07 | 11/31 (LoVo, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.7 | 1e-06 | 11/24 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +5.5 | 3e-06 | 17/31 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.68×** | +4.7 | 1e-04 | 9/36 (A549, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +4.5 | 4e-04 | 9/39 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.006 | 9/36 (SW480, A-172, …) | top dose only | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.026 | 4/37 (LoVo, SW480, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.041 | 3/38 (NCI-H23, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2874.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.392×** | -9.0 | 9e-17 | 27/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.430×** | -8.1 | 1e-13 | 25/37 (NCI-H1573, PANC-1, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.545×** | -5.9 | 9e-07 | 20/37 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.576×** | -5.3 | 1e-05 | 20/23 (PANC-1, HEC-1-A, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.606×** | -4.8 | 1e-04 | 16/37 (NCI-H23, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.418×** | -4.4 | 1e-03 | 12/31 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.665×** | -3.8 | 0.012 | 13/35 (NCI-H23, Panc 03.27, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.656×** | -3.7 | 0.015 | 12/39 (C-33 A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.677×** | -3.6 | 0.018 | 15/33 (LoVo, HepG2/C3A, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.724×** | -3.1 | 0.096 | 4/39 (NCI-H23, HepG2/C3A, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.797×** | -3.1 | 0.096 | 4/36 (SK-MEL-2, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 42.4 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 12.0× (z +14.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -15.1) |
| [[NCI-H1573 (line)]] | alt | 5.79 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0472× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 5.93 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0957× (z -10.5) |
| [[PANC-1 (line)]] | alt | 9.43 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0547× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.114× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 98.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 5.97 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0520× (z -10.8) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.103× (z -8.6) |
| [[C-33 A (line)]] | alt | 8.32 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.0561× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 4.64 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0549× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[LoVo (line)]] | wt | 2.95 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0768× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0605× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A13]] | +0.77 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.75 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.74 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.73 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.72 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[SLC2A9]] | +0.72 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[EFCAB8]] | +0.72 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[IMPG2]] | +0.72 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[MPP4]] | +0.71 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | +0.71 | +0.67 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPOCK2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CCDC144CP]] | B | CCDC144CP activity raises SPOCK2's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 1.83× lower at baseline in the lines without CCDC144CP | 0.093 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAC3]] | B | SPOCK2 activity raises STAC3's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.67× lower at baseline in the lines without SPOCK2 | 0.022 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[GAPLINC]] | B | SPOCK2 activity raises GAPLINC's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.55× lower at baseline in the lines without SPOCK2 | 0.032 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[MC1R]] | B | SPOCK2 activity raises MC1R's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without SPOCK2 | 0.043 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[CDKL4]] | B | SPOCK2 activity raises CDKL4's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without SPOCK2 | 0.051 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[ANKAR]] | B | SPOCK2 activity raises ANKAR's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without SPOCK2 | 0.059 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[KIAA1614]] | B | SPOCK2 activity raises KIAA1614's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.63× lower at baseline in the lines without SPOCK2 | 0.062 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[SLC7A9]] | B | SPOCK2 activity raises SLC7A9's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without SPOCK2 | 0.067 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[XKRX]] | B | SPOCK2 activity raises XKRX's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without SPOCK2 | 0.073 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[LAG3]] | B | SPOCK2 activity raises LAG3's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.93× lower at baseline in the lines without SPOCK2 | 0.078 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[ITGA2B]] | B | SPOCK2 activity raises ITGA2B's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without SPOCK2 | 0.080 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[MSANTD1]] | B | SPOCK2 activity raises MSANTD1's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without SPOCK2 | 0.083 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[BTG3-AS1]] | B | SPOCK2 activity raises BTG3-AS1's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without SPOCK2 | 0.096 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.8, -13.6); signed map (17.3, 7.3). **Vector** length 56.5, 8.65% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +14.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +6.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +7.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.2 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -9.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -8.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | SPARC (osteonectin), cwcv and kazal like domains proteoglycan 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:72,059,034-72,089,032 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0275, testican-2 |
| Gene groups (HGNC) | SPARC family |
| Hallmark sets | COMPLEMENT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92563](https://www.uniprot.org/uniprotkb/Q92563) (Testican-2):

> May participate in diverse steps of neurogenesis. Binds calcium.

**Summary**, from NCBI Gene [9806](https://www.ncbi.nlm.nih.gov/gene/9806):

> This gene encodes a protein which binds with glycosaminoglycans to form part of the extracellular matrix. The protein contains thyroglobulin type-1, follistatin-like, and calcium-binding domains, and has glycosaminoglycan attachment sites in the acidic C-terminal region. Three alternatively spliced transcript variants that encode different protein isoforms have been described for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:13564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13564) · Entrez [9806](https://www.ncbi.nlm.nih.gov/gene/9806) · UniProt [Q92563](https://www.uniprot.org/uniprotkb/Q92563) · Ensembl [ENSG00000107742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107742)

## Data

Gene col 2874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2874); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2874]; `tensor/DDL_lfc|DDL_z.npy` [2874]; `embed/gene_vectors.npy` [2874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2874 or target_col == 2874). Every well: [[SPOCK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPOCK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
