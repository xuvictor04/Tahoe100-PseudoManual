---
symbol: "TSPAN2"
type: "gene"
col: 5521
ensembl_id: "ENSG00000134198"
name: "tetraspanin 2"
location: "1p13.2"
module: 14
arm: "+"
pooled_cpm: 2.36
n_lines_expressing: 31
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 11
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TSPAN2

*tetraspanin 2* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.44× (z +17.8, q 0e+00, up in 15 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 0.101×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.218×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (Panc 03.27 0.133×; ⚠ cell-cycle shift, explains ~76% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02832]] (+0.62, fdr 7e-06), [[TLL1]] (+0.62, fdr 7e-06), [[LIMA1]] (+0.58, fdr 1e-05); moves opposite to [[GLUD1P3]] (-0.52, fdr 2e-05), [[FBH1]] (-0.50, fdr 3e-05), [[MEF2B]] (-0.50, fdr 5e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LGR6]] → it (grade B ⚠); 11 go from it, the strongest it → [[AFAP1L2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5521.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.44×** | +17.8 | 0e+00 | 15/18 (A-172, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.57×** | +13.3 | 4e-38 | 21/25 (A498, NCI-H23, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.35×** | +10.5 | 2e-23 | 3/3 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.35×** | +9.0 | 5e-17 | 18/21 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.22×** | +8.7 | 5e-16 | 6/9 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.44×** | +8.5 | 2e-15 | 2/6 (A498, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.03×** | +8.2 | 2e-14 | 15/24 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.93×** | +8.0 | 1e-13 | 11/17 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.90×** | +7.9 | 2e-13 | 15/24 (A498, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.89×** | +7.9 | 2e-13 | 17/25 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.24×** | +6.0 | 1e-07 | 16/25 (RPMI-7951, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.18×** | +5.5 | 1e-06 | 10/22 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +5.5 | 2e-06 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +5.1 | 1e-05 | 3/25 (SW48, NCI-H23, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.36×** | +4.5 | 2e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.005 | 5/20 (Hs 766T, J82, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.016 | 2/26 (A498, J82) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.42×** | +3.4 | 0.017 | 6/23 (CFPAC-1, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.068 | 4/24 (LoVo, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5521.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 0.101×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.218×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (Panc 03.27 0.133×; ⚠ cell-cycle shift, explains ~76% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sildenafil (drug)]] 0.05 µM |  | 0.626× | -3.2 | 0.64 | 1/22 (SW48) | inconsistent across doses | position effect removed |
| [[Norepinephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.664× | -3.1 | 0.64 | 3/24 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5521. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 15.3 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.101× (z -12.0) |
| [[A-172 (line)]] | wt | 0.919 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 70.6× (z +12.0) | — |
| [[CFPAC-1 (line)]] | alt | 3.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +8.9) | — |
| [[J82 (line)]] | alt | 3.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.77× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.133× (z -8.8) ⚠ cell-cycle shift, explains ~76% of this change |
| [[A-427 (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.258 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.651 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.810 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.931 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.270 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.595 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.395 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.184 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.783 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.766 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.180 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.223 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.219 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.608 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5521), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02832]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[TLL1]] | +0.62 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[LIMA1]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[WWC1]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[PLCB4]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ANKRD33B]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ABCG2]] | +0.56 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[CYP2S1]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[IL18]] | +0.56 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[OLFM2]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[LYPD1]] | +0.55 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[FMN2]] | +0.54 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLUD1P3]] | -0.52 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[FBH1]] | -0.50 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[MEF2B]] | -0.50 | -0.23 / -0.48 | both halves | 5e-04 |  |
| [[TMEM11-DT]] | -0.49 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[DGCR2]] | -0.49 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[THAP4]] | -0.48 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[RAB43]] | -0.48 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[UFD1]] | -0.47 | -0.50 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGR6]] | B | LGR6 activity raises TSPAN2's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 1.84× lower at baseline in the lines without LGR6 | 0.062 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2 |
| [[AFAP1L2]] | B | AFAP1L2 activity raises TSPAN2's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 1.55× lower at baseline in the lines without AFAP1L2 | 0.068 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[MITF]] | B | MITF activity raises TSPAN2's level | lines that do not express MITF (9) vs lines expressing it (41) | 1.80× lower at baseline in the lines without MITF | 0.093 | ⚠ within organs, on part of the lines; also absent: LRP12, DUBR, CYP46A1 |
| [[PRICKLE1]] | C | PRICKLE1 activity raises TSPAN2's level | lines that do not express PRICKLE1 (26) vs lines expressing it (24) | 1.55× lower at baseline in the lines without PRICKLE1 | 0.061 | ⚠ within organs, on part of the lines; also absent: COL4A2, NR0B1, THBD; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AFAP1L2]] | B | TSPAN2 activity raises AFAP1L2's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without TSPAN2 | 0.023 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[ADRB2]] | B | TSPAN2 activity raises ADRB2's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 1.86× lower at baseline in the lines without TSPAN2 | 0.025 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[RASSF5]] | B | TSPAN2 activity raises RASSF5's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 1.80× lower at baseline in the lines without TSPAN2 | 0.032 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[LINC02832]] | B | TSPAN2 activity raises LINC02832's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 1.72× lower at baseline in the lines without TSPAN2 | 0.046 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[CLDN1]] | B | TSPAN2 activity raises CLDN1's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without TSPAN2 | 0.069 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[CYP2S1]] | B | TSPAN2 activity raises CYP2S1's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 1.71× lower at baseline in the lines without TSPAN2 | 0.072 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| cells under [[Cobimetinib (drug)]] 5 µM | B | TSPAN2 activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express TSPAN2 (19) vs lines expressing it (29) | the lines without TSPAN2: 1.21× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[LINC01186]] | B | TSPAN2 activity raises LINC01186's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without TSPAN2 | 0.083 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[ANKRD1]] | B | TSPAN2 activity raises ANKRD1's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 2.21× lower at baseline in the lines without TSPAN2 | 0.096 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[SYNGR2]] | B | TSPAN2 activity raises SYNGR2's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without TSPAN2 | 0.099 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[VAV1]] | C | TSPAN2 activity raises VAV1's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without TSPAN2 | 0.041 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.4, 11.3); signed map (49.0, 16.1). **Vector** length 42.8, 7.79% of its response variance represented; |z| ≥ 3 in 690 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +13.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +17.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +3.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -0.6 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:115,048,011-115,089,503 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TSPAN-2, TSN2, FLJ12082 |
| Gene groups (HGNC) | Tetraspanin family |
| Matched by | ensembl_id |

**Function**, from UniProt [O60636](https://www.uniprot.org/uniprotkb/O60636) (Tetraspanin-2):

> May play a role in signaling in oligodendrocytes in the early stages of their terminal differentiation into myelin-forming glia and may also function in stabilizing the mature sheath.

**Summary**, from NCBI Gene [10100](https://www.ncbi.nlm.nih.gov/gene/10100):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:20659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20659) · Entrez [10100](https://www.ncbi.nlm.nih.gov/gene/10100) · UniProt [O60636](https://www.uniprot.org/uniprotkb/O60636) · Ensembl [ENSG00000134198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134198)

## Data

Gene col 5521: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5521); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5521, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5521]; `tensor/DDL_lfc|DDL_z.npy` [5521]; `embed/gene_vectors.npy` [5521]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5521 or target_col == 5521). Every well: [[TSPAN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
