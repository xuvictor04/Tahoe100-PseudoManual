---
symbol: "SATB1"
type: "gene"
col: 11301
ensembl_id: "ENSG00000182568"
name: "SATB homeobox 1"
location: "3p24.3"
module: 26
arm: "+"
pooled_cpm: 7.3
n_lines_expressing: 35
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 11
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SATB1

*SATB homeobox 1* — 3p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +7.4, q 1e-10, up in 18 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.382× (z -12.2, q 2e-31, down in 25 of 33 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.334× (z -7.3, q 4e-11, down in 21 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAZ2B]] (+0.63, fdr 1e-05), [[ATOSA]] (+0.61, fdr 1e-05), [[SIX4]] (+0.61, fdr 3e-05); moves opposite to [[MTG1]] (-0.59, fdr 1e-05), [[WDR5]] (-0.58, fdr 1e-05), [[PIGU]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SATB1-AS1]] → it (grade B ⚠); 11 go from it, the strongest it → [[MKLN1-AS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11301.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.4 | 1e-10 | 18/30 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.6 | 0.001 | 14/32 (A-172, HOP62, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.40×** | +4.3 | 0.003 | 10/32 (SW480, COLO 205, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.004 | 10/32 (A498, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +4.1 | 0.004 | 4/14 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.85×** | +4.1 | 0.005 | 7/27 (BT-474, LS 180, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **1.65×** | +3.3 | 0.070 | 3/28 (RKO, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.079 | 2/30 (LS 180, SNU-423) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.28×** | +3.2 | 0.100 | 7/24 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.41× | +3.1 | 0.10 | 8/26 (SHP-77, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11301.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.382×** | -12.2 | 2e-31 | 25/33 (LS 180, NCI-H1792, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.398×** | -11.7 | 6e-29 | 26/33 (LS 180, SW480, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.432×** | -10.6 | 5e-24 | 28/33 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.439×** | -10.4 | 3e-23 | 26/33 (LS 180, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.334×** | -7.3 | 4e-11 | 21/31 (LS 180, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.597×** | -6.3 | 3e-08 | 17/24 (HT-29, COLO 205, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.408×** | -5.9 | 2e-07 | 16/30 (LS 180, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.643×** | -5.6 | 2e-06 | 17/33 (HT-29, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.462×** | -5.1 | 2e-05 | 13/30 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.482×** | -4.8 | 7e-05 | 15/30 (NCI-H1792, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.683×** | -4.8 | 7e-05 | 14/32 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.499×** | -4.6 | 2e-04 | 12/28 (LoVo, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.508×** | -4.5 | 3e-04 | 13/30 (SW1417, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.611×** | -4.5 | 3e-04 | 8/33 (LoVo, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.637×** | -4.1 | 0.002 | 12/32 (LoVo, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.567×** | -3.7 | 0.006 | 11/31 (SW480, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.825×** | -3.4 | 0.018 | 10/33 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.686×** | -3.4 | 0.019 | 7/32 (COLO 205, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.621×** | -3.1 | 0.041 | 10/29 (HOP62, Panc 03.27, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 26.2 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -14.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 18.7 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -13.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 33.4 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -18.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0932× (z -13.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 8.84 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0728× (z -17.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 8.90 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0393× (z -13.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -9.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -9.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 19.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -9.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.801 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.788 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | +0.63 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ATOSA]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SIX4]] | +0.61 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[N4BP2L1]] | +0.60 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[AK9]] | +0.57 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[LINC02889]] | +0.57 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[STX17-DT]] | +0.57 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[NBR1]] | +0.57 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[SATB1-AS1]] | +0.56 | +0.48 / +0.28 | both halves | 3e-04 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[LINC02307]] | +0.56 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[PHF8]] | +0.56 | +0.55 / +0.26 | both halves | 3e-04 |  |
| [[MKLN1-AS]] | +0.56 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[RAMP1]] | +0.56 | +0.54 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTG1]] | -0.59 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[WDR5]] | -0.58 | -0.49 / -0.50 | both halves | 1e-05 | pathway: Differentiation of T cells |
| [[PIGU]] | -0.58 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[ABCC10]] | -0.57 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[POFUT1]] | -0.56 | -0.37 / -0.61 | both halves | 8e-05 |  |
| [[EIF2B3]] | -0.56 | -0.32 / -0.54 | both halves | 1e-04 |  |
| [[GTF2E2]] | -0.56 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[FAR1]] | -0.55 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[PDSS1]] | -0.54 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[NUP93]] | -0.54 | -0.42 / -0.47 | both halves | 4e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[TAF5L]] | -0.54 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[NTAQ1]] | -0.53 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SATB1-AS1]] | B | SATB1-AS1 activity raises SATB1's level | lines that do not express SATB1-AS1 (12) vs lines expressing it (38) | 2.57× lower at baseline in the lines without SATB1-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: CMKLR2, ENSG00000289609; maybe low, not absent |
| [[LRRN1]] | B | LRRN1 activity raises SATB1's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 2.08× lower at baseline in the lines without LRRN1 | 0.064 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[PTPRB]] | B | PTPRB activity raises SATB1's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 1.74× lower at baseline in the lines without PTPRB | 0.065 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[FOXP2]] | B | FOXP2 activity raises SATB1's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 1.94× lower at baseline in the lines without FOXP2 | 0.070 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6 |
| [[RAMP1]] | B | RAMP1 activity raises SATB1's level | lines that do not express RAMP1 (16) vs lines expressing it (34) | 1.96× lower at baseline in the lines without RAMP1 | 0.088 | ⚠ within organs, on part of the lines; also absent: IGFBP6, TRHDE, SDCBP2; maybe low, not absent |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MKLN1-AS]] | B | SATB1 activity lowers MKLN1-AS's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.40× higher at baseline in the lines without SATB1 | 0.007 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[EIF2B3]] | B | SATB1 activity lowers EIF2B3's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.49× higher at baseline in the lines without SATB1 | 0.027 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[ENTPD5]] | B | SATB1 activity lowers ENTPD5's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.38× higher at baseline in the lines without SATB1 | 0.031 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[NUP93]] | B | SATB1 activity lowers NUP93's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.38× higher at baseline in the lines without SATB1 | 0.033 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[ACTR5]] | B | SATB1 activity lowers ACTR5's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.41× higher at baseline in the lines without SATB1 | 0.039 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[NOL10]] | B | SATB1 activity lowers NOL10's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.33× higher at baseline in the lines without SATB1 | 0.041 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[POFUT1]] | B | SATB1 activity lowers POFUT1's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.34× higher at baseline in the lines without SATB1 | 0.045 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[RSU1]] | B | SATB1 activity lowers RSU1's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.49× higher at baseline in the lines without SATB1 | 0.061 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[TIMM23]] | B | SATB1 activity lowers TIMM23's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.14× higher at baseline in the lines without SATB1 | 0.079 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[ABCC10]] | B | SATB1 activity lowers ABCC10's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.31× higher at baseline in the lines without SATB1 | 0.084 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[PTPRB]] | B | SATB1 activity raises PTPRB's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 2.22× lower at baseline in the lines without SATB1 | 0.092 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (16.1, 8.1); signed map (24.5, -11.8). **Vector** length 65.8, 13.2% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.8 | +0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -2.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.8 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -10.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.0 | -12.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.8 | -11.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.5 | -10.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -5.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.2 | -4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -4.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -4.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | SATB homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.3 — chr3:18,345,377-18,445,621 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | CUT class homeoboxes and pseudogenes |
| Hallmark sets | APOPTOSIS, KRAS_SIGNALING_UP |
| Reactome | 9 pathways, smallest: Apoptotic cleavage of cellular proteins; Apoptotic execution phase; SUMOylation of chromatin organization proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01826](https://www.uniprot.org/uniprotkb/Q01826) (DNA-binding protein SATB1):

> Crucial silencing factor contributing to the initiation of X inactivation mediated by Xist RNA that occurs during embryogenesis and in lymphoma (By similarity). Binds to DNA at special AT-rich sequences, the consensus SATB1-binding sequence (CSBS), at nuclear matrix- or scaffold-associated regions. Thought to recognize the sugar-phosphate structure of double-stranded DNA. Transcriptional repressor controlling nuclear and viral gene expression in a phosphorylated and acetylated status-dependent …

**Summary**, from NCBI Gene [6304](https://www.ncbi.nlm.nih.gov/gene/6304):

> This gene encodes a matrix protein which binds nuclear matrix and scaffold-associating DNAs through a unique nuclear architecture. The protein recruits chromatin-remodeling factors in order to regulate chromatin structure and gene expression. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:10541](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10541) · Entrez [6304](https://www.ncbi.nlm.nih.gov/gene/6304) · UniProt [Q01826](https://www.uniprot.org/uniprotkb/Q01826) · Ensembl [ENSG00000182568](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182568)

## Data

Gene col 11301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11301); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11301]; `tensor/DDL_lfc|DDL_z.npy` [11301]; `embed/gene_vectors.npy` [11301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11301 or target_col == 11301). Every well: [[SATB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SATB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
