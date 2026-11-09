---
symbol: "KRT6A"
type: "gene"
col: 12977
ensembl_id: "ENSG00000205420"
name: "keratin 6A"
location: "12q13.13"
module: 97
arm: "+"
pooled_cpm: 10.24
n_lines_expressing: 9
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 24
direction_downstream: 38
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# KRT6A

*keratin 6A* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 6.45× (z +8.7, q 1e-15, up in 6 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H1573 0.0154×, Hs 766T 0.199×, LoVo 0.120×, LS 180 0.0505×, …; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1573 0.0261×, LoVo 0.113×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0386×); [[Selinexor (drug)]] 5 µM in 1 line (NCI-H1573 0.0701×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRT16]] (+0.70, fdr 7e-06), [[SCEL]] (+0.65, fdr 7e-06), [[S100P]] (+0.65, fdr 7e-06); moves opposite to [[FOXA1]] (-0.47, fdr 3e-05), [[CDKN2A]] (-0.44, fdr 9e-05), [[LTB]] (-0.42, fdr 4e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[CALB1]] → it (grade C ⚠); 38 go from it, the strongest it → [[BCR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12977.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **6.45×** | +8.7 | 1e-15 | 6/7 (LS 180, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **26.7×** | +8.5 | 5e-15 | 5/5 (LoVo, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.85×** | +8.4 | 7e-15 | 1/1 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.37×** | +8.3 | 1e-14 | 2/5 (Hs 766T, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.97×** | +6.3 | 3e-08 | 2/4 (Hs 766T, NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **3.11×** | +5.6 | 2e-06 | 4/6 (NCI-H1573, Panc 03.27, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.83×** | +5.1 | 2e-05 | 3/7 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.82×** | +5.1 | 2e-05 | 3/7 (Hs 766T, Panc 03.27, …) | all doses, flat | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.82×** | +5.1 | 2e-05 | 4/6 (NCI-H1573, Panc 03.27, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.50×** | +4.6 | 2e-04 | 2/4 (Hs 766T, Panc 03.27) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.58×** | +4.5 | 3e-04 | 0/5 | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **2.64×** | +4.4 | 4e-04 | 4/6 (Panc 03.27, NCI-H1573, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **2.38×** | +4.3 | 8e-04 | 3/6 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **4.00×** | +4.3 | 8e-04 | 6/7 (LoVo, LS 180, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.43×** | +4.2 | 9e-04 | 4/7 (NCI-H1573, Panc 03.27, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.30×** | +4.1 | 0.001 | 6/7 (NCI-H1573, LS 180, …) | two highest doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +4.0 | 0.002 | 4/7 (Panc 03.27, NCI-H1573, …) | top dose only | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **1.76×** | +3.9 | 0.003 | 4/7 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **2.19×** | +3.9 | 0.003 | 3/7 (Hs 766T, Panc 03.27, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.07×** | +3.6 | 0.009 | 5/7 (LS 180, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.03×** | +3.5 | 0.012 | 4/6 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H1573 0.0154×, Hs 766T 0.199×, LoVo 0.120×, LS 180 0.0505×, …; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1573 0.0261×, LoVo 0.113×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0386×); [[Selinexor (drug)]] 5 µM in 1 line (NCI-H1573 0.0701×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12977. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 11.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0386× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 14.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0154× (z -13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0261× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 12.0 | 1 | 2 (2 ⚠) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 28.3× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.0332× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 385 | 1 | 1 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 4.27× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 3.21 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0505× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.663 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.606 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.871 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.902 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.872 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.948 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.795 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.841 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.867 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.54 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12977), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT16]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 | pathway: Formation of the cornified envelope; STRING 928 |
| [[SCEL]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 | STRING 441 |
| [[S100P]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[TNS4]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SGPP2]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[GJB3]] | +0.57 | +0.64 / +0.53 | both halves | 1e-05 | STRING 623 |
| [[FAM83A]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 | **novel candidate** |
| [[C16orf74]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SERPINB5]] | +0.57 | +0.61 / +0.46 | both halves | 3e-05 | STRING 544 |
| [[ITPK1]] | +0.56 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[MAOA]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ABLIM2]] | +0.54 | +0.54 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXA1]] | -0.47 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CDKN2A]] | -0.44 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[LTB]] | -0.42 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[PIK3IP1]] | -0.42 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[PLAU]] | -0.40 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[FGF9]] | -0.40 | -0.47 / -0.26 | both halves | 3e-04 |  |
| [[RND1]] | -0.40 | -0.44 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 0, C 24. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALB1]] | C | CALB1 activity raises KRT6A's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 4.30× lower at baseline in the lines without CALB1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[KRT14]] | C | KRT14 activity raises KRT6A's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 4.95× lower at baseline in the lines without KRT14 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |
| [[GSDMC]] | C | GSDMC activity raises KRT6A's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 5.87× lower at baseline in the lines without GSDMC | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1; co-absent with the target |
| [[CAPN8]] | C | CAPN8 activity raises KRT6A's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 3.38× lower at baseline in the lines without CAPN8 | 0.009 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38; co-absent with the target |
| [[SERPINB5]] | C | SERPINB5 activity raises KRT6A's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 3.42× lower at baseline in the lines without SERPINB5 | 0.011 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |
| [[DSG4]] | C | DSG4 activity raises KRT6A's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 3.86× lower at baseline in the lines without DSG4 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031; co-absent with the target |
| [[TRIM29]] | C | TRIM29 activity raises KRT6A's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.53× lower at baseline in the lines without TRIM29 | 0.019 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2; co-absent with the target |
| [[TTC22]] | C | TTC22 activity raises KRT6A's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 3.04× lower at baseline in the lines without TTC22 | 0.023 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5; co-absent with the target |
| [[KRT16]] | C | KRT16 activity raises KRT6A's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 2.45× lower at baseline in the lines without KRT16 | 0.024 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6; co-absent with the target |
| [[GJB3]] | C | GJB3 activity raises KRT6A's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 2.88× lower at baseline in the lines without GJB3 | 0.024 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10; co-absent with the target |
| [[LINC00520]] | C | LINC00520 activity raises KRT6A's level | lines that do not express LINC00520 (31) vs lines expressing it (19) | 2.40× lower at baseline in the lines without LINC00520 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, LINC00589, LINC02930; co-absent with the target |
| [[S100P]] | C | S100P activity raises KRT6A's level | lines that do not express S100P (34) vs lines expressing it (16) | 2.70× lower at baseline in the lines without S100P | 0.038 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6; co-absent with the target |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 15, C 23. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCR]] | B | KRT6A activity raises BCR's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 2.31× lower at baseline in the lines without KRT6A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[ALS2CL]] | B | KRT6A activity raises ALS2CL's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 3.82× lower at baseline in the lines without KRT6A | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[RREB1]] | B | KRT6A activity raises RREB1's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 1.59× lower at baseline in the lines without KRT6A | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[SFN]] | B | KRT6A activity raises SFN's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 5.72× lower at baseline in the lines without KRT6A | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[ABLIM2]] | B | KRT6A activity raises ABLIM2's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 3.37× lower at baseline in the lines without KRT6A | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[ITPK1]] | B | KRT6A activity raises ITPK1's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 2.57× lower at baseline in the lines without KRT6A | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[PKP2]] | B | KRT6A activity raises PKP2's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 3.97× lower at baseline in the lines without KRT6A | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[PITPNM3]] | B | KRT6A activity strengthens PITPNM3's drug response | lines that do not express KRT6A (35) vs lines expressing it (7) | the lines without KRT6A respond 0.52× as strongly (z diff +1.83); strongest at Panobinostat 0.5 µM: 0.59x vs 0.25x (z diff +4.2) | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588; target measured in part of the lines; artifact flags |
| [[PHLDB2]] | B | KRT6A activity raises PHLDB2's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 1.93× lower at baseline in the lines without KRT6A | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[EFNB2]] | B | KRT6A activity raises EFNB2's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 4.09× lower at baseline in the lines without KRT6A | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[GAREM1]] | B | KRT6A activity raises GAREM1's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 2.84× lower at baseline in the lines without KRT6A | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[MPRIP]] | B | KRT6A activity weakens MPRIP's drug response | lines that do not express KRT6A (41) vs lines expressing it (8) | the lines without KRT6A respond 1.04× as strongly (z diff -0.16); strongest at Belinostat 5 µM: 1.23x vs 0.73x (z diff -5.9) | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.440). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.8, 51.2); signed map (3.6, 36.6). **Vector** length 44.7, 20.5% of its response variance represented; |z| ≥ 3 in 278 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +1.8 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +8.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +1.5 | +8.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.4 | +3.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.3 | +5.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.2 | +5.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.2 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.5 | -0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.8 | +0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | +0.1 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.8 | -0.7 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -0.7 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | keratin 6A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:52,487,176-52,493,257 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CK6C, K6C, CK6D, K6D; previously KRT6C, KRT6D |
| Gene groups (HGNC) | Keratins, type II |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [P02538](https://www.uniprot.org/uniprotkb/P02538) (Keratin, type II cytoskeletal 6A):

> Structural component of intermediate filaments in epithelial keratinocytes. Forms heteropolymers with the type I keratins KRT16 and KRT17, assembling into keratin intermediate filament networks that contribute to the structural integrity and stress resilience of stratified epithelia, particularly in epidermis, nail bed and oral mucosa. Rapidly induced in wound-edge keratinocytes and participates in cytoskeletal reorganization during re-epithelialization (By similarity). Negatively regulates …

**Summary**, from NCBI Gene [3853](https://www.ncbi.nlm.nih.gov/gene/3853):

> The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. As many as six of this type II cytokeratin (KRT6) have been identified; the multiplicity of the genes is attributed to successive gene duplication events. The genes are expressed with family members KRT16 and/or KRT17 in the …

**Accessions** — [HGNC:6443](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6443) · Entrez [3853](https://www.ncbi.nlm.nih.gov/gene/3853) · UniProt [P02538](https://www.uniprot.org/uniprotkb/P02538) · Ensembl [ENSG00000205420](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205420)

## Data

Gene col 12977: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12977); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12977, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12977]; `tensor/DDL_lfc|DDL_z.npy` [12977]; `embed/gene_vectors.npy` [12977]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12977 or target_col == 12977). Every well: [[KRT6A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT6A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
