---
symbol: "SLC7A2"
type: "gene"
col: 39
ensembl_id: "ENSG00000003989"
name: "solute carrier family 7 member 2"
location: "8p22"
module: 104
arm: "+"
pooled_cpm: 59.49
n_lines_expressing: 20
n_dd_up: 34
n_dd_down: 2
n_dd_up_clean: 29
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 12
direction_downstream: 12
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# SLC7A2

*solute carrier family 7 member 2* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.71× (z +10.3, q 4e-22, up in 5 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.82× (z +8.8, q 4e-16, up in 10 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Mebendazole (drug)]] 5 µM: 0.687× (z -3.7, q 0.094, down in 6 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H460 0.147×, BT-474 0.142×, SHP-77 0.287×; ⚠ cell-cycle shift, explains ~8% of this change); [[Auranofin (drug)]] 5 µM in 3 lines (SHP-77 0.141×, BT-474 0.184×, SW 900 0.168×); [[Panobinostat (drug)]] 5 µM in 3 lines (NCI-H460 0.154×, BT-474 0.229×, SHP-77 0.316×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (BT-474 0.155×, NCI-H460 0.187×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTMR7]] (+0.77, fdr 7e-06), [[PDK4]] (+0.62, fdr 1e-05), [[ATOH8]] (+0.62, fdr 1e-05); moves opposite to [[AZIN2]] (-0.48, fdr 5e-05), [[KCNMA1]] (-0.46, fdr 3e-05), [[LTBP4]] (-0.44, fdr 3e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SOX6]] → it (grade B ⚠); 12 go from it, the strongest it → [[HS3ST3B1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 39.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +10.3 | 4e-22 | 5/17 (C-33 A, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +8.8 | 4e-16 | 10/18 (A549, H4, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +7.8 | 1e-12 | 2/12 (H4, A549) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.11×** | +7.7 | 2e-12 | 14/17 (H4, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.95×** | +6.9 | 6e-10 | 10/17 (H4, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.94×** | +6.9 | 6e-10 | 9/17 (H4, HS-578T, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +6.7 | 2e-09 | 6/18 (C-33 A, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +6.5 | 5e-09 | 2/13 (CHP-212, hTERT-HPNE) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Budesonide (drug)]] 0.05 µM |  | **1.79×** | +6.0 | 1e-07 | 8/17 (H4, HS-578T, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.74×** | +5.7 | 5e-07 | 10/17 (HS-578T, H4, …) | two highest doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.73×** | +5.7 | 7e-07 | 9/20 (H4, HS-578T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.46×** | +5.5 | 2e-06 | 9/18 (HS-578T, H4, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.69×** | +5.4 | 2e-06 | 6/17 (H4, HS-578T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.68×** | +5.4 | 3e-06 | 8/17 (H4, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.63×** | +5.1 | 2e-05 | 10/18 (H4, HS-578T, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.9 | 3e-05 | 8/17 (H4, HS-578T, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.63×** | +4.8 | 4e-05 | 6/18 (H4, HS-578T, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +4.7 | 8e-05 | 9/18 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 39.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H460 0.147×, BT-474 0.142×, SHP-77 0.287×; ⚠ cell-cycle shift, explains ~8% of this change); [[Auranofin (drug)]] 5 µM in 3 lines (SHP-77 0.141×, BT-474 0.184×, SW 900 0.168×); [[Panobinostat (drug)]] 5 µM in 3 lines (NCI-H460 0.154×, BT-474 0.229×, SHP-77 0.316×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (BT-474 0.155×, NCI-H460 0.187×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | **0.687×** | -3.7 | 0.094 | 6/18 (SHP-77, SW 900, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.707×** | -3.6 | 0.094 | 7/17 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.730× | -3.3 | 0.13 | 8/17 (SHP-77, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.732× | -3.2 | 0.13 | 7/17 (NCI-H460, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | 0.550× | -3.2 | 0.13 | 6/17 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.716× | -3.2 | 0.13 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 39. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 43.3 | 20 | 0 | [[Triamcinolone (drug)]] 5 µM 10.6× (z +13.0) | — |
| [[HS-578T (line)]] | alt | 106 | 17 | 0 | [[Triamcinolone (drug)]] 5 µM 12.6× (z +13.4) | — |
| [[SHP-77 (line)]] | alt | 512 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -19.0) |
| [[BT-474 (line)]] | alt | 265 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -17.6) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.155× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 578 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -18.8) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.154× (z -13.0) |
| [[SW 900 (line)]] | alt | 89.2 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0891× (z -11.2) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.120× (z -10.4) |
| [[A-427 (line)]] | wt | 24.8 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0612× (z -18.6) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.379× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 232 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 35.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +13.1) | — |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 1 | 0 | [[Triamcinolone (drug)]] 5 µM 10.6× (z +10.7) | — |
| [[A-172 (line)]] | wt | 6.71 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.91 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.05 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.12 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.76 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.04 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.85 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.81 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.57 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.96 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.73 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.33 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.01 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 14.1 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.76 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 39), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR7]] | +0.77 | +0.69 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PDK4]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[ATOH8]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[IL1R1]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[DNAH5]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[PDGFRL]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 | ⚠ same locus (5.9 kb, same strand: neighbours can correlate without regulation) |
| [[ADGRD1]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[PID1]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LIN7A]] | +0.59 | +0.42 / +0.71 | both halves | 4e-05 |  |
| [[CAVIN2]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SRGN]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RTN1]] | +0.58 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[JPH2]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AZIN2]] | -0.48 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[KCNMA1]] | -0.46 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[LTBP4]] | -0.44 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[MMP1]] | -0.44 | -0.46 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 3, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOX6]] | B | SOX6 activity raises SLC7A2's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 2.48× lower at baseline in the lines without SOX6 | 0.014 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[HS3ST3B1]] | B | HS3ST3B1 activity raises SLC7A2's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 2.81× lower at baseline in the lines without HS3ST3B1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[ADAMTS9]] | B | ADAMTS9 activity raises SLC7A2's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 2.06× lower at baseline in the lines without ADAMTS9 | 0.072 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[LIN7A]] | C | LIN7A activity raises SLC7A2's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 4.71× lower at baseline in the lines without LIN7A | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[NRCAM]] | C | NRCAM activity raises SLC7A2's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 5.08× lower at baseline in the lines without NRCAM | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG; co-absent with the target |
| [[ADGRD1]] | C | ADGRD1 activity raises SLC7A2's level | lines that do not express ADGRD1 (37) vs lines expressing it (13) | 4.36× lower at baseline in the lines without ADGRD1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises SLC7A2's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 6.03× lower at baseline in the lines without RIT2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[PDGFRL]] | C | PDGFRL activity raises SLC7A2's level | lines that do not express PDGFRL (16) vs lines expressing it (34) | 4.02× lower at baseline in the lines without PDGFRL | 0.044 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ITPR1, TOX2; co-absent with the target |
| [[FGL1]] | C | FGL1 activity raises SLC7A2's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 4.56× lower at baseline in the lines without FGL1 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[LINC00824]] | C | LINC00824 activity raises SLC7A2's level | lines that do not express LINC00824 (46) vs lines expressing it (4) | 12.78× lower at baseline in the lines without LINC00824 | 0.093 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SUCNR1, ENSG00000289530; co-absent with the target |
| [[RTN1]] | C | RTN1 activity raises SLC7A2's level | lines that do not express RTN1 (31) vs lines expressing it (19) | 1.92× lower at baseline in the lines without RTN1 | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC01010, RIT2, ENSG00000289530; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises SLC7A2's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 6.19× lower at baseline in the lines without LINC03000 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HS3ST3B1]] | B | SLC7A2 activity raises HS3ST3B1's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without SLC7A2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| [[HECW2]] | B | SLC7A2 activity raises HECW2's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 2.99× lower at baseline in the lines without SLC7A2 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| [[CCND3]] | B | SLC7A2 activity lowers CCND3's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 1.21× higher at baseline in the lines without SLC7A2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| [[MTMR7]] | B | SLC7A2 activity raises MTMR7's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 2.25× lower at baseline in the lines without SLC7A2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| [[ELMO1]] | B | SLC7A2 activity raises ELMO1's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 2.46× lower at baseline in the lines without SLC7A2 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| [[SOX6]] | B | SLC7A2 activity raises SOX6's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 1.54× lower at baseline in the lines without SLC7A2 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| cells under [[Pimozide (drug)]] 0.5 µM | B | SLC7A2 activity lowers the cells' numbers under Pimozide 0.5 µM (makes them more sensitive) | lines that do not express SLC7A2 (30) vs lines expressing it (18) | the lines without SLC7A2: 1.15× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| [[BCL6]] | B | SLC7A2 activity raises BCL6's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 1.24× lower at baseline in the lines without SLC7A2 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| [[PDGFRL]] | C | SLC7A2 activity raises PDGFRL's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 3.13× lower at baseline in the lines without SLC7A2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D; co-absent with the target |
| [[KCNK2]] | C | SLC7A2 activity raises KCNK2's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 2.00× lower at baseline in the lines without SLC7A2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D; co-absent with the target |
| [[DCN]] | C | SLC7A2 activity raises DCN's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without SLC7A2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D; co-absent with the target |
| [[LIN7A]] | C | SLC7A2 activity raises LIN7A's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 3.20× lower at baseline in the lines without SLC7A2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.584). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.2, 18.0); signed map (19.1, 31.4). **Vector** length 83.3, 26.5% of its response variance represented; |z| ≥ 3 in 683 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +6.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.0 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +7.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.5 | +6.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.4 | +6.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.0 | +5.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.9 | +6.9 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 7 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:17,497,088-17,570,573 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAT-2, HCAT2, SLC7A2A, SLC7A2B, CAT-2A, CAT-2B; previously ATRC2 |
| Gene groups (HGNC) | Solute carrier family 7 |
| Hallmark sets | INFLAMMATORY_RESPONSE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P52569](https://www.uniprot.org/uniprotkb/P52569) (Cationic amino acid transporter 2):

> Functions as a permease involved in the transport of the cationic amino acids (L-arginine, L-lysine, L-ornithine and L-homoarginine); the affinity for its substrates differs between isoforms created by alternative splicing. May play a role in classical or alternative activation of macrophages via its role in arginine transport (By similarity).; [Isoform 1]: Functions as a permease that mediates the transport of the cationic amino acids (L-arginine, L-lysine, L-ornithine and L-homoarginine). …

**Summary**, from NCBI Gene [6542](https://www.ncbi.nlm.nih.gov/gene/6542):

> The protein encoded by this gene is a cationic amino acid transporter and a member of the APC (amino acid-polyamine-organocation) family of transporters. The encoded membrane protein is responsible for the cellular uptake of arginine, lysine and ornithine. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:11060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11060) · Entrez [6542](https://www.ncbi.nlm.nih.gov/gene/6542) · UniProt [P52569](https://www.uniprot.org/uniprotkb/P52569) · Ensembl [ENSG00000003989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000003989)

## Data

Gene col 39: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 39); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 39, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 39]; `tensor/DDL_lfc|DDL_z.npy` [39]; `embed/gene_vectors.npy` [39]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 39 or target_col == 39). Every well: [[SLC7A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC7A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
