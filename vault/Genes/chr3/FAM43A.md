---
symbol: "FAM43A"
type: "gene"
col: 11627
ensembl_id: "ENSG00000185112"
name: "family with sequence similarity 43 member A"
location: "3q29"
module: 112
arm: "+"
pooled_cpm: 9.07
n_lines_expressing: 36
n_dd_up: 17
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 6
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# FAM43A

*family with sequence similarity 43 member A* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.93× (z +16.3, q 0e+00, up in 26 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.557× (z -4.9, q 5e-04, down in 19 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IER3]] (+0.70, fdr 7e-06), [[FZD8]] (+0.67, fdr 7e-06), [[SERTAD1]] (+0.67, fdr 7e-06); moves opposite to [[LARP1]] (-0.55, fdr 1e-05), [[PHKB]] (-0.53, fdr 1e-05), [[NAA50]] (-0.53, fdr 2e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LHX1]] → it (grade B ⚠); 6 go from it, the strongest it → [[LARP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11627.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.93×** | +16.3 | 0e+00 | 26/30 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.00×** | +9.1 | 2e-17 | 12/23 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +8.6 | 2e-15 | 22/33 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.76×** | +8.5 | 2e-15 | 21/30 (C32, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.40×** | +7.1 | 2e-10 | 5/15 (C32, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.31×** | +6.8 | 1e-09 | 21/31 (HS-578T, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.12×** | +6.3 | 2e-08 | 15/34 (SW1417, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +6.2 | 5e-08 | 17/32 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.1 | 7e-08 | 14/30 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.99×** | +5.4 | 4e-06 | 6/19 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.1 | 2e-05 | 12/26 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +4.6 | 2e-04 | 18/33 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +4.4 | 5e-04 | 13/33 (J82, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +4.2 | 0.001 | 18/32 (HS-578T, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.58×** | +3.9 | 0.004 | 9/28 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.004 | 9/33 (J82, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.3 | 0.035 | 8/34 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11627.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.557×** | -4.9 | 5e-04 | 19/33 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.581×** | -4.4 | 0.003 | 14/32 (AsPC-1, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.583×** | -4.3 | 0.003 | 17/34 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.702×** | -4.1 | 0.006 | 19/33 (AsPC-1, J82, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.646×** | -3.6 | 0.026 | 15/34 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.633×** | -3.6 | 0.026 | 17/32 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.651×** | -3.6 | 0.026 | 9/32 (H4, HOP62, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.633×** | -3.5 | 0.028 | 15/34 (SW48, AsPC-1, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.660×** | -3.5 | 0.032 | 15/34 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.684×** | -3.2 | 0.080 | 8/32 (KATO III, NCI-H1792, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.744×** | -3.2 | 0.080 | 13/32 (AsPC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | **0.685×** | -3.1 | 0.081 | 6/32 (C32, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11627. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 36.7 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +16.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0738× (z -14.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 26.6 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +9.0) | [[Adagrasib (drug)]] 0.05 µM 0.550× (z -10.1) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.138× (z -9.3) |
| [[H4 (line)]] | wt | 41.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0968× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.05 µM 0.109× (z -9.7) |
| [[HS-578T (line)]] | alt | 16.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +13.4) | — |
| [[A498 (line)]] | wt | 5.99 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.90× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 3.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 9.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +14.6) | — |
| [[HepG2_C3A (line)]] | wt | 5.22 | 0 | 1 | — | [[Binimetinib (drug)]] 5 µM 0.0256× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 5.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.4× (z +13.3) | — |
| [[J82 (line)]] | alt | 5.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +11.8) | — |
| [[KATO III (line)]] | alt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 6.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -8.5) ⚠ toxic |
| [[SW 900 (line)]] | alt | 6.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +8.9) | — |
| [[SW48 (line)]] | wt | 13.8 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0443× (z -9.0) |
| [[A-172 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11627), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER3]] | +0.70 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[FZD8]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SERTAD1]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[IER2]] | +0.65 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[EHD1]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.65 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[BCL2A1]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[IRAK2]] | +0.64 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[PHLDA1]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[BTG1]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PHLDA2]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[MAST4]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP1]] | -0.55 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[PHKB]] | -0.53 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[NAA50]] | -0.53 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[GAPVD1]] | -0.53 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[ADPGK]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ANP32B]] | -0.52 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LHX1]] | B | LHX1 activity raises FAM43A's level | lines that do not express LHX1 (27) vs lines expressing it (23) | 1.82× lower at baseline in the lines without LHX1 | 0.072 | ⚠ within organs, on part of the lines; also absent: LHX1-DT, ADAMTS16, ECSCR |
| [[PHLDA1]] | B | PHLDA1 activity raises FAM43A's level | lines that do not express PHLDA1 (5) vs lines expressing it (45) | 2.66× lower at baseline in the lines without PHLDA1 | 0.075 | ⚠ within organs, on part of the lines; also absent: DPYSL2, PARP3, C1RL; maybe low, not absent |
| [[LIF]] | B | LIF activity raises FAM43A's level | lines that do not express LIF (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without LIF | 0.084 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[CD82]] | B | CD82 activity raises FAM43A's level | lines that do not express CD82 (11) vs lines expressing it (39) | 2.36× lower at baseline in the lines without CD82 | 0.089 | ⚠ within organs, on part of the lines; also absent: ITGA3, GBP3, CXCL3; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises FAM43A's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ARL4C]] | B | ARL4C activity raises FAM43A's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 2.23× lower at baseline in the lines without ARL4C | 0.098 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |
| [[SYNJ2]] | C | SYNJ2 activity raises FAM43A's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 2.57× lower at baseline in the lines without SYNJ2 | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LARP1]] | B | FAM43A activity lowers LARP1's level | lines that do not express FAM43A (14) vs lines expressing it (36) | 1.31× higher at baseline in the lines without FAM43A | 0.031 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ZNF697]] | B | FAM43A activity raises ZNF697's level | lines that do not express FAM43A (14) vs lines expressing it (36) | 1.81× lower at baseline in the lines without FAM43A | 0.045 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DNAH17]] | B | FAM43A activity raises DNAH17's level | lines that do not express FAM43A (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without FAM43A | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SYNJ2]] | B | FAM43A activity raises SYNJ2's level | lines that do not express FAM43A (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without FAM43A | 0.061 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CD163L1]] | B | FAM43A activity raises CD163L1's level | lines that do not express FAM43A (14) vs lines expressing it (36) | 2.12× lower at baseline in the lines without FAM43A | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SHB]] | B | FAM43A activity raises SHB's level | lines that do not express FAM43A (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without FAM43A | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.8, -0.1); signed map (2.3, 43.7). **Vector** length 86.9, 21.5% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.56 to 11); *Interleukin-10 signaling* (reactome, mean cos +0.56 to 5); *KRAS signaling up* (hallmark, mean cos +0.54 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +16.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +5.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.6 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.3 | +2.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.6 | -3.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.2 | -4.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.1 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 43 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:194,685,883-194,689,037 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90022 |
| Matched by | ensembl_id |

UniProt [Q8N2R8](https://www.uniprot.org/uniprotkb/Q8N2R8) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26888](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26888) · Entrez [131583](https://www.ncbi.nlm.nih.gov/gene/131583) · UniProt [Q8N2R8](https://www.uniprot.org/uniprotkb/Q8N2R8) · Ensembl [ENSG00000185112](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185112)

## Data

Gene col 11627: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11627); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11627, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11627]; `tensor/DDL_lfc|DDL_z.npy` [11627]; `embed/gene_vectors.npy` [11627]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11627 or target_col == 11627). Every well: [[FAM43A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM43A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
