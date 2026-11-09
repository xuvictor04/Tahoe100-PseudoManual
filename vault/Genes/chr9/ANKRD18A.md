---
symbol: "ANKRD18A"
type: "gene"
col: 11078
ensembl_id: "ENSG00000180071"
name: "ankyrin repeat domain 18A"
location: "9p13.1"
module: 124
arm: "+"
pooled_cpm: 33.88
n_lines_expressing: 39
n_dd_up: 26
n_dd_down: 10
n_dd_up_clean: 20
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# ANKRD18A

*ankyrin repeat domain 18A* — 9p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +13.0, q 1e-35, up in 27 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.467× (z -14.3, q 1e-43, down in 36 of 37 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM26-AS1]] (+0.71, fdr 6e-05), [[WARS2-AS1]] (+0.70, fdr 2e-04), [[ST7L]] (+0.70, fdr 4e-05); moves opposite to [[MOSPD3]] (-0.69, fdr 1e-05), [[YIF1B]] (-0.66, fdr 5e-04), [[SLC27A1]] (-0.65, fdr 3e-04).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[ZNF518A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11078.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +13.0 | 1e-35 | 27/37 (HT-29, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +10.5 | 4e-23 | 25/36 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +10.0 | 2e-21 | 31/37 (PANC-1, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +9.6 | 1e-19 | 17/28 (SW 900, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +8.7 | 3e-16 | 29/37 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +8.5 | 2e-15 | 21/35 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +8.4 | 3e-15 | 20/34 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +7.6 | 2e-12 | 24/37 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +5.5 | 2e-06 | 17/33 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.2 | 1e-05 | 18/36 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +5.2 | 1e-05 | 19/36 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.9 | 4e-05 | 20/37 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.9 | 4e-05 | 17/37 (Hs 766T, COLO 205, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +4.8 | 5e-05 | 17/37 (NCI-H1573, Panc 03.27, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **1.27×** | +4.3 | 7e-04 | 11/35 (J82, A-427, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.002 | 13/37 (HT-29, HS-578T, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.002 | 12/36 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.003 | 15/36 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.003 | 11/35 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.004 | 14/37 (KATO III, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11078.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.467×** | -14.3 | 1e-43 | 36/37 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.510×** | -12.7 | 3e-34 | 29/37 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.547×** | -11.3 | 2e-27 | 31/37 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.595×** | -9.2 | 5e-18 | 27/36 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -7.8 | 7e-13 | 25/37 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.467×** | -7.5 | 7e-12 | 29/36 (RKO, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.676×** | -7.4 | 2e-11 | 24/37 (LS 180, HCT15, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.484×** | -7.1 | 8e-11 | 25/37 (RKO, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.781×** | -4.7 | 2e-04 | 15/36 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.806×** | -4.1 | 0.003 | 16/37 (RKO, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -3.6 | 0.015 | 0/37 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11078. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 72.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.07× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -16.7) |
| [[SNU-1 (line)]] | wt | 73.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.290× (z -9.4) |
| [[A498 (line)]] | wt | 68.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -14.7) |
| [[A549 (line)]] | wt | 96.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -12.6) |
| [[LoVo (line)]] | wt | 40.6 | 1 | 2 | [[Harringtonine (drug)]] 5 µM 2.54× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.410× (z -8.8) |
| [[SW480 (line)]] | alt | 84.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -19.8) |
| [[COLO 205 (line)]] | alt | 81.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -11.3) |
| [[HT-29 (line)]] | alt | 21.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +12.5) | — |
| [[LS 180 (line)]] | wt | 35.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.1) | [[Ixazomib citrate (drug)]] 0.5 µM 0.317× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 11.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.92× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.81× (z +10.4) | — |
| [[RKO (line)]] | wt | 94.1 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.121× (z -9.8) |
| [[SW 900 (line)]] | alt | 43.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 29.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 33.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +12.3) | — |
| [[Hs 766T (line)]] | wt | 46.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +8.6) | — |
| [[KATO III (line)]] | alt | 30.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.352× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -11.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 37.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.5) | — |
| [[A-172 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.81 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.38 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.60 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.97 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.69 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.13 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11078), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM26-AS1]] | +0.71 | +0.70 / +0.39 | both halves | 6e-05 |  |
| [[WARS2-AS1]] | +0.70 | +0.68 / +0.32 | both halves | 2e-04 |  |
| [[ST7L]] | +0.70 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[POGLUT1]] | +0.69 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[RXYLT1]] | +0.69 | +0.67 / +0.26 | both halves | 4e-04 |  |
| [[ZNF337-AS1]] | +0.68 | +0.65 / +0.31 | both halves | 2e-04 |  |
| [[ITPA]] | +0.67 | +0.62 / +0.36 | both halves | 1e-04 |  |
| [[GCFC2]] | +0.67 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[SNX5]] | +0.66 | +0.59 / +0.35 | both halves | 1e-04 |  |
| [[RFX3-DT]] | +0.65 | +0.63 / +0.20 | ⚠ one half (not replicated) | 7e-04 |  |
| [[ZC3H7B]] | +0.65 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[IQCH-AS1]] | +0.65 | +0.66 / +0.24 | both halves | 5e-04 |  |
| [[GYG1]] | +0.64 | +0.65 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOSPD3]] | -0.69 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[YIF1B]] | -0.66 | -0.60 / -0.23 | both halves | 5e-04 |  |
| [[SLC27A1]] | -0.65 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[TMEM256]] | -0.65 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[RNF41]] | -0.64 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[TPRG1L]] | -0.63 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[YIPF1]] | -0.63 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[IGSF8]] | -0.63 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[RRAS]] | -0.63 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[METTL26]] | -0.63 | -0.58 / -0.23 | both halves | 5e-04 |  |
| [[SNRPD2]] | -0.63 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[ANKRD27]] | -0.62 | -0.58 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[MRPL55]] | -0.62 | -0.51 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANKRD18A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CACHD1]] | B | CACHD1 activity raises ANKRD18A's level | lines that do not express CACHD1 (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without CACHD1 | 0.086 | ⚠ within organs, on part of the lines; also absent: KCNK15-AS1 |
| [[HDAC6]] | B | HDAC6 activity raises ANKRD18A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises ANKRD18A's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ADAL]] | C | ADAL activity strengthens ANKRD18A's drug response | lines that do not express ADAL (3) vs lines expressing it (34) | the lines without ADAL respond 0.81× as strongly (z diff +0.91); strongest at Homoharringtonine 5 µM: 0.76x vs 1.71x (z diff +7.9) | 0.086 | ⚠ few lines (3 vs 47); across organs; co-occurs with EP300, RNF43, MSH6; also absent: SPAG4, PDE4A, ZNF532; target measured in part of the lines; artifact flags |
| [[LGALSL-DT]] | C | LGALSL-DT activity raises ANKRD18A's level | lines that do not express LGALSL-DT (4) vs lines expressing it (46) | 3.55× lower at baseline in the lines without LGALSL-DT | 0.098 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF518A]] | B | ANKRD18A activity raises ZNF518A's level | lines that do not express ANKRD18A (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without ANKRD18A | 0.037 | ⚠ within organs, on part of the lines; also absent: LRRC61, SLC27A2, CHMP4C |
| [[SLC35F2]] | B | ANKRD18A activity raises SLC35F2's level | lines that do not express ANKRD18A (11) vs lines expressing it (39) | 1.89× lower at baseline in the lines without ANKRD18A | 0.047 | ⚠ within organs, on part of the lines; also absent: LRRC61, SLC27A2, CHMP4C |
| [[P2RY11]] | B | ANKRD18A activity raises P2RY11's level | lines that do not express ANKRD18A (11) vs lines expressing it (39) | 1.04× lower at baseline in the lines without ANKRD18A | 0.063 | ⚠ within organs, on part of the lines; also absent: LRRC61, SLC27A2, CHMP4C |
| [[GNAI2]] | B | ANKRD18A activity lowers GNAI2's level | lines that do not express ANKRD18A (11) vs lines expressing it (39) | 2.07× higher at baseline in the lines without ANKRD18A | 0.067 | ⚠ within organs, on part of the lines; also absent: LRRC61, SLC27A2, CHMP4C |
| [[IQCH-AS1]] | B | ANKRD18A activity raises IQCH-AS1's level | lines that do not express ANKRD18A (11) vs lines expressing it (39) | 1.71× lower at baseline in the lines without ANKRD18A | 0.076 | ⚠ within organs, on part of the lines; also absent: LRRC61, SLC27A2, CHMP4C |
| [[NAPEPLD]] | B | ANKRD18A activity raises NAPEPLD's level | lines that do not express ANKRD18A (11) vs lines expressing it (39) | 1.25× lower at baseline in the lines without ANKRD18A | 0.077 | ⚠ within organs, on part of the lines; also absent: LRRC61, SLC27A2, CHMP4C |
| [[TBC1D22A]] | B | ANKRD18A activity raises TBC1D22A's level | lines that do not express ANKRD18A (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without ANKRD18A | 0.092 | ⚠ within organs, on part of the lines; also absent: LRRC61, SLC27A2, CHMP4C |

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.739). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-1.3, 7.0); signed map (21.8, -32.7). **Vector** length 104, 26.6% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +13.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +8.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.4 | +4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +3.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.8 | -14.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.2 | -12.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.7 | -11.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.1 | -7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.9 | -9.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -7.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 18A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.1 — chr9:38,540,567-38,620,596 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA2015, FLJ35740 |
| Gene groups (HGNC) | N-Ank proteins |
| Matched by | ensembl_id |

UniProt [Q8IVF6](https://www.uniprot.org/uniprotkb/Q8IVF6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23643](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23643) · Entrez [253650](https://www.ncbi.nlm.nih.gov/gene/253650) · UniProt [Q8IVF6](https://www.uniprot.org/uniprotkb/Q8IVF6) · Ensembl [ENSG00000180071](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180071)

## Data

Gene col 11078: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11078); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11078, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11078]; `tensor/DDL_lfc|DDL_z.npy` [11078]; `embed/gene_vectors.npy` [11078]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11078 or target_col == 11078). Every well: [[ANKRD18A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD18A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
