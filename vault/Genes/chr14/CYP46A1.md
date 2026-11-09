---
symbol: "CYP46A1"
type: "gene"
col: 437
ensembl_id: "ENSG00000036530"
name: "cytochrome P450 family 46 subfamily A member 1"
location: "14q32.2"
module: 1
arm: "-"
pooled_cpm: 3.27
n_lines_expressing: 44
n_dd_up: 27
n_dd_down: 9
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CYP46A1

*cytochrome P450 family 46 subfamily A member 1* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 23.4× (z +27.1, q 0e+00, up in 41 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.502× (z -5.9, q 2e-06, down in 19 of 41 measured lines).
> Its strongest partners by |cos| (50 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 50 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOVA2]] (+0.62, fdr 7e-05), [[DNAAF3]] (+0.57, fdr 0.001, ⚠ one half only (not replicated)), [[SLC17A7]] (+0.56, fdr 1e-04), [[C1QL1]] (+0.55, fdr 1e-04); moves opposite to [[ZNF507]] (-0.56, fdr 0.002, ⚠ one half only (not replicated)), [[EMG1]] (-0.56, fdr 1e-04), [[EEF1AKMT1]] (-0.56, fdr 3e-04), [[SMYD5]] (-0.55, fdr 6e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[TRMT5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **23.4×** | +27.1 | 0e+00 | 41/41 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **21.6×** | +26.4 | 0e+00 | 40/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **13.1×** | +22.1 | 0e+00 | 38/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.25×** | +20.2 | 0e+00 | 26/27 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **6.00×** | +15.4 | 0e+00 | 37/40 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **8.02×** | +9.4 | 8e-19 | 31/36 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.95×** | +9.3 | 1e-18 | 22/30 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.84×** | +8.6 | 5e-16 | 13/24 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +8.0 | 9e-14 | 2/4 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +5.6 | 1e-06 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +5.6 | 1e-06 | 12/40 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +5.5 | 1e-06 | 12/30 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.89×** | +5.4 | 2e-06 | 17/40 (SW480, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +5.4 | 3e-06 | 2/11 (HEC-1-A, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.71×** | +4.5 | 3e-04 | 7/33 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.55×** | +4.2 | 1e-03 | 2/25 (SW480, HEC-1-A) | top dose only | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.54×** | +3.7 | 0.007 | 9/38 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.54×** | +3.7 | 0.007 | 7/36 (NCI-H1573, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 437.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.502×** | -5.9 | 2e-06 | 19/41 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.518×** | -5.7 | 4e-06 | 19/37 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.541×** | -5.3 | 2e-05 | 15/39 (A-427, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.611×** | -4.2 | 0.003 | 13/35 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.407×** | -4.0 | 0.006 | 12/34 (NCI-H2030, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.641×** | -3.8 | 0.012 | 13/39 (NCI-H1792, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.449×** | -3.6 | 0.026 | 11/26 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.661×** | -3.4 | 0.044 | 6/40 (SNU-1, LoVo, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.686×** | -3.2 | 0.073 | 5/39 (A549, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.703× | -3.0 | 0.13 | 11/41 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.704× | -3.0 | 0.13 | 12/40 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.61 | 5 | 1 | [[Panobinostat (drug)]] 0.5 µM 43.1× (z +12.8) | [[Digitoxin (drug)]] 0.05 µM 0.0400× (z -11.0) |
| [[A498 (line)]] | wt | 2.70 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 22.4× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 1.37 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.1× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 2.56 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 37.3× (z +14.0) | — |
| [[A549 (line)]] | wt | 1.94 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.9× (z +10.3) | — |
| [[HEC-1-A (line)]] | alt | 2.44 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 35.2× (z +10.5) | — |
| [[LoVo (line)]] | wt | 3.17 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.38× (z +8.7) | [[Digitoxin (drug)]] 0.5 µM 0.0411× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 2.88 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 34.8× (z +10.5) | — |
| [[A-172 (line)]] | wt | 3.32 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 17.7× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 2.80 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 20.9× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 2.10 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 46.9× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 3.91 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 26.5× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 1.15 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 56.4× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 1.59 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 34.6× (z +8.6) | — |
| [[A-427 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.688 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.644 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 26 of them with an alert (⚠; 26 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOVA2]] | +0.62 | +0.50 / +0.38 | both halves | 7e-05 |  |
| [[DNAAF3]] | +0.57 | +0.18 / +0.58 | ⚠ one half (not replicated) | 0.001 |  |
| [[SLC17A7]] | +0.56 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[C1QL1]] | +0.55 | +0.35 / +0.38 | both halves | 1e-04 |  |
| [[PDZD7]] | +0.55 | +0.21 / +0.59 | both halves | 6e-04 |  |
| [[KIFC2]] | +0.54 | +0.32 / +0.44 | both halves | 2e-04 |  |
| [[SEZ6L2]] | +0.53 | +0.26 / +0.42 | both halves | 4e-04 |  |
| [[RRAS]] | +0.53 | +0.14 / +0.36 | ⚠ not reproduced | 0.002 |  |
| [[PCSK1N]] | +0.53 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[FOXO6]] | +0.53 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[GNAI2]] | +0.52 | +0.12 / +0.38 | ⚠ not reproduced | 0.002 |  |
| [[KMT2C]] | +0.52 | +0.38 / +0.39 | both halves | 7e-05 |  |
| [[ETFBKMT]] | +0.52 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[CYP2U1-AS1]] | +0.52 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[GAMT]] | +0.51 | +0.41 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 24 of them with an alert (⚠; 24 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF507]] | -0.56 | -0.12 / -0.54 | ⚠ one half (not replicated) | 0.002 |  |
| [[EMG1]] | -0.56 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[EEF1AKMT1]] | -0.56 | -0.33 / -0.27 | both halves | 3e-04 |  |
| [[DPH5-DT]] | -0.56 | -0.04 / -0.45 | ⚠ not reproduced | 0.006 |  |
| [[SMYD5]] | -0.55 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[TRMT5]] | -0.55 | -0.13 / -0.45 | ⚠ not reproduced | 0.002 |  |
| [[METTL8]] | -0.54 | -0.24 / -0.36 | both halves | 5e-04 |  |
| [[PPIL1]] | -0.54 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[UTP20]] | -0.53 | -0.16 / -0.48 | ⚠ not reproduced | 0.001 |  |
| [[GPATCH4]] | -0.53 | -0.16 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[QSER1]] | -0.53 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[GCFC2]] | -0.53 | -0.10 / -0.28 | ⚠ not reproduced | 0.003 |  |
| [[TYW3]] | -0.53 | -0.25 / -0.28 | both halves | 4e-04 |  |
| [[DNAJC11]] | -0.52 | -0.22 / -0.38 | both halves | 6e-04 |  |
| [[ANAPC1]] | -0.52 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[ABCE1]] | -0.52 | -0.21 / -0.49 | both halves | 6e-04 |  |
| [[MLH3]] | -0.52 | -0.22 / -0.39 | both halves | 6e-04 |  |
| [[HDDC2]] | -0.52 | -0.20 / -0.36 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CYP46A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GAMT]] | B | GAMT activity raises CYP46A1's level | lines that do not express GAMT (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without GAMT | 0.088 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers CYP46A1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRMT5]] | B | CYP46A1 activity raises TRMT5's level | lines that do not express CYP46A1 (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without CYP46A1 | 0.038 | ⚠ within organs, on part of the lines; also absent: CCDC102A, TPST1, DZIP1L; maybe low, not absent |
| [[TYW3]] | B | CYP46A1 activity raises TYW3's level | lines that do not express CYP46A1 (6) vs lines expressing it (44) | 1.55× lower at baseline in the lines without CYP46A1 | 0.072 | ⚠ within organs, on part of the lines; also absent: CCDC102A, TPST1, DZIP1L; maybe low, not absent |
| [[MLH3]] | B | CYP46A1 activity raises MLH3's level | lines that do not express CYP46A1 (6) vs lines expressing it (44) | 1.38× lower at baseline in the lines without CYP46A1 | 0.079 | ⚠ within organs, on part of the lines; also absent: CCDC102A, TPST1, DZIP1L; maybe low, not absent |
| [[NECTIN2]] | B | CYP46A1 activity lowers NECTIN2's level | lines that do not express CYP46A1 (6) vs lines expressing it (44) | 1.81× higher at baseline in the lines without CYP46A1 | 0.084 | ⚠ within organs, on part of the lines; also absent: CCDC102A, TPST1, DZIP1L; maybe low, not absent |
| [[ANAPC1]] | B | CYP46A1 activity raises ANAPC1's level | lines that do not express CYP46A1 (6) vs lines expressing it (44) | 1.44× lower at baseline in the lines without CYP46A1 | 0.086 | ⚠ within organs, on part of the lines; also absent: CCDC102A, TPST1, DZIP1L; maybe low, not absent |
| [[SNHG26]] | B | CYP46A1 activity raises SNHG26's level | lines that do not express CYP46A1 (6) vs lines expressing it (44) | 2.76× lower at baseline in the lines without CYP46A1 | 0.097 | ⚠ within organs, on part of the lines; also absent: CCDC102A, TPST1, DZIP1L; maybe low, not absent |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (6.4, -3.0); signed map (-29.3, 20.3). **Vector** length 44.4, 5.46% of its response variance represented; |z| ≥ 3 in 1,128 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +26.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +5.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +27.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +5.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +1.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 46 subfamily A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:99,684,298-99,727,301 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CYP46 |
| Gene groups (HGNC) | Cytochrome P450 family 46 |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 9 pathways, smallest: Synthesis of bile acids and bile salts via 24-hydroxycholesterol; Endogenous sterols; Synthesis of bile acids and bile salts |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6A2](https://www.uniprot.org/uniprotkb/Q9Y6A2) (Cholesterol 24-hydroxylase):

> P450 monooxygenase that plays a major role in cholesterol homeostasis in the brain. Primarily catalyzes the hydroxylation (with S stereochemistry) at C-24 of cholesterol side chain, triggering cholesterol diffusion out of neurons and its further degradation. By promoting constant cholesterol elimination in neurons, may activate the mevalonate pathway and coordinate the synthesis of new cholesterol and nonsterol isoprenoids involved in synaptic activity and learning (By similarity). Further …

**Summary**, from NCBI Gene [10858](https://www.ncbi.nlm.nih.gov/gene/10858):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This endoplasmic reticulum protein is expressed in the brain, where it converts cholesterol to 24S-hydroxycholesterol. While cholesterol cannot pass the blood-brain barrier, 24S-hydroxycholesterol can be secreted in the brain into the circulation to be returned …

**Accessions** — [HGNC:2641](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2641) · Entrez [10858](https://www.ncbi.nlm.nih.gov/gene/10858) · UniProt [Q9Y6A2](https://www.uniprot.org/uniprotkb/Q9Y6A2) · Ensembl [ENSG00000036530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000036530)

## Data

Gene col 437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 437); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 437]; `tensor/DDL_lfc|DDL_z.npy` [437]; `embed/gene_vectors.npy` [437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 437 or target_col == 437). Every well: [[CYP46A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP46A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
