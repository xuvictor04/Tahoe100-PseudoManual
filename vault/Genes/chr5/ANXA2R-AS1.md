---
symbol: "ANXA2R-AS1"
type: "gene"
col: 13244
ensembl_id: "ENSG00000215068"
name: "ANXA2R antisense RNA 1"
location: "5p12"
module: 46
arm: "+"
pooled_cpm: 10.76
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 17
n_dd_up_clean: 25
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ANXA2R-AS1

*ANXA2R antisense RNA 1* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.73× (z +18.5, q 0e+00, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.506× (z -6.4, q 1e-07, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (70 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 30 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PATL2]] (+0.74, fdr 8e-05), [[PKN2-AS1]] (+0.73, fdr 4e-05), [[TAFA2]] (+0.73, fdr 5e-05); moves opposite to [[CLTCL1]] (-0.67, fdr 7e-05), [[ANKRD27]] (-0.66, fdr 7e-04), [[NBPF3]] (-0.66, fdr 5e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.73×** | +18.5 | 0e+00 | 41/43 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.85×** | +10.4 | 8e-23 | 30/33 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.07×** | +10.2 | 4e-22 | 41/48 (A498, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.80×** | +9.8 | 1e-20 | 35/43 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +9.3 | 1e-18 | 12/19 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +7.2 | 5e-11 | 31/43 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +7.1 | 1e-10 | 18/28 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.74×** | +5.5 | 3e-06 | 26/46 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.63×** | +4.6 | 2e-04 | 21/46 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +4.4 | 5e-04 | 19/43 (Hs 766T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +4.3 | 9e-04 | 16/41 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.55×** | +4.2 | 0.001 | 21/46 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.003 | 16/46 (KATO III, COLO 205, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.006 | 16/47 (LoVo, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.007 | 13/47 (A498, Panc 03.27, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.014 | 10/48 (A498, NCI-H2347, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.40×** | +3.3 | 0.032 | 10/47 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.034 | 9/47 (A498, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13244.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.506×** | -6.4 | 1e-07 | 32/45 (HT-29, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.544×** | -5.7 | 3e-06 | 25/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.581×** | -5.4 | 1e-05 | 24/47 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.682×** | -5.4 | 1e-05 | 25/47 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.592×** | -5.2 | 2e-05 | 23/47 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.620×** | -4.7 | 2e-04 | 22/46 (HT-29, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.634×** | -4.5 | 5e-04 | 21/45 (COLO 205, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.665×** | -4.0 | 0.004 | 18/47 (HT-29, SHP-77, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.670×** | -4.0 | 0.005 | 19/42 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.673×** | -3.9 | 0.005 | 21/47 (HT-29, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.477×** | -3.8 | 0.006 | 12/41 (NCI-H460, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.697×** | -3.6 | 0.017 | 17/47 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.719×** | -3.3 | 0.049 | 14/47 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.547×** | -3.1 | 0.072 | 16/42 (PANC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.555×** | -3.0 | 0.084 | 10/45 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.731×** | -3.0 | 0.084 | 14/47 (NCI-H1573, KATO III, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **0.805×** | -3.0 | 0.084 | 9/47 (SK-MEL-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 35.0 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +11.1) | [[Ixazomib citrate (drug)]] 0.5 µM 0.125× (z -13.8) |
| [[SW480 (line)]] | alt | 6.61 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.00× (z +15.5) | — |
| [[HEC-1-A (line)]] | alt | 11.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 4.45 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.38× (z +10.2) | [[Roxadustat (drug)]] 0.05 µM 0.0629× (z -9.9) |
| [[KATO III (line)]] | alt | 10.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +9.5) | [[Ixazomib citrate (drug)]] 0.5 µM 0.163× (z -8.5) |
| [[LoVo (line)]] | wt | 6.88 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.30× (z +12.8) | [[Digitoxin (drug)]] 5 µM 0.0998× (z -10.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.111× (z -9.5) |
| [[HS-578T (line)]] | alt | 7.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.57× (z +10.7) | — |
| [[J82 (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 8.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.59× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 8.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.83× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 7.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 24.7 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.252× (z -9.4) |
| [[RKO (line)]] | wt | 7.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.87× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 8.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.67× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 7.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.33× (z +9.4) | — |
| [[A-427 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 28 of them with an alert (⚠; 28 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATL2]] | +0.74 | +0.79 / +0.37 | both halves | 8e-05 |  |
| [[PKN2-AS1]] | +0.73 | +0.70 / +0.41 | both halves | 4e-05 | same gene group |
| [[TAFA2]] | +0.73 | +0.73 / +0.39 | both halves | 5e-05 |  |
| [[FAM174B]] | +0.72 | +0.63 / +0.43 | both halves | 4e-05 |  |
| [[DECR1]] | +0.72 | +0.65 / +0.40 | both halves | 4e-05 |  |
| [[GALNT7-DT]] | +0.70 | +0.72 / +0.21 | both halves | 7e-04 |  |
| [[TAPBPL]] | +0.70 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[SCAMP1-AS1]] | +0.69 | +0.68 / +0.40 | both halves | 4e-05 | same gene group |
| [[CTSO]] | +0.69 | +0.55 / +0.38 | both halves | 6e-05 |  |
| [[BDNF-AS]] | +0.69 | +0.71 / +0.37 | both halves | 8e-05 | same gene group |
| [[TMEM202-AS1]] | +0.68 | +0.68 / +0.23 | both halves | 5e-04 | same gene group |
| [[EFCAB2]] | +0.68 | +0.62 / +0.21 | both halves | 6e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLTCL1]] | -0.67 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[ANKRD27]] | -0.66 | -0.64 / -0.21 | both halves | 7e-04 |  |
| [[NBPF3]] | -0.66 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[PBX4]] | -0.65 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[YIF1B]] | -0.64 | -0.59 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[SH3PXD2B]] | -0.64 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[MAST3]] | -0.63 | -0.53 / -0.22 | both halves | 6e-04 |  |
| [[SLC27A1]] | -0.61 | -0.61 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[LRRC42]] | -0.61 | -0.65 / -0.31 | both halves | 2e-04 |  |
| [[HDAC11]] | -0.60 | -0.54 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANXA2R-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.6% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.729). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (8.7, 14.6); signed map (25.8, -20.2). **Vector** length 95.0, 22.1% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +18.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | +10.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.6 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +4.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.2 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.7 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.5 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -4.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ANXA2R antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5p12 — chr5:43,041,572-43,064,272 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27208](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27208) · Entrez [153684](https://www.ncbi.nlm.nih.gov/gene/153684) · Ensembl [ENSG00000215068](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215068)

## Data

Gene col 13244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13244); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13244]; `tensor/DDL_lfc|DDL_z.npy` [13244]; `embed/gene_vectors.npy` [13244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13244 or target_col == 13244). Every well: [[ANXA2R-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANXA2R-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
