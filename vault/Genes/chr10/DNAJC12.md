---
symbol: "DNAJC12"
type: "gene"
col: 2922
ensembl_id: "ENSG00000108176"
name: "DnaJ heat shock protein family (Hsp40) member C12"
location: "10q21.3"
module: 59
arm: "+"
pooled_cpm: 11.6
n_lines_expressing: 25
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 12
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# DNAJC12

*DnaJ heat shock protein family (Hsp40) member C12* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.12× (z +9.8, q 4e-20, up in 2 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.506× (z -6.3, q 2e-07, down in 19 of 22 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 2 lines (HT-29 0.119×, SHP-77 0.217×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.196×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A549 0.104×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.380×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPARGC1A]] (+0.64, fdr 1e-05), [[RAB30]] (+0.58, fdr 2e-05), [[RAB9A]] (+0.57, fdr 5e-05); moves opposite to [[MACROH2A1]] (-0.58, fdr 4e-05), [[MAD1L1]] (-0.55, fdr 1e-05), [[ZNF731P]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 12 go from it, the strongest it → [[ABCA5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2922.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +9.8 | 4e-20 | 2/20 (KATO III, BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +8.0 | 3e-13 | 17/22 (KATO III, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +7.5 | 1e-11 | 11/17 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.13×** | +7.0 | 3e-10 | 13/22 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +7.0 | 3e-10 | 11/22 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +6.7 | 2e-09 | 2/11 (SW 900, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +6.6 | 3e-09 | 15/22 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.97×** | +6.3 | 2e-08 | 13/22 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +6.2 | 4e-08 | 16/22 (A549, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +5.3 | 6e-06 | 7/20 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.70×** | +4.9 | 4e-05 | 13/22 (BT-474, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +4.7 | 1e-04 | 13/21 (RKO, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +4.7 | 1e-04 | 7/21 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +4.5 | 2e-04 | 9/22 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +4.5 | 2e-04 | 11/22 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.82×** | +3.7 | 0.008 | 6/17 (NCI-H1792, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.011 | 10/22 (NCI-H2030, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2922.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 2 lines (HT-29 0.119×, SHP-77 0.217×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.196×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A549 0.104×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.380×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.506×** | -6.3 | 2e-07 | 19/22 (SHP-77, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.691× | -3.4 | 0.18 | 10/22 (COLO 205, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.713× | -3.1 | 0.30 | 15/22 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-733 (drug)]] 5 µM |  | 0.530× | -3.1 | 0.30 | 8/18 (HepG2/C3A, A549, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2922. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 51.3 | 0 | 6 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.217× (z -10.7) |
| [[A549 (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -11.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 19.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 27.2 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.119× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 27.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2922), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPARGC1A]] | +0.64 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[RAB30]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[RAB9A]] | +0.57 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[ABCA5]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[GABARAP]] ⚠ | +0.57 | +0.40 / +0.59 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EFNA1]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SNX2]] | +0.56 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[AUH]] | +0.56 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[SELENOP]] | +0.55 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[KBTBD3]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[TXNDC16]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[KMT2E]] | +0.54 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[BMF]] | +0.53 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACROH2A1]] | -0.58 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[MAD1L1]] | -0.55 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.54 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[ASPH]] | -0.52 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[TUBA1C]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[EIPR1]] | -0.51 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[PSMD1]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[GHRLOS]] | -0.50 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[BCAP31]] | -0.49 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[TPM3]] | -0.49 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[GATAD2A]] | -0.49 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[SH3TC2]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA5]] | B | DNAJC12 activity raises ABCA5's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.71× lower at baseline in the lines without DNAJC12 | 0.036 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[RNF144B]] | B | DNAJC12 activity raises RNF144B's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without DNAJC12 | 0.037 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[MRPL54]] | B | DNAJC12 activity lowers MRPL54's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.13× higher at baseline in the lines without DNAJC12 | 0.058 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[SLC11A2]] | B | DNAJC12 activity raises SLC11A2's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.28× lower at baseline in the lines without DNAJC12 | 0.068 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM | B | DNAJC12 activity lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | lines that do not express DNAJC12 (25) vs lines expressing it (23) | the lines without DNAJC12: 1.40× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[ZCRB1]] | B | DNAJC12 activity lowers ZCRB1's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.19× higher at baseline in the lines without DNAJC12 | 0.073 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[SNX2]] | B | DNAJC12 activity lowers SNX2's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.19× higher at baseline in the lines without DNAJC12 | 0.073 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| cells under [[Tofacitinib (drug)]] 0.05 µM | B | DNAJC12 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express DNAJC12 (25) vs lines expressing it (23) | the lines without DNAJC12: 0.79× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[DENND4A]] | B | DNAJC12 activity raises DENND4A's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.34× lower at baseline in the lines without DNAJC12 | 0.088 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[TUBA1C]] | B | DNAJC12 activity lowers TUBA1C's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.24× higher at baseline in the lines without DNAJC12 | 0.092 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 5 µM | B | DNAJC12 activity lowers the cells' numbers under 18β-Glycyrrhetinic acid 5 µM (makes them more sensitive) | lines that do not express DNAJC12 (25) vs lines expressing it (23) | the lines without DNAJC12: 1.11× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[MEIS1]] | B | DNAJC12 activity raises MEIS1's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without DNAJC12 | 0.097 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (17.7, -22.2); signed map (-9.9, 5.7). **Vector** length 58.5, 14.7% of its response variance represented; |z| ≥ 3 in 544 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.9 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:67,796,669-67,838,188 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JDP1 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKB3](https://www.uniprot.org/uniprotkb/Q9UKB3) (DnaJ homolog subfamily C member 12):

> Probable co-chaperone that participates in the proper folding of biopterin-dependent aromatic amino acid hydroxylases, which include phenylalanine-4-hydroxylase (PAH), tyrosine 3-monooxygenase (TH) and peripheral and neuronal tryptophan hydroxylases (TPH1 and TPH2).

**Summary**, from NCBI Gene [56521](https://www.ncbi.nlm.nih.gov/gene/56521):

> This gene encodes a member of a subclass of the HSP40/DnaJ protein family. Members of this family of proteins are associated with complex assembly, protein folding, and export. Two transcript variants encoding distinct isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:28908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28908) · Entrez [56521](https://www.ncbi.nlm.nih.gov/gene/56521) · UniProt [Q9UKB3](https://www.uniprot.org/uniprotkb/Q9UKB3) · Ensembl [ENSG00000108176](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108176)

## Data

Gene col 2922: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2922); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2922, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2922]; `tensor/DDL_lfc|DDL_z.npy` [2922]; `embed/gene_vectors.npy` [2922]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2922 or target_col == 2922). Every well: [[DNAJC12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
