---
symbol: "FRMD4A"
type: "gene"
col: 7526
ensembl_id: "ENSG00000151474"
name: "FERM domain containing 4A"
location: "10p13"
module: 13
arm: "+"
pooled_cpm: 252.45
n_lines_expressing: 26
n_dd_up: 4
n_dd_down: 27
n_dd_up_clean: 2
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 67
direction_downstream: 88
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# FRMD4A

*FERM domain containing 4A* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.31× (z +6.4, q 8e-08, up in 7 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (J82 4.93×, HOP62 4.00×, NCI-H1792 3.62×, Hs 766T 2.64×; ⚠ cell-cycle shift, explains ~20% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (J82 4.16×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (HOP62 8.39×).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.590× (z -8.6, q 4e-15, down in 21 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INSYN2B]] (+0.73, fdr 7e-06), [[CTHRC1]] (+0.70, fdr 7e-06), [[APCDD1L-DT]] (+0.68, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 67 arrows point to it, the strongest [[EVC]] → it (grade B ⚠); 88 go from it, the strongest it → [[STARD13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7526.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (J82 4.93×, HOP62 4.00×, NCI-H1792 3.62×, Hs 766T 2.64×; ⚠ cell-cycle shift, explains ~20% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (J82 4.16×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (HOP62 8.39×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +6.4 | 8e-08 | 7/24 (A549, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +5.2 | 7e-05 | 3/25 (SW480, SW 1271, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.24×** | +5.0 | 9e-05 | 12/24 (J82, HOP62, …) | top dose only | composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | 1.15× | +3.4 | 0.091 | 6/25 (J82, RKO, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.091 | 10/24 (RKO, RPMI-7951, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.2 | 0.14 | 3/25 (A549, SW 900, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | 1.41× | +3.0 | 0.21 | 12/25 (HOP62, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7526.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.590×** | -8.6 | 4e-15 | 21/24 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.625×** | -7.7 | 5e-12 | 20/24 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.643×** | -7.2 | 1e-10 | 21/24 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.687×** | -6.1 | 1e-07 | 21/24 (H4, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.687×** | -6.1 | 1e-07 | 21/24 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.710×** | -5.3 | 8e-06 | 20/23 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.723×** | -5.3 | 1e-05 | 20/24 (RKO, H4, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.802×** | -5.0 | 4e-05 | 12/24 (NCI-H1792, H4, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.569×** | -4.8 | 9e-05 | 19/24 (RKO, H4, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.745×** | -4.5 | 4e-04 | 22/24 (C32, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.761×** | -4.4 | 5e-04 | 12/24 (H4, NCI-H1792, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.631×** | -3.9 | 0.004 | 15/24 (RKO, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.794×** | -3.7 | 0.008 | 14/24 (RKO, C32, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.795×** | -3.7 | 0.009 | 13/24 (CHP-212, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.659×** | -3.6 | 0.014 | 17/24 (RKO, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.804×** | -3.5 | 0.015 | 14/24 (H4, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.805×** | -3.5 | 0.015 | 12/24 (RPMI-7951, LOX-IMVI, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.799×** | -3.4 | 0.025 | 7/24 (RKO, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 1,009 | 0 | 33 (14 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -24.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.201× (z -14.8) |
| [[C32 (line)]] | wt | 855 | 0 | 26 (15 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0506× (z -18.0) |
| [[A498 (line)]] | wt | 1,980 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0413× (z -30.9) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0897× (z -16.5) |
| [[HOP62 (line)]] | alt | 318 | 2 (1 ⚠) | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +17.3) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.39× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -13.5) |
| [[H4 (line)]] | wt | 116 | 0 | 7 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0900× (z -17.3) |
| [[hTERT-HPNE (line)]] | wt | 677 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.199× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 903 | 0 | 7 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.155× (z -12.5) |
| [[J82 (line)]] | alt | 141 | 2 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +19.3) ⚠ cell-cycle shift, explains ~20% of this change | [[Digitoxin (drug)]] 5 µM 0.263× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.329× (z -9.5) |
| [[SNU-423 (line)]] | alt | 1,267 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.141× (z -11.0) |
| [[A-172 (line)]] | wt | 385 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 143 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -10.7) |
| [[SW480 (line)]] | alt | 72.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -12.6) |
| [[CHP-212 (line)]] | wt | 435 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 240 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +14.2) ⚠ cell-cycle shift, explains ~20% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.286× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 1,035 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -12.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 149 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.5) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[HS-578T (line)]] | alt | 274 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -8.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 106 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.336× (z -9.4) |
| [[SW 1088 (line)]] | alt | 301 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 24.5 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 40.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 21.5 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 35.6 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 54.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 25.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 25.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 23.4 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 19.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 19.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.9 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 22.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 26.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.1 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 55.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 31.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.0 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 25.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INSYN2B]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CTHRC1]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L-DT]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[AFF3]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ADAM12]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[MIR100HG]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ADAMTS12]] | +0.67 | +0.57 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[APCDD1L]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[NAV1]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[EVA1A]] | +0.65 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PRRX1]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[RFTN1]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*67 arrows, 67 of them with an alert ⚠; grade A 0, B 5, C 62. Shown: the 12 strongest; 55 more arrows (55 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EVC]] | B | EVC activity raises FRMD4A's level | lines that do not express EVC (13) vs lines expressing it (37) | 4.01× lower at baseline in the lines without EVC | 0.047 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[CYGB]] | B | CYGB activity raises FRMD4A's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.78× lower at baseline in the lines without CYGB | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[FRMD6]] | B | FRMD6 activity raises FRMD4A's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 4.65× lower at baseline in the lines without FRMD6 | 0.063 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[NEBL]] | B | NEBL activity lowers FRMD4A's level | lines that do not express NEBL (17) vs lines expressing it (33) | 4.49× higher at baseline in the lines without NEBL | 0.081 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| [[LINC02454]] | B | LINC02454 activity raises FRMD4A's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 3.86× lower at baseline in the lines without LINC02454 | 0.092 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[ITGB3]] | C | ITGB3 activity raises FRMD4A's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 6.21× lower at baseline in the lines without ITGB3 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; co-absent with the target |
| [[FLI1]] | C | FLI1 activity raises FRMD4A's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 4.30× lower at baseline in the lines without FLI1 | 0.003 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises FRMD4A's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 5.43× lower at baseline in the lines without AEBP1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises FRMD4A's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 6.17× lower at baseline in the lines without ADAM12 | 0.004 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[MIR100HG]] | C | MIR100HG activity raises FRMD4A's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 6.10× lower at baseline in the lines without MIR100HG | 0.005 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises FRMD4A's level | lines that do not express GDNF (38) vs lines expressing it (12) | 5.80× lower at baseline in the lines without GDNF | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises FRMD4A's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 7.11× lower at baseline in the lines without LINC01411 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |

### Downstream of this gene

*88 arrows, 88 of them with an alert ⚠; grade A 0, B 28, C 60. Shown: the 12 strongest; 76 more arrows (76 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD13]] | B | FRMD4A activity raises STARD13's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 3.22× lower at baseline in the lines without FRMD4A | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[FRMD6]] | B | FRMD4A activity raises FRMD6's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 4.00× lower at baseline in the lines without FRMD4A | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[ARHGAP31]] | B | FRMD4A activity raises ARHGAP31's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 3.57× lower at baseline in the lines without FRMD4A | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[SYNJ2]] | B | FRMD4A activity raises SYNJ2's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.07× lower at baseline in the lines without FRMD4A | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[ARSJ]] | B | FRMD4A activity raises ARSJ's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.70× lower at baseline in the lines without FRMD4A | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[PHLDB1]] | B | FRMD4A activity raises PHLDB1's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.29× lower at baseline in the lines without FRMD4A | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[LINC02454]] | B | FRMD4A activity raises LINC02454's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.07× lower at baseline in the lines without FRMD4A | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[PCDHGA2]] | B | FRMD4A activity raises PCDHGA2's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.72× lower at baseline in the lines without FRMD4A | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[REP15]] | B | FRMD4A activity raises REP15's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without FRMD4A | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[CD82]] | B | FRMD4A activity raises CD82's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.90× lower at baseline in the lines without FRMD4A | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[PRSS23]] | B | FRMD4A activity raises PRSS23's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.60× lower at baseline in the lines without FRMD4A | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[KIAA1549L]] | B | FRMD4A activity raises KIAA1549L's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 3.69× lower at baseline in the lines without FRMD4A | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.4, 17.1); signed map (21.5, 47.1). **Vector** length 121, 39.5% of its response variance represented; |z| ≥ 3 in 1,066 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +7.1 | +5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.5 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +1.3 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +3.4 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.4 | -5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -6.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.7 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.6 | -3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | FERM domain containing 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:13,643,706-14,462,142 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10210, KIAA1294, bA295P9.4; previously FRMD4 |
| Gene groups (HGNC) | FERM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2Q2](https://www.uniprot.org/uniprotkb/Q9P2Q2) (FERM domain-containing protein 4A):

> Scaffolding protein that regulates epithelial cell polarity by connecting ARF6 activation with the PAR3 complex (By similarity). Plays a redundant role with FRMD4B in epithelial polarization (By similarity). May regulate MAPT secretion by activating ARF6-signaling.

**Summary**, from NCBI Gene [55691](https://www.ncbi.nlm.nih.gov/gene/55691):

> This gene encodes a FERM domain-containing protein that regulates epithelial cell polarity. It connects ADP ribosylation factor 6 (ARF6) with the Par protein complex, which regulates the remodeling of adherens junctions and linear actin cable formation during epithelial cell polarization. Polymorphisms in this gene are associated with Alzheimer's disease, and also with nicotine dependence. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:25491](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25491) · Entrez [55691](https://www.ncbi.nlm.nih.gov/gene/55691) · UniProt [Q9P2Q2](https://www.uniprot.org/uniprotkb/Q9P2Q2) · Ensembl [ENSG00000151474](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151474)

## Data

Gene col 7526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7526); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7526]; `tensor/DDL_lfc|DDL_z.npy` [7526]; `embed/gene_vectors.npy` [7526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7526 or target_col == 7526). Every well: [[FRMD4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRMD4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
